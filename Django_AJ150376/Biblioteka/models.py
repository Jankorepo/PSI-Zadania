from django.db import models

class Czytelnik(models.Model):
    idCzytelnik = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    wiek = models.IntegerField()
    adres = models.CharField(max_length=150)
    telefon = models.CharField(max_length=11)
    owner = models.ForeignKey('auth.User', related_name='dodani_czytelnicy', on_delete=models.CASCADE, null=True)
    class Meta:
        ordering=('idCzytelnik',)
    def __str__(self):
        return 'ID:'+str(self.idCzytelnik)+'. '+self.imie + '.  ' +self.nazwisko

class Gatunek(models.Model):
    kategoria = models.CharField(max_length=40, unique=True)
    class Meta:
        ordering = ('kategoria',)
    def __str__(self):
        return self.kategoria

class Ksiazka(models.Model):
    idKsiazka = models.AutoField(primary_key=True)
    tytul = models.CharField(max_length=300)
    autor = models.CharField(max_length=50)
    minimalny_wiek_czytelnika= models.IntegerField()
    data_wydania = models.DateField()
    gatunek = models.ForeignKey(Gatunek, related_name='ksiazki', on_delete=models.DO_NOTHING)
    czy_wypozyczona=models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='dodane_ksiazki', on_delete=models.DO_NOTHING, null=True)
    class Meta:
        ordering=('idKsiazka',)
    def __str__(self):
        return 'ID:'+str(self.idKsiazka)+'. '+self.tytul + '.  ' +self.autor

class AktualneWypozyczenia(models.Model):
    idWypozyczenia = models.AutoField(primary_key=True, unique=True)
    data_wypozyczenia = models.DateField(auto_now=True)
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE, null=True)
    czytelnik = models.ForeignKey(Czytelnik, related_name='aktualnieWypozyczoneKsiazki',
                                  on_delete=models.DO_NOTHING, null=True)
    class Meta:
        ordering=('idWypozyczenia',)
    def __str__(self):
        return 'ID:'+str(self.ksiazka.idKsiazka)+'. '+str(self.data_wypozyczenia) +'. '+self.ksiazka.tytul\
               + '.  ' + self.ksiazka.autor

class HistoriaWypozyczen(models.Model):
    idZwrot = models.AutoField(primary_key=True, unique=True)
    data_wypozyczenia = models.DateField()
    data_zwrotu = models.DateField()
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE, null=True)
    czytelnik = models.ForeignKey(Czytelnik, related_name='historia', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return 'ID:'+str(self.ksiazka.idKsiazka)+'. '+str(self.data_wypozyczenia)+str(self.data_zwrotu)\
               + '. '+self.ksiazka.tytul + '.  ' + self.ksiazka.autor
    class Meta:
        ordering=('idZwrot',)










