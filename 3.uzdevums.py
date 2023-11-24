#Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.
#Izmantojiet GIT, lai izsekotu izmaiņas un veidotu komitus

skaitlis=[1,2,3,4,5,6,7,8,9,10]
nepara_skaitlis=list(filter(lambda x:x%2==0, skaitlis))
print(nepara_skaitlis)