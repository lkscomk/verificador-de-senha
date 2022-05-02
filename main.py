#codigo para verificacao de senha nivel intermediario 
#lukas rocha Rodrigues

def pedir_senha(senha, **options):
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
    mensagem.append('' if len(senha) >= quantidade else 'Senha menor que '+str(quantidade)+' caracteres. ')

  num = True
  if numeros:
    num = 0
    for x in range(10):
      num += int(senha.count(str(x)))
    num = True if num>0 else False
    mensagem.append('' if num > 0 else 'Ausência de valores númericos. ')
    
  l_letras = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ç']
  mas = True
  if maiusculas:
    mas = 0
    for x in range(len(l_letras)):
      mas += int(senha.count(l_letras[x].upper()))
    mas = True if mas>0 else False
    mensagem.append('' if mas>0 else 'Ausência de Letras Maiúsculas. ')

  letras = True
  if minusculas:
    letras = 0
    for x in range(len(l_letras)):
      letras += int(senha.count(l_letras[x]))
    letras = True if letras>0 else False
    mensagem.append('' if mas>0 else 'Ausência de Letras Minúsculas. ')

  simb = True
  l_simbolos=['!','@','#','/','$','%','&','*','(',')']
  if simbolos:
    simb = 0
    for x in range(len(l_simbolos)):
      simb += int(senha.count(l_simbolos[x]))
    simb = True if simb > 0 else False
    mensagem.append('' if mas>0 else 'Ausência de Símbolos. ')

  conf = True
  if confirmacao:
    conf = True if senha == confirmacao else False
    mensagem.append('' if senha == confirmacao else 'As senhas precisam se iguais.')

  response = True if quant and num and mas and letras and simb and conf else False
  print(quant, num, mas, letras, simb, conf)
  #verficar_tamanho(senha)

  return {
    'resposta': response,
    'mensagemError': mensagem
  }




print(pedir_senha('@albert123N', confirmacao='@albert123N', quantidade=8, numeros=True, maiusculas=True, minusculas=True, simbolos=True))