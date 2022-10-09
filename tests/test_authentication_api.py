# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401
from openapi_server.models.unsupported_media_type_error import UnsupportedMediaTypeError  # noqa: F401


def test_create_new_user(client: TestClient):
    """Test case for create_new_user

    Create a new user for our platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_user_validation(client: TestClient):
    """Test case for create_new_user_validation

    
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/users/validate",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user_validation_details(client: TestClient):
    """Test case for get_user_validation_details

    
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users/validate",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_login(client: TestClient):
    """Test case for user_login

    
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/users/login",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_logout(client: TestClient):
    """Test case for user_logout

    
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users/logout",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200
