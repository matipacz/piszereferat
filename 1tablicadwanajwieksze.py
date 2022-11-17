n = int(input('Podaj dlugosc tablicy: '))
tab = [0]*n
i = 0
while i < n:
    tab[i] = float(input('Podaj liczbe: '))
    i = i + 1
if n == 1 :
    naj = tab[0]
    print('Największą i jedyną liczbą jest: ')
    print(naj)
else :
    print(n)
    if tab [n-2] <= tab[n-1]:
        naj = tab[n-1]
        duz = tab[n-2]
    else:
        naj = tab[n-2]
        duz = tab[n-1]
    n = n-2    
    while n > 0:
        if tab[n-1] > naj:
            duz = naj
            naj = tab[n-1]
        elif tab[n-1] <= naj and tab[n-1] > duz:
            duz = tab[n-1]
        n = n-1
    print('Dwie największe liczby to: ')
    print(naj)
    print(duz)