
#Eu tentei realizar o código sem utilizar qualquer biblioteca, para fortalecer a lógica.
#Em alguns testes  percebi que algumas pontuações como "...", ainda não invertidas, logo tento resolver isso.

sentence = " 'fui fazer um teste hoje, de um projeto de testes e esqueci meu guarda-chuvas' - Disse o Miguel"
def reverse_read(sentence):
    punctuation = ',.?!:"()[]!@#$%¨&*_+='
    separate_sentence = sentence.split()
    words_list = []

    final_punctuation = ''

    for word in separate_sentence:
        
        clean_word = word

        if word[-1] in punctuation:
            clean_word = word[:-1]
            final_punctuation = word[-1]

        if len(clean_word) >= 5:
            r_word = word[::-1]
            final_word = r_word + final_punctuation
            words_list.append(final_word)
            #return word[::-1]
        else:
            final_word = clean_word + final_punctuation
            words_list.append(final_word)
        
        final_punctuation = ''
        #return word

    text = " ".join(words_list)

    print(text)
        

reverse_read(sentence)
