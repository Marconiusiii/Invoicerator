# Invoicerator
Python-based invoice generator for Terminal that outputs Word `.docx` files.

## Current Behavior
- Builds invoice documents with `python-docx`.
- Runs as an interactive CLI workflow in Terminal.
- Does not perform PDF conversion.

## Dependencies
Install with:

```bash
pip install -r requirements.txt
```

## Profile Setup
Recommended setup:

```bash
cp user_profile.example.json user_profile.json
```

Then edit `user_profile.json` with your details.

Legacy mode is still supported with `userData.py`.

## Usage
Run interactively:

```bash
python3 invoicerator.py
```

Use an explicit profile and output path:

```bash
python3 invoicerator.py --profile user_profile.json --output invoices/acme-mar-2026.docx
```

## Notes On PDF
This script only generates `.docx` invoices. PDF export remains a separate step in Word.

## What Improved
- Cleaner structure with dedicated functions and dataclasses.
- Centralized input and validation logic.
- `Decimal` arithmetic for money and hours.
- Better error handling for missing profile data and invalid input.
- Backward compatibility with existing `userData.py`.

## Roadmap Ideas
1. Add optional non-interactive flags for faster repeated invoicing.
2. Add tests for math and input validation.
3. Add stored invoice history and automatic invoice numbering.
4. Add CSV import for time entries.
