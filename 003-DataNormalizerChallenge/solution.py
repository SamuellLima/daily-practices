
def normalized_phone_number(phone_number: str):
	
    abnormal_characters = (',','.','(','-',')', " ")
    
    normalized_number = phone_number
    
    for caractere in abnormal_characters:
        normalized_number = normalized_number.replace(caractere, "")
    print('Número normalizado:', normalized_number)

    return normalized_number
	

phone_number = str(input('Digite um número de telefone: +55 '))

def validate_number(phone_number: str):
    """Um adicional, além do desafio proposto pela IA."""
    normalized_number = normalized_phone_number(phone_number)
    
    valid_characters = ('0','1','2','3','4','5','6','7','8','9')
    
    if len(normalized_number) not in (11, 10): #Apesar do padrão da Anatel ser 11 dígitos, alguns números possuem 10. O meu por exemplo
        print('Número de telefone invalido.')
        return 'Número de telefone invalido.'

    for character in normalized_number:
        if character not in valid_characters:
            print('Número de telefone invalido.')
            return 'Número de telefone invalido.'

    print('Número validado com sucesso!')
    return 'Número validado com sucesso.'
validate_number(phone_number)


