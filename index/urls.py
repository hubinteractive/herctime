from django.urls import path

from . import views

app_name = 'index'
urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact"),
    path("romani/", views.romani, name="romani"),
    path("weaning_program/family_and_gambler", views.weaningProgram, name="family_and_gambler"),
    path("weaning_program/treatment_of_gamblers", views.treatmentGamblers, name="treatment_of_gamblers"),
    path("weaning_program/gambling_problem_scene", views.gamblingProblem, name="gambling_problem_scene"),
    path("weaning_program/gambling_addiction", views.gamblingAddiction, name="gambling_addiction"),
    path("weaning_program/pathological_gambling", views.pathologicalGambling, name="pathological_gambling"),
    path("weaning_program/dealing_with_gambling_problem", views.dealingGambling, name="dealing_with_gambling_problem"),
    path("dejan_stankovic", views.dejanStankovic, name="dejan_stankovic"),
    path("herctime/gallery", views.gallery, name="gallery"),
    path("herctime/about_us", views.aboutUs, name="about_us"),
    path("herctime/privacy_policy", views.privacyPolicy, name="privacy_policy"),
    path("video_education", views.videoEducation, name="video_education"),
    path("blog", views.blog, name="blog"),
    path("books/oprostajno_pismo", views.oprostajnoPismo, name="oprostajno_pismo"),
]