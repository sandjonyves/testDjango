import logging

from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import send_mass_mail  
logger = logging.getLogger(__name__)


def send_email_with_html_body (subject:str ,template:str ,context=dict):

    try:
        message = render_to_string(template,context)
        msg =(  subject,
            message,
            settings.EMAIL_HOST_USER,
            ["sandjonyves@gmail.com"],)
        send_mail(
            "Serad client",
            message,
            settings.EMAIL_HOST_USER,
             ["sandjonyves@gmail.com"],
            fail_silently=True,
            html_message=message,
        )
       
        return True

    except Exception as e:
        print("eror ")
        logger.error(e)
        return False