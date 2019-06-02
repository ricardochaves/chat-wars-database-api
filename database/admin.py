from django.contrib import admin

# Register your models here.
from database.models import AuDigest
from database.models import Item
from database.models import Player

admin.site.register(Item)
admin.site.register(AuDigest)
admin.site.register(Player)
