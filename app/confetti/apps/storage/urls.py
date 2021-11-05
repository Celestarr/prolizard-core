from django.urls import path

from .views import DownloadResumeView

urlpatterns = [path("member-resume/<str:member_username>/", DownloadResumeView.as_view())]
