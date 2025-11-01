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
    
    def create_template(self, width=1400, height=1000):
        """
        Create an enhanced professional certificate template
        
        Args:
            width (int): Certificate width in pixels
            height (int): Certificate height in pixels
        
        Returns:
            PIL.Image: Certificate template image
        """
        # Create a new image with elegant gradient background
        img = Image.new('RGB', (width, height), color='#FDFEFE')
        draw = ImageDraw.Draw(img)
        
        # Add subtle background with light color
        draw.rectangle([(0, 0), (width, height)], fill='#F8F9F9')
        
        # Draw outer golden border
        border_color = '#D4AF37'  # Gold
        border_width = 20
        draw.rectangle(
            [(border_width//2, border_width//2), 
             (width - border_width//2, height - border_width//2)],
            outline=border_color,
            width=border_width
        )
        
        # Draw elegant double inner border
        inner_border_1 = 40
        draw.rectangle(
            [(inner_border_1, inner_border_1), 
             (width - inner_border_1, height - inner_border_1)],
            outline='#1C2833',  # Dark navy
            width=4
        )
        
        inner_border_2 = 50
        draw.rectangle(
            [(inner_border_2, inner_border_2), 
             (width - inner_border_2, height - inner_border_2)],
            outline='#5499C7',  # Royal blue
            width=2
        )
        
        # Draw decorative corner ornaments
        corner_size = 80
        corner_offset = 60
        
        # Top-left corner ornament
        draw.ellipse([(corner_offset, corner_offset), 
                     (corner_offset + corner_size, corner_offset + corner_size)], 
                    outline='#D4AF37', width=3)
        draw.line([(corner_offset, corner_offset + corner_size//2),
                  (corner_offset + corner_size, corner_offset + corner_size//2)],
                 fill='#D4AF37', width=2)
        draw.line([(corner_offset + corner_size//2, corner_offset),
                  (corner_offset + corner_size//2, corner_offset + corner_size)],
                 fill='#D4AF37', width=2)
        
        # Top-right corner ornament
        draw.ellipse([(width - corner_offset - corner_size, corner_offset), 
                     (width - corner_offset, corner_offset + corner_size)], 
                    outline='#D4AF37', width=3)
        draw.line([(width - corner_offset - corner_size, corner_offset + corner_size//2),
                  (width - corner_offset, corner_offset + corner_size//2)],
                 fill='#D4AF37', width=2)
        draw.line([(width - corner_offset - corner_size//2, corner_offset),
                  (width - corner_offset - corner_size//2, corner_offset + corner_size)],
                 fill='#D4AF37', width=2)
        
        # Bottom-left corner ornament
        draw.ellipse([(corner_offset, height - corner_offset - corner_size), 
                     (corner_offset + corner_size, height - corner_offset)], 
                    outline='#D4AF37', width=3)
        draw.line([(corner_offset, height - corner_offset - corner_size//2),
                  (corner_offset + corner_size, height - corner_offset - corner_size//2)],
                 fill='#D4AF37', width=2)
        draw.line([(corner_offset + corner_size//2, height - corner_offset - corner_size),
                  (corner_offset + corner_size//2, height - corner_offset)],
                 fill='#D4AF37', width=2)
        
        # Bottom-right corner ornament
        draw.ellipse([(width - corner_offset - corner_size, height - corner_offset - corner_size), 
                     (width - corner_offset, height - corner_offset)], 
                    outline='#D4AF37', width=3)
        draw.line([(width - corner_offset - corner_size, height - corner_offset - corner_size//2),
                  (width - corner_offset, height - corner_offset - corner_size//2)],
                 fill='#D4AF37', width=2)
        draw.line([(width - corner_offset - corner_size//2, height - corner_offset - corner_size),
                  (width - corner_offset - corner_size//2, height - corner_offset)],
                 fill='#D4AF37', width=2)
        
        # Add decorative top accent
        accent_y = 170
        accent_width = 400
        accent_x = (width - accent_width) // 2
        draw.rectangle([(accent_x, accent_y), (accent_x + accent_width, accent_y + 4)],
                      fill='#D4AF37')
        
        # Add decorative stars/diamonds near title
        star_positions = [
            (accent_x - 40, accent_y),
            (accent_x + accent_width + 35, accent_y)
        ]
        for sx, sy in star_positions:
            # Draw diamond shape
            draw.polygon([
                (sx, sy - 15),
                (sx + 15, sy),
                (sx, sy + 15),
                (sx - 15, sy)
            ], fill='#D4AF37')
        
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
        Generate a single enhanced certificate
        
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
        
        # Get enhanced fonts with better sizing
        title_font = self.get_font(85, bold=True)
        subtitle_font = self.get_font(36)
        name_font = self.get_font(65, bold=True)
        body_font = self.get_font(38)
        small_font = self.get_font(28)
        tiny_font = self.get_font(22)
        
        # Add prestigious certificate title with shadow effect
        title_y = 100
        # Shadow
        self.add_text_centered(draw, "CERTIFICATE", title_y + 2, title_font, '#95A5A6', width)
        # Main title
        self.add_text_centered(draw, "CERTIFICATE", title_y, title_font, '#1C2833', width)
        
        # Add subtitle with elegant styling
        subtitle_y = 195
        self.add_text_centered(draw, "~ OF ACHIEVEMENT ~", subtitle_y, subtitle_font, '#5499C7', width)
        
        # Add decorative line under subtitle
        line_width = 350
        line_x = (width - line_width) // 2
        draw.rectangle([(line_x, subtitle_y + 50), (line_x + line_width, subtitle_y + 53)],
                      fill='#D4AF37')
        
        # Add "This is to certify that" with better spacing
        certify_y = 310
        self.add_text_centered(draw, "This is proudly presented to", certify_y, body_font, '#34495E', width)
        
        # Add recipient name with elegant underline
        name_y = 400
        self.add_text_centered(draw, name, name_y, name_font, '#1C2833', width)
        
        # Add underline decoration for name
        bbox = draw.textbbox((0, 0), name, font=name_font)
        name_width = bbox[2] - bbox[0]
        underline_x = (width - name_width) // 2
        underline_y = name_y + 75
        draw.line([(underline_x, underline_y), (underline_x + name_width, underline_y)],
                 fill='#D4AF37', width=3)
        
        # Add course completion text
        completion_y = 505
        self.add_text_centered(draw, "for successfully completing the course", completion_y, body_font, '#34495E', width)
        
        # Add course name with prominent styling
        course_y = 585
        self.add_text_centered(draw, course, course_y, name_font, '#2874A6', width)
        
        # Add course underline
        bbox_course = draw.textbbox((0, 0), course, font=name_font)
        course_width = bbox_course[2] - bbox_course[0]
        course_underline_x = (width - course_width) // 2
        course_underline_y = course_y + 75
        draw.line([(course_underline_x, course_underline_y), 
                  (course_underline_x + course_width, course_underline_y)],
                 fill='#5499C7', width=2)
        
        # Add grade with badge-like design if provided
        y_offset = 0
        if grade:
            grade_y = 695
            y_offset = 60
            
            # Create a badge background for grade
            grade_text = f"★ GRADE: {grade} ★"
            bbox_grade = draw.textbbox((0, 0), grade_text, font=body_font)
            grade_width = bbox_grade[2] - bbox_grade[0]
            badge_padding = 30
            badge_x = (width - grade_width - badge_padding * 2) // 2
            badge_y = grade_y - 15
            
            # Draw badge background
            draw.rounded_rectangle(
                [(badge_x, badge_y), 
                 (badge_x + grade_width + badge_padding * 2, badge_y + 60)],
                radius=30,
                fill='#27AE60',
                outline='#229954',
                width=3
            )
            
            # Add grade text in white
            self.add_text_centered(draw, grade_text, grade_y, body_font, '#FFFFFF', width)
        
        # Add date with elegant formatting
        date_y = 695 + y_offset
        date_text = f"Issued on {date}"
        self.add_text_centered(draw, date_text, date_y, small_font, '#566573', width)
        
        # Add signature lines
        sig_y = height - 180
        sig_width = 250
        left_sig_x = width // 4 - sig_width // 2
        right_sig_x = 3 * width // 4 - sig_width // 2
        
        # Left signature line
        draw.line([(left_sig_x, sig_y), (left_sig_x + sig_width, sig_y)],
                 fill='#34495E', width=2)
        self.add_text_centered(draw, "Director", sig_y + 15, tiny_font, '#566573', width // 2)
        
        # Right signature line
        draw.line([(right_sig_x, sig_y), (right_sig_x + sig_width, sig_y)],
                 fill='#34495E', width=2)
        right_center = width // 2 + width // 4
        bbox_auth = draw.textbbox((0, 0), "Authorized Signature", font=tiny_font)
        auth_width = bbox_auth[2] - bbox_auth[0]
        auth_x = right_center - auth_width // 2
        draw.text((auth_x, sig_y + 15), "Authorized Signature", font=tiny_font, fill='#566573')
        
        # Add verification seal/stamp
        seal_x = width - 180
        seal_y = height - 180
        seal_radius = 60
        
        # Draw circular seal
        draw.ellipse([(seal_x - seal_radius, seal_y - seal_radius),
                     (seal_x + seal_radius, seal_y + seal_radius)],
                    outline='#C0392B', width=5)
        draw.ellipse([(seal_x - seal_radius + 10, seal_y - seal_radius + 10),
                     (seal_x + seal_radius - 10, seal_y + seal_radius - 10)],
                    outline='#C0392B', width=2)
        
        # Add "VERIFIED" text in seal
        seal_font = self.get_font(16, bold=True)
        self.add_text_centered(draw, "VERIFIED", seal_y - 8, seal_font, '#C0392B', width + (seal_x - width//2) * 2)
        
        # Add custom fields if provided
        if custom_fields:
            current_y = 780 + y_offset
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
