# Invoicerator
Python-based invoice generator for Terminal that outputs Word `.docx` files.

## Current Behavior
- Builds invoice documents with `python-docx`.
- Runs as an interactive CLI workflow in Terminal.
- Supports full CSV-driven invoice data entry with `--csv`.
- Does not perform PDF conversion.

## Dependencies
Install with:

```bash
pip install -r requirements.txt
```

## Profile Setup
You can use either profile format. JSON is recommended.

### JSON profile (recommended)
1. Create your local profile file:

```bash
cp user_profile.example.json user_profile.json
```

2. Edit `user_profile.json` and fill in your values.
3. `user_profile.json` is ignored by git and should stay local.

### Legacy Python profile
1. Create your local legacy profile file:

```bash
cp userData.example.py userData.py
```

2. Edit `userData.py` and fill in your values.
3. `userData.py` is ignored by git and should stay local.

### Optional logo fields
Both profile formats support optional logo settings:
- `logo_path` / `userLogoPath`
- `logo_width_inches` / `userLogoWidthInches`
- `logo_alt_text` / `userLogoAltText`

Logo behavior:
- If logo path is empty, no logo is rendered.
- If logo path is set, alt text is required.
- The logo is placed in the top-right of a 2-column header table.
- Accessibility metadata is written as image description (`descr`), with image title left empty to avoid duplicate announcements.

## Usage
Run interactively:

```bash
python3 invoicerator.py
```

Run from CSV:

```bash
python3 invoicerator.py --csv invoice_entries.example.csv
```

Use explicit output file:

```bash
python3 invoicerator.py --csv invoice_entries.example.csv --output invoices/may-2026.docx
```

## CSV Format
Use one CSV file with two sections: metadata and entries, separated by a blank line.

```csv
Key,Value
Client,Acme Corp
InvoiceNumber,2026-05-001
HourlyRate,125
SubmittedDate,05/15/2026
Output,invoices/may-2026

Date,Project,Hours
05/01/2026,Accessibility audit prep,1.5
05/03/2026,Client meeting,0.75
05/04/2026,Invoice revision,2.0
```

Rules:
- Required metadata keys: `Client`, `InvoiceNumber`, `HourlyRate`, `SubmittedDate`, `Output`
- The `Output` value is the output filename or path. `.docx` is appended automatically if needed.
- `--output` overrides the CSV `Output` value when both are provided.
- Entries header must be exactly: `Date,Project,Hours`
- Date format: `MM/DD/YYYY`
- Hours must be in `0.25` increments
- If project text contains commas, quote the field

## Notes On PDF
This script only generates `.docx` invoices. PDF export remains a separate step in Word.
