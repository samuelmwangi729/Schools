from django import forms 
from .models import Sliders,Menus,SubMenus


class SlidersForm(forms.ModelForm):
    class Meta:
        model=Sliders
        fields=('__all__')

class MenuForm(forms.ModelForm):
    class Meta:
        model=Menus
        fields=('Name','hasSub')
class SubMenuForm(forms.ModelForm):
    class Meta:
        model=SubMenus
        fields=('__all__')