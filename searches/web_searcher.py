from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from config import SELECTOR_SEARCH_INPUT, SELECTOR_SEARCH_BUTTON
from func.func import prompt_open_url
import time # Задержка для загрузки страницы


def create_driver() -> webdriver.Chrome:
    """Настраивает и возвращает Chrome‑драйвер."""
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

def search_and_handle(song: str, SEARCH_URL: str) -> None:
    driver = create_driver()
    try:
        driver.get(SEARCH_URL)
        inp = driver.find_element(By.CSS_SELECTOR, SELECTOR_SEARCH_INPUT)
        btn = driver.find_element(By.CSS_SELECTOR, SELECTOR_SEARCH_BUTTON)
        time.sleep(1)  # Задержка для загрузки страницы
        inp.send_keys(song)
        btn.click()
        time.sleep(1)  # Задержка для загрузки страницы
        url = driver.current_url
        driver.quit()
        prompt_open_url(url)
    finally:
        driver.quit()