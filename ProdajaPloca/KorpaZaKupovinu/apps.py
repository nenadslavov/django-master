from django import forms
from django.apps import AppConfig


class KorpazakupovinuConfig(AppConfig):
    name = 'KorpaZaKupovinu'


IZBOR_BROJA_AUTOMOBILA = [(i, str(i)) for i in range(1, 11)]


class FormaZaDodavanjeAutomobilaUKorpu(forms.Form):
    kolicina = forms.TypedChoiceField(choices=IZBOR_BROJA_AUTOMOBILA,
                                      empty_value=1, coerce=int)  # prebaci u int
    dodati_na_kolicinu = forms.BooleanField(required=False, initial=True,
                                            widget=forms.HiddenInput)
