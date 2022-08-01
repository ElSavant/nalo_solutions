from rest_framework  import serializers
from contacts.models import Contact
from .validators import validate_file_extension

class ContactSerialiser(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ["firstname","lastname","phone","date_created"]

class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField(validators=[validate_file_extension])

