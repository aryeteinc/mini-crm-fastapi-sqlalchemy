from fastapi import FastAPI
from app.contacts.model import Contact  # noqa
from app.notes.model import Note        # noqa
from app.contacts.create.router import router as create_contact_router

app = FastAPI(title="Mini CRM")

app.include_router(create_contact_router)
