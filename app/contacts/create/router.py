from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.contacts.create.schema import CreateContactInput, CreateContactOutput
from app.contacts.create.service import create_contact
from shared.database import get_db

router = APIRouter()


@router.post("/contacts", response_model=CreateContactOutput, status_code=201)
def create_contact_endpoint(
  data: CreateContactInput,
  db: Session = Depends(get_db)
):
    return create_contact(data, db)
