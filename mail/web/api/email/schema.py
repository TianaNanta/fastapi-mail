from typing import List

from pydantic import BaseModel, EmailStr


class EmailSchema(BaseModel):
    """
    Schema for email.

    :param receiver: List[EmailStr]
    :param subject: str
    :param body: str
    :param phone: str
    :param name: str
    :param email: EmailStr
    """

    receiver: List[EmailStr]
    subject: str
    body: str
    phone: str
    name: str
    email: EmailStr
