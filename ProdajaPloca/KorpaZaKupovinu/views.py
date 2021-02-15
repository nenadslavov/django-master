from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from SalonAutomobila.models import Automobil
from .korpa import Korpa
from .forms import FormaZaDodavanjeAutomobilaUKorpu


@require_POST  # dekorator za prihvatanje POST zahteva
def DodajUKorpu(request, automobil_id):
    korpa = Korpa(request)
    automobil = get_object_or_404(Automobil, id=automobil_id)
    form = FormaZaDodavanjeAutomobilaUKorpu(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        korpa.Dodaj(automobil=automobil,
                    kolicina=cd['kolicina'],
                    dodati_na_kolicinu=cd['dodati_na_kolicinu'])
    return redirect('KorpaZaKupovinu:DetaljiKorpe')


@require_POST
def UkloniIzKorpe(request, automobil_id):
    korpa = Korpa(request)
    automobil = get_object_or_404(Automobil, id=automobil_id)
    korpa.Ukloni(automobil)
    return redirect('KorpaZaKupovinu:DetaljiKorpe')


def DetaljiKorpe(request):
    korpa = Korpa(request)
    for stavka in korpa:
        stavka['formazaazuriranjekolicine'] = FormaZaDodavanjeAutomobilaUKorpu(
            initial={'kolicina': 1, 'dodati_na_kolicinu': True})
    return render(request, 'KorpaZaKupovinu/detail.html', {'korpa': korpa})
