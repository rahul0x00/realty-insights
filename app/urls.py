from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('property-distribution', views.property_distribution, name='property_distribution'),
    path("Property lists", views.list, name="list"),
    # path("Property analysis", views.analysis, name="analysis"),
    # path('Property data', views.data, name='property_data'),

]
