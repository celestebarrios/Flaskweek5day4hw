from avengers import app, db
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    names = db.Column(db.String(150),nullable=False,unique=True)
    number = db.Column(db.String(20),nullable=False,unique=True)

    def __init__(self, names):
        self.names = names
        self.number = number
    def __repr__(self):
        return f'{self.names} : {self.number}'