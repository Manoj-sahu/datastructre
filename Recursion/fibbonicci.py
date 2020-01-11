def fibbo(n):
    if n < 1:
        print('incorrrect no')
    elif n == 1 or n == 2:
        return 1
    else:
        return fibbo(n-1) + fibbo(n-2)

for i in range(10):

    print(fibbo(i))