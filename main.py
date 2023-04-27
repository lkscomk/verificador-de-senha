def verificar_senha(senha, **options):
    maiusculas = options.get('maiusculas')
    numeros = options.get('numeros')
    minusculas = options.get('minusculas')
    simbolos = options.get('simbolos')
    quantidade = options.get('quantidade')
    confirmacao = options.get('confirmacao')
  
    quant = True
    mensagem = []
    if quantidade:
        quant = True if len(senha) >= quantidade else False
        mensagem.append('' if len(senha) >= quantidade else f'Senha menor que {quantidade} caracteres. ')

    num = True
    if numeros:
        num = 0
        for x in range(10):
            num += int(senha.count(str(x)))
        num = True if num > 0 else False
        mensagem.append('' if num > 0 else 'Ausência de valores numéricos. ')
    
    l_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ç']
    mas = True
    if maiusculas:
        mas = 0
        for x in range(len(l_letras)):
            mas += int(senha.count(l_letras[x].upper()))
        mas = True if mas > 0 else False
        mensagem.append('' if mas > 0 else 'Ausência de letras maiúsculas. ')

    letras = True
    if minusculas:
        letras = 0
        for x in range(len(l_letras)):
            letras += int(senha.count(l_letras[x]))
        letras = True if letras > 0 else False
        mensagem.append('' if letras > 0 else 'Ausência de letras minúsculas. ')

    simb = True
    l_simbolos = ['!', '@', '#', '/', '$', '%', '&', '*', '(', ')']
    if simbolos:
        simb = 0
        for x in range(len(l_simbolos)):
            simb += int(senha.count(l_simbolos[x]))
        simb = True if simb > 0 else False
        mensagem.append('' if simb > 0 else 'Ausência de símbolos. ')

    conf = True
    if confirmacao:
        conf = True if senha == confirmacao else False
        mensagem.append('' if senha == confirmacao else 'As senhas precisam ser iguais.')

    response = True if quant and num and mas and letras and simb and conf else False

    return {
        'resposta': response,
        'mensagemError': mensagem
    }


resultado = verificar_senha('SenhaSegura123!@#', confirmacao='SenhaSegura123!@#', quantidade=10, numeros=True, maiusculas=True, minusculas=True, simbolos=True)
if resultado['resposta']:
    print('Senha segura! 👍')
else:
    print('A senha não atende aos requisitos:')
    for mensagem in resultado['mensagemError']:
        print('- ' + mensagem)