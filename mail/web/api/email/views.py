from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType

from mail.settings import settings
from mail.web.api.email.schema import EmailSchema

router = APIRouter()

conf = ConnectionConfig(
    MAIL_USERNAME=settings.USERNAME,
    MAIL_PASSWORD=settings.PASSWORD,
    MAIL_FROM=settings.FROM,
    MAIL_PORT=settings.PORT,
    MAIL_SERVER=settings.SERVER,
    MAIL_FROM_NAME=settings.FROM_NAME,
    MAIL_STARTTLS=settings.STARTTLS,
    MAIL_SSL_TLS=settings.SSL_TLS,
    USE_CREDENTIALS=settings.USE_CREDENTIALS,
    VALIDATE_CERTS=settings.VALIDATE_CERTS,
)


@router.post("/send_mail")
async def simple_send(
    content: EmailSchema = Depends(),
) -> JSONResponse:
    """
    Send email with FastAPI-Mail.

    :param content: EmailSchema
    :return: JSONResponse
    """
    message = MessageSchema(
        subject=content.subject,
        recipients=content.receiver,
        subtype=MessageType.html,
        body=f"""
        <p><b>Name:</b> {content.name}</p>
        <p><b>Téléphone:</b> {content.phone}</p>
        <p><b>Email:</b> {content.email}</p>

        <p><b>Message:</b> {content.body}</p>
        """,
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "email has been sent"},
    )
