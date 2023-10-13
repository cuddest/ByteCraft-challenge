from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("register/", views.register.as_view(), name="register"),
    path("login/", views.login.as_view(), name="login"),
    path("userv/", views.userv.as_view(), name="userv"),
    path("lout/", views.lout.as_view(), name="lout"),
    path("addT/", views.TaskListCreateView.as_view(), name="AddTask"),
    path("det/<int:pk>/", views.TaskDetailView.as_view(), name="detTask"),
    path("del/<int:pk>/", views.taskDeleteView.as_view(), name="delTask"),
    path("list/", views.TaskListView.as_view(), name="listTask"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/docs", SpectacularSwaggerView.as_view(url_name= "schema")),

]
