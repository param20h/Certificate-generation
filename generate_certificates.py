"""
Certificate Generator - Automated Certificate Creation from CSV
Author: Auto-Generated
Date: November 2, 2025
"""

import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
from pathlib import Path


class CertificateGenerator:
    """Generate certificates from CSV data"""
    
    def __init__(self, csv_file, output_folder="certificates", template_path=None):
        """
        Initialize the certificate generator
        
        Args:
            csv_file (str): Path to CSV file with recipient data
            output_folder (str): Folder to save generated certificates
            template_path (str): Path to custom certificate template (optional)
        """
        self.csv_file = csv_file
        self.output_folder = output_folder
        self.template_path = template_path
        
        # Create output folder if it doesn't exist
        Path(output_folder).mkdir(parents=True, exist_ok=True)
        
        # Load CSV data
        self.data = pd.read_csv(csv_file)
        print(f"Loaded {len(self.data)} records from {csv_file}")
    
    def create_template(self, width=1200, height=900):
        """
        Create a basic certificate template
        
        Args:
            width (int): Certificate width in pixels
            height (int): Certificate height in pixels
        
        Returns:
            PIL.Image: Certificate template image
        """
        # Create a new image with white background
        img = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(img)
        
        # Draw border
        border_color = '#2C3E50'
        border_width = 15
        draw.rectangle(
            [(border_width, border_width), 
             (width - border_width, height - border_width)],
            outline=border_color,
            width=border_width
        )
        
        # Draw inner border
        inner_border = 30
        draw.rectangle(
            [(inner_border, inner_border), 
             (width - inner_border, height - inner_border)],
            outline='#3498DB',
            width=3
        )
        
        # Draw decorative corners
        corner_size = 60
        corner_color = '#E74C3C'
        positions = [
            (inner_border + 10, inner_border + 10),
            (width - inner_border - corner_size - 10, inner_border + 10),
            (inner_border + 10, height - inner_border - corner_size - 10),
            (width - inner_border - corner_size - 10, height - inner_border - corner_size - 10)
        ]
        
        for x, y in positions:
            draw.rectangle([(x, y), (x + corner_size, y + corner_size)], 
                          fill=corner_color)
        
        return img
    
    def get_font(self, size, bold=False):
        """
        Get font with fallback options
        
        Args:
            size (int): Font size
            bold (bool): Use bold font if available
        
        Returns:
            ImageFont: Font object
        """
        font_options = [
            # Windows fonts
            "C:/Windows/Fonts/arial.ttf",
            "C:/Windows/Fonts/calibri.ttf",
            "C:/Windows/Fonts/times.ttf",
            # Linux fonts
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
            # Mac fonts
            "/System/Library/Fonts/Helvetica.ttc",
        ]
        
        if bold:
            font_options = [
                "C:/Windows/Fonts/arialbd.ttf",
                "C:/Windows/Fonts/calibrib.ttf",
                "C:/Windows/Fonts/timesbd.ttf",
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                "/System/Library/Fonts/Helvetica.ttc",
            ] + font_options
        
        for font_path in font_options:
            try:
                return ImageFont.truetype(font_path, size)
            except:
                continue
        
        # Fallback to default font
        return ImageFont.load_default()
    
    def add_text_centered(self, draw, text, y_position, font, color='black', img_width=1200):
        """
        Add centered text to image
        
        Args:
            draw: ImageDraw object
            text (str): Text to add
            y_position (int): Y coordinate for text
            font: Font object
            color (str): Text color
            img_width (int): Image width for centering
        """
        # Get text bounding box
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x_position = (img_width - text_width) // 2
        
        draw.text((x_position, y_position), text, font=font, fill=color)
    
    def generate_certificate(self, name, course, date, grade="", custom_fields=None):
        """
        Generate a single certificate
        
        Args:
            name (str): Recipient name
            course (str): Course name
            date (str): Completion date
            grade (str): Grade achieved (optional)
            custom_fields (dict): Additional custom fields
        
        Returns:
            PIL.Image: Generated certificate
        """
        # Create or load template
        if self.template_path and os.path.exists(self.template_path):
            img = Image.open(self.template_path).copy()
        else:
            img = self.create_template()
        
        draw = ImageDraw.Draw(img)
        width, height = img.size
        
        # Get fonts
        title_font = self.get_font(70, bold=True)
        subtitle_font = self.get_font(30)
        name_font = self.get_font(55, bold=True)
        body_font = self.get_font(35)
        small_font = self.get_font(25)
        
        # Add certificate title
        self.add_text_centered(draw, "CERTIFICATE", 120, title_font, '#2C3E50', width)
        self.add_text_centered(draw, "OF ACHIEVEMENT", 200, subtitle_font, '#34495E', width)
        
        # Add "This is to certify that"
        self.add_text_centered(draw, "This is to certify that", 300, body_font, '#2C3E50', width)
        
        # Add recipient name (highlighted)
        self.add_text_centered(draw, name, 380, name_font, '#E74C3C', width)
        
        # Add course completion text
        self.add_text_centered(draw, "has successfully completed", 470, body_font, '#2C3E50', width)
        self.add_text_centered(draw, course, 540, name_font, '#3498DB', width)
        
        # Add grade if provided
        y_offset = 0
        if grade:
            self.add_text_centered(draw, f"with grade: {grade}", 630, body_font, '#27AE60', width)
            y_offset = 50
        
        # Add date
        self.add_text_centered(draw, f"Date: {date}", 630 + y_offset, small_font, '#7F8C8D', width)
        
        # Add custom fields if provided
        if custom_fields:
            current_y = 700 + y_offset
            for key, value in custom_fields.items():
                self.add_text_centered(draw, f"{key}: {value}", current_y, small_font, '#7F8C8D', width)
                current_y += 35
        
        return img
    
    def generate_all(self):
        """Generate certificates for all records in CSV"""
        print(f"\nGenerating certificates...")
        print("-" * 50)
        
        for index, row in self.data.iterrows():
            # Get required fields
            name = row['name']
            course = row.get('course', 'Course Completion')
            date = row.get('date', 'November 2, 2025')
            grade = row.get('grade', '')
            
            # Get custom fields (any columns not in standard fields)
            standard_fields = ['name', 'course', 'date', 'grade']
            custom_fields = {k: v for k, v in row.items() 
                           if k not in standard_fields and pd.notna(v)}
            
            # Generate certificate
            certificate = self.generate_certificate(
                name=name,
                course=course,
                date=date,
                grade=grade,
                custom_fields=custom_fields if custom_fields else None
            )
            
            # Save certificate
            safe_name = "".join(c for c in name if c.isalnum() or c in (' ', '-', '_')).strip()
            filename = f"{safe_name}_certificate.png"
            filepath = os.path.join(self.output_folder, filename)
            
            certificate.save(filepath, 'PNG', quality=95)
            print(f"✓ Generated: {filename}")
        
        print("-" * 50)
        print(f"✓ Successfully generated {len(self.data)} certificates!")
        print(f"✓ Saved to: {os.path.abspath(self.output_folder)}")


def main():
    """Main function to run certificate generation"""
    print("=" * 50)
    print("Certificate Generator")
    print("=" * 50)
    
    # Configuration
    csv_file = "sample_data.csv"
    output_folder = "certificates"
    
    # Check if CSV file exists
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found!")
        print("Please create a CSV file with columns: name, course, date, grade")
        return
    
    # Create generator and generate certificates
    generator = CertificateGenerator(csv_file, output_folder)
    generator.generate_all()
    
    print("\n✓ Done!")


if __name__ == "__main__":
    main()
