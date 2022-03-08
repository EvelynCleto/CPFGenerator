while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]   # Elimina os dois ultimos digitos do CPF
    reverso = 10          # Contador reverso
    total = 0


    # Loop do CPF
    for index in range(19):
        if index > 8:   # Primeiro indice vai de 0 a 9,
            index -= 9  # São os 9 primeiros digitos do CPF

            total += int(novo_cpf[index]) * reverso  # Valor total da multiplicacao

            reverso -= 1  # Decrementa o contador reverso
            if reverso < 2:
                reverso = 11
                d = 11 - (total % 11)

                if d > 9:  # Se o digito for > que 9 o valor é 0
                    d = 0
                total = 0  # Zera o total
                novo_cpf += str(d)     # Concatena o digito gerado no novo cpf

                #Evita sequencias. Ex.: 1111111, 000000000
                sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

                # Descobri que sequencias avaliavam como verdadeiro, então também
                # adicionei essa checagem aqui

                if cpf == novo_cpf and not sequencia:
                    print('Válido')
                else:
                    print('Inválido')

