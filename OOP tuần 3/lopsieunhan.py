class Sieu_nhan:
    def __init__(self, ten: str, vukhi: str, mausac: str):
        self.ten = ten
        self.vukhi = vukhi 
        self.mausac = mausac

    def __str__(self):
        return (f"Siêu nhân {self.ten}| "
                f"Vũ khí  {self.vukhi}|"
                f"Màu sắc{self.mausac}|")
    
Sieu_nhan_A = Sieu_nhan("Tomato","Quả cà chua","Đỏ")
Sieu_nhan_B = Sieu_nhan("Cuồng phong","Quạt","Xanh nước biển")
Sieu_nhan_C = Sieu_nhan("Deadline","Tài liệu (có thể là 1 chồng tài liệu)","Vàng")

print (Sieu_nhan_A)
print (Sieu_nhan_B)
print (Sieu_nhan_C)
    

    