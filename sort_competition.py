#!/usr/bin/env python3
"""
Sort competition.csv by handicap (descending) and model name (ascending).
"""

import csv
from pathlib import Path


def sort_competition_csv(competition_file):
    """Sort the competition.csv by handicap and model name."""
    rows = []

    # Read the current competition.csv
    with open(competition_file, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            rows.append(row)

    # Sort by handicap (descending) and then by model name (ascending, case-insensitive)
    rows.sort(key=lambda r: (-int(r['Handicap']) if r['Handicap'] else 0, r['Model'].lower()))

    # Write the sorted data back with Unix line endings
    with open(competition_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)

    return len(rows)


def main():
    """Main execution function."""
    script_dir = Path(__file__).parent
    competition_file = script_dir / 'competition.csv'

    # Check file exists
    if not competition_file.exists():
        print(f"Error: {competition_file} not found")
        return 1

    print("Sorting competition.csv...")
    row_count = sort_competition_csv(competition_file)

    print(f"✓ Sorted {row_count} rows by handicap (descending) and model name (ascending)")

    return 0


if __name__ == '__main__':
    exit(main())
