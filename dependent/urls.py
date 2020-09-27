from django.urls import include, path

from . import views
app_name = "dependent"

urlpatterns = [
     path('', views.index, name="home"),
     path('details/<int:id>', views.details, name="details"),
     path('update/<int:pk>/', views.person_update_view, name='person_change'),
     path('create', views.create, name="create"),
     path('ajax/load_division/', views.load_division, name='ajax_load_division'), # AJAX
     path('ajax/load-district/', views.load_district, name='ajax_load_district'), # AJAX
     path('ajax/load-subdistrict/', views.load_subdistrict, name='ajax_load_subdistrict'), # AJAX
]
