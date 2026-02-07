
##Online Courses API — Django REST Framework (Homework)

**<img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MHB1dG80dnRxZTRiMWFkMzQyc3VkMWZ2ZTdodzRyNHdrbDg3YzhsdSZlcD12MV9zdGlja2Vyc190cmVuZGluZyZjdD1z/tpSOcUiiMnSS9kbAHA/giphy.gif" width="60">**

<div align="center">

[![Django REST Framework](https://img.shields.io/badge/Django_REST-Framework-0C4B33?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-pypok--1-181717?style=for-the-badge&logo=github)](https://github.com/pypok-1/coursesDRF)


</div>

---

## 📋 Опис проекту

REST API для повного управління системою онлайн-курсів. Реалізовано:
- ✅ **CRUD-операції** для всіх сутностей (Create, Read, Update, Delete)
- ✅ **Валідація даних** на рівні моделей і серіалізаторів
- ✅ **Пов'язані моделі** (ForeignKey, ManyToMany)
- ✅ **REST API endpoints** зі статус-кодами HTTP
---

## 🛠️ Установка

### Вимоги
- Python 3.8+
- Django 3.2+
- Django REST Framework 3.12+

### Кроки встановлення

```bash
# 1. Клонуємо репозиторій
git clone https://github.com/pypok-1/coursesDRF.git
cd coursesDRF

# 2. Створюємо віртуальне оточення
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# 3. Встановлюємо залежності
pip install -r requirements.txt

# 4. Застосовуємо міграції
python manage.py migrate

# 5. Створюємо суперкористувача
python manage.py createsuperuser

# 6. Запускаємо сервер
python manage.py runserver
---
