from django.contrib import admin
from polls.models import Questions,Choice

admin.site.register(Questions)
admin.site.register(Choice)
