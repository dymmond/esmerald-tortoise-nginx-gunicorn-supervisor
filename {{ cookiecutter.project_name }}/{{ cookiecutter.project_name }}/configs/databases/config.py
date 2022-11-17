import os

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.psycopg",
            "credentials": {
                "host": os.environ.get("POSTGRES_HOST", "localhost"),
                "port": os.environ.get("POSTGRES_PORT", "5432"),
                "user": os.environ.get("POSTGRES_USER", "postgres"),
                "password": os.environ.get("POSTGRES_PASSWORD", "postgres"),
                "database": os.environ.get("POSTGRES_DB_NAME", "postgres"),
            },
        },
    },
    "apps": {
        "accounts": {
            "models": ["accounts.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": False,
    "timezone": "UTC",
}
