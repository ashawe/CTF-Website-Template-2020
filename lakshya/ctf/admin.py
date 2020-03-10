from django.contrib import admin
from .models import UserProfile, Questions, Submission

admin.site.register(UserProfile)
admin.site.register(Questions)
admin.site.register(Submission)
