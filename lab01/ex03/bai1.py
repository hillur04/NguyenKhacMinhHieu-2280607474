def tinhtongchan(lst):
    tong = 0
    for num in lst:
        if num % 2 ==0:
            tong += num
    return tong

inputlist = input("Nhập danh sách các số, cách nhau bằng dấu phẩu:")
numbers = list(map(int,inputlist.split(',')))

tongchan = tinhtongchan(numbers)
print("Tổng các số chẵn trong List là: ",tongchan)
