# Social Media API (minimal)

## Setup
1. pip install -r requirements (or pip install django djangorestframework djangorestframework-authtoken pillow)
2. python manage.py makemigrations && python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py runserver

## Endpoints
- POST /api/accounts/register/  -> register new user (returns token)
- POST /api/accounts/login/     -> login (returns token and user)
- GET/PUT /api/accounts/profile/ -> get or update logged-in user (requires token)

Authentication: Token auth (add header `Authorization: Token <token>`)

User model fields: username, email, bio, profile_picture, followers (ManyToMany to users)
