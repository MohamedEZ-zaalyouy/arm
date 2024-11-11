from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import FAQ, ContactMessage, Setting, Magasin, JobOffer
from .serializers import (
    ContactMessageSerializer,
    FAQSerializer,
    HomeSettingSerializer,
    CandidatureSerializer,
    MagasinSerializer,
    JobOfferSerializer,
)


class HomeSettingView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        home_setting = Setting.objects.first()
        if home_setting:
            serializer = HomeSettingSerializer(home_setting)
            return Response({"home": serializer.data})
        return Response(
            {"error": "No home setting found"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ContactMessageView(APIView):
    permission_classes = [permissions.AllowAny]
    serialiser_class = ContactMessageSerializer

    def post(self, request):
        try:
            name = request.data.get("name")
            email = request.data.get("email")
            subject = request.data.get("subject")
            message = request.data.get("message")

            if name and email and subject and message:
                contact_message = ContactMessage(
                    name=name, email=email, subject=subject, message=message
                )
                contact_message.save()
                return Response(
                    {"success": True, "message": "Message sent successfully!"}
                )
            else:
                return Response(
                    {"success": False, "message": "All fields are required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {"success": False, "message": "An error occurred."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class FAQView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        faqs = FAQ.objects.filter(status="True")
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)


class MagasinListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        magasins = Magasin.objects.filter(is_active=True)
        serializer = MagasinSerializer(magasins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CandidatureCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CandidatureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobOfferListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        job_offers = JobOffer.objects.all()
        serializer = JobOfferSerializer(job_offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
