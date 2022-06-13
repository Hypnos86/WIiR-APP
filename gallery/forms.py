from django.forms import ModelForm, DateInput
from gallery.models import Gallery, Photo


class DataFiled(DateInput):
    input_type = 'date'


class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ['project', 'name', 'add_date', 'author']
        labels = {'project': 'Nazwa i lokalizacja inwestycji', 'name': 'Data galerii', 'add_date': 'Data utworzenia',
                  'author': 'Autor'}
        exclude = ['add_date', 'author']
        widgets = {
            'name': DataFiled()}


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"
        labels = {'gallery': 'Galeria',
                  'src': 'Zdjęcie',
                  'add_date': 'Data dodania'}
