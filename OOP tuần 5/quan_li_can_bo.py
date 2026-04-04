class Can_bo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.__ho_ten = ho_ten
        self.__tuoi = tuoi
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi

    def ho_ten(self): return self.__ho_ten
    def tuoi(self): return self.__tuoi
    def gioi_tinh(self): return self.__gioi_tinh
    def dia_chi(self): return self.__dia_chi

    def loai_cb(self):
        return "Cán bộ"

    def hien_thi(self):
        print(f"Họ và tên: {self.__ho_ten}")
        print(f"Tuổi     : {self.__tuoi}")
        print(f"Giới tính: {self.__gioi_tinh}")
        print(f"Địa chỉ  : {self.__dia_chi}")

    def __str__(self):
        return f"{self.loai_cb():<10s} | {self.__ho_ten}"

class Cong_nhan(Can_bo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        if not (1 <= bac <= 10):
            raise ValueError("Bậc phải từ 1 đến 10!")
        self.__bac = bac

    def loai_cb(self):
        return "Công nhân"

    def hien_thi(self):
        print("===== CÔNG NHÂN =====")
        super().hien_thi()
        print(f"Bậc: {self.__bac}")

class Ky_su(Can_bo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super(). __init__ (ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh = nganh

    def loai_cb(self):
        return "Kỹ sư"

    def hien_thi(self):
        print("===== KỸ SƯ =====")
        super().hien_thi()
        print(f"Ngành đào tạo: {self.__nganh}")

class Nhan_vien(Can_bo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cv):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cv = cv

    def loai_cb(self):
        return "Nhân viên"

    def hien_thi(self):
        print("===== NHÂN VIÊN =====")
        super().hien_thi()
        print(f"Công việc: {self.__cv}")

class QLCB:
    def __init__(self):
        self.__ds_can_bo = []

    def them_moi(self):
        print("\n===== THÊM CÁN BỘ MỚI =====")
        print("1. Công nhân")
        print("2. Kỹ sư")
        print("3. Nhân viên")
        loai = input("Chọn loại (1/2/3): ").strip()

        ho_ten = input("Họ tên: ")
        tuoi = int(input("Tuổi: "))
        gioi_tinh = input("Giới tính: ")
        dia_chi = input("Địa chỉ: ")

        if loai == "1":
            bac = int(input("Bậc (1-10): "))
            cb = Cong_nhan(ho_ten, tuoi, gioi_tinh, dia_chi, bac)
        elif loai == "2":
            nganh = input("Ngành đào tạo: ")
            cb = Ky_su(ho_ten, tuoi, gioi_tinh, dia_chi, nganh)
        elif loai == "3":
            cv = input("Công việc: ")
            cb = Nhan_vien(ho_ten, tuoi, gioi_tinh, dia_chi, cv)
        else:
            print(" Loại không hợp lệ!")
            return
        
        self.__ds_can_bo.append(cb)
        print(f"Đã thêm: {cb}")

    def tim_kiem(self):
        tu_khoa = input("\n Nhập họ tên cần tìm: ").strip().lower()
        ket_qua = [cb for cb in self.__ds_can_bo
                   if tu_khoa in cb.ho_ten().lower()]
        if not ket_qua:
            print("Không tìm thấy!")
        else:
            print(f"Tìm thấy {len(ket_qua)} kết quả:")
            for cb in ket_qua:
                print()
                cb.hien_thi()
    
    def hien_thi_ds(self):
        if not self.__ds_can_bo:
            print("\n Danh sách trống!")
            return
        print(f"\n ===== DANH SÁCH CÁN BỘ ({len(self.__ds_can_bo)} người) =====")
        for i, cb in enumerate(self.__ds_can_bo,1):
            print(f"\n --- #{i} ---")
            cb.hien_thi()
    
    def chay(self):
        while True:
            print("\n   |=========================|")
            print("   |     QUẢN LÝ CÁN BỘ      |")
            print("   |=========================|")
            print("   | 1. Thêm cán bộ mới      |")
            print("   | 2. Tìm kiếm theo tên    |")
            print("   | 3. Hiển thị danh sách   |")
            print("   | 4. Thoát                |")
            print("   |=========================|")

            chon = input("Lựa chọn: ").strip()
            if chon == "1": self.them_moi()
            elif chon == "2": self.tim_kiem()
            elif chon == "3": self.hien_thi_ds()
            elif chon == "4": 
                print("Bye bye!")
                break
            else:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    ql = QLCB()
    ql.chay()

    
