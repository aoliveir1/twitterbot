# -*- coding: utf-8 -*-

'''
    TwitterBot:
        Robô que tuíta automaticamente trechos de músicas contidas em arquivos locais.
'''

import os
from random import randint
from twython import Twython, TwythonError
import tweepy
import random
import time

while True:  
    #Lista de arquivos contendo letras das músicas.
    letras=[]   
    
    #Percorre o diretório local.
    for dirname, dirnames, filenames in os.walk('./letras/'):
        #Laço para pegar os nomes do arquivos.
        for filename in filenames:
            letras.append((os.path.join(filename)))

    #Escolhe um arquivo aleatório.
    x=randint(0, len(letras)-1)
    
    #O arquivo ja deve estar nomeado sem a extensao .txt. 
    hashtag='#'+letras[x]

    #Pega um linha aleatória
    line=random.choice(open('./letras/'+letras[x]).readlines())
    
    # Credenciais Twitter
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    ACCESS_KEY = ''
    ACCESS_SECRET = ''
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    #Tweet
    api.update_status(hashtag+' '+line.lower()) 

    #Espera 1h
    time.sleep(3600)
