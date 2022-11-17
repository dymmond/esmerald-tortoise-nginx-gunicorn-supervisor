#!/usr/bin/env python
import os
import sys
from pathlib import Path

from esmerald import Esmerald, Gateway, Include, JSONResponse, get
from starlette import status


@get("/health-check", tags=["Health Check"], status_code=status.HTTP_200_OK)
async def health_check() -> JSONResponse:
    """
    Returns the status 200 used for render to verify the health of the application.
    """
    return JSONResponse({"detail": "healthy"})


def build_path():
    """
    Builds the path of the project and project root.
    """
    Path(__file__).resolve().parent.parent
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

    if not SITE_ROOT in sys.path:
        sys.path.append(SITE_ROOT)
        sys.path.append(os.path.join(SITE_ROOT, "apps"))


def get_application():
    """
    This is optional. The function is only used for organisation purposes.
    """
    build_path()

    app = Esmerald(
        routes=[
            Gateway("/", handler=health_check, name="health-check"),
            Include(namespace="{{ cookiecutter.project_name }}.urls"),
        ],
    )
    return app


app = get_application()
