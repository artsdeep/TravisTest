from mod import db

class Base(db.Model):
    __abstract__  = True
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,  default=db.func.current_timestamp())

class Client(Base):
    __tablename__ = 'client'
    name = db.Column(db.String(128),  nullable=False)