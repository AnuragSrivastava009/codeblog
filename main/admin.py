from django.contrib import admin


from .models import contact,login,register,item, Tutorial
from tinymce.widgets import TinyMCE
from django.db import models
class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        ("title/date", {'fields' : ['tutorial_title','tutorial_published']}),
        ("URL", {'fields': ['tutorial_slug']}),
        ("content", {'fields' : ['tutorial_content']}),
    ]

    formField_overrides= {
        models.TextField : {'widget':TinyMCE(attrs={'cols': 80, 'rows' :30})},
    }

# Register your models here.
admin.site.register(contact),
admin.site.register(login),

admin.site.register(register),

admin.site.register(item),
admin.site.register(Tutorial, TutorialAdmin),

