# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.forbidden_error import ForbiddenError  # noqa: F401
from openapi_server.models.not_acceptable_error import NotAcceptableError  # noqa: F401
from openapi_server.models.not_found_error import NotFoundError  # noqa: F401
from openapi_server.models.not_implemented_error import NotImplementedError  # noqa: F401
from openapi_server.models.relic_link_id import RelicLinkId  # noqa: F401
from openapi_server.models.too_many_requests_error import TooManyRequestsError  # noqa: F401
from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401
from openapi_server.models.unsupported_media_type_error import UnsupportedMediaTypeError  # noqa: F401


def test_bulk_update_all_settings_for_profile(client: TestClient):
    """Test case for bulk_update_all_settings_for_profile

    Bulk update of settings for a specific profile from the Relic Link API
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/profiles/{relic_link_id}/settings".format(relic_link_id={'key': openapi_server.RelicLinkId()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_setting_for_profile(client: TestClient):
    """Test case for create_new_setting_for_profile

    Create a new setting for a specific profile from the Relic Link API
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/profiles/{relic_link_id}/settings".format(relic_link_id={'key': openapi_server.RelicLinkId()}),
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


def test_partial_update_all_settings_for_profile(client: TestClient):
    """Test case for partial_update_all_settings_for_profile

    Update a specific setting for a specific profile from the Relic Link API
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/profiles/{relic_link_id}/settings".format(relic_link_id={'key': openapi_server.RelicLinkId()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_settings_for_profile(client: TestClient):
    """Test case for remove_all_settings_for_profile

    Remove all settings for a specific profile
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/profiles/{relic_link_id}/settings".format(relic_link_id={'key': openapi_server.RelicLinkId()}),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

