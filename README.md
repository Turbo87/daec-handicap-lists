# DAeC Handicap Lists Generator

Generates handicap lists for gliding competitions in Germany (Deutscher Aero Club).

## Quick Start

```bash
# Generate all lists
cargo run

# Generate only DMSt lists
cargo run -- --skip-competition

# Generate only competition lists
cargo run -- --skip-dmst
```

## Input Files

- `gliderlist.csv`: DMSt handicaps
- `competition.csv`: Competition handicaps

## Output

Generated files are placed in `output/`:

- `dmst.html` / `dmst.pdf`
- `competition.html` / `competition.pdf`

## Development

```bash
# Run tests
cargo test

# Update snapshots after intentional changes
cargo insta accept

# Format code
cargo fmt

# Sort competition.csv
python3 sort_competition.py
```

## Requirements

- Rust 1.70+
- Chrome/Chromium (for PDF generation)
- Python 3 (for CSV sorting utility)
