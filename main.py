# main.py
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk
from encrypt import vc_encrypt
from decrypt import vc_decrypt
from qr_utils import generate_qrcode, scan_qrcode


class VCApp:
    def __init__(self, master):
        self.master = master
        self.master.title("視覺密碼學圖片加密分享系統")
        self.master.geometry("800x700")

        # 加密按鈕：輸入助記詞 → 產生 QR → 視覺密碼分層
        btn_encrypt = tk.Button(
            master, text="輸入助記詞並加密", width=30, command=self.encrypt_flow
        )
        btn_encrypt.pack(pady=10)

        # 解密按鈕：選擇兩層圖 → 合成 → 掃描 QR
        btn_decrypt = tk.Button(
            master, text="選擇兩層圖層並解密", width=30, command=self.decrypt_flow
        )
        btn_decrypt.pack(pady=10)

        # 圖片顯示區
        self.canvas = tk.Label(master)
        self.canvas.pack(pady=20)

    def encrypt_flow(self):
        # 1. 讓使用者輸入助記詞
        text = simpledialog.askstring("輸入助記詞", "請輸入要隱寫的助記詞：")
        if not text:
            return

        # 2. 產生 QR Code
        qr_path = generate_qrcode(text)

        # 3. 進行視覺密碼學分層
        s1_path, s2_path = vc_encrypt(qr_path)

        # 4. 顯示第一層分享圖，並提示完成
        self.display_image(s1_path)
        messagebox.showinfo(
            "加密完成",
            f"已生成兩個分享圖層：\n{s1_path}\n{s2_path}"
        )

    def decrypt_flow(self):
        # 定義合法的檔案類型
        types_png = [
            ("PNG 圖片", ("*.png",)),
            ("所有檔案", "*.*"),
        ]

        # 選第一層
        s1 = filedialog.askopenfilename(
            title="選擇 Share1 圖層",
            filetypes=types_png
        )
        if not s1:
            return

        # 選第二層
        s2 = filedialog.askopenfilename(
            title="選擇 Share2 圖層",
            filetypes=types_png
        )
        if not s2:
            return

        # 合成並儲存
        result_path = vc_decrypt(s1, s2)

        # 顯示合成後影像
        self.display_image(result_path)

        # 嘗試掃描 QR Code
        text = scan_qrcode(result_path)
        if text:
            messagebox.showinfo("解密完成", f"隱寫助記詞為：{text}")
        else:
            messagebox.showwarning("解密完成", "未偵測到 QR Code")

    def display_image(self, path):
        """在介面上顯示指定路徑的圖片（縮放至 400×400）"""
        img = Image.open(path).resize((400, 400))
        tk_img = ImageTk.PhotoImage(img)
        self.canvas.configure(image=tk_img)
        self.canvas.image = tk_img  # 保持引用，避免被垃圾回收


if __name__ == '__main__':
    root = tk.Tk()
    app = VCApp(root)
    root.mainloop()