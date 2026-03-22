class ConCho:
    def __init__(self, ten: str , mau_sac: str, giong: str, cam_xuc="vui"):
        self.ten = ten
        self.mau_sac = mau_sac
        self.giong = giong
        self.cam_xuc = cam_xuc
    def sua(self):
        print(f"{self.ten}: Gâu gâu! ")
    def vay_duoi(self):
        print(f"{self.ten} vẫy đuôi vì {self.cam_xuc}!")
    def an(self, thuc_an):
        print(f"{self.ten} đang ăn {thuc_an}. Ngon!")
    def chay(self, toc_do):
        print(f"{self.ten} chạy với tốc độ {toc_do} km/h!")

class OTo:
    def __init__(self, hang: str, kich_thuoc: str, mau:str, gia:str):
        self.hang       = hang
        self.kich_thuoc = kich_thuoc
        self.mau        = mau
        self.gia        = gia
        self.toc_do     = 0
    def tang_toc(self, them):
        self.toc_do += them
        print(f"Tăng tốc! Tốc độ hiện tại: {self.toc_do} km/h")
    def giam_toc(self, bot):
        self.toc_do = max(0, self.toc_do - bot)
        print(f"Giảm tốc! Tốc độ hiện tại: {self.toc_do} km/h")
    def dam(self):
        print(f"Xe {self.hang} bị đâm! Dừng khẩn cấp.")
        self.toc_do = 0

class TaiKhoan:
    def __init__(self, ten_tk: str, so_tk: str, ngan_hang:str, so_du=0):
        self.ten_tk    = ten_tk
        self.so_tk     = so_tk
        self.ngan_hang = ngan_hang
        self.__so_du   = so_du  
    def rut(self, so_tien):
        if so_tien > self.__so_du:
            print("Số dư không đủ!")
        else:
            self.__so_du -= so_tien
            print(f"Rút {so_tien:,} VNĐ. Số dư còn: {self.__so_du:,}")
    def gui(self, so_tien):
        self.__so_du += so_tien
        print(f"Gửi {so_tien:,} VNĐ. Số dư mới: {self.__so_du:,}")
    def kiem_tra_so_du(self):
        print(f"[{self.ten_tk}] Số dư: {self.__so_du:,} VNĐ")


cho = ConCho("Milo", "vàng", "Golden Retriever")
cho.sua(); cho.an("xương")
xe = OTo("Toyota", "sedan", "trắng", 800_000_000)
xe.tang_toc(60); xe.tang_toc(40); xe.giam_toc(30)
tk = TaiKhoan("Nguyễn Văn A", "123456789", "Vietcombank", 5_000_000)
tk.gui(2_000_000); tk.rut(3_000_000); tk.kiem_tra_so_du()
        