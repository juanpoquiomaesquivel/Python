# https://www.youtube.com/watch?v=SqvVm3QiQVk&t=2531s

import random

print('Welcome To Your Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

number = int(input("Amount of passwords to generate: "))

length = int(input("Input your password length: "))

print("\nHere are your passwords:")

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)