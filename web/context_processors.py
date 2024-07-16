from .models import FooterContact, Social


def footer_processor(request):
    contacts = FooterContact.objects.all()
    socials = Social.objects.order_by("id")[:1].get()
    return {"contacts": contacts, "socials": socials}
