#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 Software: TTR
 Description: Calcula TTR de uma fala.
 Version: 0.0.2
 Autor: RodriguesFAS
 Register: 21/04/2018
 Update: 01/05/2018

 Email:
    <franciscosouzaacer@gmail.com>
    <fasr@cin.ufpe.br>
 
 Website:
    <http://rodriguesfas.com.br>
    <http://clubedosgeeks.com.br>
 
 Github: <https://github.com/rodriguesfas>
 
 Tutorial:
    <http://www.nltk.org/howto/childes.html>
    <http://www.nltk.org/_modules/nltk/corpus/reader/childes.html>
    <http://www.hum.uu.nl/medewerkers/a.dimitriadis/courses/data2012/use-childes.py>
    <http://ling-blogs.bu.edu/lx390f16/class-4c/#1>
    <http://ling-blogs.bu.edu/lx390f16/>
    <http://ling-blogs.bu.edu/lx390f17/standoff-annotation-xml-and-more-childes/>
 
 Corpus:
    <https://childes.talkbank.org/access/Eng-UK/Thomas.html>
    <https://childes.talkbank.org/access/>
    <https://childes.talkbank.org/data-xml/Biling/>
 
 Chatter:
    Converte Corpus .CHAT para .XML
    <https://talkbank.org/software/chatter.html>
'''


import os
import nltk
import numpy as np
import pandas as pd
import json

# comment if you don't have the pretty package
from nltk.corpus.reader import CHILDESCorpusReader


def main():

    nltk_download_dir = '/home/rodriguesfas/nltk_data'

    brown_corpus_root = os.path.join(
        nltk_download_dir, 'corpora/CHILDES/Eng-UK-MOR/Thomas/T/')

    brown_corpus = CHILDESCorpusReader(root=brown_corpus_root, fileids='.+xml')

    '''
        Fileids - Operações com arquivos.
        fileids() -> Exibe todos os arquivos.
        len() -> conta todos os arquivos.
    '''
    # print brown_corpus.fileids()
    # print len(brown_corpus.fileids())
    # file = brown_corpus.fileids()[:1]

    '''
        Exibe as propriedades dos arquivos.
    '''
    '''
    corpus_data = brown_corpus.corpus(brown_corpus.fileids())
    print(corpus_data[0]['Lang'])
    for key in sorted(corpus_data[0].keys()):
        print(key, ": ", corpus_data[0][key])
    '''

    '''
        Exibe informações de todos os participantes presente no corpus.
    '''
    '''
    corpus_participants = brown_corpus.participants(brown_corpus.fileids())
    for this_corpus_participants in corpus_participants[:2]:
        for key in sorted(this_corpus_participants.keys()):
            dct = this_corpus_participants[key]
            print(key, ": ", [(k, dct[k]) for k in sorted(dct.keys())])
    '''

    '''
        Calcular MLU
        Os critérios para o cálculo do MLU são amplamente baseados em Brown (1973).
        MLU()
        MLU(fileids='file.xml')
    '''
    mlu = brown_corpus.MLU(fileids='2-00-12.xml', speaker=['CHI'])
    # brown_corpus.MLU()

    '''
        Words - Operações com palavras.
        words()
        tagged_words()
    '''
    # brown_corpus.words(fileids='2-00-12.xml')[:10]
    # brown_corpus.tagged_words(fileids='2-00-12.xml')[:10]

    '''
        Encontra a frequência das palavras da fala de uma determinado perssonagem.
        most_common()    -> All words.
        most_common(:20) -> 20 words.
    '''
    #all_words = brown_corpus.words(fileids='2-00-12.xml')
    all_words = brown_corpus.words(fileids='2-00-12.xml', speaker=['CHI'])
    fd = nltk.FreqDist(all_words)
    words_chi = (fd.most_common())

    '''
        Sents - Operações com sentenças.
        sents()
        tagged_sents()
    '''
    # brown_corpus.sents(fileids='2-00-12.xml')[:10]
    # brown_corpus.tagged_sents(fileids='2-00-12.xml')[:10]

    '''
        Speaker - Operações com fala, permite filtrar as palavras especifica de cada participante
                  presente no corpus.
        TODOS OS PARTICIPANTES ->  speaker=['ALL']
        INTERVENTOR ->  speaker=['INV']
        MÃE         ->  speaker=['MOT']
        CRIANÇA     ->  speaker=['CHI']
    '''
    # print brown_corpus.words(fileids='2-00-12.xml', speaker=['INV'])[:50]
    # print brown_corpus.words(fileids='2-00-12.xml', speaker=['MOT'])[:50]
    # words_chi = brown_corpus.words(fileids='2-00-12.xml', speaker=['CHI'])

    '''
        Stem
        Extrai a raiz da palavra "morfologicamente".
        stem=True
    '''
    # print brown_corpus.words(fileids='2-00-12.xml', stem=True)[:30]

    '''
        Replaced
        replaced=True
    '''
    # When the argument replace is true, the replaced words are used instread of the original words.
    # print brown_corpus.words(fileids='2-00-12.xml', speaker='CHI', replace=True)[247]

    '''
        Relation
        relation=True
    '''
    # print brown_corpus.words(fileids='2-00-12.xml', relation=True)[:10]

    '''
        Operações com Idade
        age()
        age(fileids='file.xml')
        age(fileids='file.xml', month=True)
    '''
    # print brown_corpus.age()
    # print brown_corpus.age(fileids='2-00-12.xml')
    # print brown_corpus.age(fileids='2-00-12.xml', month=True)

    '''
        Exibe informações dos participantes.
        participants(fileids='file.xml')[0]
    '''
    # brown_corpus.participants(fileids='2-00-12.xml')[0]

    '''
        joinData - Junta os dados.
    '''
    joinData = [{
        'metrics': {'mlu': mlu, 'ttr': [27]},
        'words_chi': words_chi
    }]

    '''
        jsonData - Normalização dos dados para o padrão JSON.
    '''
    # converte para string para permitir manipulação dos dados.
    jsonData = str(joinData)

    # Formatação dos dados, removendo e adicionando os caracteres correspondente para JSON.
    jsonData = jsonData.replace('"', "'").replace("'s", 's').replace("(s", "('s").replace(
        "('", "{'word':'").replace("',", "','freq':'").replace('),', "'},").replace(')', "'}").replace(' ', '')

    # Envia os dados para o servidor.
    print(jsonData)


if __name__ == '__main__':
    main()
