class TuLanh:
    def __init__(self, nhanhieu, maso, nuocsx, tkdien, dungtich, gia):
        self.__nhanhieu = nhanhieu
        self.__maso = maso
        self.__nuocsx = nuocsx
        self.__tkdien = tkdien
        self.__dungtich = dungtich
        self.__gia = gia

    def __str__(self):
        tkdien = "Có" if self.__tkdien else "Không"

        return (f"Nhãn hiệu: {self.__nhanhieu}\n"
                f"Mã số: {self.__maso}\n"
                f"Nước SX: {self.__nuocsx}\n"
                f"T/K điện: {tkdien}\n"
                f"Dung tích: {self.__dungtich}L\n"
                f"Giá: {self.__gia}VNĐ")


    def nhapThongTin(self):
        self.__nhanhieu = input("Nhập Nhãn hiệu: ")
        self.__maso = input("Nhập Mã số: ")
        self.__nuocsx = input("Nước SX: ")
        self.__tkdien = input("T/K điện: ")
        self.__dungtich = input("Dung tích: ")
        self.__gia = input("Giá: ")

    def hienThi(self):
        print(self)