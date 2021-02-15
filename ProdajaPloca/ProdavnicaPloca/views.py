from django.shortcuts import render, get_object_or_404
from .models import Kategorija, Ploca


def ListaPloca(request, kategorija_slug=None):  # vraca katalog kao html
    kategorija = None
    kategorije = Kategorija.objects.all()
    ploce = Ploca.objects.filter(na_stanju=True)
    if kategorija_slug:
        kategorija = get_object_or_404(kategorija, slug=kategorija_slug)
        ploce = ploce.filter(kategorija=kategorija)
        return render(request, 'ProdavnicaPloca/Ploca/list.html',
                      {'kategorija': kategorija, 'kategorije': kategorije,
                       'ploce': ploce})
# vraćanje podatka o jednom plocau prema prosleđenom id plocaa:


def DetaljiPloca(request, id, slug):
    # vraca podatke o plocau za dati id i slug kao html odgovor
    ploca = get_object_or_404(Ploca, id=id, slug=slug,
                              na_stanju=True)
    return render(request, 'ProdavnicaPloca/ploca/detail.html',
                  {'ploca': ploca})
