pluridisciplinaridade = {"i": 5, "a": 2, "l": 2}
for x in pluridisciplinaridade: 
    print (x)
    print (pluridisciplinaridade.items())
    print (pluridisciplinaridade.keys())
    print (pluridisciplinaridade.values())

string = input ("Digite uma string: ")
conta = {}
for letra in string:
    if letra in conta:
        conta[letra] += 1
    else: 
        conta[letra] = 1
letramais = ''
for key in conta:
    if not letramais:
        letramais = key
    elif conta[key] > conta[letramais]:
        letramais = key
print (letramais)