from rest_framework.serializers import ModelSerializer, ValidationError, HyperlinkedModelSerializer,\
    HyperlinkedRelatedField, SlugRelatedField
from .models import Ksiazka, Czytelnik, Pracownik, HistoriaWypozyczen, AktualneWypozyczenia
import datetime
import random

class KsiazkaSerializer(ModelSerializer):

    class Meta:
        model= Ksiazka
        fields = ["idKsiazka","url", "tytul", "autor", "minimalny_wiek_czytelnika", "data_wydania", "gatunek"]
    def validate_data_wydania(self, value):
        data=self.get_initial()
        if datetime.datetime.strptime(data.get("data_wydania"),"%Y-%m-%d").date()>datetime.date.today():
            raise ValidationError("Data musi być późniejsza niż dzieiejszy dzień")
        return value
class CzytelnikSerializer(HyperlinkedModelSerializer):
    aktualnieWypozyczoneKsiazki=HyperlinkedRelatedField(many=True, read_only=True, view_name='aktualneWypozyczenia-detail')
    historia=HyperlinkedRelatedField(many=True, read_only=True, view_name="historiaWypożyczeń-detail")
    class Meta:
        model= Czytelnik
        fields = ["idCzytelnik","imie" ,"nazwisko" ,"wiek" ,"adres","telefon" ,"login" ,"haslo",
                  "aktualnieWypozyczoneKsiazki", "historia"]
    def validate_Haslo(self, value):
        data = self.get_initial()
        if len(data.get("haslo"))!=5:
            raise ValidationError("Hasło musi mieć 5 znaków!")
        return value
class PracownikSerializer(ModelSerializer):
    class Meta:
        model= Pracownik
        fields = ["idPracownik", "url", "imie" ,"nazwisko" ,"wiek" ,"adres" ,"telefon" ,"login" ,"haslo","stanowisko"]
    def validate_Haslo(self, value):
        data = self.get_initial()
        if len(data.get("haslo"))!=5:
            raise ValidationError("Hasło musi mieć 5 znaków!")
        return value

class AktualneWypozyczeniaSerializer(ModelSerializer):
    czytelnik=SlugRelatedField(queryset=Czytelnik.objects.all(), slug_field="nazwisko")
    ksiazka = SlugRelatedField(queryset=Ksiazka.objects.all(), slug_field="tytul")
    class Meta:
        model = AktualneWypozyczenia
        fields = ["idWypozyczenia","data_wypozyczenia" ,"ksiazka" ,"czytelnik",]

class HistoriaWypozyczenSerializer(ModelSerializer):
    czytelnik = SlugRelatedField(queryset=Czytelnik.objects.all(), slug_field="nazwisko")
    ksiazka = SlugRelatedField(queryset=Ksiazka.objects.all(), slug_field="tytul")
    class Meta:
        model = HistoriaWypozyczen
        fields = ["idZwrot", "data_wypozyczenia", "data_zwrotu" ,"ksiazka" ,"czytelnik",]

