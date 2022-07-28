import pathlib
from docx2pdf import convert
from pdf2image import convert_from_path
from pathlib import Path
import glob
import os

dir_path = pathlib.Path().absolute()   #Get the path of where the Code is put    取得目前這個 Python 程式所在的資料夾

convert(dir_path)   #Convert all DOCX in this folder to PDF    將此資料夾的所有DOCX轉換成PDF

pdfs = glob.glob("*.pdf")   #pdfs = Get a list of all PDF files in this folder    取得所有這個資料夾裡面的 PDF 並且把它做成一個 list

pdfamount = len(pdfs) #Get the amount of PDF in the folder    取得這個資料夾內 PDF 的數量

for i in range(pdfamount):   #A loop to get all PDF converted and saved    一個迴圈讓所有的 PDF 都能被轉換跟命名
    images = convert_from_path(pdfs[i], dpi=500, jpegopt={"quality": 100}, output_folder=None,  fmt='jpeg')   #covert the PDF to JPEG    將 PDF 轉換成 JPEG 
    for j in range(len(images)): 
	    images[j].save(str(pdfs[i]).replace(".pdf","") +'.jpg', 'JPEG')   #Save the JPEG you've converted in to a .jpg file    將你轉換的 JPEG 儲存下來

