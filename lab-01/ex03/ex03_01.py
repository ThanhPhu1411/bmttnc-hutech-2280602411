def tinh_tong_so_chan(lst):
    tong = 0 
    for num in lst :
        if num % 2 == 0:
            tong += num 
    return tong
#Giáo trình trang 48
input_list = input ("Nhập danh sách các số cách nhau bằng dấu phẩy:")
numbers = list(map(int,input_list.split(',')))            
tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chắn trong List là: ",tong_chan)