from flask_marshmallow import Marshmallow
from models import Ticket

ma = Marshmallow()


class TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ticket
        load_instance = True

ticket_schema = TicketSchema()
tickets_schema = TicketSchema(many=True)
