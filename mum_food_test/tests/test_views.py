import pytest
from rest_framework.test import APIClient

from mum_food_test.tests import factories


@pytest.fixture
def client() -> APIClient:
    client = APIClient()
    return client


@pytest.fixture
def ingredients_data():
    ingredients = []
    for i in range(0, 6):
        ingredients.append(factories.IngredientFactory())
    return ingredients


@pytest.mark.django_db
def test_recipes_list(client: APIClient):
    recipe = factories.RecipeFactory()
    resp = client.get('/api/recipes/')

    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['id'] == recipe.id
    assert data[0]['name'] == recipe.name


@pytest.mark.django_db
def test_recipes_detail(client: APIClient):
    recipe = factories.RecipeFactory()
    resp = client.get(f'/api/recipes/{recipe.id}/')

    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert data['id'] == recipe.id
    assert data['name'] == recipe.name


@pytest.mark.django_db
def test_recipes_like(client: APIClient):
    recipe = factories.RecipeFactory()
    resp = client.post(f'/api/recipes/{recipe.id}/like/')

    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert data['id'] == recipe.id
    assert data['name'] == recipe.name
    assert data['likes'] == recipe.likes + 1


@pytest.mark.django_db
def test_ingredients_list(client: APIClient):
    ingredient = factories.IngredientFactory()
    resp = client.get('/api/ingredients/')

    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['id'] == ingredient.id
    assert data[0]['name'] == ingredient.name


@pytest.mark.django_db
def test_ingredients_detail(client: APIClient):
    ingredient = factories.IngredientFactory()
    resp = client.get(f'/api/ingredients/{ingredient.id}/')

    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    assert data['id'] == ingredient.id
    assert data['name'] == ingredient.name
