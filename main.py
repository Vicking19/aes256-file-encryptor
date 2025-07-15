import tkinter as tk
from tkinter import filedialog, messagebox
from crypto_utils import encrypt_file, decrypt_file

def encrypt_action():
    file_path = filedialog.askopenfilename()
    if file_path:
        password = password_entry.get()
        if not password:
            messagebox.showerror("Error", "Enter password")
            return
        try:
            encrypt_file(file_path, password)
            messagebox.showinfo("Success", "File encrypted and original deleted!")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

def decrypt_action():
    file_path = filedialog.askopenfilename()
    if file_path:
        password = password_entry.get()
        if not password:
            messagebox.showerror("Error", "Enter password")
            return
        try:
            decrypt_file(file_path, password)
            messagebox.showinfo("Success", "File decrypted and .enc deleted!")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

app = tk.Tk()
app.title("AES-256 File Encryptor")
app.geometry("400x200")

tk.Label(app, text="Enter Password:").pack(pady=5)
password_entry = tk.Entry(app, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(app, text="Encrypt File", command=encrypt_action, width=25).pack(pady=10)
tk.Button(app, text="Decrypt File", command=decrypt_action, width=25).pack(pady=5)

app.mainloop()
