# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.search_param import SearchParam  # noqa: F401
from openapi_server.models.steam_id import SteamId  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401


def test_get_profile_information_from_search(client: TestClient):
    """Test case for get_profile_information_from_search

    
    """
    params = [("by_name", {'key': openapi_server.SearchParam()}),     ("by_steam_id", {'key': openapi_server.SteamId()})]
    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles/search",
        headers=headers,
        params=params,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

