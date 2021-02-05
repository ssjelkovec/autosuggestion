import re
import os.path

# db path
file_path = os.path.dirname(__file__).rpartition('\\')
db_path = f"{file_path[0]}\\db"
sve_txt = f"{db_path}\\sve.txt"


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

	for r in range(len(rijeci)):
		# provjerava da je rijec, a ne tocka ili linebreak...
		if not rijeci[r].isalnum():
			continue

		a.append(rijeci[r])
		i += 1
		if i == 3:
			i = 0
			result.append(a.copy())
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
	if not len(L):
		return [""] * 3

	Elem = elementarni_dog(stupac(L, len(L[0]) - 1))
	Rez = []

	for i in range(len(Elem)):
		Rez.append(P(Elem[i], stupac(L, len(L[0]) - 1)))
		for j in range(len(L[0]) - 1):
			Rez[i] = Rez[i] * bayes(uvjet[j], Elem[i], stupac(redak(L, Elem[i]), j),
									stupac(redak(L, Elem[i]), len(L[0]) - 1))

	for i in range(3):
		for j in range(len(Rez)):
			if(Rez[j] > Rez[i]):
				Rez[i], Rez[j] = Rez[j], Rez[i]
				Elem[i], Elem[j] = Elem[j], Elem[i]

		if len(Elem):
			return Elem[:3]
		else:
			return [""] * 3
