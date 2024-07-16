from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.html import mark_safe
from django.core.validators import FileExtensionValidator
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.utils import timezone
from django_resized import ResizedImageField


def now():
    if settings.USE_TZ:
        return timezone.localtime()
    else:
        return datetime.now()


class Home(models.Model):
    title_de = models.CharField(max_length=100)
    subtitle_de = models.CharField(max_length=200)
    title_en = models.CharField(max_length=100)
    subtitle_en = models.CharField(max_length=200)
    banner_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="home/",
        validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg"])],
    )

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Home"
        managed = True
        ordering = ("id",)

    def banner_thumbnail(self):
        if self.banner_image:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.banner_image.url
            )
        else:
            return "No Image"
        banner_thumbnail.short_description = "Home Banner"
        banner_thumbnail.allow_tags = True

    def banner_picture(self):
        if self.banner_image:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.banner_image.url
            )
        else:
            return "No Image"
        banner_picture.short_description = "Home Banner"
        banner_picture.allow_tags = True

    def __str__(self):
        return self.title_de


class Branch(models.Model):
    title_de = models.CharField("Title De", null=True, blank=True, max_length=100)
    description_de = models.CharField(
        "Description De", null=True, blank=True, max_length=250
    )
    content_de = RichTextUploadingField("Content De", null=True, blank=True)
    title_en = models.CharField("Title En", null=True, blank=True, max_length=100)
    description_en = models.CharField(
        "Description En", null=True, blank=True, max_length=250
    )
    content_en = RichTextUploadingField("Content En", null=True, blank=True)
    slug = models.SlugField(
        "Slug", max_length=250, unique=True, allow_unicode=False, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_de)
        super(Branch, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
        managed = True
        ordering = ("id",)

    def __str__(self):
        return self.title_de


class Service(models.Model):
    image = models.ImageField(
        "Image",
        upload_to="service/",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg"])],
    )
    title_de = models.CharField("Title De", null=True, blank=True, max_length=100)
    description_de = models.CharField(
        "Description De", null=True, blank=True, max_length=250
    )
    title_en = models.CharField("Title En", null=True, blank=True, max_length=100)
    description_en = models.CharField(
        "Description En", null=True, blank=True, max_length=250
    )

    def service_thumbnail(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        service_thumbnail.short_description = "Service Thumbnail"
        service_thumbnail.allow_tags = True

    def service_picture(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        service_picture.short_description = "Service Image"
        service_picture.allow_tags = True

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        managed = True
        ordering = ("id",)

    def __str__(self):
        return self.title_de


class About(models.Model):
    image = models.ImageField(
        null=True,
        blank=True,
        upload_to="about/",
        validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg"])],
    )
    video = models.URLField("Video Url", null=True, blank=True, max_length=500)
    title_de = models.CharField("Title De", null=True, blank=True, max_length=100)
    subtitle_de = models.CharField("Subtitle De", null=True, blank=True, max_length=200)
    description_de = models.TextField("Description De", null=True, blank=True)
    content_de = RichTextUploadingField("Content De", null=True, blank=True)
    title_en = models.CharField("Title En", null=True, blank=True, max_length=100)
    subtitle_en = models.CharField("Subtitle En", null=True, blank=True, max_length=200)
    description_en = models.TextField("Description En", null=True, blank=True)
    content_en = RichTextUploadingField("Content En", null=True, blank=True)

    def about_thumbnail(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        about_thumbnail.short_description = "About Thumbnail"
        about_thumbnail.allow_tags = True

    def about_picture(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        about_picture.short_description = "About Image"
        about_picture.allow_tags = True

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"
        managed = True
        ordering = ("id",)

    def __str__(self):
        return self.title_de


class Project(models.Model):
    image = models.ImageField(
        verbose_name="Image",
        null=True,
        blank=True,
        upload_to="project/",
        validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg"])],
    )
    title_de = models.CharField("Title De", null=True, blank=True, max_length=200)
    description_de = models.CharField(
        "Description De", null=True, blank=True, max_length=200
    )
    content_de = RichTextUploadingField("Content De", null=True, blank=True)
    title_en = models.CharField("Title En", null=True, blank=True, max_length=200)
    description_en = models.CharField(
        "Description En", null=True, blank=True, max_length=200
    )
    content_en = RichTextUploadingField("Content En", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField("Slug", max_length=250, unique=True, blank=True)
    author = models.CharField(
        "Author", max_length=100, default="FBF-Hagen", null=True, blank=True
    )

    def project_thumbnail(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        project_thumbnail.short_description = "Project Thumbnail"
        project_thumbnail.allow_tags = True

    def project_picture(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        project_picture.short_description = "Project Image"
        project_picture.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title_de)
        if not self.updated:
            self.updated = now()
        super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        managed = True
        ordering = ("-updated",)

    def __str__(self):
        return self.title_de


class Partner(models.Model):
    image = ResizedImageField(
        "Image",
        size=[None, 50],
        upload_to="partner/",
        quality=100,
        blank=True,
        null=True,
        force_format="PNG",
        validators=[FileExtensionValidator(allowed_extensions=["gif", "png", "jpg"])],
    )
    title = models.CharField("Title", null=True, blank=True, max_length=100)
    website = models.URLField("Website", null=True, blank=True)

    def partner_thumbnail(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        partner_thumbnail.short_description = "Partner Thumbnail"
        partner_thumbnail.allow_tags = True

    def partner_picture(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        partner_picture.short_description = "Partner Image"
        partner_picture.allow_tags = True

    class Meta:
        verbose_name = "Partner"
        verbose_name_plural = "Partners"
        managed = True

    def __str__(self):
        return self.title or "No Title"


class FooterContact(models.Model):
    title = models.CharField("Title", max_length=100, null=True, blank=True)
    address = models.CharField("Address", max_length=250, null=True, blank=True)
    email = models.CharField("Email", max_length=250, null=True, blank=True)
    phone = models.CharField("Phone", max_length=50, null=True, blank=True)
    instagram = models.URLField("Instagram", max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "Footer Contact"
        verbose_name_plural = "Footer Contacts"
        managed = True

    def __str__(self):
        return self.title or "No Title"


class Event(models.Model):
    image = models.ImageField("Image", upload_to="event/", null=True, blank=True)
    title_de = models.CharField("Title De", max_length=100, null=True, blank=True)
    title_en = models.CharField("Title En", max_length=100, null=True, blank=True)

    def event_thumbnail(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:50px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        event_thumbnail.short_description = "Event Thumbnail"
        event_thumbnail.allow_tags = True

    def event_picture(self):
        if self.image:
            return mark_safe(
                '<img src="%s" style="width:250px;" alt="" />' % self.image.url
            )
        else:
            return "No Image"
        event_picture.short_description = "Event Image"
        event_picture.allow_tags = True

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        managed = True

    def __str__(self):
        return self.title_de or "No Title"


class AfterSchool(models.Model):
    content_de = RichTextUploadingField("Content De", null=True, blank=True)
    content_en = RichTextUploadingField("Content En", null=True, blank=True)

    class Meta:
        verbose_name = "AfterSchool"
        verbose_name_plural = "AfterSchool"
        managed = True

    def __str__(self):
        return self.content_de or "No Text"


class Social(models.Model):
    facebook = models.URLField("Facebook Link", max_length=250, null=True, blank=True)
    instagram = models.URLField("Instagram Link", max_length=250, null=True, blank=True)
    youtube = models.URLField("Youtube Link", max_length=250, null=True, blank=True)

    class Meta:
        verbose_name = "Social"
        verbose_name_plural = "Socials"
        managed = True

    def __str__(self):
        return self.facebook or "No Link"


class Disclaimer(models.Model):
    disclaimer_de = RichTextUploadingField("Disclaimer De", null=True, blank=True)
    disclaimer_en = RichTextUploadingField("Disclaimer En", null=True, blank=True)
    privacy_de = RichTextUploadingField("Privacy Policy De", null=True, blank=True)
    privacy_en = RichTextUploadingField("Privacy Policy En", null=True, blank=True)

    class Meta:
        verbose_name = "Disclaimer"
        verbose_name_plural = "Disclaimers"
        managed = True

    def __str__(self):
        return self.disclaimer_de or "No Text"
