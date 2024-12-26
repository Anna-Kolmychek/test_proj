from rest_framework import serializers

from new_app.models import AppModel


class AppModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppModel
        fields = '__all__'
