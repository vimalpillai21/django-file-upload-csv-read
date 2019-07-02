from django.urls import path
from .views import DemoApiView

app_name = 'demo'

urlpatterns = [
    path('index/',DemoApiView.as_view(),name='index')
]
