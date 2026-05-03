class Can_bo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def __str__(self):
        return "\n".join ([f"Họ tên:    {self.ho_ten}",
                f"Tuổi:      {self.tuoi}",
                f"Giới tính: {self.gioi_tinh}",
                f"Địa chỉ:   {self.dia_chi}",])
    
    def to_dict(self):
        return {
            "ho_ten":    self.ho_ten,
            "tuoi":      self.tuoi,
            "gioi_tinh": self.gioi_tinh,
            "dia_chi":   self.dia_chi,
            "loai":      self.__class__.__name__,
        }
    
    @classmethod
    def from_dict(cls, d):
        return cls(
            d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"]
        )

class Cong_nhan(Can_bo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    def __str__(self):
        return super().__str__() + f"\nBậc: {self.bac}"
    
    def to_dict(self):
        d = super().to_dict()
        d["bac"] = self.bac
        return d

    @classmethod
    def from_dict(cls, d):
        return cls(
            d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"], d["bac"]
        )

class Ky_su(Can_bo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh

    def __str__(self):
        return super().__str__() + f"\nNgành: {self.nganh}"
    
    def to_dict(self):
        d = super().to_dict()
        d["nganh"] = self.nganh
        return d

    @classmethod
    def from_dict(cls, d):
        return cls(
            d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"], d["nganh"]
        )

class Nhan_vien(Can_bo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cv):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cv = cv

    def __str__(self):
        return super().__str__() + f"\nCông việc: {self.cv}"
    
    def to_dict(self):
        d = super().to_dict()
        d["cv"] = self.cv
        return d

    @classmethod
    def from_dict(cls, d):
        return cls(
            d["ho_ten"], d["tuoi"], d["gioi_tinh"], d["dia_chi"], d["cv"]
        )

import json
# Tải về phục hồi đúng loại
LOAI_MAP = {
    "Can_bo":  Can_bo,
    "Cong_nhan": Cong_nhan,
    "Ky_su": Ky_su,
    "Nhan_vien": Nhan_vien,
}

MAP_INPUT = {
    "Công nhân": "Cong_nhan",
    "Kỹ sư": "Ky_su",
    "Nhân viên": "Nhan_vien",
}

danh_sach = {}
with open("canbo.json", "r", encoding = "utf-8") as f:
    for d in json.load(f):
        cls = LOAI_MAP.get(d["loai"], Can_bo)
        cb = cls.from_dict(d)
        danh_sach[cb.ho_ten] = cb

class Quan_ly_can_bo:
    FILE = "canbo.json"

    def __init__(self):
        self.ds: dict[str, Can_bo] = {}
        self._tai_du_lieu()

    def them(self, cb: Can_bo):
        if cb.ho_ten in self.ds:
            raise ValueError(
                f"{cb.ho_ten} đã tồn tại !")
        self.ds[cb.ho_ten] = cb
        self._luu_du_lieu()

    def xoa(self, ho_ten: str):
        if ho_ten not in self.ds:
            raise KeyError(ho_ten)
        del self.ds[ho_ten]
        self._luu_du_lieu()
    
    def tim(self, ho_ten) -> Can_bo:
        return self.ds.get(ho_ten)
    
    def loc_theo_loai(self, loai: str):
        return [cb for cb in self.ds.values() if type(cb).__name__ == loai ]
    
    def _luu_du_lieu(self):
        data = [cb.to_dict() for cb in self.ds.values()]
        with open(self.FILE, "w", encoding = "utf-8") as f:
            json.dump(data,f, ensure_ascii = False, indent = 2)

    def _tai_du_lieu(self):
        try:
            with open(self.FILE, "r", encoding = "utf-8") as f :
                for d in json.load(f):
                    cls = LOAI_MAP.get(d["loai"], Can_bo)
                    cb = cls.from_dict(d)
                    self.ds[cb.ho_ten] = cb
        except FileNotFoundError:
            pass

def menu():
    qlcb = Quan_ly_can_bo()
    while True:
        print("\n ----- QUẢN LÝ CÁN BỘ ----- ")
        print("1. Xem danh sách ")
        print("2. Thêm Công nhân")
        print("3. Thêm Kỹ sư")
        print("4. Thêm Nhân viên")
        print("5. Tìm theo tên")
        print("6. Lọc theo loại")
        print("7. Xóa")
        print("0. Thoát")
        
        chon = input("Chon: ").strip()
        if chon == "1":
            for cb in qlcb.ds.values():
                print (cb)

        elif chon == "2":
            try:
                ten = input ("Họ tên: ")
                t = int(input("Tuổi: "))
                gt = input("Giới tính: ")
                dc = input("Địa chỉ: ")
                bac = int(input("Bậc (1-10): "))
                qlcb.them(Cong_nhan(
                    ten, t, gt, dc, bac))
                print("Đã lưu!")
            except(ValueError, KeyError) as e:
                print(f"Lỗi: {e}")

        elif chon == "3":
            try:
                ten = input("Họ tên: ")
                t = int(input("Tuổi: "))
                gt = input("Giới tính: ")
                dc = input("Địa chỉ: ")
                n = input("Ngành: ")
                qlcb.them(Ky_su(ten, t, gt, dc, n))
                print("Đã lưu!")
            except(ValueError, KeyError) as e:
                print(f"Lỗi: {e}")

        elif chon == "4":
            try:
                ten = input("Họ tên: ")
                t = int(input("Tuổi: "))
                gt = input("Giới tính: ")
                dc = input("Địa chỉ: ")
                cv = input("Công việc: ")
                qlcb.them(Nhan_vien(ten, t, gt, dc, cv))
                print("Đã lưu! ")
            except(ValueError, KeyError) as e:
                print(f"Lỗi: {e}")

        elif chon == "5":
                ten = input("Nhập tên cần tìm: ")
                cb = qlcb.tim(ten)
                if cb: 
                    print(cb)
                else:
                    print("Không tìm thấy!")

        elif chon =="6":
            loai = input("Loại cán bộ(Công nhân/Kỹ sư/Nhân viên): ")
            loai_code = MAP_INPUT.get(loai)
            if not loai_code:
                print ("Loại không hợp lệ!")
            else:
                for cb in qlcb.loc_theo_loai(loai_code):
                    print(cb)
        
        elif chon == "7":
            qlcb.xoa(input("Tên cần xóa: "))

        elif chon == "0": break 

        else:
            print("Chọn sai!")

if __name__ == "__main__":
    menu()