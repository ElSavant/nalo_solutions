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
    paginate_by = 20

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
        for _, row in reader.iterrows():
            new_contact = Contact(
                       id = row['id'],
                       staff_name= row["Staff Name"],
                       position= row['Designated Position'],
                       age= row["Age"],
                       year_joined= row["Year Joined"]
                       )
            new_contact.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)

