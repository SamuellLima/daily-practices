from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

expected_product = "Sauce Labs Backpack"

def login(login: str,
          password: str):
    try:        
        browser_options = Options()
        prefs = {'credentials_enable_service': False, 'profile.password_manager_enabled': False}
        browser_options.add_experimental_option("prefs", prefs) #Desativa o aviso de senhas vazadas padrão do google chrome ao efetuar login
        
        browser = webdriver.Chrome(options=browser_options) #abrir navegador

        browser.get("https://www.saucedemo.com")
        browser.maximize_window() #Tela cheia para facilitar a visualização

        browser.find_element('id', 'user-name').send_keys(login)
        browser.find_element('id', 'password').send_keys(password)
        login_button = browser.find_element("id", "login-button") 

        login_button.click()
        try: #Verificando se foi possível logar.
            wait = WebDriverWait(browser, 3)
            wait.until(EC.visibility_of_element_located((By.ID, 'shopping_cart_container')))
            print('✅ Login realizado com sucesso.')
        except:
            print('❌ Falha no Login')
            exit()

        print('Login Efetuado com sucesso.')
        return browser
    
    except ValueError as Erro:
        print(f'Erro: {Erro}')
        browser.quit()
        

def check_products(username: str,
                   password: str):
    product_names = []
    
    browser = login(username, password)
    try:     
        inventory_list = browser.find_elements(By.CLASS_NAME, 'inventory_item_name') #Busca o nome de todos os produtos.
        
        if not inventory_list: #Verifica se há produtos no site.
            print('ERRO: The list of products is empty.')

        for product in inventory_list:
            print(f'Available products: {product.text}')
            product_names.append(product.text)

        if expected_product in product_names:
            print(f'✅ TESTE APROVADO! O produto {expected_product} foi encontrado.')
        
        else:
            print(f'❌ TESTE FALHOU: O produto {expected_product} não foi encontrado.')
        #products = [] --- IGNORE
        
        #for product in inventory_list: --- IGNORE
        #    product = product.text --- IGNORE
        #    products.append(product) --- IGNORE
        
        #repeat = reduce(lambda x, y: {**x,y : x.get(y, 0)+1}, [products]) --- IGNORE
        #print(repeat)    --- IGNORE
        
        browser.quit()
        
    except ValueError as Erro:
        print(f'Erro inesperado: {Erro}')
    

username = 'standard_user'
password = 'secret_sauce'

#username = str(input('User: '))
#password = str(input('Password: '))
check_products(username, password)
    