"""
Esmerald settings for {{ cookiecutter.project_name }} project.
"""

from typing import Optional

from esmerald.conf.enums import EnvironmentType

from ..settings import AppSettings


class TestingAppSettings(AppSettings):
    debug: bool = True
    app_name: str = "My application in testing mode."
    title: str = "Testing {{ cookiecutter.project_name }}"
    environment: Optional[str] = EnvironmentType.TESTING
