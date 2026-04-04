LUONG_CO_BAN = 5_000_000
class Nhan_vien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.__ma_nv = ma_nv
        self.__ho_ten = ho_ten
        self.__nam_sinh = nam_sinh
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi
        self.__he_so_luong = he_so_luong if he_so_luong >0 else 1.0
        self.__luong_toi_da = luong_toi_da

    def ma_nv(self): return self.__ma_nv
    def ho_ten(self): return self.__ho_ten
    def nam_sinh(self): return self.__nam_sinh
    def gioi_tinh(self): return self.__gioi_tinh
    def dia_chi(self): return self.__dia_chi
    def he_so_luong(self): return self.__he_so_luong
    def luong_toi_da(self): return self.__luong_toi_da

    def tinh_luong(self):
        return LUONG_CO_BAN * self.__he_so_luong
    
    def hien_thi(self):
        print(f"Mã nhân viên: {self.__ma_nv}")
        print(f"Họ và tên   : {self.__ho_ten}")
        print(f"Năm sinh    : {self.__nam_sinh}")
        print(f"Giới tính   : {self.__gioi_tinh}")
        print(f"Địa chỉ     : {self.__dia_chi}")
        print(f"Hệ số lương : {self.__he_so_luong}")
        print(f"Lương tối đa: {self.tinh_luong():,.0f} VNĐ")

class Cong_tac_vien(Nhan_vien):
    HD_HOP_LE = ["3 tháng", "6 tháng", "1 năm"]

    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, thoi_han_hd, phu_cap_ld):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        if thoi_han_hd not in Cong_tac_vien.HD_HOP_LE:
            raise ValueError(f" Thời hạn hợp đồng là: {Cong_tac_vien.HD_HOP_LE}")
        self.__thoi_han_hd = thoi_han_hd
        self.__phu_cap_ld = phu_cap_ld

    def tinh_luong(self):
        return super().tinh_luong() + self.__phu_cap_ld

    def hien_thi(self):
        print("===== CỘNG TÁC VIÊN =====")
        super().hien_thi()
        print(f"Thời hạn hợp đồng: {self.__thoi_han_hd} ")
        print(f"Phụ cấp          : {self.__phu_cap_ld:,.0f} VNĐ")

class NV_chinh_thuc(Nhan_vien):
    def __init__ (self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, vi_tri):
        super(). __init__ (ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.__vi_tri = vi_tri

    def hien_thi(self):
        print("===== NHÂN VIÊN CHÍNH THỨC =====")
        super().hien_thi()
        print(f"Vị trí: {self.__vi_tri}")

class Truong_phong(Nhan_vien):
    def __init__ (self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da, ngay_bat_dau_ql, phu_cap_ql):
        super(). __init__ (ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.__ngay_bat_dau_ql = ngay_bat_dau_ql
        self.__phu_cap_ql = phu_cap_ql

    def tinh_luong(self):
        return super().tinh_luong() + self.__phu_cap_ql

    def hien_thi(self):
        print("===== TRƯỞNG PHÒNG =====")
        super().hien_thi()
        print(f"Ngày bắt đầu quản lý: {self.__ngay_bat_dau_ql}")
        print(f"Phụ cấp             : {self.__phu_cap_ql} VNĐ")

ctv = Cong_tac_vien(1353, "Phạm Đăng Tuấn", 2007, "Nam", "xã Đông Anh", 2.0, 20_000_000, "3 tháng", 500_000)
ctv.hien_thi()
nv = NV_chinh_thuc(2454, "Đỗ Trần Bá Điều", 2002, "Nam", "xã Thư Lâm", 2.5, 50_000_000, "Kỹ sư")
nv.hien_thi()
tp = Truong_phong(3536, "Nguyễn Chu Thái Phương", 1999, "Nam", "xã Phúc Thịnh", 3.0, 60_000_000, "23/01/2025", 1_000_000)
tp.hien_thi()