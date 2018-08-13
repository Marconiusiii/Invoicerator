from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
document = Document()

document.add_heading('Marco Salsiccia')

header = document.add_paragraph()
header.add_run("901 Santiago St.\n")
header.add_run("San Francisco CA 94116\n")
header.add_run('408-314-5401\n')
header.add_run('marco.salsiccia@gmail.com')
document.add_paragraph()

document.add_heading('Invoice', level=2).alignment=WD_ALIGN_PARAGRAPH.CENTER

print "Invoicerator 1.0\nGenerate invoices as Word Documents."
print "Who is this invoice for?"
invClient = raw_input("Company Name >")
clientP = document.add_paragraph('Invoicing to: ')
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
	print "Client:"
	client = raw_input(">")
	print "Hours worked:"
	hours = raw_input(">")
	hoursWorked += int(hours)

	print "Date: %s, Client: %s, Hours: %s" %(date, client, hours)
	entry = table.rows[totalRows]
	entry.cells[0].text = date
	entry.cells[1].text = client
	entry.cells[2].text = hours
	print "Anything more to log?"
	answer = raw_input("y/n")
	if answer == 'y':
		continue
	else:
		print "Ok, finished making your table."
		break
rate = input("What is your rate? >")
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
document.save('GeneratedInvoice.docx')