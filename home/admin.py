from django.contrib import admin
from home.models import Setting, ContactMessage, FAQ, Candidature, Magasin, JobOffer


class SettingtAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "update_at", "status"]


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "subject", "update_at", "status"]
    readonly_fields = ("name", "subject", "email", "message", "ip")
    list_filter = ["status"]


class FAQAdmin(admin.ModelAdmin):
    list_display = ["question", "answer", "ordernumber", "status"]
    list_filter = ["status"]


class MagasinAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "opening_time", "closing_time", "image_tag")
    readonly_fields = ("image_tag",)


admin.site.register(Setting, SettingtAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Candidature)
admin.site.register(JobOffer)
admin.site.register(Magasin, MagasinAdmin)
