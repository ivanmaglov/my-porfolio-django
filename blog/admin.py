from django.contrib import admin

# Register your models here.
from .models import Blog

class BlogAdmin(admin.ModelAdmin):

    list_display = ('title', 'p_date')
    list_filter=['p_date']
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date Information', {'fields': ['p_date'], 'classes': ['collapse']}),
        (None, {'fields': ['image']}),
        (None, {'fields': ['post']}),
    ]

    search_fields = ('title',)
    ordering = ('p_date',)


admin.site.register(Blog,BlogAdmin)
