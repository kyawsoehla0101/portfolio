from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('post/<str:slug>/', views.detail, name="detail"),
    path('blog/', views.allBlog, name="allblog"),
    path('category/<str:slug>/', views.categorypost, name="categorypost"),
]
