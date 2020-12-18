from django.db import models

class Czytelnik(models.Model):
    idCzytelnik = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    wiek = models.IntegerField()
    adres = models.CharField(max_length=150)
    telefon = models.CharField(max_length=11)
    login = models.CharField(max_length=30, unique=True)
    haslo = models.CharField(max_length=30)

    def __str__(self):
        return 'ID:'+str(self.idCzytelnik)+'. '+self.imie + '.  ' +self.nazwisko

class Ksiazka(models.Model):
    idKsiazka = models.AutoField(primary_key=True)
    tytul = models.CharField(max_length=300)
    autor = models.CharField(max_length=50)
    minimalny_wiek_czytelnika= models.IntegerField()
    data_wydania = models.DateField()
    gatunek = models.CharField(max_length=30)
    def __str__(self):
        return 'ID:'+str(self.idKsiazka)+'. '+self.tytul + '.  ' +self.autor

class AktualneWypozyczenia(models.Model):
    idWypozyczenia = models.AutoField(primary_key=True, unique=True)
    data_wypozyczenia = models.DateField(auto_now=True)
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE, null=True)
    czytelnik = models.ForeignKey(Czytelnik, related_name='aktualnieWypozyczoneKsiazki', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return 'ID:'+str(self.ksiazka.idKsiazka)+'. '+str(self.data_wypozyczenia) +'. '+self.ksiazka.tytul\
               + '.  ' + self.ksiazka.autor

class HistoriaWypozyczen(models.Model):
    idZwrot = models.AutoField(primary_key=True, unique=True)
    data_wypozyczenia = models.DateField()
    data_zwrotu = models.DateField()
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE, null=True)
    czytelnik = models.ForeignKey(Czytelnik, related_name='historia', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return 'ID:'+str(self.ksiazka.idKsiazka)+'. '+str(self.data_wypozyczenia)+str(self.data_zwrotu)\
               + '. '+self.ksiazka.tytul + '.  ' + self.ksiazka.autor
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
    def __str__(self):
        return 'ID:'+str(self.idPracownik)+'. '+self.imie + '.  ' +self.nazwisko










