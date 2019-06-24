from django import forms

from photoeditor.models import UploadImage


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = UploadImage
        fields = ['height', 'width', 'img']
