



giolam= float(input("Nhập số giờ làm việc 1 tuần của nhân viên:"))
luong = int(input("Nhập mức lương tiêu chuẩn 1 giờ của nhân viên:"))
luongtieuchuan = float(44*luong)
luongtangca = float( luong * 1.5 * (giolam - 44))
if(giolam > 44):
    luongthucnhan = float(luongtieuchuan + luongtangca)
else:
    luongthucnhan = luongtieuchuan

print("Lương thực nhận của nhân viên là: ",luongthucnhan,"nghìn đồng")


