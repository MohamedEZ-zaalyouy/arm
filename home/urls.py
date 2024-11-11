from django.urls import path
from .views import (
    HomeSettingView,
    ContactMessageView,
    FAQView,
    CandidatureCreateView,
    MagasinListView,
    JobOfferListView,
)

urlpatterns = [
    path("setting/", HomeSettingView.as_view(), name="home-setting"),
    path("contact/", ContactMessageView.as_view(), name="contact-message"),
    path("faq/", FAQView.as_view(), name="faq"),
    path("magasins/", MagasinListView.as_view(), name="magasin-list"),
    ##
    path("candidature", CandidatureCreateView.as_view(), name="candidature-create"),
    path("job_offers", JobOfferListView.as_view(), name="joboffer-list"),
]
