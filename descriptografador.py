def descriptografar_cifra_cesar(ciphertext, chave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyzçáâãàéêíóôõúüABCDEFGHIJKLMNOPQRSTUVWXYZÇÁÂÃÀÉÊÍÓÔÕÚÜ'
    plaintext = ''
    
    for char in ciphertext:
        if char in alfabeto:
            indice = alfabeto.index(char)
            novo_indice = (indice - chave) % len(alfabeto)
            plaintext += alfabeto[novo_indice]
        else:
            plaintext += char
    
    return plaintext


mensagem_criptografada = input("Digite a mensagem criptografada: ")
chave_cifra = int(input("Digite a chave da cifra de César: "))

mensagem_descriptografada = descriptografar_cifra_cesar(mensagem_criptografada, chave_cifra)
print("Mensagem descriptografada:", mensagem_descriptografada)