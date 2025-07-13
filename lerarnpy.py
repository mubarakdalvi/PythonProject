a = int(25)
b = str('gd')
c = float(25.00)
d = bool(False)
e = None
f = complex(2j)
g = range(20)
hg = list(str(12))
i = tuple((24,4))
j = set((3245,54564))
k = dict({"name": "Mub"})
l = frozenset((14,451,5))

# operators arithematic

r1 = a * c
r2 = a + c
r3 = a - c
r4 = a / c
r5 = a % c

print(r1,r2,r3,r4,r5)

# operators comparison

r6 = a == c
r7 = a >= c
r8 = a <= c
r9 = a > c
r10 = a < c
r11 = a != c

print(r6,r7,r8,r9,r10,r11)


# operators logical

r12 = a and c
r13 = a or c 
r14 = not a and c

print(r12,r13,r14)

# operators bitwise

r15 = a & int(c)
r16 = a | int(c)
r17 = a ^ int(c)
r18 = a << 2
r19 = a >> 2
r120 = ~a
r121 = ~int(c)

print(r15,r16,r17,r18,r19,r120,r121)

# operators assignment

a += 2
a -= 2
a *= 2
a /= 2
a %= 2


# operators identity

r27 = a is c
r28 = a is not c

print(r27,r28)


# operators membership

r29 = a in g
r30 = a not in g

print(r29,r30)

# operators special

r31 = a // c  # Floor division
r32 = a ** 2  # Exponentiation

print(r31, r32)


studentWhoAre18 = [{
    "name" : "Mubarak",
    "Age" : 10
},
{    "name" : "Ali","Age" : 17},
{    "name" : "Ahmed","Age" : 15},
{    "name" : "Sara","Age" : 31},
{    "name" : "Hassan","Age" : 21}
]

for i in studentWhoAre18:
    if i["Age"] >= 18:
        print(f"{i['name']} is {i['Age']} years old and is eligible to vote.")
    else:
        print(f"{i['name']} is {i['Age']} years old and is not eligible to vote.")


import random
password = random.randint(1000, 9999)
print(password)

chances = 3

while chances:
    transaction = input('Enter a numebr: ')
    if not transaction.isdigit():
        print('Please enter a valid number.')
        continue
    if transaction == str(password):
        print('You guessed the password correctly!')
        break
    else:
        chances -= 1 
        if chances > 0:
            print(f'Wrong guess! You have {chances} chances left.')
        else:
            print(f'Sorry, you have used all your chances. The password was {password}.')  