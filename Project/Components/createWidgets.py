import tkinter as tk
from PIL import ImageFilter


def create_widgets(self, load_image, apply_filter, reset_image, save_image):
    # load_button = tk.Button(
    #     text="Carregar Imagem",
    #     command=load_image,
    #     bg="#007bff",
    #     fg="#ffffff",
    #     font=("Arial", 12),
    #     padx=10,
    #     pady=5,
    # )
    # load_button.pack(pady=10)

    # image_label = tk.Label(bg="#e6f7ff")
    # image_label.pack(pady=10)

    # filters_frame = tk.Frame(bg="#e6f7ff")
    # filters_frame.pack(pady=20)

    # filters = [
    #     ("Blur", ImageFilter.BLUR),
    #     ("Contour", ImageFilter.CONTOUR),
    #     ("Edge Enhance", ImageFilter.EDGE_ENHANCE),
    #     ("Emboss", ImageFilter.EMBOSS),
    #     ("Sharpen", ImageFilter.SHARPEN),
    #     ("Smooth", ImageFilter.SMOOTH),
    # ]

    # for filter_name, filter_type in filters:
    #     tk.Button(
    #         filters_frame,
    #         text=filter_name,
    #         command=lambda ft=filter_type: apply_filter(ft),
    #         bg="#007bff",
    #         fg="#ffffff",
    #         font=("Arial", 12),
    #         padx=10,
    #         pady=5,
    #     ).pack(side="left", padx=10, pady=5)

    # buttons_frame = tk.Frame(bg="#e6f7ff")
    # buttons_frame.pack(pady=10)

    # reset_button = tk.Button(
    #     buttons_frame,
    #     text="Reset Image",
    #     command=reset_image,
    #     bg="#007bff",
    #     fg="#ffffff",
    #     font=("Arial", 12),
    #     padx=10,
    #     pady=5,
    # )
    # reset_button.pack(side="left", pady=10)

    # save_button = tk.Button(
    #     buttons_frame,
    #     text="Save Image",
    #     command=save_image,
    #     bg="#007bff",
    #     fg="#ffffff",
    #     font=("Arial", 12),
    #     padx=10,
    #     pady=5,
    # )
    # save_button.pack(side="left", pady=10)

    ##########################################

    self.load_button = tk.Button(
        self.root,
        text="Carregar Imagem",
        command=self.load_image,
        bg="#007bff",
        fg="#ffffff",
        font=("Arial", 12),
        padx=10,
        pady=5,
    )
    self.load_button.pack(pady=10)

    self.image_label = tk.Label(self.root, bg="#e6f7ff")
    self.image_label.pack(pady=10)

    self.filters_frame = tk.Frame(self.root, bg="#e6f7ff")
    self.filters_frame.pack(pady=20)

    filters = [
        ("Blur", ImageFilter.BLUR),
        ("Contour", ImageFilter.CONTOUR),
        ("Edge Enhance", ImageFilter.EDGE_ENHANCE),
        ("Emboss", ImageFilter.EMBOSS),
        ("Sharpen", ImageFilter.SHARPEN),
        ("Smooth", ImageFilter.SMOOTH),
    ]

    for filter_name, filter_type in filters:
        tk.Button(
            self.filters_frame,
            text=filter_name,
            command=lambda ft=filter_type: self.apply_filter(ft),
            bg="#007bff",
            fg="#ffffff",
            font=("Arial", 12),
            padx=10,
            pady=5,
        ).pack(side="left", padx=10, pady=5)

    self.buttons_frame = tk.Frame(self.root, bg="#e6f7ff")
    self.buttons_frame.pack(pady=10)

    self.reset_button = tk.Button(
        self.buttons_frame,
        text="Reset Image",
        command=self.reset_image,
        bg="#007bff",
        fg="#ffffff",
        font=("Arial", 12),
        padx=10,
        pady=5,
    )
    self.reset_button.pack(side="left", pady=10)

    self.save_button = tk.Button(
        self.buttons_frame,
        text="Save Image",
        command=self.save_image,
        bg="#007bff",
        fg="#ffffff",
        font=("Arial", 12),
        padx=10,
        pady=5,
    )
    self.save_button.pack(side="left", pady=10)
