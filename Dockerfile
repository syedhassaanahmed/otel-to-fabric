FROM python:3.12-bullseye

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY main.py pyproject.toml uv.lock /app/
WORKDIR /app
RUN uv sync --frozen --no-cache

# Run the application.
CMD ["./.venv/bin/fastapi", "run", "main.py", "--port", "80", "--host", "0.0.0.0"]