# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.not_implemented_error import NotImplementedError  # noqa: F401
from openapi_server.models.relic_link_id import RelicLinkId  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.ulid import Ulid  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401


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


def test_get_details_for_profile(client: TestClient):
    """Test case for get_details_for_profile

    Retrieve the details for a specific profile
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles/{relic_link_id}".format(relic_link_id={'key': openapi_server.RelicLinkId()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_details_for_tournament(client: TestClient):
    """Test case for get_details_for_tournament

    Retrieve details for a tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}".format(tournament_id={'key': openapi_server.Ulid()}),
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


def test_get_game_identifier_collection(client: TestClient):
    """Test case for get_game_identifier_collection

    Retrieve a list of all game identifiers for games
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/games",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_info_collection_for_game(client: TestClient):
    """Test case for get_info_collection_for_game

    Retrieve all available information for a specific game
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/games/{game_id}/info".format(game_id={'key': openapi_server.Ulid()}),
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


def test_get_leaderboard_collection(client: TestClient):
    """Test case for get_leaderboard_collection

    Retrieve all leaderboards
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/leaderboards",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_setting_collection_for_profile(client: TestClient):
    """Test case for get_setting_collection_for_profile

    Retrieve all settings for a specific profile
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles/{relic_link_id}/settings".format(relic_link_id={'key': openapi_server.RelicLinkId()}),
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

