import os
from PDFParser import *
from TaskList import *


if __name__ == "__main__":

    dir_path = "data_files/download"
    tasks = TaskList()

    for name in os.listdir(dir_path):
        print(f"file: {name} | ", end="")
        name = f"{dir_path}/{name}"

        if not PDFParser.is_pdf(name):
            print("not pdf")
            continue

        text_from_pdf = PDFParser.get_text_from_pdf(name)
        tasks.add_from_pdf_txt(text_from_pdf, True)
        print("parsed")

    tasks.save_to_file("data_files/text_from_pdf.md")
    tasks.save_to_testownik("data_files/testownik_from_pdfs")
    print(tasks.print_report())