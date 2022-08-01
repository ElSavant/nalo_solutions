
from django.urls import path
from .views import ContactList,ContactDetail,FileUploadView

urlpatterns = [
    path('contacts/', ContactList.as_view(),name = "list_contacts"),
    path('contacts/<int:pk>/', ContactDetail.as_view()),
    path('contacts_upload', FileUploadView.as_view()),
]