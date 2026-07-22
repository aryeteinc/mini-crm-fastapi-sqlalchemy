

from sqlalchemy.orm import Session

from app.contacts.create.schema import CreateContactInput, CreateContactOutput
from app.contacts.model import Contact


def create_contact(data: CreateContactInput, db: Session) -> CreateContactOutput:
  contact = Contact(**data.model_dump())
  db.add(contact)
  db.commit()
  db.refresh(contact)

  return CreateContactOutput.model_validate(contact)
