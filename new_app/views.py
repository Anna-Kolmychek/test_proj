from rest_framework import generics

from new_app.models import AppModel
from new_app.serializers import AppModelSerializer


class AppListAPIView(generics.ListAPIView):
    queryset = AppModel.objects.all()
    serializer_class = AppModelSerializer

    def get_queryset(self):
        if not AppModel.objects.exists():
            AppModel.objects.create(title='first obj')
            AppModel.objects.create(title='second obj')
        return super().get_queryset()
