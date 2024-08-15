from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['weight', 'fat', 'tbw', 'bmi', 'muscle_mass', 'bone_density']
        widgets = {
            'weight': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'decimal'}),
            'fat': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'decimal'}),
            'tbw': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'decimal'}),
            'bmi': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'decimal'}),
            'muscle_mass': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'decimal'}),
            'bone_density': forms.NumberInput(attrs={'step': 0.1, 'inputmode': 'decimal'}),
        }
