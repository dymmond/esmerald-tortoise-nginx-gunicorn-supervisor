"""
Esmerald settings for {{ cookiecutter.project_name }} project.
"""
from typing import Any, List, Optional, Union

from esmerald.conf.enums import EnvironmentType
from esmerald.conf.global_settings import EsmeraldAPISettings
from esmerald.config import CORSConfig
from esmerald.contrib.databases.tortoise import init_database, stop_database
from esmerald.types import LifeSpanHandler
from pydantic import Field

from ..configs.databases.config import TORTOISE_ORM


async def start_database():
    await init_database(config=TORTOISE_ORM)


async def close_database():
    await stop_database()


class AppSettings(EsmeraldAPISettings):
    app_name: str = "My application in production mode."
    title: str = "{{ cookiecutter.project_name }} - Production"
    environment: Optional[str] = EnvironmentType.PRODUCTION
    secret_key: str = Field(
        default="esmerald-insecure-$4#ze98ureg&s%7-r&%wq1rwqas$47%o", env="SECRET_KEY"
    )
    enable_openapi: bool = Field(default=False, env="ENABLE_OPENAPI")
    allowed_hosts: Optional[Union[str, List[str]]] = Field(default=[], env="ALLOWED_HOSTS")
    cors_origins: Optional[Union[str, List[str]]] = Field(default=[], env="CORS_ALLOWED_ORIGINS")
    redirect_slashes: bool = False

    @property
    def cors_config(self) -> CORSConfig:
        return CORSConfig(allow_origins=self.cors_origins)

    @property
    def on_startup(self) -> List[LifeSpanHandler]:
        """
        List of events/actions to be done on_startup.
        """
        return [start_database]

    @property
    def on_shutdown(self) -> List[LifeSpanHandler]:
        """
        List of events/actions to be done on_shutdown.
        """
        return [close_database]

    class Config:
        @classmethod
        def parse_env_var(cls, field_name: str, raw_val: str) -> Any:
            if field_name in ("allowed_hosts", "cors_origins"):
                values_list = [value for value in raw_val.split(",")]
                return values_list
            return cls.json_loads(raw_val)
