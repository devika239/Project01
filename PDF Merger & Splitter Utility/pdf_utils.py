import PyPDF2

def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def split_pdf(pdf_path, output_folder):
    reader = PyPDF2.PdfReader(pdf_path)
    for i in range(len(reader.pages)):
        writer = PyPDF2.PdfWriter()
        writer.add_page(reader.pages[i])
        output_filename = f"{output_folder}/page_{i+1}.pdf"
        with open(output_filename, 'wb') as out:
            writer.write(out)

def extract_pages(pdf_path, page_numbers, output_path):
    reader = PyPDF2.PdfReader(pdf_path)
    writer = PyPDF2.PdfWriter()
    for num in page_numbers:
        writer.add_page(reader.pages[num - 1])
    with open(output_path, 'wb') as out:
        writer.write(out)

