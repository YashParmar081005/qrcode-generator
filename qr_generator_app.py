import customtkinter as ctk
import qrcode
from tkinter import messagebox
from PIL import ImageTk

# ---------------- App Config ----------------
ctk.set_appearance_mode("dark")   # dark / light
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("QR Code Generator")
app.geometry("450x550")
app.resizable(False, False)

# ---------------- Animation Helpers ----------------
def animate_button(btn):
    btn.configure(scale=1.05)
    app.after(150, lambda: btn.configure(scale=1))

# ---------------- QR Generator Function ----------------
def generate_qr():
    url = entry.get().strip()
    
    if not url:
        messagebox.showwarning("Input Error", "Please enter a URL or text")
        return

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=3
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#1f6aa5", back_color="white")
    img.save("qrcode.png")

    qr_img = ImageTk.PhotoImage(img)
    qr_label.configure(image=qr_img, text="")
    qr_label.image = qr_img

    animate_button(generate_btn)

# ---------------- UI Layout ----------------
title = ctk.CTkLabel(
    app,
    text="QR Code Generator",
    font=("Segoe UI", 26, "bold")
)
title.pack(pady=20)

subtitle = ctk.CTkLabel(
    app,
    text="Generate QR Codes instantly",
    font=("Segoe UI", 14),
    text_color="gray"
)
subtitle.pack(pady=5)

entry = ctk.CTkEntry(
    app,
    width=350,
    height=45,
    placeholder_text="Enter URL or any text"
)
entry.pack(pady=20)

generate_btn = ctk.CTkButton(
    app,
    text="Generate QR",
    width=200,
    height=45,
    font=("Segoe UI", 16),
    corner_radius=12,
    command=generate_qr
)
generate_btn.pack(pady=15)

qr_label = ctk.CTkLabel(
    app,
    text="Your QR will appear here",
    font=("Segoe UI", 14),
    width=300,
    height=300
)
qr_label.pack(pady=20)

footer = ctk.CTkLabel(
    app,
    text="Made with Python 💙",
    font=("Segoe UI", 12),
    text_color="gray"
)
footer.pack(side="bottom", pady=10)

# ---------------- Start App ----------------
app.mainloop()


# import qrcode

# url = input("Enter the URL: ").strip()
# file_path = "qrcode.png"

# qr = qrcode.QRCode()
# qr.add_data(url)

# img = qr.make_image()
# img.save(file_path)

# print("QR Code was generated!")