# Name: Nafisa Chowdhury
# PSID: 11591144

parts = input().split()
name = parts[0]
age = parts[-1]
while name != '-1':
    try:
        age = int(parts[1]) + 1
    except ValueError:
        age = 0
    print('{} {}'.format(name, age))

    parts = input().split()
    name = parts[0]
