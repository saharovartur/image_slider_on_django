from django.shortcuts import render

from images.models import Image


def image_list(request):
    images = Image.objects.all()
    return render(request, 'base.html', {'images': images})
