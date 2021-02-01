L = [["rainy", "mild", "high", "true", "no"],
     ["sunny", "hot", "high", "false", "no"],
     ["sunny", "hot", "high", "true", "no"],
     ["overcast", "hot", "high", "false", "yes"],
     ["rainy", "mild", "high", "false", "yes"],
     ["rainy", "cool", "normal", "false", "yes"],
     ["rainy", "cool", "normal", "true", "no"],
     ["overcast", "cool", "normal", "true", "yes"],
     ["sunny", "mild", "high", "false", "no"],
     ["sunny", "cool", "normal", "false", "yes"],
     ["rainy", "mild", "normal", "false", "yes"],
     ["sunny", "mild", "normal", "false", "yes"],
     ["overcast", "mild", "high", "true", "yes"],
     ["overcast", "hot", "normal", "false", "yes"]]

import re


def P(A, skup):
    return skup.count(A) / len(skup)


def bayes(A, uvjet, skup_A, skup_uvjet):
    count = 0

    for i in range(len(skup_A)):
        if skup_A[i] == A and skup_uvjet[i] == uvjet:
            count += 1

    return count / len(skup_uvjet)


def stupac(L, index):
    Li = []

    for i in L:
        Li.append(i[index])

    return Li


def elementarni_dog(L):
    Elem = []

    for i in L:
        if i not in Elem:
            Elem.append(i)

    return Elem


def redak(L, uvjet):
    Nova_lista = []

    for i in L:
        if i[len(L[0]) - 1] == uvjet:
            Nova_lista.append(i)

    return Nova_lista


def naivni_bayes(L, uvjet):
    Elem = elementarni_dog(stupac(L, len(L[0]) - 1))
    Rez = []

    for i in range(len(Elem)):
        Rez.append(P(Elem[i], stupac(L, len(L[0]) - 1)))
        for j in range(len(L[0]) - 1):
            Rez[i] = Rez[i] * bayes(uvjet[j], Elem[i], stupac(redak(L, Elem[i]), j),
                                    stupac(redak(L, Elem[i]), len(L[0]) - 1))

    for i in range(len(Rez)):
        Rez[i] *= 2

    return Rez


def sve_rijeci():
    f = open("sve.txt", "r", encoding="utf-8")
    tekst = f.read()
    rijeci = tekst.split(" ")
    broj = 0

    for r in rijeci:
        broj += 1
    print(broj)


def broji_rijec(r):
    f = open("sve.txt", "r", encoding="utf-8")
    tekst = f.read()
    # rijeci = tekst.split(" ")
    return tekst.count(r)

# sve_rijeci()
# print(broji_rijec("zabava"))

# print(naivni_bayes(L, ["sunny", "cool", "high", "true"]))
