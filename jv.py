from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(
    'https://forms.office.com/pages/responsepage.aspx?id=QhQEvrbz4UuFCeypyBdSjx4yJ1StPPpItnAoFIkziDJUQ09OMUFHNkRZRzdTOElNVlZCVkRaR1BYQSQlQCNjPTEu'
    ) # Abre o formulario

time.sleep(2) # Tempo pra eu ver o que está acontecendo

aluno = driver.find_element_by_xpath('') # x-path do input do nome do aluno
ano_2 = driver.find_element_by_xpath('') # x-path da alternativa do ano
sala_A = driver.find_element_by_xpath('') # x-path da alternativa da sala
submit = driver.find_element_by_xpath('') # x-path do botao de submeter


aluno.send_keys('João Vítor Benjamim Pires')

sala_A.click()
ano_2.click()
submit.click()

time.sleep(2)


driver.quit()

# pra rodar a aplicação use $python3 jv.py