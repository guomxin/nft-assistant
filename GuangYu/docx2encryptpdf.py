import sys
from docx2pdf import convert
from PyPDF2 import PdfFileWriter, PdfFileReader

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("{} <tag>".format(sys.argv[0]))
        sys.exit(1)
    tag = sys.argv[1]
    docx_file_name = "data/日交易额_{}.docx".format(
        tag
    )
    pdf_file_name = "data/日交易额_{}.pdf".format(
        tag
    ) 
    
    convert(docx_file_name, pdf_file_name)
    # 禁掉pdf的各种权限（包括复制）
    pdf_reader = PdfFileReader(pdf_file_name)
    pdf_writer = PdfFileWriter()
    for pi in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(pi)
        watermark = PdfFileReader("watermark.pdf")
        wm_page = watermark.pages[0]
        wm_page.mergePage(page)
        pdf_writer.addPage(wm_page)
    pdf_writer.encrypt("", "shuang", permissions_flag = 0)
    with open(pdf_file_name, "wb") as out:
        pdf_writer.write(out)