from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(
    'https://forms.office.com/pages/responsepage.aspx?id=QhQEvrbz4UuFCeypyBdSjx4yJ1StPPpItnAoFIkziDJUQ09OMUFHNkRZRzdTOElNVlZCVkRaR1BYQSQlQCNjPTEu'
    ) # Abre o formulario

time.sleep(2) # Tempo pra eu ver o que está acontecendo

aluno = driver.find_element_by_xpath('') # x-path do input do nome do aluno
ano = driver.find_element_by_xpath('') # x-path do input do ano
sala = driver.find_element_by_xpath('') # x-path do input da sala

aluno.send_keys('Beatriz Benjamim Pires')


time.sleep(2)


driver.quit()

# pra rodar a aplicação use $python3 triz.py
