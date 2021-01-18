from rest_framework.test import APITestCase
from . import views
from .models import Gatunek, Czytelnik
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from django import urls
import datetime


class GatunekTests(APITestCase):
    def post_gatunek(self, kategoria):
        url = reverse(views.GatunekList.name)
        data = {'kategoria': kategoria}
        response = self.client.post(url, data, format='json')
        return response

    def test_post_and_get_book_category(self):
        kategoria = 'nowy gatunek'
        response = self.post_gatunek(kategoria)
        assert response.status_code == status.HTTP_201_CREATED
        assert Gatunek.objects.count() == 1
        assert Gatunek.objects.get().kategoria == kategoria

    def test_update_book_category(self):
        kategoria = 'nowy gatunek'
        response = self.post_gatunek(kategoria)
        url = urls.reverse(views.GatunekDetail.name,None,{response.data['pk']})
        zmieniona_kategoria = 'inny nowy gatunek'
        data = {'kategoria': zmieniona_kategoria}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['kategoria'] == zmieniona_kategoria

    def test_get_book_category(self):
        kategoria = 'nowy gatunek'
        response = self.post_gatunek(kategoria)
        url = urls.reverse(views.GatunekDetail.name,None,{response.data['pk']})
        get_response = self.client.patch(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['kategoria'] == kategoria

class CzytelnikTests(APITestCase):
    def post_czytelnik(self, imie, nazwisko, wiek, adres, telefon, owner):
        url = reverse(views.CzytelnikList.name)
        data = {'imie': imie,'nazwisko': nazwisko, 'wiek': wiek,'adres': adres,
                'telefon': telefon, 'owner': owner}
        response = self.client.post(url, data, format='json')
        return response
    def test_post_and_get_czytelnik(self):
        imie = 'Jan'
        nazwisko= "Wiśniewski"
        wiek= 81
        adres = "Wojska Polskiego 8/1"
        telefon = '123456789'
        owner = 1
        response = self.post_czytelnik(imie, nazwisko, wiek, adres, telefon, owner)
        assert response.status_code == status.HTTP_201_CREATED
        assert Czytelnik.objects.count() == 1
        assert Czytelnik.objects.get().imie == imie
        assert Czytelnik.objects.get().nazwisko == nazwisko
        assert Czytelnik.objects.get().wiek == wiek
        assert Czytelnik.objects.get().adres == adres
        assert Czytelnik.objects.get().telefon == telefon

    def test_update_czytelnik(self):
        imie = 'Jan'
        nazwisko = "Wiśniewski"
        wiek = 81
        adres = "Wojska Polskiego 8/1"
        telefon = '123456789'
        owner = 1
        response = self.post_czytelnik(imie, nazwisko, wiek, adres, telefon, owner)
        url = urls.reverse(views.CzytelnikDetail.name, None, {response.data['pk']})
        nowy_adres = "Wojska Polskiego 8/1"
        nowy_telefon = '123456789'
        data = {'imie': imie, 'nazwisko': nazwisko, 'wiek': wiek, 'adres': nowy_adres,
                'telefon': nowy_telefon, 'owner': owner}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['telefon'] == nowy_telefon
        assert patch_response.data['adres'] == nowy_adres

