import re, sys

number = str(input('Enter a number of the form a,b(c). If there is no fractional part or period, write false instead: '))
abc = re.findall(r'\w+', number)
a, b, c = abc[0], abc[1], abc[2]

if b != 'false' and c != 'false':
    n = len(c) * '9' + len(b) * '0'
    remains = b + c
    m_b = int(b)
elif c != 'false':
    n = len(c) * '9'
    remains = c
    m_b = 0
else:
    sys.exit('The number is finite')

a, n, remains = int(a), int(n), int(remains)
m = int(a * n + remains - m_b)
reduction_max = 1

for reduction in range(2, min(m, n) + 1):
     if m / reduction % 1 == 0 and n / reduction % 1 == 0 and reduction > reduction_max:
            reduction_max = reduction
m, n = m / reduction_max, n / reduction_max


if number[0] == '-':
    print('-', m,'/', n)
else:
    print(m,'/', n)
