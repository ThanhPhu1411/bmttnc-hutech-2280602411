def tinh_tong_so_chan(lst):
    sum = 0
    for num in lst:
        if num % 2 == 0:
            sum += num
    return sum
input_list = input("Nhập dãy số, cách nhau bởi dấu phẩy: ")
numbers = list(map(int,input_list.split(",")))
tong_chan= tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong list là:", tong_chan)
