# ALX Django Library Project

This project demonstrates a Django app with:

- Custom User model
- Book management (list, search, add)
- Security best practices: CSRF, XSS protection, secure headers
- Fully functional templates and forms

## How to Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install django
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
