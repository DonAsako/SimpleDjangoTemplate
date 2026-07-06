# SimpleDjangoTemplate

A professional, batteries-included template for Django projects.

Click **"Use this template"** on GitHub to bootstrap a new repository.

## What's inside

- **Django 6** with a split settings package (`base` / `development` / `production` / `ci`)
- **Custom user model** (`accounts.User`) wired from day one
- **12-factor config** — everything read from the environment (or a `.env`) via [django-environ](https://django-environ.readthedocs.io/), one `DATABASE_URL` for the database
- **[uv](https://docs.astral.sh/uv/)** for dependency & environment management
- **Ruff** (lint + format), **mypy** (strict, with `django-stubs`), **djLint** (Django templates), **pytest** (`pytest-django`, coverage)
- **pre-commit** hooks, a **GitHub Actions** CI pipeline and **Dependabot** (weekly deps + actions updates)
- **`.editorconfig`** and shared **VS Code** settings for a consistent editor experience
- **django-debug-toolbar** in development
- **`justfile`** task runner and hashed static files (`ManifestStaticFilesStorage`) in production

## Requirements

- Python **3.14+**
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Getting started

After creating your repo from this template:

```bash
uv sync                          # create the venv and install everything
cp .env.example .env             # then edit .env (at least DJANGO_SECRET_KEY)
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Generate a secret key:

```bash
uv run python -c "from django.core.management.utils import get_random_secret_key as k; print(k())"
```

Install the git hooks once:

```bash
uv run pre-commit install
```

## Daily commands

A [`justfile`](justfile) wraps the common tasks (optional — install
[just](https://github.com/casey/just), e.g. `sudo pacman -S just`). Run `just`
to list every recipe.

| `just` recipe    | Raw command                                           | What it does        |
| ---------------- | ----------------------------------------------------- | ------------------- |
| `just install`   | `uv sync && uv run pre-commit install`                | Deps + git hooks    |
| `just run`       | `uv run python manage.py runserver`                   | Run the dev server  |
| `just migrate`   | `uv run python manage.py migrate`                     | Apply migrations    |
| `just test`      | `uv run pytest`                                       | Run the test suite  |
| `just lint`      | `uv run ruff check . && uv run ruff format --check .` | Lint & format check |
| `just fmt`       | `uv run ruff check --fix . && uv run ruff format .`   | Auto-fix & format   |
| `just typecheck` | `uv run mypy .`                                       | Type-check          |
| `just check`     | lint + typecheck + test                               | Full quality gate   |
| `just hooks`     | `uv run pre-commit run --all-files`                   | Run every hook      |

Everything works without `just` too — just use the raw commands.

## Settings

Settings are split by environment and selected with `DJANGO_SETTINGS_MODULE`:

| Module                         | Used for                        | Default in            |
| ------------------------------ | ------------------------------- | --------------------- |
| `project.settings.development` | Local development               | `manage.py`           |
| `project.settings.production`  | Deployment (fails loud)         | `wsgi.py` / `asgi.py` |
| `project.settings.ci`          | Test suite in CI                | CI workflow           |
| `project.settings.base`        | Shared base (not used directly) |                       |

Configuration comes from environment variables — see [`.env.example`](.env.example)
for the full list. The database is configured through a single `DATABASE_URL`
(SQLite by default in development, Postgres in production/CI).

## Layout

```
.
├── manage.py
├── project/                # project config (not an app)
│   ├── settings/          # base / development / production / ci
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/                   # your Django apps live here
│   └── accounts/          # custom user model (apps.accounts)
├── tests/                 # pytest suite
├── static/  templates/    # your static files and templates
├── .env.example
└── pyproject.toml         # deps + ruff / mypy / pytest config
```

## Deployment

Production settings require `DJANGO_SECRET_KEY`, `ALLOWED_HOSTS` and `DATABASE_URL`
to be set (they have no defaults, so a missing one fails at boot). TLS is assumed
to be terminated by a reverse proxy setting `X-Forwarded-Proto`; static files are
served by that proxy from `STATIC_ROOT` after `collectstatic`.

At deploy time, run once:

```bash
uv run python manage.py migrate
uv run python manage.py createcachetable   # required: default cache is DatabaseCache
uv run python manage.py collectstatic --noinput
```

## Commit convention

Commits must follow [Conventional Commits](https://www.conventionalcommits.org/):

```text
feat(scope): add new capability
fix: correct off-by-one in parser
chore: bump dependencies
```

Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.

## License

Released under the GPL-3.0-or-later license. See [LICENSE](LICENSE).
