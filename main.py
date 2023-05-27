
import csv
from datetime import datetime


class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Klasik(Pizza):
    def __init__(self):
        super().__init__("Klasik", 80)


class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita", 100)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("TürkPizza", 130)


class SadePizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 75)


class Decorator():
    def __init__(self, component, description, cost):
        self.component = component
        self.description = description
        self.cost = cost

    def get_cost(self):
        return self.component.get_cost() + \
            Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
            ' ' + Pizza.get_description(self)


class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Zeytin", 8)


class Mantar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Mantar", 10)


class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Keci Peyniri", 15)


class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Et", 20)


class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Soğan", 8)


class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza, "Mısır", 8)


def main():
    global pizzaT, pizzaS
    with open("Menu.txt", "w", encoding="utf-8") as file:
        file.write("""
    *Lütfen Bir Pizza Tabanı Seçiniz:
    1: Klasik
    2: Margarita
    3: TürkPizza
    4: Sade Pizza
    * ve seçeceğiniz sos:
    11: Zeytin
    12: Mantarlar
    13: Keçi Peyniri
    14: Et
    15: Soğan
    16: Mısır
    * Teşekkür ederiz!
                    """)

    with open("Menu.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)

    while True:
        try:
            pizzaTaban = int(input("Pizza Tabanı Seçin:"))
            if 1 <= pizzaTaban <= 4:
                if pizzaTaban == 1:
                    pizzaT = Klasik()
                    break
                elif pizzaTaban == 2:
                    pizzaT = Margarita()
                    break
                elif pizzaTaban == 3:
                    pizzaT = TurkPizza()
                    break
                elif pizzaTaban == 4:
                    pizzaT = SadePizza()
                    break
                else:
                    break
            else:
                print("1-4 arasında rakam giriniz")
        except ValueError:
            print("Lütfen sayı veya rakam giriniz")

    while True:
        try:
            pizzaSos = int(input("Pizza Sosu Seçin:"))
            if 11 <= pizzaSos <= 16:
                if pizzaSos == 11:
                    pizzaS = Zeytin(pizzaT)
                    break
                elif pizzaSos == 12:
                    pizzaS = Mantar(pizzaT)
                    break
                elif pizzaSos == 13:
                    pizzaS = KeciPeyniri(pizzaT)
                    break
                elif pizzaSos == 14:
                    pizzaS = Et(pizzaT)
                    break
                elif pizzaSos == 15:
                    pizzaS = Sogan(pizzaT)
                    break
                elif pizzaSos == 16:
                    pizzaS = Misir(pizzaT)
                    break
                else:
                    break
            else:
                print("11-16 arasında sayı giriniz")
        except ValueError:
            print("Lütfen sayı veya rakam giriniz")

    print(f"\nTOPLAM FİYAT: {pizzaS.get_cost()} TL  \nPİZZA ve SOS: {pizzaS.get_description()} \n")

    print("Sipariş tamamlamak için bilgilerinizi giriniz")
    ad = input("Ad: ")
    soyad = input("Soyad: ")

    while True:
        try:
            TC_no = int(input("TC numarası: "))
            k_k_numarası = int(input("Kredi kartı numarası:"))
            sifre = int(input("Kart Şifresi: "))
            break
        except ValueError:
            print("\nlütfen TC numarası, kart numarası ve şifreyi  tekrardan sayı olarak giriniz\n")

    cost = pizzaS.get_cost()
    description = pizzaS.get_description()

    now = datetime.now()
    time_now = now.strftime("%H:%M:%S  %m-%d-%Y")

    data = [ad, soyad, TC_no, k_k_numarası, cost, description, time_now, sifre]

    with open("Orders_Database.csv", "a", newline="", encoding="utf-8") as file:
        content_file = csv.writer(file)
        content_file.writerow(data)

    print("Siparişiniz Tamamlandı")


if __name__ == '__main__':
    main()
