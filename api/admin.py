from django.contrib import admin

from api.models import testimonial, prayerRequest, gallery

# Register your models here.
admin.site.register(testimonial)
admin.site.register(prayerRequest)
admin.site.register(gallery)

# fields = ('image_tag',)
# readonly_fields = ('image_tag',)
