from django.contrib import admin
from item.models import Category, Item, Images
from home.models import Reservation
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Images)
admin.site.register(Reservation)