
###############################
#  Pasos con Selenium en Python
###############################
# from selenium import webdriver

# Iniciar el navegador
# driver = webdriver.Edge()
# driver.get("https://www.google.com")

# # Cerrar el navegador
# driver.quit()


###############################
#  Funciones básicas:
###############################

# from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Edge()
# driver.get("https://www.google.com")

# # Buscar el campo de búsqueda y escribir "Selenium"
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Youtube")
# search_box.submit()
# time.sleep(5) // Esperar 5 segundos

# # Cerrar el navegador
# driver.quit()


###############################
#  Identificación de Elementos
###############################

# driver.find_element(By.ID, "APjFqb").send_keys("Selenium WebDriver")


################################################
#  Ejecución de Pruebas en Múltiples Navegadores 
################################################
browser_name = "edge" 
 
if browser_name.lower() == "chrome": 
    driver = webdriver.Chrome() 
elif browser_name.lower() == "firefox": 
    driver = webdriver.Firefox() 
elif browser_name.lower() == "edge": 
    driver = webdriver.Edge() 

################################################
#  Manejo de Ventanas y Marcos
################################################
# driver.get("https://www.google.com")
# driver.switch_to.new_window("tab")
# driver.switch_to.window(driver.window_handles[0])

################################################
#  Pruebas Avanzadas con Selenium y Python
################################################
# driver.execute_script("alert('Ejecutando JavaScript desde Selenium');")


#################################################
#  Generación de Informes y Registro
################################################



time.sleep(5)
driver.quit()

