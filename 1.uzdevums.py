#Izveidojiet Python programmu, kas saskaita no 1 līdz lietotāja ievadītam skaitlim, izmantojot for ciklu.
#Izmantojiet GIT, lai izsekotu izmaiņas programmas kodā un izveidotu komitus, tos ievietojot arī GITHUB.


cipars=int(input("Ievadi skaitli :"))
skaitlis=[1, cipars]
rezultats=list(filter(lambda x:x%2, skaitlis))
print(rezultats)