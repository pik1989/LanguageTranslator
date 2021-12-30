# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 22:24:52 2021

@author: User
"""

import streamlit as st 
import googletrans
translator = googletrans.Translator()
def get_key(val):
    for key, value in googletrans.LANGUAGES.items():
         if val == value:
                return key
    return "key doesn't exist"
st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)
option=st.selectbox('Select Language',tuple(googletrans.LANGUAGES.values()))
text=st.text_area('Input the text')
translated = translator.translate(text, dest=get_key(option))
st.write(translated.text)