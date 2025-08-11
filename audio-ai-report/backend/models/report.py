from sqlalchemy import Column, Integer, String, Text
from backend.database.session import Base

class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, autoincrement=True)
    audio_file_path = Column(String(255), nullable=False)
    transcription_text = Column(Text, nullable=False)
    generated_report = Column(Text, nullable=False)
    created_at = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Report(id={self.id}, audio_file_path={self.audio_file_path}, created_at={self.created_at})>"