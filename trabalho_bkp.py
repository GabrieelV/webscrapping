#!/usr/bin/env python3

from selenium import webdriver
import requests, os, bs4, platform, time
from imagem import downloadImagem
from envioEmail import enviarEmail

# ========================= Funções =================================== #
def pegaNomeFilme():
	'''Pega o nome dos filmes na página.'''
	try:
		nome = browser.find_elements_by_class_name('lister-item-header')
	except:
		print('Nome do filme nao encontrado')
		return
	
	for filme in nome:
		# Pega o nome do filme e formata removendo sujeiras
		nomeFilme = filme.text
		nomeFilme = nomeFilme.split('. ')[1:]
		if len(nomeFilme) > 1:
			nomeFilme = nomeFilme[0] + '. ' + nomeFilme[1]
		else:
			nomeFilme = nomeFilme[0]
		nomeFilme = nomeFilme.split(' (')[0]
		#print(nomeFilme)
		informacoes['nomeDoFilme'].append(nomeFilme)
		
	print('Pegando nome dos filmes ... ' + str(len(informacoes['nomeDoFilme'])) + '/' + str(quantidade))
		
		
def pegaAnoFilme():
	'''Pega o ano dos filmes na página.'''
	try:
		ano = browser.find_elements_by_class_name('lister-item-header')
	except:
		print('Ano do filme nao encontrado')
		return

	for filme in ano:
		anoFilme = filme.text
		if (anoFilme.split(' (')[1])[0] == '1' or (anoFilme.split(' (')[1])[0] == '2':
			anoFilme = anoFilme.split(' (')[1]
		elif (anoFilme.split(' (')[2])[0] == '1' or (anoFilme.split(' (')[2])[0] == '2':
			anoFilme = anoFilme.split(' (')[2]
		else:
			anoFilme = anoFilme.split(' (')[3]
		anoFilme = anoFilme[0:4]
		#print(anoFilme)
		informacoes['anoDoFilme'].append(anoFilme)
		
	print('Pegando ano dos filmes ... ' + str(len(informacoes['anoDoFilme'])) + '/' + str(quantidade))


def pegaRatingFilme():
	'''Pega o rating do filme na página.'''
	try:
		rating = browser.find_elements_by_name('ir')
	except:
		print('Rating nao encontrado')
		return

	for filme in rating:
		#print(filme.text)
		informacoes['ratingDoFilme'].append(filme.text)
		
	print('Pegando rating dos filmes ... ' + str(len(informacoes['ratingDoFilme'])) + '/' + str(quantidade))


def pegaMetascoreFilme():
	'''Pega o metascore do filme na página.'''
	try:
		metascore = browser.find_elements_by_class_name('ratings-bar')
	except:
		print('Metascore nao encontrado')
		return
		
	for filme in metascore:
		metascoreFilme = filme.text.split(' Metascore')[0]
		metascoreFilme = metascoreFilme.split('this')[1]
		metascoreFilme = metascoreFilme[1:]
		informacoes['metascoreDoFilme'].append(metascoreFilme)
		#print(metascoreFilme)
		
	print('Pegando metascore dos filmes ... ' + str(len(informacoes['metascoreDoFilme'])) + '/' + str(quantidade))


def pegaVotosFilme():
	'''Pega os votos dos filmes na página'''
	try:
		votos = browser.find_elements_by_class_name('sort-num_votes-visible')
	except:
		print('Elemento nao encontrado')
	
	for filme in votos:
		votosFilme = filme.text.split('Votes: ')[1]
		#print(votosFilme)
		votosFilme = votosFilme.split(' ')[0]
		#print(votosFilme)
		informacoes['votosDoFilme'].append(votosFilme)
		
	print('Pegando quantidade de votos dos filmes ... ' + str(len(informacoes['votosDoFilme'])) + '/' + str(quantidade))


