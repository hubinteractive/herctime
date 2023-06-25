from django.urls import path

from . import views

app_name = 'index-serbian'

urlpatterns = [
    path("", views.index, name="index-sr"),
    path("contact/", views.contact, name="contact"),
    path("weaning_program/treatment_of_gamblers", views.treatmentGamblers, name="treatment_of_gamblers"),
    path("weaning_program/family_and_gambler", views.weaningProgram, name="family_and_gambler"),
    path("weaning_program/gambling_problem_scene", views.gamblingProblem, name="gambling_problem_scene"),
    path("weaning_program/gambling_addiction", views.gamblingAddiction, name="gambling_addiction"),
    path("weaning_program/pathological_gambling", views.pathologicalGambling, name="pathological_gambling"),
    path("weaning_program/dealing_with_gambling_problem", views.dealingGambling, name="dealing_with_gambling_problem"),
    
]