from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO
import re

def generate_pdf(template_html):
    try:
        pdf = BytesIO()
        doc = SimpleDocTemplate(pdf, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Strip HTML tags and get plain text
        clean_text = re.sub(r'<[^>]+>', ' ', template_html)
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()

        # Add content to PDF
        story.append(Paragraph("Smartcart Invoice", styles['Title']))
        story.append(Spacer(1, 20))
        story.append(Paragraph(clean_text, styles['Normal']))

        doc.build(story)
        pdf.seek(0)
        return pdf

    except Exception as e:
        print(f"PDF generation error: {e}")
        return None