from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import json

from .forms import ContactForm

from .models import (
    Home,
    Branch,
    Service,
    About,
    Project,
    Event,
    Partner,
    FooterContact,
    Disclaimer,
)


def index(request):
    lang = request.session.get("language", "en")
    home = Home.objects.get(id=1)
    branches = Branch.objects.all().order_by("id")[:3]
    about = About.objects.all().order_by("id")[:1].get()
    projects = Project.objects.order_by("-updated")[:3]
    partners = Partner.objects.all().order_by("id")

    return render(
        request,
        "index.html",
        {
            "language": lang,
            "home": home,
            "branches": branches,
            "about": about,
            "projects": projects,
            "partners": partners,
        },
    )


def about(request):
    lang = request.session.get("language", "en")
    about = About.objects.all().order_by("id")[:1].get()
    services = Service.objects.all().order_by("id")
    partners = Partner.objects.all().order_by("id")
    return render(
        request,
        "about.html",
        {
            "language": lang,
            "about": about,
            "services": services,
            "partners": partners,
        },
    )


def branch(request, slug):
    lang = request.session.get("language", "en")
    branch = Branch.objects.filter(slug=slug).get()
    return render(
        request,
        "branch.html",
        {
            "language": lang,
            "branch": branch,
        },
    )


def project(request, slug="all"):
    lang = request.session.get("language", "en")
    if slug == "all":
        projects = Project.objects.all()
        return render(
            request,
            "projects.html",
            {
                "language": lang,
                "projects": projects,
            },
        )
    else:
        project = Project.objects.get(slug=slug)
        return render(
            request,
            "project_detail.html",
            {
                "language": lang,
                "project": project,
            },
        )


def event(request):
    lang = request.session.get("language", "en")
    event = Event.objects.all().order_by("-id")
    return render(
        request,
        "event.html",
        {
            "language": lang,
            "event": event,
        },
    )


def contact(request):
    lang = request.session.get("language", "en")
    contacts = FooterContact.objects.all().order_by("-id")

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            print(name, phone, email, message)
            send_mail(
                "Contact form message from fbf-hagen.de by {}".format(name),
                message,
                settings.EMAIL_HOST_USER,
                ["selimozkan@gmail.com"],
                auth_user=settings.EMAIL_HOST_USER,
                auth_password=settings.EMAIL_HOST_PASSWORD,
            )

    return render(
        request,
        "contact.html",
        {
            "language": lang,
            "contacts": contacts,
        },
    )


def disclaimer(request):
    lang = request.session.get("language", "en")
    disclaimer = Disclaimer.objects.all().order_by("id")[:1].get()
    partners = Partner.objects.all().order_by("id")
    return render(
        request,
        "disclaimer.html",
        {
            "language": lang,
            "disclaimer": disclaimer,
            "partners": partners,
        },
    )


def privacy(request):
    lang = request.session.get("language", "en")
    disclaimer = Disclaimer.objects.all().order_by("id")[:1].get()
    partners = Partner.objects.all().order_by("id")
    return render(
        request,
        "privacy.html",
        {
            "language": lang,
            "disclaimer": disclaimer,
            "partners": partners,
        },
    )


def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


def change_language(request, lng="en"):
    request.session["language"] = "%s" % lng
    if request.META.get("HTTP_REFERER"):
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    else:
        return HttpResponseRedirect("/")
