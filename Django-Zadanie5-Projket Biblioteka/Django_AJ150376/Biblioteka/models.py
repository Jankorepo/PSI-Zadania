from django.db import models


class Ksiazka(models.Model):
    idKsiazka = models.AutoField(primary_key=True)
    tytul = models.CharField(max_length=300)
    autor = models.CharField(max_length=50)
    minimalny_wiek_czytelnika= models.IntegerField()
    data_wydania = models.DateField()
    gatunek = models.CharField(max_length=30)
class Czytelnik(models.Model):

    idCzytelnik = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    wiek = models.IntegerField()
    adres = models.CharField(max_length=150)
    telefon = models.CharField(max_length=11)
    login = models.CharField(max_length=30, unique=True)
    haslo = models.CharField(max_length=30)

class Pracownik(models.Model):
    idPracownik = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    wiek = models.IntegerField()
    adres = models.CharField(max_length=30)
    telefon = models.CharField(max_length=30)
    login = models.CharField(max_length=30, unique=True)
    haslo = models.CharField(max_length=30)
    stanowisko = models.CharField(max_length=30)

class PunktOdbiorczy(models.Model):
    numer_schowka = models.IntegerField(primary_key=True)
    przechowywane_ksiazki = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    haslo = models.CharField(max_length=5)

class WypozyczoneKsiazki(models.Model):
    idWypozyczenie = models.AutoField(primary_key=True)
    data_wypozyczenia = models.DateField(auto_now=True)
    idKsiazki = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    idCzytelnika = models.ForeignKey(Czytelnik, on_delete=models.CASCADE)

class HistoriaWypozyczen(models.Model):
    idZwrot = models.AutoField(primary_key=True, unique=True)
    data_wypozyczenia = models.DateField(auto_now=True)
    data_zwrotu = models.DateField()
    idKsiazki = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    idCzytelnika = models.ForeignKey(Czytelnik, on_delete=models.CASCADE)








