# 🔐 AES-256 File Encryptor Tool

This is a simple and secure desktop application to **encrypt and decrypt files** using the AES-256 encryption algorithm. It provides a **graphical user interface (GUI)** for ease of use and automatically deletes the original/encrypted files after processing.

---

## 🚀 Features

- AES-256 encryption with password protection 🔐
- GUI-based interface (Tkinter)
- Auto-deletes original file after encryption
- Auto-deletes `.enc` file after decryption
- Clean and minimal design

---

## 🛠️ Requirements

- Python 3.6 or higher
- Dependencies (install with pip):
  ```bash
  pip install pycryptodome
  ```

---

## 📦 How to Run

1. Clone or download the ZIP of this project.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tool:
   ```bash
   python main.py
   ```

---

## 🧪 How It Works

- **Encrypt File**: Select a file → It will be encrypted and saved as `<filename>.enc`. Original file is deleted.
- **Decrypt File**: Select a `.enc` file → It will be decrypted and saved as `<filename>.dec`. Encrypted file is deleted.
- You can rename `.dec` file to original extension (e.g., `.jpg`, `.pdf`)

---

## ⚠️ Important

- Keep your password safe — there is no password recovery.
- The tool does not retain metadata about original file extension. You must rename `.dec` files manually.

---

## 👨‍💻 Author

- **Author**: Vikas Lalchand Mallah  
- **Email**: vikas.malllah@dyptmail.edu.in  
- **Institution**: DY Patil International University  
