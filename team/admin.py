from django.contrib import admin
from .models import (
    TeamCatalogue,
    Team
)


admin.site.register(TeamCatalogue)
admin.site.register(Team)
