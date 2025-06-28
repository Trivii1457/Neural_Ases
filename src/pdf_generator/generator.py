from fpdf import FPDF

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename

    def create_pdf(self, content):
        

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for paragraph in content:
            pdf.multi_cell(0, 10, paragraph)
            pdf.ln()

        pdf.output(self.filename)

    def save_report(self, dimensions, generated_texts):
        content = []
        for dimension, text in zip(dimensions, generated_texts):
            content.append(f"Dimension: {dimension}\n{text}\n")
        
        self.create_pdf(content)