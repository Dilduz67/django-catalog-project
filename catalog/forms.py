from django import  forms
from catalog.models import Product,Version

class ProductForm(forms.ModelForm):
    vrong_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model =Product
        fields = '__all__'


    def clean_name(self):
        cleaned_data=self.cleaned_data['name']

        for v in self.vrong_list:
            if v in cleaned_data:
                raise forms.ValidationError("Недопустимое слово!")

        return cleaned_data

    def clean_description(self):
        cleaned_data=self.cleaned_data['description']

        for v in self.vrong_list:
            if v in cleaned_data:
                raise forms.ValidationError("Недопустимое слово!")

        return cleaned_data

class VersionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Version
        fields = "__all__"
