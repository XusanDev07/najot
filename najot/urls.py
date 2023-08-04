from django.urls import path
from najot.views import Main

urlpatterns = [
    path('main/', Main.as_view())
]
