# Тесты Selenium на Python

Этот репозиторий содержит автоматизированные тесты для веб-приложения, написанные на Python с использованием Selenium WebDriver. Тесты запускаются при push в репозиторий и генерируют отчет в формате Allure.

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/d-timoshin/test_run.git
```

2. Установите зависимости:

```
pip install -r requirements.txt
```

## Запуск тестов

Для запуска тестов локально выполните команду:

```
pytest tests/
```

## Отчет Allure

После выполнения тестов будет сгенерирован отчет Allure в директории `allure-results`. Для просмотра отчета выполните команду:

```
allure serve allure-results/
```

Это откроет отчет Allure в вашем браузере.

## Интеграция с CI/CD

Тесты автоматически запускаются при каждом push в репозиторий с помощью GitHub Actions. После выполнения тестов генерируется отчет Allure.
