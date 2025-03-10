from django.urls import path
from .views import JobListView, JobUpdateView, JobDeleteView, JobDetailView, JobCreateView, RegionListView, HomeView, RegionDetailView, MyJobListView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user_job_list/<str:username>/', MyJobListView.as_view(), name='user_job_list'),
    path('region/<int:pk>/', RegionDetailView.as_view(), name='region_detail'),
    path('regions/', RegionListView.as_view(), name='region_list'),
    path('job_list/', JobListView.as_view(), name='job_list'),
    path('job/<int:pk>/edit/', JobUpdateView.as_view(), name='job_edit'),
    path('job/<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('job/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('job/new', JobCreateView.as_view(), name='job_new'),
    path('city_id/<int:region_id>/', views.get_cities, name='city_id'), #viloyatni tanlaganda shahar chiqishi uchun. JavaScript uchun

]