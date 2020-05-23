#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: Report
 Description: Report script of child communication analysis.
 Version: 0.0.1
'''

__author = "RodriguesFAS"
__data__ = "04/04/2018"

import nltk
import json
import numpy as np
import pandas as pd



dataset = '/home/fasr/Developer/aacreport/data/dataset/corpora/childes/Eng-UK-MOR/Barbara/sentence_Belfast_barb01.txt'

# loard corpus
corpus_root = open(dataset).read()
# corpus_root = pd.read_fwf(dataset)
# corpus_root = pd.read_csv(dataset)


'''
    Tokenizer
    - Converte todo o corpus para letras minusculas.
    - Separa todas as palavras do corpus.
    - Remove todos os tokens não alfabéticos.
    - Retorna todas as palavras do corpus separadas. 
'''
def Tokenizer():
    corpus_lowercase = corpus_root.lower()
    tokens = nltk.word_tokenize(corpus_lowercase)
    return [word for word in tokens if word.isalpha()]


'''
    ListWordsNoRepet
    - Retorna todas as palavras do corpus sem repetição.
'''
def ListWordsNoRepet():
    return list(set(Tokenizer()))


'''
    WordsFrequency
    - Retorna a frequência das palavras
'''
def WordsFrequency():
    freq_dist = nltk.FreqDist(Tokenizer())
    return freq_dist.most_common()



'''
    ClassGrammatical
    - Identifica as classes gramaticais de cada palavra.
    - Identifica cada entidade.
    - Retorna lista de palavras classificada.
'''
def ClassGrammatical():
    return nltk.chunk.ne_chunk(nltk.pos_tag(ListWordsNoRepet()))


'''
    SaveCSV
    - Salvas os dados em um arquivo CSV.
'''
def SaveCSV():
    words_class_grammatical = ClassGrammatical()
    words_frequency = WordsFrequency()

    df_data = {
        'words_class_grammatical': [words_class_grammatical],
        'words_frequency': [words_frequency]
    }

    df = pd.DataFrame(df_data)

    print(df)



'''
    JoinDataTable
'''
def JoinDataTable():
    return 'null'


'''
    NumberToken
    - Retorna o numero total de palavras encontradas na fala.
'''
def NumberToken():
    return len(Tokenizer())


'''
    NumberTypes
    Retorna a quantidades de palavras presente na fala excluido todas as repetições.
'''
def NumberTypes():
    return len(ListWordsNoRepet())


'''
    MLU
'''
def MLU():
    return 1.2557935


'''
    TTR
'''
def TTR():
    return (float(NumberTypes()) / float(NumberToken())) * 100


'''
    FormatJSON
    - Monta a estrutura dos dados.
    - Converte os dados para uma String, para facilitar a formatação dos dados.
    - Formata os dados no padrão Json, removendo e adicionando caracteres. 
    - Retotna os dados em formato Json.
'''
def FormatJSON():

    joinData = [
        {
            'metrics': {
                'mlu': MLU(),
                'ttr': TTR()
            },
            'words_chi': WordsFrequency()
        }
    ]

    jsonFormat = str(joinData)

    jsonData = jsonFormat.replace('"', "'").replace("'s", 's').replace("(s", "('s").replace(
        "('", "{'word':'").replace("',", "','freq':'").replace('),', "'},").replace(')', "'}").replace(' ', '')

    return jsonData



if __name__ == '__main__':

    # Envia os dados para o servidor.
    print(FormatJSON())
    #print(SaveCSV())
