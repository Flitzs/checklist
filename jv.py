from selenium import webdriver
import time
import smtplib 
from email.message import EmailMessage

driver = webdriver.Chrome()
driver.get(
    '.'
    ) # Abre o formulario

time.sleep(2) # Tempo pra eu ver o que está acontecendo

aluno = driver.find_element_by_xpath('') # x-path do input do nome do aluno
ano_2 = driver.find_element_by_xpath('') # x-path da alternativa do ano
sala_A = driver.find_element_by_xpath('') # x-path da alternativa da sala
submit = driver.find_element_by_xpath('') # x-path do botao de submeter
confirmar = driver.find_element_by_css_selector('') # a classe de confirmação de enviado
print(confirmar.text)

aluno.send_keys('.')

sala_A.click()
ano_2.click()
submit.click()

time.sleep(1)

############ CONFIRMAÇÃO POR EMAIL ############

username = "." 
password = "." 

msg = EmailMessage()
msg['From'] = username # de quem é
msg['To'] = '.' # Pra quem é

if(confirmar.text) == "O texto que aparece qnd vc manda":
    print("td certin") 
    msg['Subject'] = 'Checklist Diário' # Assunto Email
    msg.set_content('confirmar.text') # a mensagem
    #
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: 
        smtp.login(username, password) # Login usando o email
        smtp.send_message(msg) # Manda a mensagem
else:
    print('eRrOr')
    # manda o email de erro tb
    msg['Subject'] = 'Cagou'
    msg.set_content('Vai ter que ser manual msm') 
    #
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: 
        smtp.login(username, password) 
        smtp.send_message(msg) 


driver.quit()

# pra rodar a aplicação use $python3 jv.py