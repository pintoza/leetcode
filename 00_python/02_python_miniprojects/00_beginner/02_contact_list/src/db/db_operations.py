from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from .models import Base, Contact

engine = create_engine('sqlite:///data/db/contacts.db')
session = Session(engine)

def add_contact(name, phone):
    contact = Contact(name=name, phone=phone)
    session.add(contact)
    session.commit()

