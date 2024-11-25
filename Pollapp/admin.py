# PollsApp/admin.py

from django.contrib import admin
from .models import Question, Choices,Creator

# Register models individually
admin.site.register(Creator)
admin.site.register(Question)
admin.site.register(Choices)
