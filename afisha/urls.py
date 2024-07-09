from django.contrib import admin
from django.urls import path
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/movies/', views.movies_list_api_view),
    path('api/v1/movies/<int:id>/', views.movies_detail_api_view),
]
