from .models import Jobs
from django import forms


class JobForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = '__all__'

