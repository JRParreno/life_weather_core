from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['pk', 'user_profile', 'title',
                  'note', 'status', 'date_created']

        extra_kwargs = {
            'date_created': {
                'read_only': True
            },
        }
