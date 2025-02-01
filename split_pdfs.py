import PyPDF2
import os


def split_pdf(input_pdf_, split_page, output_pdf1, output_pdf2):
    # Open the PDF file
    with open(input_pdf_, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        total_pages = len(reader.pages)

        # Create writers for both parts
        writer1 = PyPDF2.PdfWriter()
        writer2 = PyPDF2.PdfWriter()

        # Add pages to first part (from 0 to split_page - 1)
        for i in range(split_page):
            writer1.add_page(reader.pages[i])

        # Add pages to second part (from split_page to end)
        for i in range(split_page, total_pages):
            writer2.add_page(reader.pages[i])

        # Save first PDF
        with open(output_pdf1, "wb") as output1:
            writer1.write(output1)

        # Save second PDF
        with open(output_pdf2, "wb") as output2:
            writer2.write(output2)

    print(f'PDF split successfully into {output_pdf1} and {output_pdf2}')


# Example usage:
pdfs_path = r'/home/franks/Documents/'
os.chdir(pdfs_path)

input_pdf = 'input.pdf'  # The file path of the output PDF
split_pdf1 = 'output1.pdf'
split_pdf2 = 'output2.pdf'
split_pdf(input_pdf, 1, split_pdf1, split_pdf2)
