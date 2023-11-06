from django.contrib import admin
from .models import Todo, Diary, DiaryLapse

admin.site.register(Todo)
admin.site.register(Diary)
admin.site.register(DiaryLapse)
