p1 = [8,8,7,9,10,9]
p2 = [7,7,9,9,10,9]

media_p1= sum(p1)/len(p1)
print(media_p1)
media_p2= sum(p1)/len(p2)
print(media_p2)

if media_p1 > media_p2:
    print("A turma teve melhor média na prova 1")
elif media_p2 > media_p1:
    print("A turma teve melhor média na prova 2")
else:
    print("A turma teve a mesma média nas duas provas")