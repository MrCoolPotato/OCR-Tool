import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract
import os

class ImageOCRApp:
    def __init__(self, master):
        self.master = master
        self.master.title("OCR Tool")

        
        self.master.geometry("1200x800")
        self.master.resizable(False, False)

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        
        self.image_label = tk.Label(self.master)
        self.text_display = tk.Text(self.master, wrap="word", height=50, width=120)
        self.select_image_button = tk.Button(self.master, text="Select Image", command=self.select_image_ocr)

        
        self.image_label.pack(pady=10)
        self.select_image_button.pack(pady=5)
        self.text_display.pack(side=tk.LEFT, pady=10)

    def select_image_ocr(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            try:
                self.display_image(file_path)
                extracted_text = self.perform_image_ocr(file_path)
                self.text_display.insert(tk.END, extracted_text + "\n")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def perform_image_ocr(self, image_path):
        try:
            image = Image.open(image_path)
            extracted_text = pytesseract.image_to_string(image)
            return extracted_text
        except Exception as e:
            raise Exception("Error performing OCR: " + str(e))

    def display_image(self, image_path):
        try:
            img = Image.open(image_path)
            img.thumbnail((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.image_label.configure(image=img)
            self.image_label.image = img
        except Exception as e:
            raise Exception("Error displaying image: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageOCRApp(root)
    root.mainloop()