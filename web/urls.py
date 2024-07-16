from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("branch/<slug>/", views.branch, name="branch"),
    path("about/", views.about, name="about"),
    path("project/", views.project, name="project"),
    path("project/<slug>/", views.project, name="project"),
    path("event/", views.event, name="event"),
    path("afterschool/", views.afterschool, name="afterschool"),
    path("contact/", views.contact, name="contact"),
    path("disclaimer/", views.disclaimer, name="disclaimer"),
    path("privacy-policy/", views.privacy, name="privacy-policy"),
    path("change-language/<lng>/", views.change_language, name="change-language"),
]
