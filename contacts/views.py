#from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
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


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)


