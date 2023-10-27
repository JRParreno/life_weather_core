from django.shortcuts import render
from rest_framework import generics, permissions, response, status
from .serializers import TodoSerializer
from .models import Todo, Diary, DairyLapse
from .paginate import ExtraSmallResultsSetPagination


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Todo.objects.all().order_by('date_created')
    pagination_class = ExtraSmallResultsSetPagination

    def get_queryset(self):
        user = self.request.user

        query_set = Todo.objects.filter(
            user_profile__user__pk=user.pk).order_by('date_updated')

        return query_set
