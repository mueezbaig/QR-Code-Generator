import tkinter as tk
import pyqrcode
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import tkinter.colorchooser
from tkinter import filedialog

def generate_qr():
    url = url_entry.get()
    if not url:
        messagebox.showwarning("Warning", "Please enter a URL.")
        return
    
    color = qr_color.get()
    try:
        qr = pyqrcode.create(url)
        qr.png("qr.png", scale=8, module_color=color) 
        
        qr_image = Image.open("qr.png")
        qr_image = ImageTk.PhotoImage(qr_image)
        
        qr_label.config(image=qr_image)
        qr_label.image = qr_image
        
    except Exception as e:
        messagebox.showerror("Error", str(e))

def reset():
    url_entry.delete(0, tk.END)
    qr_label.config(image=None)
    if 'qr.png' in os.listdir():
        os.remove("qr.png")
    root.update_idletasks()  # Update the GUI


def exit_app():
    root.destroy()

def save_qr():
    if 'qr.png' in os.listdir():
        filename = tk.filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All Files", "*.*")])
        if filename:
            os.rename("qr.png", filename)
    else:
        messagebox.showinfo("Information", "No QR code generated to save.")

def copy_url():
    url = url_entry.get()
    if url:
        root.clipboard_clear()
        root.clipboard_append(url)
        root.update_idletasks()  # Update the clipboard
        messagebox.showinfo("Success", "URL copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No URL to copy!")

def choose_color():
    color = tkinter.colorchooser.askcolor()[1]
    qr_color.set(color)

root = tk.Tk()
root.title("QR CODE GENERATOR")
root.geometry("450x700")
root.configure(bg="#e6e6fa")

url_label = tk.Label(root, text="Enter URL:",width=50)
url_entry = tk.Entry(root, width=450)

qr_color = tk.StringVar(root)
qr_color.set('#000000')  # Default color is black

color_label = tk.Label(root, text="Choose Color:")
color_button = tk.Button(root, text="Pick Color",width=50, command=choose_color)
color_display = tk.Label(root, textvariable=qr_color, bg="white", relief="solid", width=6)

generate_button = tk.Button(root, text="Generate QR Code", width=50, command=generate_qr)
save_button = tk.Button(root, text="Save QR Code", width=50, command=save_qr)
copy_button = tk.Button(root, text="Copy URL", width=50, command=copy_url)
reset_button = tk.Button(root, text="Reset", width=50, command=reset)
exit_button = tk.Button(root, text="Exit", width=50, command=exit_app)

qr_label = tk.Label(root)
error_label = tk.Label(root, fg="red")

url_label.pack(pady=5)
url_entry.pack(pady=5)
color_label.pack(pady=5)
color_button.pack(pady=5)
color_display.pack(pady=5)
qr_label.pack(pady=5)
generate_button.pack(pady=5)
copy_button.pack(pady=5)
save_button.pack(pady=5)
reset_button.pack(pady=5)
exit_button.pack(pady=5)

error_label.pack(pady=5)

root.mainloop()