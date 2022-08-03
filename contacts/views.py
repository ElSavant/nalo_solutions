from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics,status
from rest_framework.response import Response
import  pandas as pd
from .models import Contact
from .serialisers import ContactSerialiser,FileUploadSerializer


# Create your views here.
class ContactList(LoginRequiredMixin,generics.ListCreateAPIView):

    queryset = Contact.objects.all()
    serializer_class = ContactSerialiser
    

class ContactDetail(LoginRequiredMixin,generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerialiser


class UploadFileView(LoginRequiredMixin,generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        reader.fillna('',inplace=True)
        ##Add code to check for right columns
        for _, row in reader.iterrows():
            new_contact = Contact(
                       firstname = row["firstname"],
                       lastname = row['lastname'],
                       phone = row["phone"],
                       company = row["company"],
                       job_title = row["job_title"],
                       birthday = row["birthday"] if row["birthday"] else "1900-01-01",
                       email = row["email"]
                       )
            try:
                new_contact.save()
            except:
                ##Add code to prompt user of contacts already in database
                continue
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

