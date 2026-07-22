

from pydantic import BaseModel, EmailStr, ConfigDict


class CreateContactInput(BaseModel):
  name: str
  email: EmailStr
  phone: str|None = None

class CreateContactOutput(BaseModel):
    id: int
    name: str
    email: str
    phone: str | None

    model_config = ConfigDict(from_attributes = True)