def criaArquivoComLista():
	'''Cria um arquivo Ranking.txt com o ranking dos filmes.'''
	try:	
		arquivo = open('Ranking.txt', 'w')
		arquivo.write('{: <8}''{: <8}''{: <13}''{: <70}''{: <11}''{: <4}\n'.format('#','imdb','metascore','filme','votos','ano'))
		arquivo.close()
	except:
		print('Erro ao criar arquivo')
	else:
		print('Arquivo Criado com sucesso')


def gravaRankingNoArquivo(pagina):
	'''Grava o ranking dos filmes no arquivo Ranking.txt'''

	print('Adicionando a lista de filmes ao arquivo Ranking.txt')
	a = pagina - 1
	try:
		arquivo = open('Ranking.txt', 'a')
		for a in range(a + 250):
			arquivo.write('{: <8}''{: <8}'.format(str(a + 1), informacoes['ratingDoFilme'][a]))
			if informacoes['metascoreDoFilme'][a] == '':
				arquivo.write('{: <13}'.format('n/a'))
			else:
				arquivo.write('{: <13}'.format(informacoes['metascoreDoFilme'][a]))
			arquivo.write('{: <70}''{: <11}''({: <4})\n'.format(informacoes['nomeDoFilme'][a], informacoes['votosDoFilme'][a], informacoes['anoDoFilme'][a]))
			
			
		arquivo.close()
			
	except:
		print('Erro ao adicionar lista ao arquivo Ranking.txt')


# ===================================================================== #

# ========================= Main ====================================== #

# Identifica o sistema operacional
if platform.system() == 'Linux':
	limpar = 'clear'
else:
	limpar = 'cls'

informacoes = {'nomeDoFilme':[], 'anoDoFilme':[], 'ratingDoFilme':[], 'metascoreDoFilme':[], 'votosDoFilme':[]}

tipo = int(input('Como deseja ordenar:\n 1 - Votos\n 2 - Estrela\n 3 - Nome\nInforme o numero: ' ))
ano = int(input('Qual o ano para a busca: '))
quantidade = int(input('Informe a quantidade (multiplos de 250) de filmes a serem buscados: '))
os.system(limpar)

print('Preparando para coletar os dados ...')

# Identifica o tipo de ordenação.
if (tipo == 1): #ordena por votos
	url = 'https://www.imdb.com/search/title?title_type=feature,tv_movie&release_date='+str(ano)+'&sort=num_votes,desc&count=250&start='
if( tipo == 2): #ordena por estrela
	url = 'https://www.imdb.com/search/title?title_type=feature,tv_movie&release_date='+str(ano)+'&sort=user_rating,desc&count=250&start='
if( tipo == 3): #ordena por nome
	url = 'https://www.imdb.com/search/title?title_type=feature,tv_movie&release_date='+str(ano)+'&sort=alpha,desc&count=250&start='


browser = webdriver.Firefox()

# Captura as informações
for pagina in range(1, quantidade + 1, 250):
	
	browser.get(url + str(pagina))
	pegaNomeFilme()
	pegaAnoFilme()
	pegaRatingFilme()
	pegaMetascoreFilme()
	pegaVotosFilme()
	downloadImagem(url, pagina, quantidade)
	os.system(limpar)



# Cria o arquivo Ranking.txt e salva os dados.
criaArquivoComLista()
gravaRankingNoArquivo(pagina)

time.sleep(3)
os.system(limpar)


# Envia o email
email = int(input('Deseja enviar o anexo por email:\n1 - Sim\n2 - Não\nResposta: '))
if email == 1:
	os.system(limpar)
	print('Iniciando envio de e-mail')
	try:
		 enviarEmail(limpar)
	except:
		print('Erro ao enviar email')
		novamente = int(input('Deseja tentar novamente:\n1 - Sim\n2 - não\nResposta: '))
		os.system(limpar)
		if(novamente == 1):
			enviarEmail(limpar)
		else:
			print('Envio de email cancelado.')

print()
print('Processo concluido.')
