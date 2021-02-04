import re
import os.path

# db path
file_path = os.path.dirname(__file__).rpartition('\\')
db_path = f"{file_path[0]}\\db"
sve_txt = f"{db_path}\\sve.txt"


def sve_rijeci():
	f = open(sve_txt, "r", encoding="utf-8")
	tekst = f.read()
	rijeci = tekst.split(" ")
	return len(rijeci)


# funkcija uzima argument rijec
# broji koliko se puta rijec ponavalja u tekstu
def broji_rijec(rijec):

	f = open(sve_txt, "r", encoding="utf-8")
	tekst = f.read()
	return tekst.count(rijec)


# varijabla koja sprema broj rijeci u tekstu
# sluzi tome da se broj rijeci negdje pamti a ne svaki put ponovnno racuna
broj_svih_rijeci = sve_rijeci()


# funkcija razdvaja rijeci iz teksta u 2d polje
# npr.
# [["ovo", "je", "samo"], ["test", "12", "34"], ["test", "je", ovo]]

def napravi_array():
	f = open(sve_txt, "r", encoding="utf-8")

	result = []
	tekst = f.read()
	rijeci = tekst.split(" ")

	a = []
	i = 0

	for r in range(broj_svih_rijeci):
		# provjerava da je rijec, a ne tocka ili linebreak...
		if not rijeci[r].isalnum():
			continue

		a.append(rijeci[r])
		i += 1
		if i == 3:
			i = 0
			temp = a.copy()
			result.append((temp))
			a.clear()

	# print(result)
	return result


L = napravi_array()


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


def elementarni_dog(V):
	Elem = []

	for i in V:
		if i not in Elem:
			Elem.append(i)
	return Elem


def redak(L, uvjet):
	Nova_lista = []

	for i in L:
		if i[len(L[0]) - 1] == uvjet:
			Nova_lista.append(i)

	return Nova_lista

def prve_dvije(uvjet):
	r = []
	for i in L:
		if i[0] == uvjet[0] and i[1] == uvjet[1]:
			r.append(i)

	return r



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

		for i in range(2):
			for j in range(len(Rez)):
				if(Rez[j] > Rez[i]):
					tmp = Rez[i]
					Rez[i] = Rez[j]
					Rez[j] = tmp
					tmp = Elem[i]
					Elem[i] = Elem[j]
					Elem[j] = tmp

		r = [Elem[0], Elem[1]]
	return r