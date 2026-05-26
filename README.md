# Playwright + Pytest E2E UI Tests

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-9.x-orange)](https://docs.pytest.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.x-green)](https://playwright.dev/python/)
[![Allure](https://img.shields.io/badge/Allure-Report-yellow)](https://docs.qameta.io/allure/)

Автоматизированные E2E-тесты веб-приложения на стеке **Playwright + Pytest + Allure**. Проект демонстрирует применение паттерна PageObject Model, фикстур, параметризации и CI/CD.

---

## Тестируемое приложение

Демо-сайт: [QA Automation Engineer UI Course](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login)

Репозиторий приложения: [GitHub](https://github.com/Nikita-Filonov/qa-automation-engineer-ui-course)

---

## Покрытие тестами

### Страница авторизации
- Успешная авторизация с валидными данными
- Авторизация с некорректными данными (негативный сценарий)
- Переход со страницы авторизации на страницу регистрации

### Страница дашборда
- Корректное отображение элементов страницы

### Страница курсов
- Пустой список курсов
- Создание нового курса
- Редактирование существующего курса

---

## Используемые паттерны и технологии

- **PageObject Model** — страницы описаны отдельными классами
- **PageComponent** — повторяющиеся элементы выделены в компоненты
- **PageFactory** — фабрика для инициализации страниц
- **Фикстуры** — браузер, страницы, Allure-отчётность вынесены в отдельные модули и подключаются через `conftest.py` как плагины
- **Параметризация** — позитивные и негативные сценарии
- **Pydantic Settings** — настройки проекта через переменные окружения (`.env`)
- **Allure Report** — отчёты с шагами и скриншотами при падении
- **CI/CD** — GitHub Actions с автозапуском по коммиту

---

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/DmitriyChernakov/autotests-ui.git
cd autotests-ui
```

### 2. Установить зависимости

```bash
pip install -r requirements.txt
playwright install --with-deps
```

### 3. Запустить тесты

```bash
pytest -m regression --alluredir=allure-results
```

### 4. Просмотреть Allure-отчёт

```bash
allure serve ./allure-results
```

**Примечание:** Allure должен быть установлен локально. Инструкция по установке: [Allure](https://allurereport.org/docs/)
