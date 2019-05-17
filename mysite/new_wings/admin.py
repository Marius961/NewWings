from django.contrib import admin
from django.contrib import admin
from .models import Slider,PersonalDate


class PersonalDateAdmin(admin.ModelAdmin):
    list_display =['full_name',' age','city','profesion','problem ','reabilitations_type','diseases']

admin.site.register(Slider)
admin.site.register(PersonalDate)
#
# admin.site.register(MetaTag)
#

# admin.site.register(FirstSection)
# admin.site.register(ServisList)
# admin.site.register(SecondSection)
# admin.site.register(FourthSection)
# admin.site.register(ContactSectiion)
# #
# Register your models here.
