#Zadanie 1
LoremIpsum="Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym." \
           " Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej" \
           " książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając" \
           " praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy" \
           " Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum" \
           " oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
#Zadanie 2
imie="Adam"
litera_1 = imie[2]
nazwisko="Jankowiak"
litera_2 = nazwisko[3]

print('W tekście jest %i liter %s , oraz %i liter %s'% (LoremIpsum.count(litera_1), litera_1, LoremIpsum.count(litera_2), litera_2))
#Zadanie 3

print('{:^6}'.format('zip'))
print('{:4d}'.format(42))
print('{:=+5d}'.format(23))
class Data(object):

    def __repr__(self):
        return 'räpr'
print('{0!r} {0!a}'.format(Data()))
print('{:10.5}'.format('xylophone'))

#Zadanie 4

print(dir("Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym."))
help("Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym.".count)

#Zadanie 5
ja="jankowiaK adaM"
ja=ja[::-1]
print(ja)

#Zadanie 6
lista1=[0,9,2,3,4,5,6,7,8,1]
lista2=lista1[5:]
lista1=lista1[0:5]
print(lista1, lista2)

#Zadanie 7
lista=lista1+lista2
lista.insert(0,0)
listaPom=lista
listaPom.sort()
print(listaPom)

#Zadanie 8
st1=(150900, "Marek Aureliusz")
st2=(150901, "Jan Kowal")
st3=(150902, "Michał Rydz")
st4=(150903, "Lena Pszczoła")
st5=(150904, "Paweł Pucek")

#Zadanie 9
slownik = dict([st1, st2, st3, st4, st5])

print(slownik.keys())


#zadanie 10
listaNumerow=["123456789", "123456789", "987654321", "987654321", "87394283", "342551234"]
lisNumerowBezPowt=set(listaNumerow)
print(lisNumerowBezPowt)

#zadanie 11
for i in range(1,11):
    print(i)

#zadanie 12
for i in range(100,19,-5):
    print(i)

#zadanie 13
slownik2 = dict({"jeden": 1, "dwa": 2, "trzy": 3})
listaSlownikow=[slownik, slownik, slownik2]
print(listaSlownikow)

