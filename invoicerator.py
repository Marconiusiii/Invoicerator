from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from userData import *

document = Document()

print "Invoicerator 1.1\nGenerate invoices as Word Documents.\nBy: Marco Salsiccia"
print "Who is this invoice for?"

while True:
	try:
		invClient = raw_input("Company Name >")
	except ValueError:
		print "Invalid entry. Try again."
		continue
	print "Invoice is for: {}".format(invClient)
	print "Type 'c' and hit Enter to Confirm, or just hit Enter to try again."
	try:
		choice = raw_input('>')
	except ValueError:
		continue
	if choice.lower() == 'c':
		break

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
hoursWorked = 0.00

while True:
	table.add_row()
	totalRows += 1
	print "Date of Service:"
	date = raw_input("MM/DD/YY >")
	print "Project:"
	project = raw_input(">")
	print "Hours worked in 0.25 increments:"
	hours = input(">")
	hoursWorked += hours

	print "Date: {date}, Project: {project}, Hours: {hrs}".format(date=date, project=project, hrs=hours)
	print "Does that look correct?"
	check = raw_input("y/n >")
	if check.lower().startswith('y'):
		entry = table.rows[totalRows]
		entry.cells[0].text = date
		entry.cells[1].text = project
		entry.cells[2].text = str(hours)
	else:
		print "Ok, redoing your entry."
		continue
	print "Anything more to log? y/n"
	answer = raw_input(">")
	if answer.lower().startswith('y'):
		continue
	else:
		print "Ok, finished making your invoice table."
		break

print "What is your hourly rate?"
rate = input("$>")
format(rate, '.2f')
total = hoursWorked * rate
format(total, '.2f')

print "You are owed $%i." %total

rateP = document.add_paragraph()
rateP.add_run("Rate: ").bold=True
rateP.add_run("$%r" %rate)
tHours = document.add_paragraph()
tHours.add_run("Total Hours: ").bold=True
tHours.add_run('%r' %hoursWorked)
payment = document.add_paragraph()
payment.add_run("Total Owed: ").bold=True
payment.add_run("$%r" %(total * 1.00))
document.add_paragraph()

document.add_paragraph('Total is due within 14 days of receiving this invoice.')

print "What do you want to name your invoice? .docx will be automatically appended."
filename = raw_input('>') + '.docx'
document.save(filename)

print "Invoice saved as {}. Goodbye!".format(filename)