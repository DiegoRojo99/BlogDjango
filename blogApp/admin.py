from django.contrib import admin
from .models import Post, Tag, Team, Theme, Division, Conference

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Team)
admin.site.register(Theme)
admin.site.register(Division)
admin.site.register(Conference)