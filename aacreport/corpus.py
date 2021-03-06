#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    @ Class: Corpus
    @ Description: Essa classe configura e carrega o corpus.
'''

__data__ = '04/05/2018'


class Corpus(object):

    path = '/home/rodriguesfas/Mestrado/aacreport/dataset/corpora/childes/Eng-UK-MOR'
    dir_corpus = '/Barbara'
    file = '/sentence_Belfast_barb01.txt'
    
    src = str(path + dir_corpus + file)

    def loard(self):
        corpus_root = open(__class__.src).read()
        return corpus_root
