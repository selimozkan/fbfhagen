from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import json

from .models import Home, Branch, About, Project, Partner, FooterContact, Disclaimer


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


def about(request):
    lang = request.session.get("language", "en")
    about = About.objects.all().order_by("id")[:1].get()
    return render(
        request,
        "about.html",
        {
            "language": lang,
            "about": about,
        },
    )


def project(request, slug):
    lang = request.session.get("language", "en")
    project = Project.objects.get(slug=slug)
    return render(
        request,
        "project.html",
        {
            "language": lang,
            "project": project,
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
    return HttpResponseRedirect("/")
