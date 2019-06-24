from io import BytesIO

import numpy
from PIL import Image
from django.core.files.base import ContentFile

from django.shortcuts import render, redirect
from django.urls import reverse

from photoeditor.models import UploadImage

from photoeditor.forms import UploadImageForm

from photoeditor.seam_carving import Carver


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('/auth/login/')


def your_photo(request):
    list_of_img = UploadImage.objects.filter(user=request.user)
    return render(request, 'yourPhotos.html', {'list_of_img': list_of_img})


def upload_photo(request):
    if request.method == "GET":
        image_form = UploadImageForm()
        return render(request, 'uploadPhoto.html', {'image_form': image_form,})
    elif request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            up_img = form.save(commit=False)
            height = form.cleaned_data.get('height')
            width = form.cleaned_data.get('width')

            filestr = request.FILES['img'].read()
            npimg = numpy.fromstring(filestr, numpy.uint8)
            obj = Carver(npimg, height, width)
            img = obj.get_final_img()

            im = Image.fromarray(img)
            thumb_io = BytesIO()
            im.save(thumb_io, format="png", quality=60)
            up_img.img.save("output_img.jpg", ContentFile(thumb_io.getvalue()), save=False)

            up_img.user = request.user
            up_img.height = height
            up_img.width = width
            form.save()
            return redirect(reverse('photoeditor:index'))
