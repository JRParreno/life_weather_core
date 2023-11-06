from rest_framework import serializers
from .models import Todo, Diary, DiaryLapse


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['pk', 'user_profile', 'title',
                  'note', 'status', 'date_created']

        extra_kwargs = {
            'date_created': {
                'read_only': True
            },
            'user_profile': {
                'read_only': True
            }
        }


class DiaryLapseSerializer(serializers.ModelSerializer):
    diary_pk = serializers.CharField(write_only=True)

    class Meta:
        model = DiaryLapse
        fields = ['pk', 'note', 'date_created', 'diary_pk']

        extra_kwargs = {
            'date_created': {
                'read_only': True
            }
        }


class DiarySerializer(serializers.ModelSerializer):
    diary_lapses = DiaryLapseSerializer(
        source='diary_parent', many=True, read_only=True)

    class Meta:
        model = Diary
        fields = ['pk', 'user_profile', 'title',
                  'date_created', 'diary_lapses']

        extra_kwargs = {
            'date_created': {
                'read_only': True
            },
            'user_profile': {
                'read_only': True
            }
        }
