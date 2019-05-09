from django import forms
from .models import Potential


class PotentialForm(forms.ModelForm):
    class Meta:
        model = Potential
        fields = ['username','email','phone','question']