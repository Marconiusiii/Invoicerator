from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from userData import *

document = Document()

print "Invoicerator 1.0\nGenerate invoices as Word Documents."
print "Who is this invoice for?"
invClient = raw_input("Company Name >")


document.add_heading(userName)

header = document.add_paragraph()
header.add_run(userStreetAddress+'\n')
header.add_run(userCityStateZip+'\n')
header.add_run(userPhone+'\n')
header.add_run(userEmail+'\n')

document.add_paragraph()

document.add_heading('INVOICE', level=2).alignment=WD_ALIGN_PARAGRAPH.CENTER
document.add_paragraph()
clientP = document.add_paragraph()
clientP.add_run('Invoicing to: ').bold=True
clientP.add_run(invClient)

table = document.add_table(rows=1, cols=3)

headerCells = table.rows[0].cells
headerCells[0].text = 'Date'
headerCells[1].text = 'Project'
headerCells[2].text = 'Hours'

totalRows = 0
hoursWorked = 0

while True:
	table.add_row()
	totalRows += 1
	print "Date of Service:"
	date = raw_input("mm/dd/yy >")
	print "Project:"
	project = raw_input(">")
	print "Hours worked:"
	hours = raw_input(">")
	hoursWorked += int(hours)

	print "Date: %s, Project: %s, Hours: %s" %(date, project, hours)
	entry = table.rows[totalRows]
	entry.cells[0].text = date
	entry.cells[1].text = project
	entry.cells[2].text = hours
	print "Anything more to log? y/n"
	answer = raw_input(">")
	if answer.lower().startswith('y'):
		continue
	else:
		print "Ok, finished making your invoice table."
		break

print "What is your hourly rate?"
rate = input("$>")
total = hoursWorked * rate
print "You are owed $%d." %total

rateP = document.add_paragraph()
rateP.add_run("Rate: ").bold=True
rateP.add_run("$%d" %rate)
tHours = document.add_paragraph()
tHours.add_run("Total Hours: ").bold=True
tHours.add_run('%s' %hoursWorked)
payment = document.add_paragraph()
payment.add_run("Total Owed: ").bold=True
payment.add_run("$%d" %total)
document.add_paragraph()

document.add_paragraph('Total is due within 30 days of receiving this invoice.')

print "What do you want to name your invoice? .docx will be automatically appended."
filename = raw_input('>') + '.docx'
document.save(filename)

print "Invoice saved as %s. Goodbye!" %filename