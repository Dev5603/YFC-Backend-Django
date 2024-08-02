from django.contrib import admin

from .models import User, Offer, Plan, Category, Blog, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Plan)
admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Comment)