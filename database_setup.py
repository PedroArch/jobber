from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# SQLAlchemy object init
Base = declarative_base()





# End of File
if __name__ == "__main__":
    # Creating DB
    engine = create_engine("sqlite:///jobber.db")
    Base.metadata.create_all(engine)
