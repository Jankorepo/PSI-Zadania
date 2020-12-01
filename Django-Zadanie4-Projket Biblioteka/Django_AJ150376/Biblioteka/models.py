from django.db import models

class Ksiazka(models.Model):
    idKsiazka = models.AutoField(primary_key=True)
    tytul = models.CharField(max_length=300)
    autor = models.CharField(max_length=50)
    min_wiek_czytelnika= models.IntegerField()
    data_wydania = models.DateField()
    gatunek = models.CharField(max_length=30)
    data_wyporzyczenia = models.DateField()
class Czytelnik(models.Model):
    idCzytelnik = models.AutoField(primary_key=True )
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    wiek = models.IntegerField()
    adres = models.CharField(max_length=150)
    telefon = models.CharField(max_length=11)
    login = models.CharField(max_length=30)
    haslo = models.CharField(max_length=30)
    posiadane_ksiazki=models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
class Pracownik(models.Model):
    idPracownik = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    wiek = models.IntegerField()
    adres = models.CharField(max_length=30)
    telefon = models.CharField(max_length=30)
    login = models.CharField(max_length=30)
    haslo = models.CharField(max_length=30)
    stanowisko = models.CharField(max_length=30)
class PunktOdbiorczy(models.Model):
    numer_schowka = models.IntegerField(primary_key=True)
    przechowywane_ksiazki = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    haslo = models.CharField(max_length=5)








