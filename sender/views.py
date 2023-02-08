# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.http import HttpResponse
from .models import SentEmail

def tracking_mail(request):
    # Get the email from the request query parameters
    email = request.GET.get('email')

    # Try to get the sent email object
    # For completely correct work, in the SentEmail model, 
    # you need to add a separate identifier unique for each message 
    # You can use id
    sent_email = SentEmail.objects.filter(subscriber__email=email).first()
    if sent_email:
        # Update the `opened_at` field of the sent email object to indicate that the email was opened
        sent_email.opened_at = timezone.now()
        sent_email.save()

    return HttpResponse('Tracking email opened successfully!')
