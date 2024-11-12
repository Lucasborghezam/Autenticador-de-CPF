# Autenticador de CPF

Este projeto é um **validador de CPF** em Python, que verifica se um CPF brasileiro é válido de acordo com os critérios de numeração do CPF.

## Funcionalidades

O código realiza as seguintes verificações para validar um CPF:

1. **Conversão**: Recebe o CPF inserido pelo usuário, remove caracteres especiais (pontos e traços) e converte os dígitos para uma lista de inteiros.
2. **Validação de Tamanho**: Confirma que o CPF possui exatamente 11 dígitos.
3. **Validação de Dígitos Iguais**: Rejeita CPFs com todos os dígitos iguais, pois são inválidos.
4. **Cálculo dos Dígitos Verificadores**: Calcula os dois dígitos verificadores do CPF e compara com os fornecidos pelo usuário para verificar a validade.

