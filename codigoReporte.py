import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    edge_options = Options()
    edge_options.add_experimental_option("detach", True)  # Mantiene el navegador abierto
    driver = webdriver.Edge(options=edge_options)
    yield driver
    driver.quit()

def test_page(driver):
    driver.get("https://demo.automationtesting.in/Index.html")

    btnLog = driver.find_element(By.CSS_SELECTOR, "a:has(img#enterimg)")
    btnLog.click()
    time.sleep(5)


    # Verificar que los resultados sean relevantes
    assert "Register" in driver.title or "https://demo.automationtesting.in/Register.html" in driver.page_source
