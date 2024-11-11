"""General Config & Models For The App"""

# from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field
from django.db import models
from django.utils.html import mark_safe


class Setting(models.Model):
    """Setting App"""

    STATUS = (
        ("True", "True"),
        ("False", "False"),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=100)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    smtpserver = models.CharField(blank=True, max_length=50)
    smtpemail = models.CharField(blank=True, max_length=50)
    smtppassword = models.CharField(blank=True, max_length=10)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to="images/")
    facebook = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    twitter = models.CharField(blank=True, max_length=50)
    youtube = models.CharField(blank=True, max_length=50)
    aboutus = CKEditor5Field(blank=True, config_name="extends")
    contact = CKEditor5Field(blank=True, config_name="extends")
    references = CKEditor5Field(blank=True, config_name="extends")
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Setting Contact App"""

    STATUS = (
        ("New", "New"),
        ("Read", "Read"),
        ("Closed", "Closed"),
    )
    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default="New")
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class FAQ(models.Model):
    """FAQ for The App"""

    STATUS = (
        ("True", "True"),
        ("False", "False"),
    )
    ordernumber = models.IntegerField()
    question = models.CharField(max_length=200)
    answer = CKEditor5Field(config_name="extends")
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Magasin(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du Magasin")
    address = models.CharField(max_length=255, verbose_name="Adresse")
    city = models.CharField(max_length=100, verbose_name="Ville")
    postal_code = models.CharField(max_length=10, verbose_name="Code Postal")
    phone_number = models.CharField(max_length=20, verbose_name="Numéro de Téléphone")
    email = models.EmailField(verbose_name="Email", blank=True, null=True)

    opening_time = models.TimeField(verbose_name="Heure d'ouverture")
    closing_time = models.TimeField(verbose_name="Heure de fermeture")
    description = CKEditor5Field(
        verbose_name="Description du Magasin", config_name="extends"
    )
    image = models.ImageField(
        upload_to="magasin_images/",
        verbose_name="Image du Magasin",
        blank=True,
        null=True,
    )

    manager_name = models.CharField(
        max_length=100, verbose_name="Nom du Gérant", blank=True, null=True
    )
    is_active = models.BooleanField(default=True, verbose_name="Magasin Actif")

    class Meta:
        verbose_name = "Magasin"
        verbose_name_plural = "Magasins"
        ordering = ["city", "name"]

    def __str__(self):
        return f"{self.name} - {self.city}"

    # Method to display the image thumbnail
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" height="50" />')
        return "No Image"

    image_tag.short_description = "Image Preview"


class JobOffer(models.Model):
    FULL_TIME = "Temps plein"
    PART_TIME = "Temps partiel"
    EMPLOYMENT_TYPE_CHOICES = [
        (FULL_TIME, "Full-time"),
        (PART_TIME, "Part-time"),
    ]

    label = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOICES,
        default=FULL_TIME,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.label} - {self.address} ({self.employment_type})"


class Candidature(models.Model):
    job_offer = models.ForeignKey(
        JobOffer,
        on_delete=models.CASCADE,
        related_name="candidatures",
        null=True,
        blank=True,
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    job_title = models.CharField(max_length=100)
    cv = models.FileField(upload_to="cvs/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title}"
