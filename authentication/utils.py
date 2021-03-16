from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from rest_framework import status
from .models import *

class Util:
    @staticmethod
    def send_email(data):
        email= EmailMessage(
            subject=data['email_subject'],body= data['email_body'],to=[data['to_email']]
        )
        email.send()
class ResetEmail:
    @staticmethod
    def reset_email(self,request, user, user_data, relativeLink):
        current_site = get_current_site(request).domain
        absurl = 'http://'+ current_site+ relativeLink+str(user.uid)

        email_body = 'Hi ' + 'forgot password, Use below link to Reset your password \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'forgot your password, Reset here'}
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()
        return Response(user_data, status=status.HTTP_201_CREATED)
