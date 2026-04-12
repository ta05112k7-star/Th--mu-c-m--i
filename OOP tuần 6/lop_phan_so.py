from math import gcd

class Mau_so_bang_khong(Exception):
    def __init__(self):
        super().__init__("mẫu số không được bằng 0")

class Phan_so:
    def __init__(self, tu = 0, mau = 1):
        self.tu_so = tu
        self.mau_so = mau
   
    @property
    def tu_so(self): return self.__tu 
    @tu_so.setter
    def tu_so(self, value):
        self.__tu = value

    @property
    def mau_so(self): return self.__mau
    @mau_so.setter 
    def mau_so(self, value):
        if value == 0:
            raise Mau_so_bang_khong()
        self.__mau = value

    def toi_gian(self):
        g = gcd(abs(self.__tu), abs(self.__mau))
        tu = self.__tu // g
        mau = self.__mau // g
        if mau < 0:
            tu, mau = -tu, -mau
        return Phan_so(tu,mau)

    def is_toi_gian(self):
        return gcd(abs(self.__tu), abs(self.__mau)) == 1

    def __add__ (self, other):
        tu = self.__tu * other.__mau + other.__tu *self.__mau
        mau = self.__mau * other.__mau
        return Phan_so(tu, mau).toi_gian()
    
    def __sub__(self, other):
        tu = self.__tu * other.__mau - other.__tu * self.__mau
        mau =  self.__mau * other.__mau
        return Phan_so(tu, mau).toi_gian()
    
    def __mul__(self, other):
        return Phan_so(
            self.__tu * other.__tu,
            self.__mau * other.__mau
        ).toi_gian()
    
    def __truediv__(self, other):
        if other.__tu == 0 :
            raise ZeroDivisionError("Chia phân số có tử bằng 0")
        return Phan_so(
            self.__tu * other.__mau,
            self.__mau * other.__tu
        ).toi_gian()
    
    # So sánh

    def __eq__(self, other):
        # so sánh bằng giá trị thực (quy về tối giản)
        a = self.toi_gian()
        b = other.toi_gian()
        return a.__tu == b.__tu and a.__mau == b.__mau
    
    def __lt__(self, other):
        # so sánh bằng tích chéo (tránh chia số thực)
        return self.__tu * other.__mau < other.__tu * self.__mau
    
    def __gt__(self, other):
        return self.__tu * other.__mau > other.__tu * self.__mau
    
    def __hash__(self):
        r = self.toi_gian()
        return hash((r.__tu, r.__mau))
    
    # Hiển thị

    def __str__(self):
        if self.__mau == 1:
            return str(self.__tu)
        return f"{self.__tu}/{self.__mau}"
    
    def __repr__(self):
        return f"Phan_so({self.__tu}, {self.__mau})"
    
    #Chương trình ứng dụng

# Tạo dãy phân số

ds = [Phan_so(2,4), Phan_so(3,6), Phan_so(1,3), Phan_so(5,7)]

#In ra màn hình
print("--- Dãy phân số và dạng tối giản ---")
for ps in ds:
    tg = ps.toi_gian()
    print(f" {ps} -> tối giản: {tg} (đã TG? {ps.is_toi_gian()})")

#Phép toán
print("\n --- Phép toán ---")
psa = Phan_so(1,3)
psb = Phan_so(5,7)
print(f"{psa} + {psb} = {psa + psb}")
print(f"{psa} - {psb} = {psa - psb}")
print(f"{psa} * {psb} = {psa * psb}")
print(f"{psa} / {psb} = {psa / psb}")

#Sắp xếp tăng dần
print("\n --- Sắp xếp tăng dần ---")
for ps in sorted(ds):
    tg = ps.toi_gian()
    print(f"{tg} = {ps.tu_so/ps.mau_so:.4f}")

#so sánh
print("\n --- So sánh --- ")
print(f" 2/4 == 3/6 ? {Phan_so(2,4) == Phan_so(3,6)}")
print(f" 1/3 < 5/7 ? {Phan_so(1,3) < Phan_so(5,7)}")
print(f" 5/7 < 1/3 ? {Phan_so(5,7) > Phan_so(1,3)}")

# loại trùng bằng set (dùng__hash__)
ds2 = [Phan_so(1,2), Phan_so(2,4), Phan_so(3,6)]
unique = list(set(ds2))
print(f" Trước: {[str(p) for p in ds2]}")
print(f" Sau set: {[str(p) for p in unique]}")

print("\n --- Validation ---")
try:
    ps_loi = Phan_so(5,0)
except Mau_so_bang_khong as e:
    print(f"Bắt lỗi: {e}")



        
         