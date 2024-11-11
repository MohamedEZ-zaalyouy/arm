from rest_framework import serializers
from .models import FAQ, ContactMessage, Setting, Magasin, JobOffer
from .models import Candidature


class HomeSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        exclude = ["create_at", "update_at", "status"]


class MagasinSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Magasin
        fields = [
            "id",
            "name",
            "address",
            "city",
            "postal_code",
            "phone_number",
            "email",
            "opening_time",
            "closing_time",
            "description",
            "manager_name",
            "is_active",
            "image_url",
        ]

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None


class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = [
            "job_offer",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "job_title",
            "cv",
        ]


class JobOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOffer
        fields = ["id", "label", "address", "employment_type"]
