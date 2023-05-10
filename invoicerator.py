from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from userData import *
date = project = ""
hours = 0.0
invNumber = 0
def userEntry():
	while True:
		try:
			return input('>')
		except ValueError:
			print("Oh no! Invalid entry, try again.")


document = Document()

print("Invoicerator 1.3\nGenerate invoices as Word Documents.\nBy: Marco Salsiccia")

while True:
	print("Who is receiving this invoice?")
	invClient = userEntry()
	print(f"Invoice is for: {invClient}")
	print("Type 'c' and hit Enter to Confirm, or just hit Enter to try again.")
	try:
		choice = input('>')
	except ValueError:
		print("Invalid entry!")
	if choice.lower() == 'c':
		break

print("What's the Invoice Number?")
invNumber = userEntry()

#Begin Formatting
title = document.add_heading().add_run(userName)
titleFont = title.font
titleFont.name = 'Helvetica'
titleFont.size = Pt(18)

header = document.add_paragraph()
uTitle = header.add_run(userStreetAddress+'\n'+userCityStateZip+'\n'+userPhone+'\n'+userEmail+'\n')
underTitle = uTitle.font
underTitle.name = 'Helvetica'
underTitle.size = Pt(11)
document.add_paragraph()

document.add_heading('INVOICE', level=2).alignment=WD_ALIGN_PARAGRAPH.CENTER
document.add_paragraph()
clientP = document.add_paragraph()
inTo = clientP.add_run('Invoicing to: ')
inTo2 = clientP.add_run(invClient)
clientP.add_run('\n')
inNum = clientP.add_run('Invoice #')
inNum2 = clientP.add_run(invNumber)
fontInTo = inTo.font
fontInTo2 = inTo2.font
fontInNum = inNum.font
fontInNum2 = inNum2.font
fontInTo.name = fontInTo2.name = fontInNum.name = fontInNum2.name = 'Helvetica'
fontInTo.bold = fontInNum.bold = True

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
	print("Date of Service (MM/DD/YYYY):")
	date = userEntry()
	print("Project:")
	project = userEntry()
	print("Hours worked in 0.25 increments:")
	while True:
		try:
			hours = float(input(">"))
			break
		except ValueError:
			print("Invalid! Try again!")
	hoursWorked += hours

	print(f"Date: {date}, Project: {project}, Hours: {hours}")
	print("Does that look correct?")

	check = userEntry()
	if check.lower().startswith('y'):
		print("Great, creating entry.")
		entry = table.rows[totalRows]
		entry.cells[0].text = date
		entry.cells[1].text = project
		entry.cells[2].text = str(hours)
	else:
		print("Ok, redoing your entry.")
		continue
	print("Anything more to log? y/n ")
	while True:
		try:
			answer = input(">")
			break
		except ValueError:
			print("Whoops, you broke it. Try again.")

	if answer.lower() in ['y', 'yes']:
		continue
	else:
		print("Ok, finished making your invoice table.")
		break

print("What is your hourly rate?")
rate = int(userEntry())
format(rate, '.2f')
total = hoursWorked * rate
format(total, '.2f')

print(f"You are owed ${total:0.2F}.")

rateP = document.add_paragraph()
rt = rateP.add_run("Rate: ")
rt2 = rateP.add_run("${:0.2F}".format(rate))
rtFont = rt.font
rt2Font = rt2.font
rtFont.name = rt2Font.name = 'Helvetica'
rtFont.bold = True

tHours = document.add_paragraph()
totHours = tHours.add_run("Total Hours: ")
totHours2 = tHours.add_run('{}'.format(hoursWorked))
tH = totHours.font
tH2 = totHours2.font
tH.name = tH2.name = 'Helvetica'
tH.bold = True

payment = document.add_paragraph()
pay = payment.add_run("Total Owed: ")
pay2 = payment.add_run("${:0.2F}".format(total))
payFont = pay.font
pay2Font = pay2.font
payFont.name = pay2Font.name = 'Helvetica'
payFont.bold = True

document.add_paragraph()

late = document.add_paragraph().add_run(userLateFees)
lateFont = late.font
lateFont.name = 'Helvetica'

howToPay = document.add_paragraph().add_run(userPay)
howFont = howToPay.font
howFont.name = 'Helvetica'

print("What do you want to name your invoice? .docx will be automatically appended.")
while True:
	try:
		filename = input('>') + '.docx'
		document.save(filename)
		break
	except ValueError:
		print("That filename didn't work, try again.")

print(f"Invoice saved as {filename}. Goodbye!")