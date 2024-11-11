from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import JobOffer, Candidature


class CandidatureCreateAPITestCase(APITestCase):
    def setUp(self):
        # Create a sample job offer to link with candidature
        self.job_offer = JobOffer.objects.create(
            label="Développeur Frontend",
            address="Casablanca, Maroc",
            employment_type=JobOffer.FULL_TIME,
        )

        # Define the URL for creating a candidature
        self.url = reverse("candidature-create")

    def test_create_candidature(self):
        # Prepare the data for creating a candidature
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "johndoe@example.com",
            "phone_number": "1234567890",
            "job_title": "Frontend Developer",
            "cv": None,  # Assuming no file for this test
            "job_offer": self.job_offer.id,
        }

        # Send POST request to create a candidature
        response = self.client.post(self.url, data, format="json")

        # Print response data if there is a validation error
        if response.status_code != status.HTTP_201_CREATED:
            print("Error details:", response.data)

        # Check if the candidature was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
