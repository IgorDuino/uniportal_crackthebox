from django.contrib import admin
from django.urls import path

from customauth.views import login_view
import scholarship.views
import dashboard.views
import students.views
import papers.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("scholarship/", scholarship.views.scholarship, name="scholarship"),
    path("login/", login_view, name="login"),
    path("myaccount/", students.views.myaccount, name="myaccount"),
    path("myaccount/edit/", students.views.myaccount_edit, name="myaccount_edit"),
    path("papers/", papers.views.papers, name="papers"),
    path("papers/generate/", papers.views.generate_paper, name="generate_paper"),
    path("", dashboard.views.dashboard, name="dashboard"),
]
