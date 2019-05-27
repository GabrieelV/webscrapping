#!/usr/bin/env python3

import requests, os, bs4, selenium

def downloadImagem(url, pagina, quantidade):
	'''Baixa as imagens dos filmes da página'''
	try:
		os.makedirs('fotos', exist_ok=True) # Armazena comics na pasta ./fotos
		
		print('Baixando as imagens ...')
		 
		# Faz o download da página.
		res = requests.get(url + str(pagina))
		res.raise_for_status()

		soup = bs4.BeautifulSoup(res.text, 'html.parser')

		#Encontra a url.
		filmeElem = soup.select('img.loadlate')
		
		i = pagina - 1
		j = 0
		
		while i < 20:
			if filmeElem == []:
				print('Não foi possível encontrar a imagem')
			else:
				filmeUrl = filmeElem[j].get('loadlate')
				#Substitui parte da URL para baixar a imagem em tamanho grande.
				filmeUrl = filmeUrl.replace('67_CR0,0,67,98_AL_.jpg', '182_CR0,0,182,268_AL_.jpg')
				
				#Download da imagem.
				#print('Downloading imagem %s...' % (comicUrl))

				res = requests.get(filmeUrl)
				res.raise_for_status()

				# Salva a imagem na pasta ./fotos
				imageFile = open(os.path.join('fotos', os.path.basename(str(i + 1)) + '.jpg'), 'wb')
				for chunk in res.iter_content(100000):
					imageFile.write(chunk)
				imageFile.close()
				i = i + 1
				j = j + 1

	except:
		print('Ocorreu erro no download das imagens')
