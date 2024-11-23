import PyPDF2
import os


def remove_pdf_password(input_pdf, output_pdf, password):
    # Open the input PDF file
    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Check if the PDF is encrypted
        if reader.is_encrypted:
            # Try to decrypt the PDF with the provided password
            try:
                reader.decrypt(password)
            except Exception as e:
                print(f"Failed to decrypt PDF: {e}")
                return

        # Create a writer object for the output PDF
        writer = PyPDF2.PdfWriter()

        # Add all pages to the writer
        for page in range(len(reader.pages)):
            writer.add_page(reader.pages[page])

        # Write the output PDF without a password
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

    print(f"Password removed. New PDF saved as: {output_pdf}")


# Example usage
pdfs_path = r'/home/franks/Documents/Applications/Wencai Visitor Visa/Funding'
os.chdir(pdfs_path)
input_pdf_path = 'Huaxia Bank Trading Record.pdf'  # Path to the input PDF file
output_pdf_path = 'Huaxia Bank Trading Record Decrypted.pdf'  # Path to save the output PDF file
pdf_password = '810939'  # Password for the input PDF

remove_pdf_password(input_pdf_path, output_pdf_path, pdf_password)
