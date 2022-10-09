# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.count_param import CountParam  # noqa: F401
from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.game_id import GameId  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.relic_link_id import RelicLinkId  # noqa: F401
from openapi_server.models.since_param import SinceParam  # noqa: F401
from openapi_server.models.start_param import StartParam  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.ulid import Ulid  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401


def test_get_ledger_collection_for_profile(client: TestClient):
    """Test case for get_ledger_collection_for_profile

    Retrieve the rating ledger for a specific profile
    """
    params = [("game", {'key': openapi_server.GameId()}),     ("start", {'key': openapi_server.StartParam()}),     ("leaderboard_id", {'key': openapi_server.Ulid()}),     ("count", {'key': openapi_server.CountParam()}),     ("since", {'key': openapi_server.SinceParam()})]
    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles/{relic_link_id}/ledger".format(relic_link_id={'key': openapi_server.RelicLinkId()}),
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

