#!/usr/bin/env python3

import smtplib
import sys
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviarEmail(limpar):
	'''Envia os anexos por email'''
	# Coleta dados
	email = input('Digite o email: ')
	senha = input('Digite a senha: ')
	tomador = input('Digite o email destinatario: ')
	assunto = input('Assunto: ')
	texto = input('O que deseja escrever no email: \n')

	try:

		COMMASPACE = ', '

		sender = email
		gmail_password = senha
		recipients = [tomador]
		text = texto

		outer = MIMEMultipart()
		outer['Subject'] = assunto
		outer['To'] = COMMASPACE.join(recipients)
		outer['From'] = email
		outer.attach(MIMEText(text, 'plain'))
		outer.preamble = 'Você não verá isso no MIME-aware mail reader.\n'
		composed = outer.as_string()
		
	except:
		print('Email ou senha esta incorreto')

	else:

# Adiciona os anexos na mensagem
		try:
			with open('Ranking.txt', 'rb') as fp:
				msg = MIMEBase('application', "octet-stream")
				msg.set_payload(fp.read())
			encoders.encode_base64(msg)
			msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename('Ranking.txt'))
			outer.attach(msg)
		except:
			print("Não foi possível abrir o arquivo. Error: ", sys.exc_info()[0])
			raise

	composed = outer.as_string()

	# Enviando e-mail
	try:
		with smtplib.SMTP('smtp.gmail.com', 587) as s:
			s.ehlo()
			s.starttls()
			s.ehlo()
			s.login(sender, gmail_password)
			s.sendmail(sender, recipients, composed.encode("utf8"))
			s.close()
		os.system(limpar)
		print("Email enviado!")
	except:
		print("Não foi possível enviar o email. Error: ", sys.exc_info()[0])
		raise
