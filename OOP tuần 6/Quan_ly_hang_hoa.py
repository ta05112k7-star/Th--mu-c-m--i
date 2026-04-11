from abc import ABC, abstractmethod

class Gia_ko_hop_le(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f"Giá '{gia}' không hợp lệ (phải >=0)")

class Hang_hoa(ABC):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__nha_sx = nha_sx
        self.gia = gia

    @property
    def ma_hang(self): return self.__ma_hang
    @property
    def ten_hang(self): return self.__ten_hang
    @property
    def nha_sx(self): return self.__nha_sx
    @property
    def gia(self): return self.__gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise Gia_ko_hop_le(value)
        self.__gia = value
    @abstractmethod
    def loai_hang(self):
        pass

    def mo_ta(self):
        return (f"[{self.loai_hang()}] | Mã hàng: {self.__ma_hang} "
                f"| Tên hàng: {self.__ten_hang} | Nhà sản xuất: {self.__nha_sx}"
                f"| Giá: {self.__gia:,.0f} VNĐ")
    
    def __str__(self):
        return self.mo_ta()
    def __repr__(self):
        return (f"{self.__class__.__name__}('{self.__ma_hang}', "
                f"'{self.__ten_hang}', '{self.__nha_sx}','{self.__gia}')")
    def __eq__(self, other):
        if not isinstance(other, Hang_hoa):
            return NotImplemented
        return self.__ma_hang == other.__ma_hang
    def __lt__(self, other):
        return self.__gia < other.__gia
    def __hash__(self):
        return hash(self.__ma_hang)
    
class Hang_Dien_may(Hang_hoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__tg_bao_hanh = tg_bao_hanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat

    def loai_hang(self):
        return "Điện máy"
    
    def mo_ta(self):
        return (f"{super().mo_ta()} | Bảo hành: {self.__tg_bao_hanh} tháng"
                f"| {self.__dien_ap} V | {self.__cong_suat} W")

class Hang_Sanh_su(Hang_hoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__loai_nguyen_lieu = loai_nguyen_lieu
    
    def loai_hang(self):
        return "Sành sứ"
    
    def mo_ta(self):
        return (f"{super().mo_ta()} | Nguyên liệu: {self.__loai_nguyen_lieu}")
    
class Hang_Thuc_pham(Hang_hoa):
    def __init__(self, ma_hang, ten_hang,  nha_sx, gia, nsx, hsd):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.__nsx = nsx
        self.__hsd = hsd

    def loai_hang(self):
        return "Thực phẩm"
    
    def mo_ta(self):
        return (f"{super().mo_ta()} | Ngày sản xuất: {self.__nsx}"
                f" | Hạn sử dụng: {self.__hsd}")
sp1 = Hang_Dien_may(1532, "Điều hòa", "Daikin", 16_000_000, 12, 220, 150)
sp2 = Hang_Sanh_su(2143, "Bát sứ cao cấp", "Gốm sứ Bát Tràng", 500_000, "Sứ cao cấp")
sp3 = Hang_Thuc_pham(3152, "Ức gà tươi", "Mealdeli", 70_000, "22/03/2026", "22/04/2026")

print("--- Đa hình ---")
kho = [sp1,sp2,sp3]
for sp in kho:
    print(sp)

print("\n --- Sắp xếp theo gia ---")
for sp in sorted(kho):
    print(f" {sp.gia:>12,.0f} VNĐ | {sp.ten_hang}")

print("\n --- So sánh và loại trùng --- ")
sp1_copy = Hang_Dien_may(1532, "Điều hòa", "Daikin", 16_000_000, 12, 220, 150)
print(f" sp1 == sp1_copy? {sp1 == sp1_copy}")
print(f" Xét loại trùng: {len([sp1, sp2, sp1_copy])} -> {len(set([sp1, sp2, sp1_copy]))}")

print("\n --- Validation ---")
try:
    sp_loi = Hang_Dien_may("BM789", "Test", "X", -4000, 12, 220, 50)
except Gia_ko_hop_le as e:
    print(f" Bắt lỗi: {e}")

try:
    h = Hang_hoa("X", "Test", "Y", 100)
except TypeError as e:
    print(f" ABC: {e}")

print("\n --- Lưu file(with) ---")
with open ("kho_hang.txt", "w", encoding = "utf-8") as f:
    for sp in kho:
        f.write(repr(sp) + "\n")
print(f"Đã Lưu { len(kho)} sản phẩm")