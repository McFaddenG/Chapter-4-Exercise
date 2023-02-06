def computegrade(si):
    if 0.0 <= si <= 1.0:
        if si >= 0.9:
            g = 'A'
        elif si >= 0.8:
            g = 'B'
        elif si >= 0.7:
            g = 'C'
        elif si >= 0.6:
            g = 'D'
        elif si < 0.6:
            g = 'F'
        else:
            g = 'Bad score'
        return g
   
s = input('Enter Score: ')
g = computegrade(s)

try:
    s = float(s)
except ValueError:
    print('Bad score')

print(g)