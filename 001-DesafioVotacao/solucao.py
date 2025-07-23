#22-07-2025
### 1:30

votes = ['Python', 'JavaScript', 'Gato', 'Github', 'Python', 'Java', 'Flutter', 'JavaScript', 'Python', 'C#']

def count_votes(list):
    scoreboard = {}
    winners = []

    if len(list) < 2:
        return "Deve haver ao menos dois candidatos."
    
    for code_languages in list:
        if not code_languages in scoreboard:
            scoreboard[code_languages] = 0
        
        if code_languages in scoreboard:
            scoreboard[code_languages] += 1
            
            #score = list.count(code_languages)
            #scoreboard[code_languages] += score - Descartei essa ideia

    if scoreboard:
        max_votes = max(scoreboard.values())
    
    for code_languages, votes in scoreboard.items():
        if votes == max_votes:
            winners.append(code_languages)
    
    if len(winners) > 1:
        return print(f'Os vencedores foram: {winners}! Com um incrivel empate de {max_votes} votos!')
    else:
        return print(f'O vencedor foi: {winners}! Com incríveis {max_votes} votos!')

count_votes(votes)


