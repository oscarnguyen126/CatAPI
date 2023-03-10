from fastapi import HTTPException
import math


DEFAULT_LIMIT = 100


class CRUD:
    def __init__(self, model, db):
        self.model = model
        self.db = db
        self.query = db.query(model)

    def set_query(self, query):
        self.query = query

    def get_all(self):
        return self.query.limit(DEFAULT_LIMIT).all()

    def paginate(self, limit=DEFAULT_LIMIT, offset=0):
        total = self.query.count()
        objs = self.query.offset(offset).limit(limit).all()
        page = math.ceil(int(offset) / int(limit)) if limit and offset else 1
        pages = math.ceil(total / int(limit)) if limit else 1

        return {
            "page": page,
            "pages": pages,
            "total": len(objs),
            "items": [obj.to_dict() for obj in objs],
        }

    def get_by_id(self, id):
        res = self.query.filter(self.model.id == id).first()
        if not res:
            raise HTTPException(
                status_code=404,
                detail=f"{self.model.__tablename__} with id {id} is not exist",
            )
        return res

    def find(self, conditions):
        res = self.query.filter_by(**conditions).first()
        # if not res:
        #     raise HTTPException(
        #         status_code=404,
        #         detail=f"{self.model.__tablename__} with id {id} is not exist",
        #     )
        return res

    def create(self, obj):
        persisted_obj = self.model(**obj.dict())
        self.db.add(persisted_obj)
        self.db.commit()
        return persisted_obj

    def update(self, id, obj):
        persisted_obj = self.get_by_id(id)
        self.query.filter_by(id=id).update(obj.dict())
        self.db.commit()
        self.db.refresh(persisted_obj)
        return persisted_obj

    def delete(self, id):
        persisted_obj = self.get_by_id(id)
        self.db.delete(persisted_obj)
        self.db.commit()
        return f"{persisted_obj} is deleted"
