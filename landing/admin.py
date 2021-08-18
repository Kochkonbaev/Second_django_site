from django.contrib import admin
from .models import Feedback, Landing, Workers

admin.site.register(Landing)
admin.site.register(Workers)
admin.site.register(Feedback)

