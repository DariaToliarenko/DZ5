import requests
from bs4 import BeautifulSoup

def parse_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Парсинг заголовка страницы
        title = soup.title.string if soup.title else "Заголовок не найден"
        print(f"Заголовок страницы: {title}")
        
        # Парсинг заголовков секций
        section_headers = []
        for i in range(1, 7):  # h1 до h6
            headers = soup.find_all(f'h{i}')
            section_headers.extend([header.get_text(strip=True) for header in headers])
        
        print("Заголовки секций:")
        for header in section_headers:
            print(header)

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(f"Заголовок: {title}\n")
        f.write("Заголовки секций:\n")
        for header in section_headers:
            f.write(f"{header}\n")
            
    print("Данные сохранены в output.txt")

if __name__== "__main__":
    url = input("Введите URL для парсинга: ")
    parse_page(url)