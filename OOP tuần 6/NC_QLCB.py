from abc import ABC, abstractmethod

class Tuoi_khong_hop_le(Exception):
    def __init__(self, tuoi):
        self.__tuoi = tuoi
        super(). __init__(f"Tuổi {tuoi} không hợp lệ (18-65)")

class Bac_khong_hop_le(Exception):
    def __init__(self, bac):
        self.__bac = bac
        super().__init__(f"Bậc {bac} không hợp lệ (1-10)")


class Can_bo(ABC):

    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.__ho_ten = ho_ten
        self.tuoi = tuoi
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi

    @property
    def ho_ten(self): return self.__ho_ten
    @property
    def tuoi(self): return self.__tuoi
    @property
    def gioi_tinh(self): return self.__gioi_tinh
    @property
    def dia_chi(self): return self.__dia_chi

    @tuoi.setter 
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise Tuoi_khong_hop_le(value)
        self.__tuoi = value

    @abstractmethod
    def mo_ta(self):
        pass

    def __str__(self):
        return (f"{self.__ho_ten} | {self.__tuoi} tuổi"
                f" | {self.__gioi_tinh} | {self.__dia_chi}"
                f" | {self.mo_ta()}")
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__ho_ten}', {self.__tuoi})"
    
    def __eq__(self, other): 
        if not isinstance(other, Can_bo): return NotImplemented
        return self.ho_ten == other.__ho_ten and self.__tuoi == other.__tuoi
    
    def __lt__(self, other):
        return self.__ho_ten < other.__ho_ten
    
    def __hash__(self):
        return hash ((self.__ho_ten, self.__tuoi))
    
class Cong_nhan(Can_bo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac
       
    @property
    def bac(self): return self.__bac
    @bac.setter
    def bac(self,value):
        if not (1 <= value <= 10):
            raise Bac_khong_hop_le(value)
        self.__bac = value

    def mo_ta(self):
            return f"Công nhân bậc: {self.__bac}"
        
class Ky_su(Can_bo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh = nganh

    def mo_ta(self):
        return f"Kỹ sư ngành: {self.__nganh}"
        
class Nhan_vien(Can_bo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cv):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cv = cv 

    def mo_ta(self):
        return f"Công việc của nhân viên: {self.__cv}"
        
ds = [Cong_nhan("Nguyễn Đức Anh", 35, "Nam", "Hà Nội", 5),
      Ky_su("Trần Diên Quân", 24, "Nam", "Hà Nội", "Điện - Điện tử"),
      Nhan_vien("Trương Thảo Linh", 24, "Nữ", "Nam Định", "Kế toán")]

print("--- Đa hình: 1 vòng lặp, 3 loại CB ---")
for cb in ds:
    print(cb)

print("\n --- Sắp xếp theo tên (A-Z) ---")
for cb in sorted(ds):
    print (f" {cb.ho_ten}")

print("\n --- Validation ---")
try:
    Cong_nhan("X", 15, "Nam", "HN", 5)
except Tuoi_khong_hop_le as e:
    print(f"{e}")

print("\n --- Lưu file ---")
with open("canbo.txt", "w", encoding = "utf-8") as f:
    for cb in ds:
        f.write(str(cb)+"\n")
print(f"Đã lưu {len(ds)} cán bộ")