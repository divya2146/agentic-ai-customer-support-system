from pydantic import BaseModel


class TicketCreate(BaseModel):
    customer_name: str
    issue: str


class TicketUpdate(BaseModel):
    status: str