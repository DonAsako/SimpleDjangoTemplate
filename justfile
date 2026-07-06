# SimpleDjangoTemplate — task runner. Run `just` to list recipes.
# https://github.com/casey/just

set dotenv-load := true

manage := "uv run python manage.py"

# List available recipes
default:
    @just --list

# Install dependencies and git hooks
install:
    uv sync
    uv run pre-commit install

# Run the development server
run *args:
    {{ manage }} runserver {{ args }}

# Open a Django shell
shell:
    {{ manage }} shell

# Create migrations for changed models
makemigrations *args:
    {{ manage }} makemigrations {{ args }}

# Apply migrations
migrate *args:
    {{ manage }} migrate {{ args }}

# Create a superuser
superuser:
    {{ manage }} createsuperuser

# Run the test suite (pass extra pytest args, e.g. `just test -k user`)
test *args:
    uv run pytest {{ args }}

# Run the test suite with coverage
cov:
    uv run pytest --cov

# Lint and check formatting (Python + Django templates, no changes)
lint:
    uv run ruff check .
    uv run ruff format --check .
    if find templates -name '*.html' -type f | grep -q .; then uv run djlint templates --check; fi

# Auto-fix lint issues and format (Python + Django templates)
fmt:
    uv run ruff check --fix .
    uv run ruff format .
    if find templates -name '*.html' -type f | grep -q .; then uv run djlint templates --reformat; fi

# Static type-check
typecheck:
    uv run mypy .

# Run every pre-commit hook on all files
hooks:
    uv run pre-commit run --all-files

# Update pre-commit hook revisions (Dependabot doesn't touch these)
update-hooks:
    uv run pre-commit autoupdate

# Full quality gate: lint, type-check, tests
check: lint typecheck test

# Collect static files (production)
collectstatic:
    {{ manage }} collectstatic --noinput

# Create the database cache table
cachetable:
    {{ manage }} createcachetable
