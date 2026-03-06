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
Legacy mode is supported with `userData.py`.

Optional logo fields in `userData.py`:
- `userLogoPath = ""`
- `userLogoWidthInches = 1.5`
- `userLogoAltText = "M3 Logo"`

Logo behavior:
- If `userLogoPath` is empty, no logo is rendered.
- If `userLogoPath` is set, logo alt text is required.
- The logo is placed in the top-right of a 2-column header table.

## Usage
Run interactively:

```bash
python3 invoicerator.py
```

## Notes On PDF
This script only generates `.docx` invoices. PDF export remains a separate step in Word.

## What Improved
- Cleaner structure with dedicated functions and dataclasses.
- Centralized input and validation logic.
- `Decimal` arithmetic for money and hours.
- Better error handling for missing profile data and invalid input.
- Backward compatibility with existing `userData.py`.
- Automatic due date calculation from submitted date plus 30 days.
- Optional logo support with required alt text when logo is enabled.

## Roadmap Ideas
1. Add optional non-interactive flags for faster repeated invoicing.
2. Add tests for math and input validation.
3. Add stored invoice history and automatic invoice numbering.
4. Add CSV import for time entries.
