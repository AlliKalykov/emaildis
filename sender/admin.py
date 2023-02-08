# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Subscriber, EmailTemplate, SentEmail

from .tasks import send_emails_to_all_subscribers

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'birth_date', 'date_subscribed']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['birth_date', 'date_subscribed']
    ordering = ['-date_subscribed']

    def send_email(modeladmin, request, queryset):
        subscriber_ids = list(queryset.values_list('id', flat=True))
        send_emails_to_all_subscribers.delay(subscriber_ids)
    actions = [send_email]


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ['subject', 'body']
    search_fields = ['subject']


@admin.register(SentEmail)
class SentEmailAdmin(admin.ModelAdmin):
    list_display = ['subscriber', 'email_template', 'sent_at', 'opened_at']
    search_fields = ['subscriber__email']
    list_filter = ['sent_at', 'opened_at']
    ordering = ['-sent_at']

