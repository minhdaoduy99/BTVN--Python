import tkinter as tk
from tkinter import messagebox

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x380")
cua_so.resizable(False, False)

bien_hien_thi = tk.StringVar(value="")

def bam_nut(ky_tu):
    bieu_thuc_hien_tai = bien_hien_thi.get()
    bien_hien_thi.set(bieu_thuc_hien_tai + str(ky_tu))

def xoa_toan_bo():
    bien_hien_thi.set("")

def xoa_mot_ky_tu():
    bieu_thuc = bien_hien_thi.get()
    bien_hien_thi.set(bieu_thuc[:-1])

def tinh_ket_qua():
    bieu_thuc = bien_hien_thi.get().strip()
    if not bieu_thuc:
        return
    try:
        ket_qua = eval(bieu_thuc)
        if isinstance(ket_qua, float) and ket_qua.is_integer():
            ket_qua = int(ket_qua)
        bien_hien_thi.set(str(ket_qua))
    except ZeroDivisionError:
        messagebox.showerror("Loi", "Khong the chia cho 0")
        bien_hien_thi.set("")
    except Exception:
        messagebox.showerror("Loi", "Bieu thuc khong hop le")
        bien_hien_thi.set("")

entry_hien_thi = tk.Entry(
    cua_so,
    textvariable=bien_hien_thi,
    font=("Arial", 18),
    justify="right",
    bd=5,
    relief="sunken"
)
entry_hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=8, sticky="nsew")

danh_sach_nut = [
    ("C", 1, 0, xoa_toan_bo),
    ("<-", 1, 1, xoa_mot_ky_tu),
    ("(", 1, 2, lambda: bam_nut("(")),
    ("/", 1, 3, lambda: bam_nut("/")),

    ("7", 2, 0, lambda: bam_nut("7")),
    ("8", 2, 1, lambda: bam_nut("8")),
    ("9", 2, 2, lambda: bam_nut("9")),
    ("*", 2, 3, lambda: bam_nut("*")),

    ("4", 3, 0, lambda: bam_nut("4")),
    ("5", 3, 1, lambda: bam_nut("5")),
    ("6", 3, 2, lambda: bam_nut("6")),
    ("-", 3, 3, lambda: bam_nut("-")),

    ("1", 4, 0, lambda: bam_nut("1")),
    ("2", 4, 1, lambda: bam_nut("2")),
    ("3", 4, 2, lambda: bam_nut("3")),
    ("+", 4, 3, lambda: bam_nut("+")),

    ("0", 5, 0, lambda: bam_nut("0")),
    (".", 5, 1, lambda: bam_nut(".")),
    (")", 5, 2, lambda: bam_nut(")")),
    ("=", 5, 3, tinh_ket_qua),
]

for text, r, c, cmd in danh_sach_nut:
    btn = tk.Button(
        cua_so,
        text=text,
        font=("Arial", 12, "bold"),
        width=5,
        height=2,
        command=cmd
    )
    btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

if __name__ == "__main__":
    cua_so.mainloop()
