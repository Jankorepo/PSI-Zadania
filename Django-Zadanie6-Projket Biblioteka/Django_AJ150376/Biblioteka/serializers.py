from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Ksiazka, Czytelnik, Pracownik, PunktOdbiorczy, WypozyczoneKsiazki, HistoriaWypozyczen
import datetime

class KsiazkaSerializer(ModelSerializer):
    class Meta:
        model= Ksiazka
        fields = ["idKsiazka", "tytul", "autor", "minimalny_wiek_czytelnika", "data_wydania", "gatunek"]
    def validate_data_wydania(self, value):
        data=self.get_initial()
        if datetime.datetime.strptime(data.get("data_wydania"),"%Y-%m-%d").date()>datetime.date.today():
            raise ValidationError("Data musi być późniejsza niż dzieiejszy dzień")
        return value
class CzytelnikSerializer(ModelSerializer):
    class Meta:
        model= Czytelnik
        fields = ["idCzytelnik","imie" ,"nazwisko" ,"wiek" ,"adres","telefon" ,"login" ,"haslo" ]
    def validate_Haslo(self, value):
        data = self.get_initial()
        if len(data.get("haslo"))!=5:
            raise ValidationError("Hasło musi mieć 5 znaków!")
        return value
class PracownikSerializer(ModelSerializer):
    class Meta:
        model= Pracownik
        fields = ["idPracownik", "imie" ,"nazwisko" ,"wiek" ,"adres" ,"telefon" ,"login" ,"haslo","stanowisko"]
    def validate_Haslo(self, value):
        data = self.get_initial()
        if len(data.get("haslo"))!=5:
            raise ValidationError("Hasło musi mieć 5 znaków!")
        return value
class PunktOdbiorczySerializer(ModelSerializer):
    class Meta:
        model= PunktOdbiorczy
        fields = ["numer_schowka" ,"przechowywane_ksiazki" ,"haslo"]

    def validate_Haslo(self, value):
        data = self.get_initial()
        if len(data.get("haslo"))!=4:
            raise ValidationError("Hasło musi mieć 4 znaki!")
        return value
class WypozyczoneKsiazkiSerializer(ModelSerializer):
    class Meta:
        model = WypozyczoneKsiazki
        fields = ["idWypozyczenie","data_wypozyczenia" ,"idKsiazki" ,"idCzytelnika"]

class HistoriaWypozyczenSerializer(ModelSerializer):
    class Meta:
        model = HistoriaWypozyczen
        fields = ["idZwrot","data_wypozyczenia", "data_zwrotu" ,"idKsiazki" ,"idCzytelnika"]