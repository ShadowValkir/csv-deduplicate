import argparse
import pandas as pd

def deduplicate_csv(input_file, overwrite=False, output_file=None):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file)

    if overwrite:
        output_file = input_file
        # Ask for confirmation before overwriting
        confirmation = input(f"Are you sure you want to overwrite '{input_file}'? (yes/no): ").strip().lower()
        if confirmation not in ('yes', 'y'):
            print("Operation cancelled.")
            return

    # Drop duplicate rows based on all columns
    deduplicated_df = df.drop_duplicates()

    # Save the deduplicated DataFrame to a new CSV file
    deduplicated_df.to_csv(output_file, index=False)
    print(f"Deduplicated CSV saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deduplicate a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("-o", "--output_file", default=None, help="Path to save the deduplicated CSV file. If omitted, the input file will be overwritten.")
    args = parser.parse_args()

    should_overwrite = args.output_file is None

    deduplicate_csv(
        input_file=args.input_file,
        overwrite=should_overwrite,
        output_file=args.output_file or args.input_file
    )