from django.contrib import admin
from .models import Tutorial


# customize admin
class TutorialAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp"]
	list_filter = ["updated","timestamp"]
	search_fields = ["title","content"]
	class Meta:
		model = Tutorial


# Register your models here.
admin.site.register(Tutorial, TutorialAdmin)