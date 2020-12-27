from ..utils.database import db

class Todo(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.Text,nullable=False)
    desc=db.Column(db.Text,nullable=False)


    def __repr__(self):
        return f"todo :{self.name}"


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


