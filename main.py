# vc_image_encryptor/main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from encrypt import vc_encrypt
from decrypt import vc_decrypt
from qr_utils import generate_qrcode, scan_qrcode


class VCApp:
    def __init__(self, master):
        self.master = master
        self.master.title("視覺密碼學圖片加密分享系統")
        self.master.geometry("800x700")

        self.image_path = None
        self.share1_path = None
        self.share2_path = None

        tk.Button(master, text="選擇圖片進行加密", command=self.load_image).pack(pady=10)
        tk.Button(master, text="合成 Share 圖解密圖片", command=self.combine_images).pack(pady=10)

        self.text_entry = tk.Entry(master, width=50)
        self.text_entry.pack(pady=10)
        tk.Button(master, text="輸入文字生成 VC QR 圖", command=self.generate_qr_shares).pack(pady=10)

        self.canvas = tk.Label(master)
        self.canvas.pack(pady=20)

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.bmp")])
        if not path:
            return
        self.image_path = path
        s1, s2 = vc_encrypt(self.image_path)
        self.share1_path, self.share2_path = s1, s2
        messagebox.showinfo("加密完成", f"已生成：\n{s1}\n{s2}")
        self.display_image(s1)

    def combine_images(self):
        s1_path = filedialog.askopenfilename(title="選擇 Share1", filetypes=[("PNG Files", "*.png")])
        if not s1_path:
            return
        s2_path = filedialog.askopenfilename(title="選擇 Share2", filetypes=[("PNG Files", "*.png")])
        if not s2_path:
            return
        result = vc_decrypt(s1_path, s2_path)
        messagebox.showinfo("解密完成", f"已合成：{result}")
        self.display_image(result)
        text = scan_qrcode(result)
        if text:
            messagebox.showinfo("QR 掃描結果", f"內容為：{text}")

    def generate_qr_shares(self):
        text = self.text_entry.get()
        if not text:
            messagebox.showwarning("錯誤", "請輸入要生成 QRCode 的文字")
            return
        qr_path = generate_qrcode(text)
        s1, s2 = vc_encrypt(qr_path)
        self.display_image(s1)
        messagebox.showinfo("VC QR 圖生成成功", f"QR 圖已分層為：\n{s1}\n{s2}")

    def display_image(self, path):
        img = Image.open(path).resize((400, 400))
        tk_img = ImageTk.PhotoImage(img)
        self.canvas.configure(image=tk_img)
        self.canvas.image = tk_img


if __name__ == '__main__':
    root = tk.Tk()
    app = VCApp(root)
    root.mainloop()
