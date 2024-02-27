import os
import PyPDF2


def compress_pdf(input_path, output_path):
    with open(input_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)

        # Create a PdfWriter object to write the compressed PDF
        writer = PyPDF2.PdfWriter()

        # Copy pages from input PDF to output PDF
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            page.compress_content_streams()
            writer.add_page(page)

        # Write the output PDF with compression
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)


input_path_ = r'/home/franks/Documents/Important Documents'
output_path_ = input_path_
input_file_ = 'Yi Zhao Citizenship Certificate.pdf'
output_file_ = 'Yi Zhao Citizenship Certificate_compressed.pdf'
compress_pdf(os.path.join(input_path_, input_file_), os.path.join(output_path_, output_file_))
