from celery import task
from django.urls import reverse
from django.core.mail import send_mail
from django.template import Template, Context

from .models import Subscriber, EmailTemplate

@task
def send_emails_to_all_subscribers(subscriber_ids=[]):
    # for purity, you need to make the sending for each subscriber separate
    subscribers = Subscriber.objects.filter(id__in=subscriber_ids) if subscriber_ids else Subscriber.objects.all()
    email_template = EmailTemplate.objects.first()

    if subscribers and email_template:
        subject = email_template.subject
        template = ''
        with open(email_template.attachment.path, 'r') as f:
            template = f.read()

        # print(reverse('sender:tracking_mail'))
        for subscriber in subscribers:
            context = {
                'first_name': subscriber.first_name,
                'last_name': subscriber.last_name,
                'age': subscriber.get_age(),
                'track_url': "http://yourdomain.com"+reverse('sender:tracking_mail')+str('?email='+subscriber.email)
            }
            print(context['track_url'])
            message = Template(template).render(Context(context))
            # print(message)
            # connect after configuring SMTP for mail
            # send_mail(subject, message, 'alli.kalykov@gmail.com', [subscriber.email], html_message=message)
    return 'Succs'