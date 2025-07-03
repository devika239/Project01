import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from pdf_utils import merge_pdfs, split_pdf, extract_pages

class PDFToolUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger & Splitter Utility")

        tk.Button(root, text="Merge PDFs", command=self.merge_pdfs).pack(pady=5)
        tk.Button(root, text="Split PDF", command=self.split_pdf).pack(pady=5)
        tk.Button(root, text="Extract Pages", command=self.extract_pages).pack(pady=5)

    def merge_pdfs(self):
        files = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        if files:
            output_file = filedialog.asksaveasfilename(defaultextension=".pdf")
            if output_file:
                merge_pdfs(files, output_file)
                messagebox.showinfo("Success", f"PDFs merged and saved to {output_file}")

    def split_pdf(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            folder = filedialog.askdirectory()
            if folder:
                split_pdf(file, folder)
                messagebox.showinfo("Success", f"PDF split into pages in {folder}")

    def extract_pages(self):
        file = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file:
            page_numbers_str = simpledialog.askstring("Pages", "Enter page numbers (comma separated, e.g. 1,3,5):")
            if page_numbers_str:
                page_numbers = [int(num.strip()) for num in page_numbers_str.split(',')]
                output_file = filedialog.asksaveasfilename(defaultextension=".pdf")
                if output_file:
                    extract_pages(file, page_numbers, output_file)
                    messagebox.showinfo("Success", f"Pages extracted to {output_file}")
