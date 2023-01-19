from django.shortcuts import render

from gestArticles.models import Article, Category

def  articles_list(request):
    categories = Category.objects.all()
    articles = Article.objects.all() 
    return render(request,"gestArticles/articles_list.html",{'articles': articles,'categories':categories})
def articles_details(request,id):
    article =  Article.objects.get(id=id)
    categories = Category.objects.all()
    return render(request,"gestArticles/articles_detail.html",{'article':article,'categories':categories})
def categories(request,id):
    categories = Category.objects.all()
    articles = Article.objects.filter(category = id) 
    return render(request,"gestArticles/articles_list.html",{'articles': articles,'categories':categories})
