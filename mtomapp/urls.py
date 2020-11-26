from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
     path('addbook', views.addbook),
     path('additem/<str:which_form>', views.additem),
    path('viewbook/<str:id>', views.viewbook),
    path('addAuthortobook/<str:bid>/<str:aid>', views.addAuthortobook),
    path('addauthor', views.addauthor),
    path('viewauthor/<str:id>', views.viewauthor),
    path('addBooktoAuthor/<str:bid>/<str:aid>', views.addBooktoAuthor),
]