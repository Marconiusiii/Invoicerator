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
