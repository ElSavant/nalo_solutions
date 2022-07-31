from rest_framework  import serializers
from contacts.models import Contact

class ContactSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ["firstname","lastname","phone","date_created"]