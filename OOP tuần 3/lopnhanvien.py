class NhanVien:
    LUONG_MAX = 50_000_000
    def __init__(self, ten_nhan_vien: str, luong_co_ban: float, he_so_luong: float ):
        self.__tenNhanVien = ten_nhan_vien
        self.__luongCoBan = luong_co_ban
        self.__heSoLuong = he_so_luong
    @property
    def tenNhanVien(self): return self.__tenNhanVien

    @tenNhanVien.setter
    def tenNhanVien(self, value):
        if not value.strip():
            raise ValueError("Tên không được rỗng!")
        self.__tenNhanVien = value
    
    @property
    def luongCoBan(self): return self.__luongCoBan 

    @luongCoBan.setter
    def luongCoBan(self, value):
        if value < 0:
            raise ValueError("Lương không được âm!")
        self.__luongCoBan = value

    @property
    def heSoLuong(self): return self.__heSoLuong

    @heSoLuong.setter
    def heSoLuong(self, value):
        if value <= 0:
            raise ValueError("Hệ số lương phải > 0!")
        self.__heSoLuong = value

    def tinhluong(self)-> float:
        return self.__luongCoBan * self.__heSoLuong

    def inThongTin(self):
        luong = self.tinhluong()
        print(f"""
╔══════════════════════════════════════╗
║        THÔNG TIN NHÂN VIÊN           ║
╠══════════════════════════════════════╣
║ Tên       : {self.__tenNhanVien:<25}║
║ Lương CB  : {self.__luongCoBan:>20,.0f} VNĐ ║
║ Hệ số     : {self.__heSoLuong:>25.1f} ║
║ Lương TT  : {luong:>20,.0f} VNĐ ║
╚══════════════════════════════════════╝""")   

    def tangluong(self, delta: float)->bool:
        luong_moi = (self.__luongCoBan + delta) * self.__heSoLuong
        if luong_moi > NhanVien.LUONG_MAX:
            print (f"  Lương mới ({luong_moi:,.0f}) vượt LUONG_MAX. Không tăng!")
            return False
        self.__luongCoBan += delta
        print (f"Đã tăng lương! Lương mới: {self.tinhluong():,.0f} VNĐ")
        return True
    
nv = NhanVien("Nguyễn Xuân Anh Tú", 20_000_000, 2.0)
nv.inThongTin()
nv.tangluong(5_000_000)
nv.tangluong(10_000_000)