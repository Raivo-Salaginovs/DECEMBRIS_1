#Izveidojiet Python programmu, kas izmanto while ciklu, lai atrastu pirmo skaitli, kura kvadrāts ir lielāks par 1000.
#Izmantojiet GIT, lai izsekotu kodu un veidotu komitus.

skaitlis=[1,2,3,4,5,6,7,8,9,10]
kvadrati=list(filter(lambda x:x%2==0 or x%3==0, skaitlis))
print(kvadrati)