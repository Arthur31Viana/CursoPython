#Atribuindo variável
maisIgual, menosIgual, vezesIgual, divididoIgual, moduloIgual = 9, 9, 9, 9, 9

#Concatenação
print(str(maisIgual) +' - '+ str(maisIgual))

maisIgual += 1 #resultado 10
menosIgual -= 1 #resultado 8
vezesIgual *= 1 #resultado 9
divididoIgual /= 1 #resultado 9
moduloIgual %= 2 #resultado 1

#Atribuindo variável com resultado
a, b, c = 2, 4, 8
a, b, c = a*2, a+b+c, a*b*c
