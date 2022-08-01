#from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics,status
from rest_framework.response import Response
import  pandas as pd
from .models import Contact
from .serialisers import ContactSerialiser,FileUploadSerializer


# Create your views here.
class ContactList(generics.ListCreateAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactSerialiser
    

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialiser


class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        reader.fillna('',inplace=True)
        for _, row in reader.iterrows():
            birthday = row["birthday"] if row["birthday"] != "" else "1900-01-01"
            print(birthday)
            new_contact = Contact(
                       firstname = row["firstname"],
                       lastname = row['lastname'],
                       phone = row["phone"],
                       company = row["company"],
                       job_title = row["job_title"],
                       birthday = row["birthday"] if row["birthday"] != "" else "1900-01-01",
                       email = row["email"]
                       )
            new_contact.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

