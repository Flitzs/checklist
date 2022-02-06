from selenium import webdriver
import time

driver = webdriver.Chrome()

# sala = driver.find_element_by_name('raf664648e7d14555898ed0b8c7b4b3a4')
# ano = driver.find_element_by_name('re7c0319c7c1a41588e129a98785252ca')
# nome = driver.find_element_by_class('office-form-question-textbox office-form-textfield-input form-control office-form-theme-focus-border border-no-radius')

# print(sala)
# print(ano)
# print(nome)

driver.get('http://www.google.com/');
time.sleep(2) # Tempo pra eu ver o que está acontecendo
search_box = driver.find_element_by_name('q')
search_box.send_keys('funciona')
search_box.submit()
time.sleep(2)


driver.quit()