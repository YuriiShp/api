from django.urls import path
from app.views import ReportApiView, AuthorApiView, ReportNestedApiView

urlpatterns = [
    path('reports/', ReportApiView.as_view()),
    path('authors/', AuthorApiView.as_view()),
    path('reports_nested/', ReportNestedApiView.as_view()),
]
