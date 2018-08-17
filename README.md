# Invoicerator
Python-based Invoice Generator

## Dependencies

This little app uses the python-docx API, so be sure to install it using the requirements file or by running:

$ pip install python-docx

## What it does

Invoicerator will generate an easy-to-read invoice putting your name and information at the top of the file, set up a table with columns for Date, Project, and Hours worked, ask you for your hourly rate, prompt you for a filename to save it out, and finish up by creating a .docx file for you to send out to the client.

## How to use it

1. Open Terminal/iTerm and navigate to the directory where you've placed the Invoicerator files.
2. Open the userData.py file and fill in the variables with your information. Save and close.
3. Run Invoicerator with the $python invoicerator.py command.
4. You'll be prompted to put in the name of your client. Type it in and hit Enter.
5. The generated invoice table takes in a Date, Project name, and Hours worked. Enter each of these when prompted. An entry will be displayed followed by a prompt asking if you have more to log. Hitting Yes will repeat the process and add one more row to your table. Entering No will continue to the next step.
6. Enter your hourly rate.
7. You'll be prompted for a filename. Enter it here and hit Enter to finish the generation process. A Word document with the filename will appear in the same directory as Invoicerator.
8. Email that off to your client and wait for your money to roll in!

