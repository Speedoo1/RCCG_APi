from django.urls import path

from api import views

urlpatterns = [
    path('testimonial', views.testimonialView),
    path('addTestimonial', views.addTestimonial),
    path('deleteTestimonial/<str:pk>/', views.deleteTestimonial),

    path('prayerRequest', views.prayerRequestView),
    path('addPrayerRequest', views.addprayerRequest),
    path('deletePrayerRequest/<str:pk>/', views.deletePrayerRequest),
    path('gallery/', views.gallerys),
    path('event/', views.events),
    path('life_youtube/', views.life_youtubes),

]
