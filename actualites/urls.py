from django.contrib import admin
from django.urls import path

from gestArticles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/',views.articles_list,name="articles-list"),
    path('articles/<int:id>/',views.articles_details,name="articles-details"),
     path('categories/<int:id>/',views.categories,name="categories-details"),
    
]
