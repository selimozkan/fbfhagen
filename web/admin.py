from django.contrib import admin
from django.contrib.auth.models import Group

from .models import (
    Home,
    Branch,
    Service,
    About,
    Project,
    Event,
    AfterSchool,
    Partner,
    FooterContact,
    Social,
    Disclaimer,
)

admin.site.site_header = "Fbf-Hagen Administration"
admin.site.unregister(Group)


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    fields = [
        "banner_picture",
        "banner_image",
        "title_de",
        "subtitle_de",
        "title_en",
        "subtitle_en",
    ]
    list_display = [
        "banner_thumbnail",
        "title_de",
        "subtitle_de",
    ]
    readonly_fields = ["banner_picture"]

    def has_add_permission(self, request):
        count = Home.objects.all().count()
        if count == 0:
            return True
        return False


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = [
        "title_de",
        "description_de",
        "slug",
    ]

    def has_add_permission(self, request):
        count = Branch.objects.all().count()
        if count < 4:
            return True
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = [
        "service_picture",
        "image",
        "title_de",
        "description_de",
        "title_en",
        "description_en",
    ]
    list_display = [
        "service_thumbnail",
        "title_de",
        "description_de",
    ]
    readonly_fields = ["service_picture"]

    def has_add_permission(self, request):
        count = Service.objects.all().count()
        if count < 4:
            return True
        return False


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fields = [
        "about_picture",
        "image",
        "video",
        "title_de",
        "subtitle_de",
        "description_de",
        "content_de",
        "title_en",
        "subtitle_en",
        "description_en",
        "content_en",
    ]

    list_display = [
        "about_thumbnail",
        "title_de",
        "subtitle_de",
    ]
    readonly_fields = ["about_picture"]

    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = [
        "project_picture",
        "image",
        "title_de",
        "description_de",
        "content_de",
        "title_en",
        "description_en",
        "content_en",
        "author",
        "created",
        "updated",
        "slug",
    ]

    list_display = [
        "project_thumbnail",
        "title_de",
        "slug",
    ]
    readonly_fields = ["project_picture", "created", "updated"]
    ordering = ("-updated",)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = [
        "event_picture",
        "image",
        "title_de",
        "title_en",
    ]

    list_display = [
        "event_thumbnail",
        "title_de",
    ]
    readonly_fields = [
        "event_picture",
    ]
    ordering = ("-id",)


@admin.register(AfterSchool)
class AfterSchoolAdmin(admin.ModelAdmin):
    fields = [
        "content_de",
        "content_en",
    ]
    list_display = [
        "id",
        "content_de",
    ]

    def has_add_permission(self, request):
        count = AfterSchool.objects.all().count()
        if count == 0:
            return True
        return False


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    fields = [
        "partner_picture",
        "image",
        "title",
        "website",
    ]

    list_display = [
        "partner_thumbnail",
        "title",
        "website",
    ]
    list_display_links = [
        "partner_thumbnail",
        "title",
    ]
    readonly_fields = ["partner_picture"]
    ordering = ("id",)


@admin.register(FooterContact)
class FooterContactAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "email",
        "phone",
    ]
    list_display_links = [
        "id",
        "title",
    ]
    ordering = ("id",)


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "facebook",
        "instagram",
        "youtube",
    ]
    list_display_links = [
        "id",
        "facebook",
    ]

    def has_add_permission(self, request):
        count = Social.objects.all().count()
        if count == 0:
            return True
        return False


@admin.register(Disclaimer)
class DisclaimerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "disclaimer_de",
    ]
    list_display_links = [
        "id",
        "disclaimer_de",
    ]

    def has_add_permission(self, request):
        count = Disclaimer.objects.all().count()
        if count == 0:
            return True
        return False
