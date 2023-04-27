# 🔒🔑 Verificador de Senha

Este repositório contém uma função que permite verificar se uma senha atende aos requisitos passados como parâmetros. A função recebe os seguintes parâmetros:

- `senha`: a senha a ser verificada.
- `confirmacao`: confirmação da senha. O valor padrão é a própria senha.
- `quantidade`: a quantidade mínima de caracteres que a senha deve ter. O valor deve ser um número inteiro.
- `numeros`: um valor booleano que indica se a senha deve conter números. O valor deve ser booleano.
- `maiusculas`: um valor booleano que indica se a senha deve conter letras maiúsculas. O valor deve ser booleano.
- `minusculas`: um valor booleano que indica se a senha deve conter letras minúsculas. O valor deve ser booleano.
- `simbolos`: um valor booleano que indica se a senha deve conter símbolos. O valor deve ser booleano.

A função retorna um dicionário com as seguintes chaves:

- `resposta`: um valor booleano que indica se a senha atende a todos os requisitos.
- `mensagemError`: uma lista com mensagens de erro para cada requisito que não foi atendido.

## Como utilizar 🤔

Para utilizar a função, basta importá-la e passar os parâmetros desejados:

```python
resultado = verificar_senha('SenhaSegura123!@#', confirmacao='SenhaSegura123!@#', quantidade=10, numeros=True, maiusculas=True, minusculas=True, simbolos=True)

if resultado['resposta']:
    print('Senha segura! 👍')
else:
    print('A senha não atende aos requisitos:')
    for mensagem in resultado['mensagemError']:
        print('- ' + mensagem)
```

## Tecnologias utilizadas 💻

Este projeto foi desenvolvido em Python

## Autor 👨‍💻

Desenvolvido por LUKAS.