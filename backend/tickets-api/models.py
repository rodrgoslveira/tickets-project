from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ticket(db.Model):
    ticketId = db.Column(db.String(256), primary_key=True)
    subject = db.Column(db.String(256), index=True)
    date = db.Column(db.String(256), nullable=False)
    from_a = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(256), nullable=False)
    body = db.Column(db.String(256), nullable=False)
