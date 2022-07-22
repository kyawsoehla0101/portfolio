from django.contrib import admin
from .models import About, Blog, Category, Contact, Gallery, Hero, Skill, Tag, Typing, Year
# Register your models here.
admin.site.register(Hero)
admin.site.register(Typing)
admin.site.register(About)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Gallery)
admin.site.register(Year)