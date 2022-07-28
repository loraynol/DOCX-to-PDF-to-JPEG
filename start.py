from msilib import sequence
import pathlib
from docx2pdf import convert
from pdf2image import convert_from_path
from pathlib import Path
import glob
import os



dir_path = pathlib.Path().absolute() #得知目前Python所在的資料夾

convert(dir_path) #將此資料夾轉換成pdf

pdfs = glob.glob("*.pdf") #pdfs = 檔名list

pdfamount = len(pdfs) #pdfamount = pdf檔案數量

for i in range(pdfamount): 

    images = convert_from_path(pdfs[i], dpi=500, jpegopt={"quality": 100}, output_folder=None,  fmt='jpeg')
    for j in range(len(images)):
	    images[j].save(str(pdfs[i]).replace(".pdf","") +'.jpg', 'JPEG')

