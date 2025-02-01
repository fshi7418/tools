import PyPDF2
import os


def combine_pdfs(pdf_list_, output_path_):
    # Create a PDF merger object
    merger = PyPDF2.PdfMerger()

    # Loop through all the PDFs in the list
    for pdf in pdf_list_:
        with open(pdf, 'rb') as f:
            # Append each PDF to the merger
            merger.append(f)

    # Write out the combined PDF to a file
    with open(output_path_, 'wb') as output_file:
        merger.write(output_file)


# Example usage:
pdfs_path = '/home/franks/Documents/'
os.chdir(pdfs_path)
pdf_list = ['pdf1.pdf', 'pdf2.pdf', ]  # Replace with your actual PDF file paths
output_path = 'output.pdf'  # The file path of the output PDF
combine_pdfs(pdf_list, output_path)
