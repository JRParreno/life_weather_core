from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response, status
from .serializers import TodoSerializer, DiarySerializer, DiaryLapseSerializer
from .models import Todo, Diary, DiaryLapse
from .paginate import ExtraSmallResultsSetPagination
from user_profile.models import UserProfile


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Todo.objects.all().order_by('-date_updated')
    pagination_class = ExtraSmallResultsSetPagination

    def get_queryset(self):
        user = self.request.user

        query_set = Todo.objects.filter(
            user_profile__user__pk=user.pk).order_by('-date_updated')

        return query_set

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            user_profile = get_object_or_404(
                UserProfile, user=self.request.user)
            todo = Todo.objects.create(
                title=data['title'], note=data['note'], user_profile=user_profile, status=data['status'])

            data = {
                "pk": todo.pk,
                "title": todo.title,
                "note": todo.note,
                "date_created": todo.date_created,
                "status": todo.status,
            }

            return response.Response(data, status=status.HTTP_201_CREATED)

        return super().post(request, *args, **kwargs)


class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Todo.objects.all().order_by('date_created')


class DiaryListCreateView(generics.ListCreateAPIView):
    serializer_class = DiarySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Diary.objects.all().order_by('-date_updated')
    pagination_class = ExtraSmallResultsSetPagination

    def get_queryset(self):
        user = self.request.user

        query_set = Diary.objects.filter(
            user_profile__user__pk=user.pk).order_by('-date_updated')

        return query_set

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = DiarySerializer(data=data)
        if serializer.is_valid():
            user_profile = get_object_or_404(
                UserProfile, user=self.request.user)
            diary = Diary.objects.create(
                title=data['title'], user_profile=user_profile)

            data = {
                "pk": diary.pk,
                "title": diary.title,
                "diary_lapses": [],
                "date_created": diary.date_created,
            }

            return response.Response(data, status=status.HTTP_201_CREATED)

        return super().post(request, *args, **kwargs)


class DiaryLapseCreateView(generics.CreateAPIView):
    serializer_class = DiaryLapseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = DiaryLapse.objects.all().order_by('-date_updated')

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = DiaryLapseSerializer(data=data)
        if serializer.is_valid():
            diary = get_object_or_404(
                Diary, pk=data['diary_pk'])
            diary_lapse = DiaryLapse.objects.create(
                note=data['note'], diary=diary)

            data = {
                "pk": diary_lapse.pk,
                "note": diary_lapse.note,
                "date_created": diary_lapse.date_created,
            }

            return response.Response(data, status=status.HTTP_201_CREATED)

        return super().post(request, *args, **kwargs)
