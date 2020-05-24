#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
import plotly.express as px

from aacreport.analysis import Analysis


path_corpus = (
    "/home/fasr/Developer/aacreport/data/dataset/corpora/childes/Eng-UK-MOR/Barbara/"
)
analysi = Analysis(path_corpus)


@st.cache
def get_report() -> dict:
    report = analysi.FormatJSON()
    return report


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
st.json(get_report())


st.header("Frequent words")
st.write("")

dfj = pd.DataFrame.from_dict(get_report())

values = st.sidebar.slider(
    "Price range",
    float(dfj.freq.min()),
    float(dfj.freq.clip(upper=1000.0).max()),
    (50.0, 300.0),
)
f = px.histogram(
    df.query(f"price.between{values}"), x="price", nbins=15, title="Price distribution"
)
f.update_xaxes(title="Price")
f.update_yaxes(title="No. of listings")
st.plotly_chart(f)
