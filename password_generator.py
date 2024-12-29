# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 16:15:37 2024

@author: USER
"""

# password_generator.py
import random
import string

def generate_password():
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    print(f"Generated Password: {password}")

generate_password()
