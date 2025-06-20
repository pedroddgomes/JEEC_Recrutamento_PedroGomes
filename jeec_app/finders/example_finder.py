from jeec_app.models.example import Example

class ExampleFinder:
    @classmethod
    def get_from_id(cls, id):
        query, session = Example.get_query()
        try:
            result = query.filter_by(id=id).first()
            return result
        finally:
            session.close()

    @classmethod
    def get_all(cls):
        query, session = Example.get_query()
        try:
            return query.order_by(Example.id).all()
        finally:
            session.close()
