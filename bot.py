# -*- coding: utf-8 -*-

'''
    Twitter Bot:
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
    
    #Percorre o diretório.
    for dirname, dirnames, filenames in os.walk('./letras/'):
        #Pegar os nomes do arquivos.
        for filename in filenames:
            #Testa se é arquivo .txt, se for adiciona na lista.
            if '.txt' in filename:
                letras.append((os.path.join(filename)))

    #Embaralha a lista.
    random.shuffle(letras)
    #Escolhe um arquivo aleatório.
    x = randint(0, len(letras)-1)

    #Arquivo selecionado
    filename=open('./letras/'+letras[x],'r')
    f=filename.readlines()
    filename.close()
    
    #Pegar um linha aleatória
    num_lines = sum(1 for line in open('./letras/'+letras[x]))
    line = random.choice(open('./letras/'+letras[x]).readlines())
    
    # Credenciais Twitter
    CONSUMER_KEY = 'xxx'
    CONSUMER_SECRET = 'xxx'
    ACCESS_KEY = 'xxx'
    ACCESS_SECRET = 'xxx'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    #Tweet
    api.update_status(line)

    #Espera 1h
    time.sleep(3600)
