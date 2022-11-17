from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
CREATE TABLE IF NOT EXISTS "hubuser" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "first_name" VARCHAR(150) NOT NULL,
    "last_name" VARCHAR(150) NOT NULL,
    "username" VARCHAR(150) NOT NULL UNIQUE,
    "email" VARCHAR(120) NOT NULL UNIQUE,
    "password" VARCHAR(128) NOT NULL,
    "last_login" TIMESTAMPTZ,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "is_staff" BOOL NOT NULL  DEFAULT False,
    "is_superuser" BOOL NOT NULL  DEFAULT False,
    "uuid" UUID NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "hubuser"."first_name" IS 'First name';
COMMENT ON COLUMN "hubuser"."last_name" IS 'Last name';
COMMENT ON COLUMN "hubuser"."username" IS 'Username';
COMMENT ON COLUMN "hubuser"."email" IS 'Email address';
COMMENT ON COLUMN "hubuser"."password" IS 'Password';
COMMENT ON COLUMN "hubuser"."last_login" IS 'Last login';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
