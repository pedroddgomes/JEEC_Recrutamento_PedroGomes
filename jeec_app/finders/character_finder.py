from jeec_app.models.character import Character

class CharacterFinder:
    @classmethod
    def get_from_id(cls, id):
        query, session = Character.get_query()
        try:
            result = query.filter_by(id=id).first()
            return result
        finally:
            session.close()
    
    @classmethod
    def get_by_name(cls, name):
        query, session = Character.get_query()
        try:
            return query.filter(Character.name.ilike(f"%{name}%")).all()
        finally:
            session.close()

    @classmethod
    def get_by_age(cls, age):
        query, session = Character.get_query()
        try:
            return query.filter_by(age=age).all()
        finally:
            session.close()
    
    @classmethod
    def get_by_birthday(cls, birthday):
        query, session = Character.get_query()
        try:
            return query.filter(Character.birthday.ilike(f"%{birthday}%")).all()
        finally:
            session.close()

    @classmethod
    def get_by_gender(cls, gender):
        query, session = Character.get_query()
        try:
            return query.filter(Character.gender.ilike(f"%{gender}%")).all()
        finally:
            session.close()

    @classmethod
    def get_by_alive(cls, alive):
        query, session = Character.get_query()
        try:
            return query.filter_by(alive=alive).all()
        finally:
            session.close()

    @classmethod
    def get_all(cls):
        query, session = Character.get_query()
        try:
            return query.order_by(Character.id).all()
        finally:
            session.close()
