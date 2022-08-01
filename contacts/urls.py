
from django.urls import path
from .views import ContactList,ContactDetail,UploadFileView

urlpatterns = [
    path('contacts/', ContactList.as_view(),name = "list_contacts"),
    path('contacts/<int:pk>/', ContactDetail.as_view()),
    path('contacts_upload/', UploadFileView.as_view()),
]