from rest_framework import serializers

from api.models import prayerRequest, testimonial, gallery, event, life_youtube


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


class eventserializer(serializers.ModelSerializer):
    class Meta:
        model = event
        fields = '__all__'


class youtubeserializer(serializers.ModelSerializer):
    class Meta:
        model = life_youtube
        fields = '__all__'
