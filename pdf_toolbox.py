import os
from tkinter import *
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger
from PIL import Image
import fitz  # PyMuPDF


# -------------- MERGE PDF FUNCTIONS --------------

pdf_list = []

def add_pdfs():
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    for f in files:
        if f not in pdf_list:
            pdf_list.append(f)
            merge_listbox.insert(END, os.path.basename(f))

def clear_list():
    pdf_list.clear()
    merge_listbox.delete(0, END)

def merge_pdfs():
    if not pdf_list:
        messagebox.showwarning("No Files", "Please add at least one PDF.")
        return

    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save merged PDF as"
    )
    if not output_file:
        return  # user cancelled

    try:
        merger = PdfMerger()
        for pdf in pdf_list:
            merger.append(pdf)

        merger.write(output_file)
        merger.close()
        messagebox.showinfo("Success", f"PDFs merged successfully!\n\nSaved as:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong while merging:\n{e}")


# -------------- PDF → IMAGES FUNCTIONS --------------

def pdf_to_images():
    pdf_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if not pdf_path:
        return

    out_dir = filedialog.askdirectory(
        title="Select folder to save images"
    )
    if not out_dir:
        return

    try:
        doc = fitz.open(pdf_path)
        base_name = os.path.splitext(os.path.basename(pdf_path))[0]

        for page_index in range(len(doc)):
            page = doc[page_index]
            pix = page.get_pixmap(dpi=150)
            out_name = f"{base_name}_page_{page_index+1}.png"
            out_path = os.path.join(out_dir, out_name)
            pix.save(out_path)

        doc.close()
        messagebox.showinfo(
            "Success",
            f"PDF converted to images successfully!\n\nSaved in:\n{out_dir}"
        )
    except Exception as e:
        messagebox.showerror("Error", f"Error converting PDF to images:\n{e}")


# -------------- IMAGES → PDF FUNCTIONS --------------

def images_to_pdf():
    image_files = filedialog.askopenfilenames(
        title="Select image files (in order)",
        filetypes=[
            ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"),
            ("All Files", "*.*")
        ]
    )
    if not image_files:
        return

    output_file = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Save PDF as"
    )
    if not output_file:
        return

    try:
        # Open and convert all images to RGB
        images = [Image.open(img_path).convert("RGB") for img_path in image_files]

        first_image = images[0]
        rest_images = images[1:]

        first_image.save(output_file, save_all=True, append_images=rest_images)
        messagebox.showinfo("Success", f"Images merged into PDF!\n\nSaved as:\n{output_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Error converting images to PDF:\n{e}")


# -------------- GUI SETUP --------------

root = Tk()
root.title("PDF Toolbox - Merge & Convert")
root.geometry("500x500")

title_label = Label(root, text="📄 PDF Toolbox", font=("Segoe UI", 16, "bold"))
title_label.pack(pady=10)


# ---- Merge PDFs Section ----
merge_frame = LabelFrame(root, text="Merge PDFs", padx=10, pady=10)
merge_frame.pack(fill="x", padx=10, pady=5)

Label(merge_frame, text="Selected PDF files:", font=("Segoe UI", 9, "bold")).pack(anchor="w")

merge_listbox = Listbox(merge_frame, width=55, height=8)
merge_listbox.pack(padx=5, pady=5)

merge_btn_frame = Frame(merge_frame)
merge_btn_frame.pack(pady=5)

Button(merge_btn_frame, text="Add PDFs", width=12, command=add_pdfs).grid(row=0, column=0, padx=5)
Button(merge_btn_frame, text="Clear List", width=12, command=clear_list).grid(row=0, column=1, padx=5)
Button(merge_frame, text="Merge to PDF", width=20, command=merge_pdfs).pack(pady=5)


# ---- Converters Section ----
convert_frame = LabelFrame(root, text="Converters", padx=10, pady=10)
convert_frame.pack(fill="x", padx=10, pady=10)

Button(convert_frame, text="PDF ➜ Images", width=20, height=2, command=pdf_to_images).pack(pady=5)
Button(convert_frame, text="Images ➜ PDF", width=20, height=2, command=images_to_pdf).pack(pady=5)

Label(root, text="Tip: For best results, keep all PDFs and images closed while converting.",
      fg="gray").pack(pady=10)

root.mainloop()

