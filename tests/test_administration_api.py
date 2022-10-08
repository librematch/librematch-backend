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


def test_get_information_collection_for_application(client: TestClient):
    """Test case for get_information_collection_for_application

    Retrieve a list of available application information
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/application",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_profile_collection(client: TestClient):
    """Test case for get_profile_collection

    Retrieve all available profiles
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles",
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


def test_get_stat_collection_for_application(client: TestClient):
    """Test case for get_stat_collection_for_application

    Retrieve a list of only application statistics
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/application/statistics",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_status_collection_for_application(client: TestClient):
    """Test case for get_status_collection_for_application

    Retrieve only application status
    """

    headers = {
        "BasicAuth": "special-key",
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/application/status",
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

