import file_menager as mng
def funZad1(lista1, lista2):
    i=0
    lista=[]
    while i<len(lista1) and i<len(lista2):
        if i%2==0:
            lista.append(lista1[i])
        else:
            lista.append(lista2[i])
        i=i+1
    return lista
lista1=[1,5,2,8]
lista2=[12,56,23,98]
print(funZad1(lista1,lista2))

def funZad2(data_text):
    słowniczek={
        'lenght': len(data_text),
        'letters': list(data_text),
        'big_letters': data_text.upper(),
        'small_letters': data_text.lower(),
    }
    return słowniczek

print(funZad2("Hello There"))


def funZad3(text,letter):
    return text.replace(letter, "")
print("\n "+funZad3("HelloThere", "l"))

def funZad4(value, temperature_type):
    if temperature_type=="Kelvin":
        if value<-273.15:
            return ("Błąd")
        else:
            return value+273.15
    if temperature_type == "Rankie":
        if value < -273.15:
            return ("Błąd")
        else:
            return (value + 273.15) * 1.8
    if temperature_type == "Farenhait":
        if value < -273.15:
            return ("Błąd")
        else:
            return (value * 1.8) + 32
print(funZad4(100, "Farenhait"))


class Kalkulator:
    def add(self,x,y):
        return x+y
    def difference(self,x,y):
        if x-y<0:
            return y-y
        return x-y
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y!=0:
            return x/y
        return "Błąd"
x=Kalkulator()
print(x.add(3,5))

class ScienceKalkulator(Kalkulator):
    def potegowanie(self,x,y):
        return x**y

y=ScienceKalkulator()
print(y.potegowanie(2,5))



def funZad7(word):
    str = ""
    for i in word:
        str = i + str
    return str
print(funZad7("HelloThere"))



pliku=mng.FileManager("plik.txt")
pliku.update_file("Hello")
pliku.read_file()







