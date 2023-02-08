# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime, timedelta

from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    date_subscribed = models.DateTimeField(auto_now_add=True)


    def get_age(self):
        today = datetime.now().date()
        age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return age


class EmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachment = models.FileField(upload_to='email_attachments/')


class SentEmail(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    email_template = models.ForeignKey(EmailTemplate, on_delete=models.CASCADE)
    sent_at = models.DateTimeField(auto_now_add=True)
    opened_at = models.DateTimeField(null=True, blank=True)
