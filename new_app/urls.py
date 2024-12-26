from django.urls import path

from new_app.apps import NewAppConfig
from new_app.views import AppListAPIView

app_name = NewAppConfig.name

urlpatterns = [
    path('', AppListAPIView.as_view()),
]