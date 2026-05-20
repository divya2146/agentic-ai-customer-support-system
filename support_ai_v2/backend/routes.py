from fastapi import APIRouter
from pydantic import BaseModel

from services.ticket_service import TicketService

router = APIRouter()

ticket_service = TicketService()


class TicketRequest(BaseModel):
    customer_name: str
    issue: str


@router.post("/tickets")
def create_ticket(ticket: TicketRequest):

    result = ticket_service.create_ticket(
        ticket.customer_name,
        ticket.issue
    )

    return result


@router.get("/tickets")
def get_tickets():

    return ticket_service.get_tickets()