class NhanVien:
    LUONG_MAX = 50_000_000

    def __init__(self, ten_nhan_vien, luong_co_ban, he_so_luong ):
        self.__ten_nhan_vien = ten_nhan_vien
        self.__luong_co_ban  = luong_co_ban
        self.__he_so_luong   = he_so_luong

    def getten_nhan_vien(self):
        return self.__ten_nhan_vien
    def getluong_co_ban(self):
        return self.__luong_co_ban
    def gethe_so_luong(self):
        return self.__he_so_luong
    
    def setten_nhan_vien(self, value):
        self.__ten_nhan_vien = value
    def setluong_co_ban(self, value):
        if value < 0:
            print("Lương không được âm!")
            return
        self.__luong_co_ban = value
    def sethe_so_luong(self, value):
        if value <= 0:
            print ("Hệ số lương phải lớn hơn 0!")
            return
        self.__he_so_luong = value

    def tinh_luong(self):
        return self.__luong_co_ban * self.__he_so_luong
    
    def in_thong_tin(self):
        luong = self.tinh_luong()
        print("========== DANH SÁCH NHÂN VIÊN ==========")
        print(f"Tên nhân viên  : {self.__ten_nhan_vien}")
        print(f"Lương cơ bản   : {self.__luong_co_ban:,.0f} VNĐ")
        print(f"Hệ số lương    : {self.__he_so_luong}")
        print(f"Lương thực tế  : {luong:,.0f} VNĐ")
        print("=========================================")

    def tang_luong(self, delta):
        
        he_so_moi = self.__he_so_luong + delta
        luong_moi = self.__luong_co_ban * he_so_moi
        if luong_moi > NhanVien.LUONG_MAX:
            print (f"Lương mới ({luong_moi:,.0f}) vượt LUONG_MAX ({NhanVien.LUONG_MAX:,.0f} VNĐ)")
            return False
        self.__he_so_luong = he_so_moi
        print (f" Đã tăng hệ số lương! Lương mới: {self.tinh_luong():,.0f} VNĐ")
        return True
    
nv = NhanVien("Nghiêm Thọ Tài", 15_000_000, 2.5)
nv.in_thong_tin()

print("\n----- Test tangluong -----")
nv.tang_luong(0.5)
nv.in_thong_tin()

nv.tang_luong(3.0)

print("\n----- Test getter/setter -----")
print(f"Tên: {nv.getten_nhan_vien()}")
nv.setluong_co_ban(17_000_000)
print (f"Lương cơ bản mới  : {nv.getluong_co_ban():,.0f}")
print (f"Lương thực tế mới : {nv.tinh_luong():,.0f}")

    