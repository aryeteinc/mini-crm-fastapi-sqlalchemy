from fastapi import FastAPI

import shared.models  # noqa
from app.contacts.create.router import router as create_contact_router

app = FastAPI(title="Mini CRM")

app.include_router(create_contact_router)
