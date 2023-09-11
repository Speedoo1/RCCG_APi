from rest_framework import serializers

from api.models import prayerRequest, testimonial, gallery


class testimonialserializer(serializers.ModelSerializer):
    class Meta:
        model = testimonial
        fields = '__all__'


class prayerRequestserializer(serializers.ModelSerializer):
    class Meta:
        model = prayerRequest
        fields = '__all__'


class galleryserializer(serializers.ModelSerializer):
    class Meta:
        model = gallery
        fields = '__all__'
