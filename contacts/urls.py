
from django.urls import path
from contacts import views

urlpatterns = [
    path('contacts/', views.ContactList.as_view(),name = "list_contacts"),
    path('contacts/<int:pk>/', views.ContactDetail.as_view()),
]