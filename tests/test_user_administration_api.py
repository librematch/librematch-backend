# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.ulid import Ulid  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401
from openapi_server.models.unsupported_media_type_error import UnsupportedMediaTypeError  # noqa: F401


def test_bulk_update_all_user_details(client: TestClient):
    """Test case for bulk_update_all_user_details

    Bulk update details for a specific user profile on our platform if it exists
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/users/{user_id}".format(user_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_users(client: TestClient):
    """Test case for bulk_update_all_users

    Bulk update of all users of our platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


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


def test_get_details_for_user(client: TestClient):
    """Test case for get_details_for_user

    Retrieve details for a specific user profile on our platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users/{user_id}".format(user_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user_collection(client: TestClient):
    """Test case for get_user_collection

    Retrieve all users of our platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_all_users(client: TestClient):
    """Test case for partial_update_all_users

    Partially update details for all user profiles
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_user(client: TestClient):
    """Test case for partial_update_user

    Update details for a specific user profile on our platform if it exists
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/users/{user_id}".format(user_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_users(client: TestClient):
    """Test case for remove_all_users

    Remove all users from our platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_user(client: TestClient):
    """Test case for remove_user

    Remove user from our platform if it exists
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/users/{user_id}".format(user_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

