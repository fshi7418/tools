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
pdfs_path = r'/home/franks/Documents/Applications/Permanent Resident Travel Document 2025/赵泉霖永久居民签证申请材料/护照全部/赵泉霖'
os.chdir(pdfs_path)

input_pdf = 'passport part 1-25.pdf'  # The file path of the output PDF
split_pdf1 = 'passport part 1-25 real.pdf'
split_pdf2 = 'passport part 26.pdf'
split_pdf(input_pdf, 13, split_pdf1, split_pdf2)
