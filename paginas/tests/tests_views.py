import pytest
from django.urls import resolve, reverse
from pytest_django.asserts import assertTemplateUsed

@pytest.fixture
def home_response(client):
    return  client.get(reverse("paginas:inicio"))

@pytest.fixture
def home_response(client):
    return  client.get(reverse("paginas:home"))

class TestPaginainicial:
    def test_reverse_resolve(self):
        assert reverse("paginas:inicio") == "/"
        assert resolve("/").view_name == "paginas:inicio"

    def test_status_code(self, home_response):
        assert home_response.status_code == 200

    def test_template(self, home_response):
        assertTemplateUsed(home_response, "index.html")


class TestHomeView:
    def test_reverse_resolve(self):
        assert reverse("paginas:home") == "/home/"
        assert resolve("/home/").view_name == "paginas:home"

    def test_status_code(self, about_response):
        assert about_response.status_code == 200

    def test_template(self, about_response):
        assertTemplateUsed(about_response, "home.html")