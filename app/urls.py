from django.urls import path
from app.views import ReportApiView

urlpatterns = [
    path('reports/', ReportApiView.as_view())
]
