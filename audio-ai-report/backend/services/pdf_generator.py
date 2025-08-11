from fpdf import FPDF

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()

    def add_title(self, title):
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, title, ln=True, align='C')

    def add_section(self, title, content):
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(0, 10, title, ln=True)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, content)

    def save_report(self, dimensions, generated_text):
        self.add_title("Informe Generado")
        self.add_section("Dimensiones", str(dimensions))
        self.add_section("Texto Generado", generated_text)
        self.pdf.output(self.filename)