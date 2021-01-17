from rest_framework.serializers import ModelSerializer, ValidationError, HyperlinkedModelSerializer,\
    HyperlinkedRelatedField, SlugRelatedField, ReadOnlyField
from .models import Ksiazka, Gatunek, Czytelnik, HistoriaWypozyczen, AktualneWypozyczenia
import datetime
from django.contrib.auth.models import User

class KsiazkaSerializer(ModelSerializer):
    gatunek = SlugRelatedField(queryset=Gatunek.objects.all(), slug_field='kategoria')
    ksiazke_dodal = ReadOnlyField(source='owner.username')
    class Meta:
        model= Ksiazka
        fields = ['pk',"idKsiazka","url", "tytul", "autor", "minimalny_wiek_czytelnika", "data_wydania",
                  "gatunek","czy_wypozyczona", 'ksiazke_dodal']
    def validate_data_wydania(self, value):
        data=self.get_initial()
        if datetime.datetime.strptime(data.get("data_wydania"),"%Y-%m-%d").date()>datetime.date.today():
            raise ValidationError("Data musi być późniejsza niż dzieiejszy dzień")
        return value
class GatunekSerializer(HyperlinkedModelSerializer):
    ksiazki = HyperlinkedRelatedField(many=True, read_only=True, view_name='ksiazka-detail')
    class Meta:
        model = Gatunek
        fields = [ 'pk', 'kategoria', 'ksiazki']

class CzytelnikSerializer(HyperlinkedModelSerializer):
    aktualnieWypozyczoneKsiazki=HyperlinkedRelatedField(many=True, read_only=True, view_name='aktualnewypozyczenia-detail')
    historia=HyperlinkedRelatedField(many=True, read_only=True, view_name="historiawypożyczeń-detail")
    czytelnika_dodal = ReadOnlyField(source='owner.username')
    class Meta:
        model= Czytelnik
        fields = ['pk', 'url',"idCzytelnik","imie" ,"nazwisko" ,"wiek" ,"adres","telefon", 'czytelnika_dodal',
                  "aktualnieWypozyczoneKsiazki", "historia"]

class AktualneWypozyczeniaSerializer(ModelSerializer):
    czytelnik=SlugRelatedField(queryset=Czytelnik.objects.all(), slug_field="nazwisko")
    ksiazka = SlugRelatedField(queryset=Ksiazka.objects.all().exclude(czy_wypozyczona=True), slug_field="tytul")
    class Meta:
        model = AktualneWypozyczenia
        fields = ['url',"idWypozyczenia","data_wypozyczenia" ,"ksiazka" ,"czytelnik",]
class HistoriaWypozyczenSerializer(ModelSerializer):
    czytelnik = SlugRelatedField(queryset=Czytelnik.objects.all(), slug_field="nazwisko")
    ksiazka = SlugRelatedField(queryset=Ksiazka.objects.all(), slug_field="tytul")
    class Meta:
        model = HistoriaWypozyczen
        fields = ["idZwrot", "data_wypozyczenia", "data_zwrotu" ,"ksiazka" ,"czytelnik",]

class PracownikDodaneKsiazkiSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Ksiazka
        fields = ['idKsiazka','tytul' ]

class PracownikDodaniCzytelnicySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Czytelnik
        fields = ['idCzytelnik','imie', 'nazwisko' ]

class PracownikSerializer(HyperlinkedModelSerializer):
    dodane_ksiazki=PracownikDodaneKsiazkiSerializer(many=True,read_only=True)
    dodani_czytelnicy = PracownikDodaniCzytelnicySerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['pk','username','dodane_ksiazki','dodani_czytelnicy']
