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


def test_bulk_update_all_admins_for_tournament(client: TestClient):
    """Test case for bulk_update_all_admins_for_tournament

    Bulk update of admins for a specific tournament for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/tournaments/{tournament_id}/admins".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_brackets_for_tournament(client: TestClient):
    """Test case for bulk_update_all_brackets_for_tournament

    Bulk update all brackets for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/tournaments/{tournament_id}/brackets".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_tournaments(client: TestClient):
    """Test case for bulk_update_all_tournaments

    Bulk update of tournaments
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_admin_for_tournament(client: TestClient):
    """Test case for create_new_admin_for_tournament

    Create a new admin for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/tournaments/{tournament_id}/admins".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_bracket_for_tournament(client: TestClient):
    """Test case for create_new_bracket_for_tournament

    Create a new bracket for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/tournaments/{tournament_id}/brackets".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_tournament(client: TestClient):
    """Test case for create_new_tournament

    Create a new tournament for a game available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_admin_collection_for_tournament(client: TestClient):
    """Test case for get_admin_collection_for_tournament

    Retrieve all admins for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/admins".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_bracket_collection_for_tournament(client: TestClient):
    """Test case for get_bracket_collection_for_tournament

    Retrieve all brackets for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/brackets".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_info_collection_for_tournament(client: TestClient):
    """Test case for get_info_collection_for_tournament

    Retrieve all information for a specific tournament for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/info".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_match_collection_for_tournament(client: TestClient):
    """Test case for get_match_collection_for_tournament

    Retrieve all match data for a specific tournament for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/matches".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_tournament(client: TestClient):
    """Test case for get_stat_collection_for_tournament

    Retrieve all statistics for a specific tournament for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/stats".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_tournament_identifier_collection(client: TestClient):
    """Test case for get_tournament_identifier_collection

    Retrieve all available tournaments for all games available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_all_admins_for_tournament(client: TestClient):
    """Test case for partial_update_all_admins_for_tournament

    Update details of admins for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/tournaments/{tournament_id}/admins".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_bracket_for_tournament(client: TestClient):
    """Test case for partial_update_bracket_for_tournament

    Partial update all brackets for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/tournaments/{tournament_id}/brackets".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_tournaments(client: TestClient):
    """Test case for partial_update_tournaments

    Partial update of tournaments
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_admins_for_tournament(client: TestClient):
    """Test case for remove_all_admins_for_tournament

    Remove all admins for a specific tournament for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/tournaments/{tournament_id}/admins".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_brackets_for_tournament(client: TestClient):
    """Test case for remove_all_brackets_for_tournament

    Remove all brackets for a specific tournament for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/tournaments/{tournament_id}/brackets".format(tournament_id={'key': openapi_server.Ulid()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_tournaments(client: TestClient):
    """Test case for remove_all_tournaments

    Remove all tournaments
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200
