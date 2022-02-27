from django.urls import path
from . import views
urlpatterns = [
    path('<int:course_id>/', views.detail, name='detail'),
    path('', views.courses, name='home-page'),
]
