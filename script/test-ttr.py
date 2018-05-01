#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: TTR
 Description: 
 Version: 0.0.1
 Date: 03/03/2018
 Autor: RodriguesFAS
 Email: <franciscosouzaacer@gmail.com> | <fasr@cin.ufpe.br>
 Website: <http://rodriguesfas.com.br> | <http://clubedosgeeks.com.br>
 Github: <https://github.com/rodriguesfas>
'''

import nltk
import sys
import json
import numpy as np

#Read data from stdin


def read_in():
    lines = sys.stdin.readlines()
    #Since our input would only be having one line, parse our JSON data from that
    return json.loads(lines[0])


def main():
    # get our data as an array from read_in()
    #text_src = read_in()
    text_src = "But what are thoughts? Well, we all have them. They are variously described as ideas, notions, concepts, impressions, perceptions, views, beliefs, opinions, values, and so on. At times they are brief, coming and going in an instant. On other occasions they seem to endure and we can mull them over again and again in the act we call thinking. We can put them aside, fall asleep, and then return to them later. We refer to them as things we can handle. However, this is just a metaphor."

    #define todas as palavras em minusculas
    text_lowercase = text_src.lower()

    # tokennizer
    tokens = nltk.word_tokenize(text_lowercase)

    # Remove todos os tokens não alphabetic
    words = [word for word in tokens if word.isalpha()]
    #print ">> Lista de todas as palavras: \n", words

    words_not_repeat = list(set(words))
    #print ">> Lista de todas as palavras sem repetição: \n", words_not_repeat

    # Cria uma lista com todas as palavras e o numero de sua frequência.
    lista = []

    for y in xrange(len(words)):
	    aux = words[y], words.count(words[y])
	    lista.append(aux)

    #print ">> Lista de palavras com frequência \n", list(set(lista))

    rank = list(set(lista))

    # print "Remove duplicados: ", rank

    # Calcular o numero de tokens e o numero de types.
    num_of_tokens = len(words)
    num_of_types = len(rank)

    #print ">> Number of Tokens", num_of_tokens
    #print ">> Number of Types", num_of_types

    # Calcula o valor do Tipo-token Ratio
    ttr = float(num_of_types) / float(num_of_tokens) * 100

    #print ">> Type-token ration %.2f" % ttr, "%"

    #return the sum to the output stream

    jsonData = {
            "ttr": ttr,
            "num_of_tokens": num_of_tokens,
            "num_of_types": num_of_types,
            "words_not_repeat": words_not_repeat
        }

    # Envia dados para o server
    #print(json.dumps(jsonData))



if __name__ == '__main__':
    main()
