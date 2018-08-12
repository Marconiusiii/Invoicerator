from docx import Document

document = Document()


document.add_heading('Invoice Generation')
table = document.add_table(rows=1, cols=3)

headerCells = table.rows[0].cells
headerCells[0].text = 'Date'
headerCells[1].text = 'Project'
headerCells[2].text = 'Hours'

totalRows = 0
while True:
	table.add_row()
	totalRows += 1
	print "Date of Service:"
	date = raw_input("mm/dd/yy >")
	print "Client:"
	client = raw_input(">")
	print "Hours worked:"
	hours = raw_input(">")
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
		print "Ok, saving."
		break

document.save('invoiceGen.docs')