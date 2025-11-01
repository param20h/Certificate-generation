# Certificate Generator System

An automated system to generate professional certificates from CSV data.

## Features

- ✅ Generate certificates from CSV file
- ✅ Customizable certificate template
- ✅ Support for multiple fields (name, course, date, grade, etc.)
- ✅ Professional certificate design with borders and decorations
- ✅ Batch processing for multiple recipients
- ✅ PNG output format with high quality

## Requirements

- Python 3.7+
- Pillow (PIL)
- pandas

## Installation

1. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

1. Prepare your CSV file with the following columns:
   - `name` (required): Recipient's name
   - `course` (optional): Course name
   - `date` (optional): Completion date
   - `grade` (optional): Grade achieved
   - Any additional custom fields

2. Run the script:
```bash
python generate_certificates.py
```

3. Find generated certificates in the `certificates` folder

### CSV Format Example

```csv
name,course,date,grade
John Smith,Python Programming,November 2 2025,A+
Emma Johnson,Web Development,November 2 2025,A
Michael Brown,Data Science,November 2 2025,A-
```

### Custom Usage

```python
from generate_certificates import CertificateGenerator

# Initialize generator
generator = CertificateGenerator(
    csv_file="your_data.csv",
    output_folder="output_certificates"
)

# Generate all certificates
generator.generate_all()

# Or generate a single certificate
certificate = generator.generate_certificate(
    name="John Doe",
    course="Advanced Python",
    date="November 2, 2025",
    grade="A+"
)
certificate.save("john_doe_cert.png")
```

## Certificate Template

The default template includes:
- Professional border design
- Decorative corner elements
- Centered text layout
- Color-coded sections
- High-quality PNG output (1200x900 pixels)

### Using a Custom Template

You can use your own certificate template image:

```python
generator = CertificateGenerator(
    csv_file="data.csv",
    template_path="my_template.png"
)
```

## Output

- Format: PNG
- Resolution: 1200x900 pixels (default)
- Naming: `{RecipientName}_certificate.png`
- Location: `certificates/` folder

## Customization

### Modify Certificate Design

Edit the `create_template()` method in `generate_certificates.py` to customize:
- Colors
- Border styles
- Dimensions
- Layout

### Add More Fields

Simply add columns to your CSV file. The system automatically includes them on the certificate.

## Troubleshooting

**Issue: Font not found**
- The script uses fallback fonts automatically
- For best results, ensure Arial or Calibri is installed on your system

**Issue: CSV file not found**
- Make sure `sample_data.csv` is in the same directory as the script
- Or specify the full path to your CSV file

## License

MIT License - Feel free to use and modify for your needs!

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.
