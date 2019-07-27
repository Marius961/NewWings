from django.contrib import admin
from django.contrib import admin
from .models import *
class InformationAdmin (admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True
class SliderAdmin (admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 5:
      return False
    else:
      return True
class SocialAdmin (admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 3:
      return False
    else:
      return True
class ContactAdmin (admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(Slider,SliderAdmin)
admin.site.register(Information,InformationAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Social,SocialAdmin)
admin.site.register(Reabil)
admin.site.register(Sponsor)
admin.site.register(Donate)
admin.site.register(New)
admin.site.register(Suport)
# admin.site.register(MetaTag)
#

# admin.site.register(FirstSection)
# admin.site.register(ServisList)
# admin.site.register(SecondSection)
# admin.site.register(FourthSection)
# admin.site.register(ContactSectiion)
# #
# Register your models here.
