from rest_framework import serializers
from najot.models.docktor_qushish import Doktor


class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doktor
        fields = "__all__"

