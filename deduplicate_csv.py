import argparse
import pandas as pd

def deduplicate_csv(input_file, output_file, subset=None):
    if output_file == input_file:
        confirmation = input(f"Are you sure you want to overwrite '{input_file}'? (yes/no): ").strip().lower()
        if confirmation not in ('yes', 'y'):
            print("Operation cancelled.")
            return

    df = pd.read_csv(input_file)
    deduplicated_df = df.drop_duplicates(subset=subset)
    removed = len(df) - len(deduplicated_df)
    deduplicated_df.to_csv(output_file, index=False)
    print(f"Removed {removed} duplicate rows ({len(df)} → {len(deduplicated_df)})")
    print(f"Deduplicated CSV saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deduplicate a CSV file.")
    parser.add_argument("input_file", help="Path to the input CSV file.")
    parser.add_argument("-o", "--output_file", default=None, help="Path to save the deduplicated CSV file. If omitted, the input file will be overwritten.")
    parser.add_argument("-s", "--subset", nargs="+", default=None, help="Column name(s) to deduplicate on. If omitted, all columns are used.")
    args = parser.parse_args()

    deduplicate_csv(
        input_file=args.input_file,
        output_file=args.output_file or args.input_file,
        subset=args.subset,
    )
