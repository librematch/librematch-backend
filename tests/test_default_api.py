# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.game_id import GameId  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401


def test_get_details_for_game(client: TestClient):
    """Test case for get_details_for_game

    Retrieve details for a game with a specific identifiers
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/games/{game_id}".format(game_id={'key': openapi_server.GameId()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

