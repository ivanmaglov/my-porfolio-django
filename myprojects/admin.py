from django.contrib import admin

from . models import Projects

class ProjectAdmin(admin.ModelAdmin):

    list_display = ('title', 'programming_language', 'pub_date', 'framework')
    list_filter = ['pub_date', 'programming_language','framework' ]
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None, {'fields': ['programming_language']}),
        (None, {'fields': ['framework']}),
        (None, {'fields': ['picture']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['link']}),
        (None, {'fields': ['file']}),
    ]

    search_fields = ('title','framework',)
    ordering = ('pub_date',)


admin.site.register(Projects,ProjectAdmin)

#from django.contrib.admin.models import LogEntry
#LogEntry.objects.all().delete()
