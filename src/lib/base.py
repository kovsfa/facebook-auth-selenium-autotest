from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def init_driver():
    # Указываем пути к chrome и chromedriver
    chromedriver_path = r"D:\\chromedriver-win64\\chromedriver.exe"
    chrome_path = r"D:\\chrome-win64\\chrome.exe"

    # Настраиваем опции браузера
    chrome_options = Options()
    chrome_options.binary_location = chrome_path
    chrome_options.add_experimental_option("detach", True)
    # ошибка в доступе к исполняемому файлу в режиме sandbox
    chrome_options.add_argument("--no-sandbox")

    # Создаем экземпляр службы с указанным путем
    service = Service(executable_path=chromedriver_path)

    return webdriver.Chrome(service=service, options=chrome_options)


driver = init_driver()
