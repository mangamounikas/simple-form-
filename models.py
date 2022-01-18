from simpleform.db import Database
db= Database().db

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(120))

    def __repr__(self) -> str:
        return str(self.id)