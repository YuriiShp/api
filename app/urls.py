from django.urls import path
from app.views import AuthorApiView, PostApiView

urlpatterns = [
    path('authors/', AuthorApiView.as_view()),
    path('post/', PostApiView.as_view()),
]
