def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
#Sử dụng hàm và in kết quả 
intput_string = input("Mời nhập chuỗi cần đảo ngược:")
print("Chuỗi đảo ngược là :",dao_nguoc_chuoi(intput_string))