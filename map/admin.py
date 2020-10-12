from django.contrib import admin


from .models import sighting
from .models import sightshow


admin.site.register(sighting)
admin.site.register(sightshow)



# Register your models here.
