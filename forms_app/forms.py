from django import forms
from .models import FormModel


class PostForm(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = {'name', 'address', 'operating_budget', 'description', 'number_of_employees', 'image_url'}
        order_field = ['name', 'address', 'operating_budget', 'description', 'number_of_employees']

