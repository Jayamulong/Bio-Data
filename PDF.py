from turtle import left
from fpdf import FPDF
pdf = FPDF('P', 'mm', 'Letter')
pdf.add_page()

import json
JSONData = open('Infos.json','r')
JSONInfo = JSONData.read()
Data = json.loads(JSONInfo)

#Header
pdf.image('Pic.png', 140, 30, 50)
pdf.set_font('times', 'B', 30)
pdf.cell(0, 10, 'Bio Data', border=0, ln=True, align='C')

#Personal Information
pdf.cell(100, 8, " ", ln=True)
pdf.set_font('times', 'B', 18)
pdf.cell(150, 20, 'Personal Infomation', ln=1)
pdf.set_font('times', "I", 14)
pdf.set_text_color(r=0, g=0, b=0)
pdf.cell(12, 7, Data[0]['Name'], ln=True,)
pdf.cell(12, 7, Data[0]['Age'], ln=True,)
pdf.cell(12, 7, Data[0]['Gender'], ln=True,)
pdf.cell(12, 7, Data[0]['Address'], ln=True,)
pdf.cell(12, 7, Data[0]['Cellphone Number'], ln=True,)
pdf.cell(12, 7, Data[0]['Civil Status'], ln=True,)
pdf.cell(12, 7, Data[0]['Birth Place'], ln=True,)
pdf.cell(12, 7, Data[0]['Birth Date'], ln=True,)
pdf.cell(12, 7, Data[0]['Siblings'], ln=True,)
pdf.cell(12, 7, Data[0]['Height'], ln=True,)
pdf.cell(12, 7, Data[0]['Weight'], ln=True,)
pdf.cell(12, 7, Data[0]['Religion'], ln=True,)
pdf.cell(12, 7, Data[0]['Nationality'], ln=True,)
pdf.cell(12, 7, Data[0]['Dialect'], ln=True,)
pdf.cell(12, 7, Data[0]['Father Name'], ln=True,)
pdf.cell(12, 7, Data[0]['Father Occupation'], ln=True,)
pdf.cell(12, 7, Data[0]['Mother Name'], ln=True,)
pdf.cell(12, 7, Data[0]['Mother Occupation'], ln=True)

#Education Background
pdf.cell(100, 8, " ", ln=True)
pdf.set_font('times', 'B', 18)
pdf.cell(150, 20, 'Education Background', ln=1)
pdf.set_font('times', "I", 14)
pdf.set_text_color(r=0, g=0, b=0)
pdf.cell(12, 7, Data[0]['Elementary'], ln=True,)
pdf.cell(12, 7, Data[0]['Junior'], ln=True,)
pdf.cell(12, 7, Data[0]['Senior'], ln=True,)
pdf.cell(12, 7, Data[0]['College'], ln=True,)

pdf.output('AMULONG_JAY_ANDREY.pdf')