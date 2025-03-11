#Nhập số từ người dùng 
so = int (input("Nhập một số nguyên :"))
#Kiểm tra số đó có chẵn hay không'
if so % 2 == 0:
    print(so,"Là Số chẵn")
else: 
    print(so,"Không phải là số chẵn.")