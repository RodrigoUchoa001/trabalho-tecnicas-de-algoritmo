# Retorna o numero máximo de bandidos
# que podem ser capturados
def policeThief(arr, n, k):
	i = 0
	l = 0
	r = 0
	res = 0
	thi = []
	pol = []

	# guarda os indices em listas
	while i < n:
		if arr[i] == 'P':
			pol.append(i)
		elif arr[i] == 'T':
			thi.append(i)
		i += 1

	# acompanha os menores indices de
    # ladrao: lad[l], policia: pol[r]
	while l < len(thi) and r < len(pol):
		
		# podem ser pegos
		if (abs( thi[l] - pol[r] ) <= k):
			res += 1
			l += 1
			r += 1
			
		# incrementa o index minimo
		elif thi[l] < pol[r]:
			l += 1
		else:
			r += 1

	return res

# testando
arr1 = ['P', 'T', 'T', 'P', 'T']
k = 2
n = len(arr1)
print(("Máximo de ladrões que podem ser pegos: {}".
    format(policeThief(arr1, n, k))))

arr2 = ['T', 'T', 'P', 'P', 'T', 'P']
k = 2
n = len(arr2)
print(("Máximo de ladrões que podem ser pegos: {}".
    format(policeThief(arr2, n, k))))

arr3 = ['P', 'T', 'P', 'T', 'T', 'P']
k = 3
n = len(arr3)
print(("Máximo de ladrões que podem ser pegos: {}".
    format(policeThief(arr3, n, k))))

# This code is contributed by `jahid_nadim`
