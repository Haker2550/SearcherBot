import requests
from bs4 import BeautifulSoup
from config import SELECTOR_SONG_META, SOURCE_URL

def parse_song_names(url):
    # Отправляем GET-запрос к странице
    response = requests.get(url)
    response.raise_for_status()  # Проверяем успешность запроса
        
    # Создаем объект BeautifulSoup для парсинга
    soup = BeautifulSoup(response.text, 'html.parser')
        
    # ВАЖНО: Замените следующую строку на правильный CSS-селектор 
    # для нахождения названий песен на вашей конкретной странице
    song_meta = soup.select(SELECTOR_SONG_META)  # Примерный селектор
    if song_meta:
        song_namfilter = song_meta[0].get('content', '') # Извлекаем текст названия песни
        song_name = [song_namfilter.replace(' - YouTube Music', '')]  # Разделяем названия по запятой
    return song_name