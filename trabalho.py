from selenium import webdriver


def pegaNomeFilme():
	'''Pega o nome dos filmes na página.'''
	try:
		nome = browser.find_elements_by_class_name('lister-item-header')
	except:
		print('Nome do filme nao encontrado')
		return
		
	print('Pegando nome dos filmes ...')
	
	for filme in nome:
		## NOME FILME
		nomeFilme = filme.text
		nomeFilme = nomeFilme.split('. ')[1]
		nomeFilme = nomeFilme.split(' (')[0]
		#print(nomeAno)
		informacoes['nomeDoFilme'].append(nomeFilme)
		
		
def pegaAnoFilme():
	'''Pega o ano dos filmes na página.'''
	try:
		ano = browser.find_elements_by_class_name('lister-item-header')
	except:
		print('Ano do filme nao encontrado')
		return

	print('Pegando ano dos filmes ...')

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


def pegaRatingFilme():
	'''Pega o rating do filme na página.'''
	try:
		rating = browser.find_elements_by_name('ir')
	except:
		print('Rating nao encontrado')
		return

	print('Pegando rating dos filmes ...')

	for filme in rating:
		#print(filme.text)
		informacoes['ratingDoFilme'].append(filme.text)
		

def pegaMetascoreFilme():
	'''Pega o metascore do filme na página.'''
	try:
		metascore = browser.find_elements_by_class_name('ratings-bar')
	except:
		print('Metascore nao encontrado')
		return
		
	print('Pegando Metascore dos filmes ...')
		
	for filme in metascore:
		metascoreFilme = filme.text.split(' Metascore')[0]
		metascoreFilme = metascoreFilme.split('this')[1]
		metascoreFilme = metascoreFilme[1:]
		informacoes['metascoreDoFilme'].append(metascoreFilme)
		#print(metascoreFilme)


def pegaVotosFilme():
	'''Pega os votos dos filmes na página'''
	try:
		votos = browser.find_elements_by_class_name('sort-num_votes-visible')
	except:
		print('Elemento nao encontrado')
	
	print('Pegando votos dos filmes ...')
	
	for filme in votos:
		votosFilme = filme.text.split('Votes: ')[1]
		#print(votosFilme)
		votosFilme = votosFilme.split(' ')[0]
		#print(votosFilme)
		informacoes['votosDoFilme'].append(votosFilme)


### MAIN
browser = webdriver.Firefox()
ano = '2017'

#browser.get('https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&count=250')

informacoes = {'nomeDoFilme':[], 'anoDoFilme':[], 'ratingDoFilme':[], 'metascoreDoFilme':[], 'votosDoFilme':[]}

for a in range(1, 2001, 250):
	
	browser.get('https://www.imdb.com/search/title?title_type=feature,tv_movie&release_date=2017&sort=num_votes,desc&count=250&start=' + str(a))
	
	pegaNomeFilme()
	pegaAnoFilme()
	pegaRatingFilme()
	pegaMetascoreFilme()
	pegaVotosFilme()

	#print(informacoes)
	print(len(informacoes['nomeDoFilme']))
	print(len(informacoes['anoDoFilme']))
	print(len(informacoes['ratingDoFilme']))
	print(len(informacoes['metascoreDoFilme']))
	print(len(informacoes['votosDoFilme']))

	
	


#browser.get('https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&count=250&start=' + str(a))	
#https://selenium-python.readthedocs.io/navigating.html
