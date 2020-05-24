#!/usr/bin/env python
# -*- coding: utf-8 -*-

import nltk
import json
import os
import numpy as np
import pandas as pd

__title__ = "Report"
__description__ = "Report of child communication analysis."
__author = "RodriguesFAS"
__data__ = "04/04/2018"
__version__ = "0.0.2"
__changelog__ = ["Initial NodeJS", "Remove NodeJS include streamlit."]


class Analysis(object):
    """Analysis"""

    def __init__(self, path_corpus):
        # loard corpus
        self.corpus_root = open(os.path.join(path_corpus, "speaks.txt")).read()
        self.corpus_info = pd.read_csv(os.path.join(path_corpus, "info.csv"))
        # self.corpus_root = pd.read_fwf(dataset)

    def info_corpus(self):
        return self.corpus_info

    def Tokenizer(self):
        """
            Tokenizer
            - Converte todo o corpus para letras minusculas.
            - Separa todas as palavras do corpus.
            - Remove todos os tokens não alfabéticos.
            - Retorna todas as palavras do corpus separadas. 
        """
        corpus_lowercase = self.corpus_root.lower()
        tokens = nltk.word_tokenize(corpus_lowercase)
        return [word for word in tokens if word.isalpha()]

    def ListWordsNoRepet(self):
        """
            ListWordsNoRepet
            - Retorna todas as palavras do corpus sem repetição.
        """
        collection = set(self.Tokenizer())
        return list(collection)

    def WordsFrequency(self):
        """
            WordsFrequency
            - Retorna a frequência das palavras.
        """
        freq_dist = nltk.FreqDist(self.Tokenizer())
        return freq_dist.most_common()

    def ClassGrammatical(self):
        """
            ClassGrammatical
            - Identifica as classes gramaticais de cada palavra.
            - Identifica cada entidade.
            - Retorna lista de palavras classificada.
        """
        return nltk.chunk.ne_chunk(nltk.pos_tag(self.ListWordsNoRepet()))

    def SaveCSV(self):
        """
            SaveCSV
            - Salvas os dados em um arquivo CSV.
        """
        words_class_grammatical = self.ClassGrammatical()
        words_frequency = self.WordsFrequency()

        df_data = {
            "words_class_grammatical": [words_class_grammatical],
            "words_frequency": [words_frequency],
        }

        df = pd.DataFrame(df_data)

        print(df)

    def JoinDataTable(self):
        """
            JoinDataTable
        """
        return "null"

    def NumberToken(self):
        """
            NumberToken
            - Retorna o numero total de palavras encontradas na fala.
        """
        return len(self.Tokenizer())

    def NumberTypes(self):
        """
            NumberTypes
            Retorna a quantidades de palavras presente na fala excluido todas as repetições.
        """
        return len(self.ListWordsNoRepet())

    def MLU(self):
        """
            MLU
        """
        return 1.2557935

    def TTR(self):
        """
            TTR
        """
        return (float(self.NumberTypes()) / float(self.NumberToken())) * 100

    def FormatJSON(self):
        """
            FormatJSON
            - Monta a estrutura dos dados.
            - Converte os dados para uma String, para facilitar a formatação dos dados.
            - Formata os dados no padrão Json, removendo e adicionando caracteres. 
            - Retotna os dados em formato Json.
        """
        data = {}
        data["mlu"] = self.MLU()
        data["ttr"] = self.TTR()

        d = list()
        for item in self.WordsFrequency():
            d.append({"word": item[0], "freq": item[1]})

        data["frequency_of_words"] = d

        return data


if __name__ == "__main__":
    path_dataset = "/home/fasr/Developer/aacreport/data/dataset/corpora/childes/Eng-UK-MOR/Barbara/sentence_Belfast_barb01.txt"
    print(Analysis(path_dataset).FormatJSON())
    # print(Analysis().SaveCSV())
