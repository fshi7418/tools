import PyPDF2
import os


def combine_pdfs(pdf_list, output_path):
    # Create a PDF merger object
    merger = PyPDF2.PdfMerger()

    # Loop through all the PDFs in the list
    for pdf in pdf_list:
        with open(pdf, 'rb') as f:
            # Append each PDF to the merger
            merger.append(f)

    # Write out the combined PDF to a file
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)


# Example usage:
pdfs_path = '/home/franks/Documents/Applications/Permanent Resident Travel Document 2025/赵泉霖永久居民签证申请材料'
os.chdir(pdfs_path)
pdf_list = ['赵泉霖出入境记录.pdf', '赵泉霖出入境记录英文.pdf', ]  # Replace with your actual PDF file paths
output_path = 'applicant_entry_exit_records.pdf'  # The file path of the output PDF
combine_pdfs(pdf_list, output_path)
