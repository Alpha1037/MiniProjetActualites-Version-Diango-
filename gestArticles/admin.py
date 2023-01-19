from django.contrib import admin

from gestArticles.models import Article, Category

class CategoryAdmin(admin.ModelAdmin):  
    list_display = ('label','active')
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')  
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
