import PyPDF2
import sys


template = PyPDF2.PdfFileReader(open('super.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)


with open('watermarked_output.pdf','wb')as file:
	output.write(file)








# input_file = "super.pdf"
# output_file = "watermarked.pdf"
# watermark_file = "wtr.pdf"


# with open(input_file, "rb") as filehandle_input:
#     # read content of the original file
#     pdf = PyPDF2.PdfFileReader(filehandle_input)
#     with open(watermark_file, "rb") as filehandle_watermark:
#         # read content of the watermark
#         watermark = PyPDF2.PdfFileReader(filehandle_watermark)

#         # get first page of the original PDF
#         first_page = pdf.getPage(0)

#         # get first page of the watermark PDF
#         first_page_watermark = watermark.getPage(0)

#         # merge the two pages
#         first_page.mergePage(first_page_watermark)

#         # create a pdf writer object for the output file
#         pdf_writer = PyPDF2.PdfFileWriter()

#         # add page
#         pdf_writer.addPage(first_page)

#         with open(output_file, "wb") as filehandle_output:
#             # write the watermarked file to the new file
#             pdf_writer.write(filehandle_output)

# #write water.pdf on all pdf pages
# #grab the file
# #read the file with PyPdf2 reader
# #loop through super and merge each page with the watermark pdf

# with open('super.pdf','wb') as file:
# 	merger = PyPDF2.PdfFileMerger()
#  	for page in file:
#  		with open('wtr.pdf', 'rb') as wtr_mark:
#  			merger.append(page)


# inputs = sys.argv[1:]
# def pdf_combiner(pdf_list):
# 	merger = PyPDF2.PdfFileMerger()
# 	for pdf in pdf_list:
# 		print(pdf)
# 		merger.append(pdf)

# 	merger.write('super.pdf')

# pdf_combiner(inputs)


# grab the file
# with open('dummy.pdf','rb') as file:
# 	reader = PyPDF2.PdfFileReader(file)
# 	page = reader.getPage(0)
# 	page.rotateCounterClockwise(90)
# 	writer = PyPDF2.PdfFileWriter()
# 	writer.addPage(page)
# 	with open('tilt.pdf','wb') as new_file:
# 		writer.write(new_file)
