nome = input('Qual é seu nome?: ')
idade = input('Qual é sua idade?: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, mas vc não digitou nada.')