from django.urls import path
from . import views 


app_name = 'restaurants'

urlpatterns = [
    path('map/', views.map_restaurants, name='map'),
    path('search/', views.search_page, name='search'),
    path('<int:pk>/', views.restaurant_detail, name='detail'),
    path('search/results/', views.search_results, name='search_results'),
    path('nearby/', views.nearby_restaurants, name='nearby'),
]