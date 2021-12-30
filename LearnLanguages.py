# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 22:35:35 2021

@author: User
"""

import googletrans

translator = googletrans.Translator()

print(googletrans.LANGUAGES)

translated = translator.translate('How are you', 
                     dest = 'hi')

print(translated.text)