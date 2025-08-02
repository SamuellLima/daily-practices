from collections import Counter
import re
from nltk.corpus import stopwords

stops_in_portuguese = set(stopwords.words('portuguese'))
stops_in_english = set(stopwords.words('english'))

path = r"" # <--- put your path here


with open(path, "r", encoding='utf-8') as file:
    content = file.read()

    clean_content = re.sub(r'[^\w\s]', '', content).lower().split() #---> treating the words (removing punctuations)
    
    filtered_words = [
    word for word in clean_content
    if word not in stops_in_english and word not in stops_in_portuguese    
        ]
    
    c = Counter(filtered_words) # ---> Creates a dict with the number of times the word appeared
    
    k_highest_value = max(c, key=c.get)# ---> get key
    v_highest_value = c[k_highest_value]# ---> get value

    print(f"Word: {k_highest_value}\nValue: {v_highest_value}")

    # -----------------------------------------------------------------------------
    # ATTENTION:
    #
    # to run this script, you need to have the NLTK libraries installed, and the 'stopwords' data package downloaded
    #   
    # ***run this command in a python terminal***:
    # import nltk
    # nltk.download('stopwords')

    # Thank you for coming here 👍

