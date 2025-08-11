from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.session import Base
from backend.models.report import Report

DATABASE_URL = "sqlite:///./test.db"  # Cambiar a la URL de la base de datos real

def seed_database():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear las tablas
    Base.metadata.create_all(engine)

    # Sembrar datos iniciales
    sample_report = Report(
        title="Informe de Prueba",
        content="Este es un informe de prueba generado automáticamente.",
        created_at=datetime.utcnow()
    )

    session.add(sample_report)
    session.commit()
    session.close()

if __name__ == "__main__":
    seed_database()