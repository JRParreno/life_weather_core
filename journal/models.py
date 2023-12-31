from django.db import models
from user_profile.models import UserProfile
from django.utils import timezone


class Todo(models.Model):

    TODO = 'TODO'
    ON_PROCESS = 'ON PROCESS'
    DONE = 'DONE'
    CANCELLED = 'CANCELLED'
    ARCHIVED = 'ARCHIVED'

    TODO_CHOICES = [
        (TODO, 'Todo'),
        (ON_PROCESS, 'On Process'),
        (CANCELLED, 'Cancelled'),
        (ARCHIVED, 'Archived'),
        (DONE, 'Done'),
    ]

    user_profile = models.ForeignKey(
        UserProfile, related_name='user_todo', on_delete=models.CASCADE)
    title = models.CharField(max_length=250,)
    note = models.TextField()
    status = models.CharField(
        max_length=15, choices=TODO_CHOICES, default=TODO)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} - {self.status}'


class Diary(models.Model):
    user_profile = models.ForeignKey(
        UserProfile, related_name='user_diary', on_delete=models.CASCADE)
    title = models.CharField(max_length=250,)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title} - {self.date_created.strftime("%m/%d/%Y, %H:%M:%S")}'


class DiaryLapse(models.Model):
    diary = models.ForeignKey(
        Diary, related_name='diary_parent', on_delete=models.CASCADE)
    note = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.diary.title} - {self.date_created.strftime("%m/%d/%Y, %H:%M:%S")}'
