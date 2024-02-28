from django.contrib import admin

from .models import Contact, NewsletterSubscribers

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')


class NewsletterSubscribersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribed_on')

admin.site.register(Contact, ContactAdmin)
admin.site.register(NewsletterSubscribers, NewsletterSubscribersAdmin)

