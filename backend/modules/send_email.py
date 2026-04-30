from email.message import EmailMessage
import aiosmtplib
import random
import os
from dotenv import load_dotenv
from pydantic import EmailStr

async def send_otp(email:EmailStr):
    message=EmailMessage()
    message["From"]=os.getenv("sender_name")
    message["To"]=email
    message["Title"]="Otp verification code"
    otp=random.randint(100000,999999)
    try:
        message.set_content(f"""Hello,

            Welcome to Predicta! To complete your verification, please use the following one-time password (OTP):

            🔑 Your OTP: {otp}

            This code will expire in 5 minutes. For your security, do not share this code with anyone.

            If you did not request this verification, please ignore this message.

            Thank you,
            The Predicta Team
            """)
        await aiosmtplib.send(
            message,
            hostname=os.getenv("hostname"),
            username=os.getenv("sender_name"),
            use_tls=True,
            password=os.getenv("password")
        )
    except Exception:
        return None
    else:
        return otp