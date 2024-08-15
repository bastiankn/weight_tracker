from django import forms
from .models import Mass

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Mass
        fields = ['weight', 'fat', 'tbw', 'bmi', 'muscle_mass', 'bone_density']
        widgets = {
            'weight': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'float'}),
            'fat': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'float'}),
            'tbw': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'float'}),
            'bmi': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'float'}),
            'muscle_mass': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'float'}),
            'bone_density': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'float'}),
        }
