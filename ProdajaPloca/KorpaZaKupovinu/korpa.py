from decimal import Decimal
from django.conf import settings
from SalonAutomobila.models import Automobil


class Korpa(object):
    def __init__(self, request):
        self.sesija = request.session  # tekuca sesija
        korpa = self.sesija.get(settings.KORPA_ZA_KUPOVINU_SESSION_KEY)
    # uzeti korpu iz tekuce sesije, ako je nema kreirati je
        if not korpa:
            korpa = self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY] = {}
            self.korpa = korpa

    def __iter__(self):  # za view i sablone
        automobili_ids = self.korpa.keys()
        automobili = Automobil.objects.filter(id__in=automobili_ids)
        korpakopija = self.korpa.copy()
        for automobil in automobili:
            korpakopija[str(automobil.id)]['automobil'] = automobil
            for stavka in korpakopija.values():
                stavka['cena'] = Decimal(stavka['cena'])
                stavka['ukupna_cena'] = stavka['cena'] * stavka['kolicina']
                yield stavka  # vraca generator

    def __len__(self):  # za ukupan broj automobila u korpi
        return sum(stavka['kolicina'] for stavka in self.korpa.values())

    def Dodaj(self, automobil, kolicina=1, dodati_na_kolicinu=True):
        automobil_id = str(automobil.id)
        if automobil_id not in self.korpa:
            self.korpa[automobil_id] = {'kolicina': 0,
                                        'cena': str(automobil.cena)}
        if dodati_na_kolicinu:
            self.korpa[automobil_id]['kolicina'] += kolicina
        else:
            self.korpa[automobil_id]['kolicina'] = kolicina
            self.sesija.modified = True

    # da Django "zna" da je sesija modifikovana te da je snimi
    def Ukloni(self, automobil):  # uklanjanje automobila iz korpe
        automobil_id = str(automobil.id)
        if automobil_id in self.korpa:
            del self.korpa[automobil_id]
            self.sesija.modified = True

    def ObrisiJeIzSesije(self):  # uklanjanje korpe iz sesije
        del self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY]
        self.sesija.modified = True

    def UzmiUkupnuCenu(self):  # ukupna cena u korpi
        return sum(Decimal(stavka['cena']) * stavka['kolicina'] for stavka in
                   self.korpa.values())
