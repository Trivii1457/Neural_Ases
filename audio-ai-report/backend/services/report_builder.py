from .nlp_pipeline import NLPipeline
from .pdf_generator import PDFGenerator
from ..models.report import Report
from ..database.session import SessionLocal

class ReportBuilder:
    def __init__(self):
        self.nlp_pipeline = NLPipeline()
        self.pdf_generator = PDFGenerator()

    def build_report(self, audio_transcription):
        # Process the transcription through the NLP pipeline
        report_data = self.nlp_pipeline.process_transcription(audio_transcription)

        # Create a report instance
        report = Report(**report_data)

        # Save the report to the database
        self.save_report_to_db(report)

        # Generate PDF report
        pdf_path = self.pdf_generator.generate_pdf(report)

        return report, pdf_path

    def save_report_to_db(self, report):
        db = SessionLocal()
        try:
            db.add(report)
            db.commit()
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()