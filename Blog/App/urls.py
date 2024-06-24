from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.PostList.as_view(), name="Home"),
    path('<slug:slug>/', views.DetailedView.as_view(), name="post_detail"),
]
