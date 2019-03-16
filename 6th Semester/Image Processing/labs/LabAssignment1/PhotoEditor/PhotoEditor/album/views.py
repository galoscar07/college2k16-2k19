import numpy
from PIL import Image
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render, redirect

from PhotoEditor.album.effects import convert_grayscale
from .models import Photo
from .forms import PhotoForm


def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'album/photo_list.html', {'form': form, 'photos': photos})


def photo_edit(request, *args, **kwargs):
    # hacky thing but we know for sure that post request will only be when a filter button was pressed
    if request.POST == {}:
        # means the user entered the page for the first time => display same photo in both parts
        photo_id = int(kwargs['photo_id'])
        photo = Photo.objects.filter(pk=photo_id)
        return render(request, 'album/photo_edit.html', {'photo1': photo[0], 'photo2': photo[0]})
    else:
        # means that the user pressed a button
        photo_id = int(kwargs['photo_id'])
        photo = Photo.objects.filter(pk=photo_id)[0]
        if 'gray_scale' in request.POST.keys():
            image_normal = Image.open(photo.file)
            image_normal = convert_grayscale(image_normal)
            image_normal.save("out.jpg", "JPEG", quality=80, optimize=True, progressive=True)
            import pdb;pdb.set_trace()
            path = default_storage.save(photo.file.path + 'gray', ContentFile('new content'))
            photo2 = Photo.objects.create(file=path)
            return render(request, 'album/photo_edit.html', {'photo1': photo, 'photo2': photo2})
        elif 'gray_scale' in request.POST.keys():
            # apply
            pass
        elif 'gray_scale' in request.POST.keys():
            # apply
            pass
        elif 'gray_scale' in request.POST.keys():
            # apply
            pass
        else:
            # apply
            pass
        import pdb;pdb.set_trace()
