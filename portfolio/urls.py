from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/<str:section>/", views.manage_items, name="manage"),
    path("dashboard/<str:section>/add/", views.edit_item, name="add"),
    path("dashboard/<str:section>/<int:pk>/edit/", views.edit_item, name="edit"),
    path("dashboard/<str:section>/<int:pk>/delete/", views.delete_item, name="delete"),
]
