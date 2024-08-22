from django.urls import path

from . import views


urlpatterns = [
    # ex: /polls/
    path("zoo", views.zoo, name="zoo"),
    path("zoo/create", views.parents_create, name="parents_create"),
    path("zoo/delete", views.parents_delete, name="parents_delete"),
    path("zoo/union", views.childs_to_parents, name="childs_to_parents"),

]
