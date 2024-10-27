from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.base import driver
from lib.credentials import facebook_email, facebook_pass

# Переходим на сайт
driver.get("https://www.facebook.com/")

try:
    # Ждем пока форма авторизации загрузится
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'form[data-testid="royal_login_form"]'))
    )
    print("Форма авторизации найдена")

    # Находим поле ввода логина и вводим логин
    driver.find_element(
        By.CSS_SELECTOR, 'input[data-testid="royal_email"]').send_keys(facebook_email)
    print("Логин ввели")

    # Находим поле ввода пароля и вводим пароль
    driver.find_element(
        By.CSS_SELECTOR, 'input[data-testid="royal_pass"]').send_keys(facebook_pass)
    print("Пароль ввели")

    # Нажимаем кнопку "Вход"
    driver.find_element(
        By.CSS_SELECTOR, 'button[data-testid="royal_login_button"]').click()
    print("Кнопка входа нажата, ждем перехода на следующую страницу")

    # Ожидаем появления элемента, который подтверждает успешный вход
    WebDriverWait(driver, 10).until(
        # тут у меня элемент scrollview
        # потому что у меня не было аккаунта FB,
        # это элемент на странице, уведомляющее о проверке акка
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#scrollview"))
    )
    print("Авторизация выполнена успешно")

except Exception as e:
    print("Авторизация не выполнена:", e)

# Закрытие браузера
driver.quit()
