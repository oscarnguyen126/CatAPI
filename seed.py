from database import standalone_session
import csv
from models import Cat


with open("cats.csv") as file:
    reader_obj = csv.reader(file, delimiter=",")

    with standalone_session as session:
        session.begin()
        try:
            session.query(Cat).delete()
            for idx, row in enumerate(reader_obj):
                if idx == 0:
                    continue
                db_cat = Cat(breed=row[5], size=row[4], age=row[2], gender=row[3])
                session.add(db_cat)
        except:
            session.rollback()
            raise
        else:
            session.commit()
