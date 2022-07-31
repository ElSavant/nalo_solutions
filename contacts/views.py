#from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from .models import Contact
from .serialisers import ContactSerialiser


# Create your views here.
class ContactList(generics.ListCreateAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactSerialiser
    paginate_by = 20

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialiser

