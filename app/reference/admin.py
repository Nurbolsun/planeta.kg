from django.contrib import admin
from .models import *


class PartAdmin(admin.ModelAdmin):
    exclude = ('location',)

    def save_model(self, request, obj, form, change):
        obj.location = 'Бишкек'
        super().save_model(request, obj, form, change)


admin.site.register(Category)
admin.site.register(PartImage)
admin.site.register(RefCarMark)
admin.site.register(RefCarFuel)
admin.site.register(RefCarGearBox)
admin.site.register(RefCarSteeringWheel)
admin.site.register(RefCarWheelDrive)
admin.site.register(RefCarModel)
admin.site.register(Part, PartAdmin)