from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import testimonial, prayerRequest, gallery, event, life_youtube, newsletter
from api.serializer import testimonialserializer, prayerRequestserializer, galleryserializer, eventserializer, \
    youtubeserializer


# Create your views here.

@api_view(['GET'])
def testimonialView(request):
    testimonials = testimonial.objects.all().order_by('date_posted')
    # foodlist.objects.all()
    if testimonials:
        serializer = testimonialserializer(testimonials, many=True)
        return Response(serializer.data)
    else:
        context = {'empty': 'No Testimonial found'}
        return Response(context)


@api_view(['GET'])
def addTestimonial(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        header = request.GET.get('header')
        location = request.GET.get('location')
        message = request.GET.get('message')
        setTestimonial = testimonial(name=name, email=email, location=location, heading=header, text=message)
        if setTestimonial:
            setTestimonial.save()
            context = {'success': 'testimonial added successfully'}
        else:
            context = {'error': 'issue occur please try again later'}
    return Response(context)


@api_view(['GET'])
def deleteTestimonial(request, pk):
    getTestimonial = testimonial.objects.get(id=pk)
    getTestimonial.delete()
    context = {'success': 'Testimonial deleted successfully'}
    return Response(context)


@api_view(['GET'])
def prayerRequestView(request):
    prayer = prayerRequest.objects.all().order_by('date_posted')

    if prayer:
        serializer = prayerRequestserializer(prayer, many=True)
        return Response(serializer.data)
    else:
        context = {'empty': 'No Prayer request yet'}
        return Response(context)


@api_view(['GET'])
def addprayerRequest(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    header = request.GET.get('header')
    location = request.GET.get('location')
    message = request.GET.get('message')
    setprayer = prayerRequest(name=name, email=email, location=location, heading=header, text=message)
    if setprayer:
        setprayer.save()
        context = {'success': 'Prayer Request added successfully'}
    else:
        context = {'error': 'issue occur please try again later'}
    return Response(context)


@api_view(['GET'])
def deletePrayerRequest(request, pk):
    getprayer = prayerRequest.objects.get(id=pk)
    getprayer.delete()
    context = {'success': 'Prayer request deleted successfully'}
    return Response(context)


@api_view(['GET'])
def gallerys(request):
    getGallery = gallery.objects.all()
    if getGallery:
        serialize = galleryserializer(getGallery, many=True)
        return Response(serialize.data)
    else:
        context = {'empty': 'no gallery yet'}
        return Response(context)


@api_view(['GET'])
def events(request):
    getevent = event.objects.all()
    if getevent:
        serialize = eventserializer(getevent, many=True)
        return Response(serialize.data)
    else:
        context = {'empty': 'no event yet'}
        return Response(context)


@api_view(['GET'])
def life_youtubes(request):
    getlife_youtube = life_youtube.objects.all()
    if getlife_youtube:
        serialize = youtubeserializer(getlife_youtube, many=True)
        return Response(serialize.data)
    else:
        context = {'empty': 'no life_youtubes yet'}
        return Response(context)


# @api_view(['GET'])
def newsletters(request):
    if request.method == 'POST':

        emails = request.POST.get('email')
        try:
            news = newsletter.objects.get(email=emails)
        except:
            newsletter(email=emails)
            if newsletter:
                emails.save()
                context = {'saved': 'email saved successfully'}
                return Response(context)
            else:
                return Response({'error:': 'error saving email'})
    return Response({'exist': 'Email already exist '})
