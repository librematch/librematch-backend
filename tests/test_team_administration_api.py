# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.not_implemented_error import NotImplementedError  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.ulid import Ulid  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401
from openapi_server.models.unsupported_media_type_error import UnsupportedMediaTypeError  # noqa: F401


def test_bulk_update_all_teams(client: TestClient):
    """Test case for bulk_update_all_teams

    Bulk update of teams
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_team(client: TestClient):
    """Test case for create_new_team

    Create a new team
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_details_for_team(client: TestClient):
    """Test case for get_details_for_team

    Retrieve details of a team
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/teams/{team_id}".format(team_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_team(client: TestClient):
    """Test case for get_stat_collection_for_team

    Retrieve a list of stats for a specific team
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/teams/{team_id}/stats".format(team_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_team_collection(client: TestClient):
    """Test case for get_team_collection

    Retrieve all available teams
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_all_teams(client: TestClient):
    """Test case for partial_update_all_teams

    Partial update of all teams
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_teams(client: TestClient):
    """Test case for remove_all_teams

    Remove all teams
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

