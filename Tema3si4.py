# Să se scrie o funcție care primește un număr nedefinit de parametrii și să
# se calculeze suma parametrilor care reprezintă numere întregi sau reale.

# def sum_numbers(*args):
#     total = 0
#     for arg in args:
#         if isinstance(arg, (int, float)):
#             total += arg
#     return total
#
#
# print(sum_numbers(1, 2, 'x', 'ccc'))




#   Să se scrie o funcție recursivă care primește ca parametru o lista cu numere întregi și returnează:
# ○ suma totală a numerelor
# ○ suma numerelor pare
# ○ suma numerelor impare




# Să se scrie o funcție care citește de la tastatură și returnează valoarea
# dacă aceasta este un număr întreg, altfel returnează valoarea 0.


# def read_integer():
#     value = input("Introduceți o valoare: ")
#     try:
#         value = int(value)
#         print(value)
#     except ValueError:
#         return 0
#
#
# read_integer()




# Să se scrie o clasă Fractie(numarator, numitor) care sa implementeze următoarele metode:
# ○ __init__ : instanțiem numărător și numitor
# ○ __str__ : afisam "numărător/numitor"
# ○ __add__ : returnam o noua fractie care reprezinta adunarea
# ○ __sub__: returnam o nouă fracție care reprezinta scădearea
# ○ inverse: returnează o nouă fracție (inversa fracției)


class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"

    def __add__(self, other):
        numarator_nou = self.numarator * other.numitor + other.numarator * self.numitor
        numitor_nou = self.numitor * other.numitor
        return Fractie(numarator_nou, numitor_nou)

    def __sub__(self, other):
        numarator_nou = self.numarator * other.numitor - other.numarator * self.numitor
        numitor_nou = self.numitor * other.numitor
        return Fractie(numarator_nou, numitor_nou)

    def inverse(self):
        return Fractie(self.numitor, self.numarator)


f1 = Fractie(1, 2)
f2 = Fractie(3, 4)

print(f1)   # afișează "1/2"
print(f2)   # afișează "3/4"

f3 = f1 + f2
print(f3)   # afișează "5/4"