#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
import plotly.express as px


import matplotlib.pyplot as plt
import numpy as np

from aacreport.analysis import Analysis


path_corpus = (
    "/home/fasr/Developer/aacreport/data/dataset/corpora/childes/Eng-UK-MOR/Barbara/"
)
analysi = Analysis(path_corpus)


@st.cache
def get_report() -> dict:
    report = analysi.FormatJSON()
    return report

report = get_report()


@st.cache
def get_info_corpus():
    return pd.read_csv(
        "/home/fasr/Developer/aacreport/data/dataset/corpora/childes/Eng-UK-MOR/Barbara/info.csv"
    )


st.title("DashBoard AAC Report Peformance")
st.markdown("Child communication analysis report.")

st.header("Mean Length of Utterance (MLU)")
st.markdown(
    "> Average speaking time is a measure of language productivity in children. \
        It is traditionally calculated by collecting 100 utterances spoken by a \
            child and dividing the number of morphemes by the number of utterances. \
                A higher MLU is used to indicate a higher level of language proficiency. \
                    [Article](https://www.sltinfo.com/mean-length-of-utterance/)"
)

st.header("Type Token Ratio (TTR)")
st.markdown(
    "> A type-token ratio (TTR) is the total number of UNIQUE words (types)\
         divided by the total number of words (tokens) in a given segment of \
             language. ... The closer the TTR ratio is to 1, the greater the lexical\
                  richness of the segment.\
                      [Article](https://www.sltinfo.com/type-token-ratio/)"
)

st.header("Corpus")
st.markdown("> Data child speak.")

df = get_info_corpus()
st.dataframe(df.head())

st.header("Report")
st.markdown("> Result Json Data.")
st.json(report)


st.header("Frequent words")
st.write("")

dfjson = pd.DataFrame(report['frequency_of_words'])

arr = [dfjson['word'][:10], dfjson['freq']]
plt.hist(arr, bins=20)
st.pyplot()

st.markdown("## Party time!")
st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
btn = st.button("Celebrate!")
if btn:
    st.balloons()