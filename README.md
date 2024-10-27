# Установка и запуск

## Установка

Устанавливаем venv виртуальное окружение, активируем и на него устанавливаем селениум.

```sh
python -m venv .venv
source .venv/Scripts/activate
pip install selenium
```

## Запуск тестов

### Запуск конкретного теста

Нажимаем F5 в VSCode с открытым в редакторе файлом теста в проекте, например `facebook_auth.test.py` или через команду в терминале (перед запуском надо активировать env):

```sh
source .venv/Scripts/activate
python src/facebook_auth.test.py
```

### Запуск всех тестов (с предактивацией venv)

```sh
./run.sh
```
