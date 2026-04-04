class Hang_hoa:
    def __init__(self, ma_hang, ten_hang, nsx):
        self.__ma_hang = ma_hang
        self.__ten_hang = ten_hang
        self.__nsx = nsx
    
    def ma_hang(self):
        return self.__ma_hang
    def ten_hang(self):
        return self.__ten_hang
    def nsx(self):
        return self.__nsx
    
    def hien_thi(self):
        print(f"Mã hàng     : {self.__ma_hang}")
        print(f"Tên hàng    : {self.__ten_hang}")
        print(f"Nhà sản xuất: {self.__nsx}")
    
class Hang_Dien_may(Hang_hoa): 
    def __init__(self, ma_hang, ten_hang, nsx, gia, tg_bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nsx)
        self.__gia = gia
        self.__tg_bao_hanh = tg_bao_hanh
        self.__dien_ap = dien_ap
        self.__cong_suat = cong_suat
    
    def hien_thi(self):
        print("===== HÀNG ĐIỆN MÁY =====")
        super().hien_thi()
        print(f"Giá thành         : {self.__gia} VNĐ")
        print(f"Thời gian bảo hành: {self.__tg_bao_hanh} Tháng")
        print(f"Điện áp           : {self.__dien_ap} V")
        print(f"Công suất         : {self.__cong_suat} W")

class Hang_Sanh_su(Hang_hoa):
    def __init__(self, ma_hang, ten_hang, nsx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nsx)
        self.__gia = gia
        self.__loai_nguyen_lieu = loai_nguyen_lieu
    
    def hien_thi(self):
        print("===== HÀNG SÀNH SỨ =====")
        super().hien_thi()
        print(f"Giá thành       : {self.__gia} VNĐ")
        print(f"Loại nguyên liêu: {self.__loai_nguyen_lieu}")

class Hang_Thuc_pham(Hang_hoa):
    def __init__(self, ma_hang, ten_hang, nsx, gia, ngay_sx, hsd):
        super().__init__(ma_hang, ten_hang, nsx)
        self.__gia = gia
        self.__ngay_sx = ngay_sx
        self.__hsd = hsd
    
    def hien_thi(self):
        print("===== HÀNG THỰC PHẨM ===== ")
        super().hien_thi()
        print(f"Giá thành    : {self.__gia} VNĐ")
        print(f"Ngày sản xuất: {self.__ngay_sx}")
        print(f"Hạn sử dụng  : {self.__hsd}")

dm = Hang_Dien_may(1234,"Điều hòa", "LG", 16_000_000, 12, 20, 2000)
dm.hien_thi()
ss = Hang_Sanh_su(2341, "Bát", "Gốm sứ Mạnh Hải", 500_000, "Sứ cao cấp")
ss.hien_thi()
tp = Hang_Thuc_pham(3214, "Thịt lợn sạch", "Mealdeli", 35_000, "23/3/2026", "1/4/2026")
tp.hien_thi()