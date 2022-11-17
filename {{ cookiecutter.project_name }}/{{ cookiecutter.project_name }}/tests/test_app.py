from esmerald.testclient import EsmeraldTestClient

from ..main import get_application


def create_app():
    app = get_application()
    return app


def get_client():
    return EsmeraldTestClient(create_app())


class TestHealthCheck:
    def test_can_reach_health_check(self):
        client = get_client()

        url = client.app.url_path_for("health-check")

        response = client.get(url)

        assert response.status_code == 200

    def test_reverse_name_health_check(self):
        client = get_client()

        url = client.app.url_path_for("health-check")

        assert url == "/health-check"


class TestWelcome:
    def test_can_reach_welcome(self):
        client = get_client()

        response = client.get("/api/v1/welcome")

        assert response.status_code == 200
