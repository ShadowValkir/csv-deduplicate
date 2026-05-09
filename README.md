# CSV Deduplicate

A small Python utility to remove duplicate rows from CSV files and save a cleaned output.

## Features

- Remove duplicate rows based on full-row comparison
- Preserve original CSV structure
- Easy command-line usage

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shadowvalkir/csv-deduplicate.git
   cd csv-deduplicate
   ```
2. Install dependencies:
   ```bash
   python3 -m pip install -r requirements.txt
   ```

## Usage

> **Warning:** Overwriting the input file will permanently remove duplicate rows from your original data. Make sure to back up your file if you may need the original version.

Run the script with the input CSV file and optionally specify an output file:

Example:
```bash
python deduplicate.py input.csv -o output.csv
```

> **Danger:** If no output file is specified, the original file will be overwritten by default.
```bash
python deduplicate.py input.csv # input.csv is overwritten
```

## Notes

- Ensure the input file is a valid CSV.
- Duplicates are removed based on exact row matches.