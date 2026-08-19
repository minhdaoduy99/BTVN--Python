import keyword

ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Ten:", ten)
print("Diem toan:", diem_toan)
print("Diem van:", diem_van)
print("So luong mon hoc:", so_luong_mon_hoc)
print("Muc luong toi thieu:", MUC_LUONG_TOI_THIEU)
print()

print(keyword.kwlist)
print("So luong tu khoa:", len(keyword.kwlist))
print()

a = 17
b = 5
print("Bai 5.1:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print()

diem = 6.5
tuoi = 20
print("Bai 5.2:")
la_kha = diem >= 6.5 and diem < 8.0
chua_du_18_hoac_tren_60 = tuoi < 18 or tuoi > 60
phu_dinh = not (diem >= 6.5 and diem < 8.0)
print("Diem loai kha:", la_kha)
print("Tuoi chua du 18 hoac tren 60:", chua_du_18_hoac_tren_60)
print("Phu dinh dieu kien diem:", phu_dinh)
print()

x = 10
print("Bai tap 5.3:")
x += 5
print("x sau += 5:", x)
x -= 3
print("x sau -= 3:", x)
x *= 2
print("x sau *= 2:", x)
x /= 4
print("x sau /= 4:", x)
x //= 2
print("x sau //= 2:", x)
x **= 3
print("x sau **= 3:", x)

danh_sach = [1, 2, 3, "python"]
print("3 in danh_sach:", 3 in danh_sach)

list1 = [1, 2, 3]
list2 = list1
print("list1 is list2:", list1 is list2)
print()

print("Bai 5.4:")
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)
print()

print("Bai 6.1:")
bien = 10
print(bien, type(bien))
bien = "Xin chao"
print(bien, type(bien))
bien = 3.14
print(bien, type(bien))
bien = True
print(bien, type(bien))
print()

print("Bai 6.2:")
ho_ten = "Nguyen Van A"
diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))
