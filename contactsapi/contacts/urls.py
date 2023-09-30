from django.urls import path
from . import views

urlpatterns = [
    path('',views.ContactAPIList.as_view()),
    path('<int:pk>',views.ContactAPIDetail.as_view())
]
