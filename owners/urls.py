from django.urls import path
from .views import DogListView, OwnerListView

urlpatterns = [
    path('/owner',OwnerListView.as_view()),
    path('/dog',DogListView.as_view())
]
