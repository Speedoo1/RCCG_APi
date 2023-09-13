from django.contrib import admin

from api.models import testimonial, prayerRequest, gallery, life_youtube, event

# Register your models here.
admin.site.register(testimonial)
admin.site.register(prayerRequest)
admin.site.register(gallery)
admin.site.register(life_youtube)
admin.site.register(event)

# fields = ('image_tag',)
# readonly_fields = ('image_tag',)
