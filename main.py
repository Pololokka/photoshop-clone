import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter


class ImageEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GeoShop")
        self.root.geometry("1000x600")
        self.root.configure(bg="#e6f7ff")

        self.original_image = None
        self.image = None
        self.image_tk = None

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )

        if file_path:
            self.original_image = Image.open(file_path)
            self.image = self.original_image.copy()
            self.display_image()

    def display_image(self):
        if self.image:
            aspect_ratio = self.image.width / self.image.height
            new_width = 600
            new_height = int(new_width / aspect_ratio)
            self.image_tk = ImageTk.PhotoImage(
                self.image.resize((new_width, new_height), Image.LANCZOS)
            )
            self.image_label.config(image=self.image_tk)
