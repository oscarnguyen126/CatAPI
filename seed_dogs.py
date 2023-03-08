from libs.database import standalone_session
import csv
from routers.dogs.models import Dog


with open("./seed_data/dog_breeds.csv") as file:
    reader_obj = csv.reader(file, delimiter=",")

    with standalone_session as session:
        session.begin()
        try:
            session.query(Dog).delete()
            for idx, row in enumerate(reader_obj):
                if idx == 0:
                    continue
                db_dog = Dog(
                    breed=row[0],
                    origin=row[1],
                    color=row[2],
                    height=row[3],
                    eyes_color=row[4],
                    longevity=row[5],
                    character=row[6],
                    health_problems=row[7],
                )
                session.add(db_dog)
        except:
            session.rollback()
            raise
        else:
            session.commit()
