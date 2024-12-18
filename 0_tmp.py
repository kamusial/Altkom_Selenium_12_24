# # import time
# from time import sleep, time_ns
#
# print('Siema')
# # time.sleep(3)
#
# sleep(3)
# print('papa')
#
# try:
#     age = int(input('Ile masz lat? '))
# except ValueError:
#     pass

word = 'piesek'
print(type(word))

print(len(word))

czlowiek_1 = [324623, 'Kamil', 'mail@mail.com', 22]
czlowiek_2 = [362423, 'Kamil', 'mail@mail.com', 3]
czlowiek_3 = [324523, 'Kamil', 'mail@mail.com', 4]
people_list = []
people_list.append(czlowiek_1)
people_list.append(czlowiek_2)
people_list.append(czlowiek_3)

print(people_list)

def dodaj_urlop(czlowiek, ile):
    if czlowiek[3] >= ile:
        czlowiek[3] -= ile
    else:
        print('Brak mozliwosci')

dodaj_urlop(people_list[1], 5)
print(people_list[1])

nazwa = 'piesek'
zmienna = 5

