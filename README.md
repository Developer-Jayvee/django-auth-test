# Django Basic Authentication

A small Django authentication project with signup, login, profile protection, Django admin, PostgreSQL, and JWT support.

## Features

- User signup and login
- Protected profile route using a JWT decorator
- Django admin integration
- PostgreSQL database configuration
- Environment-based database and JWT configuration

## Tech Stack

- Python
- Django
- PostgreSQL
- PyJWT
- python-dotenv

## Project Structure

```text
accounts/       Authentication views, URLs, templates, and models
config/         Django project settings and root URL configuration
core/           JWT utilities, decorators, and middleware
manage.py       Django management entry point
```

## Prerequisites

- Python 3.12 or newer
- PostgreSQL
- A virtual environment

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install the project dependencies:

```bash
pip install django psycopg[binary] pyjwt python-dotenv
```

3. Create the environment file:

```bash
cp .env.example .env
```

4. Update `.env` with your PostgreSQL and JWT values:

```dotenv
DB_HOST=127.0.0.1
DB_PORT=5432
DB_NAME=django_authapp
DB_USER=<database-user>
DB_PASSWORD=<database-password>

JWT_SECRET_KEY=<a-long-random-secret>
JWT_ALGO=HS256
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Create an administrator account:

```bash
python manage.py createsuperuser
```

7. Start the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/accounts/login/` in your browser.

## Routes

| Route | Description |
| --- | --- |
| `/accounts/signup/` | Create a new account |
| `/accounts/login/` | Log in |
| `/accounts/profile/<user_id>/` | View the protected profile |
| `/accounts/test/` | Test the user profile list view |
| `/admin/` | Django administration |

## Environment Variables

- `DB_HOST`: PostgreSQL host
- `DB_PORT`: PostgreSQL port
- `DB_NAME`: Database name
- `DB_USER`: Database username
- `DB_PASSWORD`: Database password
- `JWT_SECRET_KEY`: Secret used to sign JWT tokens
- `JWT_ALGO`: JWT signing algorithm

Keep `.env` private and never commit real credentials or JWT secrets.

## Development

Run Django checks:

```bash
python manage.py check
```

Run tests:

```bash
python manage.py test
```
