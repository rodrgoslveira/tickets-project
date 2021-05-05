import sys
from flask import Flask, jsonify, request, url_for
from marshmallow.exceptions import ValidationError
from schemas import ma, ticket_schema, tickets_schema
from models import db, Ticket
from const import *

app = Flask(__name__)
#initialization
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ticket.db"
db.init_app(app)
ma.init_app(app)
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
#Views
#GET METHODS
@app.route("/", methods=["GET"])
@app.route("/getTickets", methods=["GET"])
def list_tickets():
    tickets = Ticket.query.all()
    return after_request(tickets_schema.jsonify(tickets))

@app.route("/tickets/<string:id>", methods=["GET"])
def get_ticket(id):
    ticket = Ticket.query.filter(Ticket.ticketId==id).first_or_404()
    return after_request(tickets_schema.jsonify(tickets))

#POST, PUT, DELETE METHODS
@app.route("/tickets", methods=["POST"])
def create_ticket():
    try:
        ticket = ticket_schema.load(request.form, instance=ticket)
    except ValidationError as errors:
        response = jsonify(errors.messages)
        response.status_code = HttpStatus.BAD_REQUEST
        return response

    db.session.add(ticket)
    db.session.commit()
    response = jsonify({"message": "created"})
    location = url_for("get_ticket", id = ticket.ticketId)
    resp.status_code = HttpStatus.CREATED
    response.headers["Location"] = location
    return resp

@app.route("/tickets/<string:id>", methods=["PUT"])
def edit_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    try:
        ticket = ticket_schema.load(request.form, instance=ticket)
    except ValidationError as errors:
        response = jsonify(errors.messages)
        response.status_code = HttpStatus.BAD_REQUEST
        return response

    db.session.add(ticket)
    db.session.commit()
    response = jsonify({"message": "updated"})
    response.status_code = HttpStatus.OK
    return response

@app.route("/tickets/<string:id>", methods=["DELETE"])
def delete_ticket(id):
    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    response = jsonify({"message": "deleted"})
    response.status_code = HttpStatus.OK
    return response

#config and run
if __name__ == "__main__":
    if "createdb" in sys.argv:
        with app.app_context():
            db.create_all()
        print("Database created!")

    elif "seeddb" in sys.argv:
        with app.app_context():
            ticket_one = Ticket(ticketId= "xk3d03",
                        subject= "Hola, mi item esta roto",
                        date= "2020-03-01 01:30:00Z",
                        from_a= "Joaquin Perez",
                        status= "SOLVED",
                        body= "Mi producto llego roto, no funcionacomo debería",)
            ticket_two = Ticket(ticketId= "xx35",
                        subject= "Hola, mi item no llego",
                        date= "2020-03-02 05:30:00Z",
                        from_a= "Romina Esperanto",
                        status= "NEW",
                        body= "Mi producto no llegó, cuando deberíallegar?",)
            ticket_tre = Ticket(ticketId= "xx",
                        subject= "Hola, dde",
                        date= "2020-03-02 05:30:00Z",
                        from_a= "Romina Esperanto",
                        status= "NEW",
                        body= "Mi producto no llegó, cuando deberíallegar?",)
            db.session.add(ticket_one)
            db.session.add(ticket_two)
            db.session.add(ticket_tre)
            db.session.commit()
        print("Database seeded!")

    else:
        app.run(debug=True)
