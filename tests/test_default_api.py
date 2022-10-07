# coding: utf-8

from fastapi.testclient import TestClient


from openapi_server.models.unauthorized_error import UnauthorizedError  # noqa: F401


def test_bulk_update_all_admins_for_tournament(client: TestClient):
    """Test case for bulk_update_all_admins_for_tournament

    Bulk update of admins for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/tournaments/{tournament_id}/admins".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_brackets_for_tournament(client: TestClient):
    """Test case for bulk_update_all_brackets_for_tournament

    Bulk update all brackets for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/tournaments/{tournament_id}/brackets".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_settings_for_profile(client: TestClient):
    """Test case for bulk_update_all_settings_for_profile

    Bulk update of settings for a specific profile from the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/profiles/{relic_link_id}/settings".format(relic_link_id=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_teams(client: TestClient):
    """Test case for bulk_update_all_teams

    Bulk update of teams
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_tournaments(client: TestClient):
    """Test case for bulk_update_all_tournaments

    Bulk update of tournaments
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_user_details(client: TestClient):
    """Test case for bulk_update_all_user_details

    Bulk update details for a specific user profile on our platform if it exists
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/users/{user_id}".format(user_id='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_user_stats(client: TestClient):
    """Test case for bulk_update_all_user_stats

    Bulk update of stats for a specific user profile on our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/users/{user_id}/stats".format(user_id='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_bulk_update_all_users(client: TestClient):
    """Test case for bulk_update_all_users

    Bulk update of all users of our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_admin_for_tournament(client: TestClient):
    """Test case for create_new_admin_for_tournament

    Create a new admin for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/tournaments/{tournament_id}/admins".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_bracket_for_tournament(client: TestClient):
    """Test case for create_new_bracket_for_tournament

    Create a new bracket for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/tournaments/{tournament_id}/brackets".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_setting_for_profile(client: TestClient):
    """Test case for create_new_setting_for_profile

    Create a new setting for a specific profile from the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/profiles/{relic_link_id}/settings".format(relic_link_id=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_team(client: TestClient):
    """Test case for create_new_team

    Create a new team
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_tournament(client: TestClient):
    """Test case for create_new_tournament

    Create a new tournament for a game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_user(client: TestClient):
    """Test case for create_new_user

    Create a new user for our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_user_stats(client: TestClient):
    """Test case for create_new_user_stats

    Create a new stat for a specific user profile on our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/users/{user_id}/stats".format(user_id='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_create_new_user_validation(client: TestClient):
    """Test case for create_new_user_validation

    
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/users/validate",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_admin_collection_for_tournament(client: TestClient):
    """Test case for get_admin_collection_for_tournament

    Retrieve all admins for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/admins".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_bracket_collection_for_tournament(client: TestClient):
    """Test case for get_bracket_collection_for_tournament

    Retrieve all brackets for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/brackets".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_definition_collection_for_game(client: TestClient):
    """Test case for get_definition_collection_for_game

    Retrieve all available definitions for a specific game using Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/games/{game_id}/definitions".format(game_id='game_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_details_for_game(client: TestClient):
    """Test case for get_details_for_game

    Retrieve details for a game with a specific identifier using Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/games/{game_id}".format(game_id='game_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_details_for_leaderboard(client: TestClient):
    """Test case for get_details_for_leaderboard

    Retrieve details for a specific leaderboard
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/leaderboards/{leaderboard_id}".format(leaderboard_id='leaderboard_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_details_for_profile(client: TestClient):
    """Test case for get_details_for_profile

    Retrieve the details for a specific profile from the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles/{relic_link_id}".format(relic_link_id=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_details_for_team(client: TestClient):
    """Test case for get_details_for_team

    Retrieve details of a team
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/teams/{team_id}".format(game_id='game_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_details_for_tournament(client: TestClient):
    """Test case for get_details_for_tournament

    Retrieve details for a tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_details_for_user(client: TestClient):
    """Test case for get_details_for_user

    Retrieve details for a specific user profile on our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users/{user_id}".format(user_id='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_game_identifier_collection(client: TestClient):
    """Test case for get_game_identifier_collection

    Retrieve a list of all game identifiers for games using Relic Link API
    """

    headers = {
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

    Retrieve all available information for a specific game using Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/games/{game_id}/info".format(game_id='game_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_info_collection_for_tournament(client: TestClient):
    """Test case for get_info_collection_for_tournament

    Retrieve all information for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{tournament_id}/info".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_information_collection_for_application(client: TestClient):
    """Test case for get_information_collection_for_application

    Retrieve a list of available application information
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/application",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_leaderboard_collection(client: TestClient):
    """Test case for get_leaderboard_collection

    Retrieve all leaderboards hosted on the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/leaderboards",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_leaderboard_collection_for_game(client: TestClient):
    """Test case for get_leaderboard_collection_for_game

    Retrieve all leaderboards for a specific game using Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/games/{game_id}/leaderboards".format(game_id='game_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_match_collection_for_game(client: TestClient):
    """Test case for get_match_collection_for_game

    Retrieve all matches for a specific game using Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/games/{game_id}/matches".format(game_id='game_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_match_collection_for_leaderboard(client: TestClient):
    """Test case for get_match_collection_for_leaderboard

    Retrieve all matches on a specific leaderboard for a certain game hosted on the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/leaderboards/{leaderboard_id}/matches".format(leaderboard_id='leaderboard_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_match_collection_for_profile(client: TestClient):
    """Test case for get_match_collection_for_profile

    Retrieve all matches for a specific profile from the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles/{relic_link_id}/matches".format(relic_link_id=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_match_collection_for_team(client: TestClient):
    """Test case for get_match_collection_for_team

    Retrieve a list of matches for a specific team
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/teams/{team_id}/matches".format(game_id='game_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_profile_collection(client: TestClient):
    """Test case for get_profile_collection

    Retrieve all available profiles from the Relic Link API
    """

    headers = {
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

    Retrieve all settings for a specific profile from the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles/{relic_link_id}/settings".format(relic_link_id=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_application(client: TestClient):
    """Test case for get_stat_collection_for_application

    Retrieve a list of only application statistics
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/application/statistics",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_leaderboard(client: TestClient):
    """Test case for get_stat_collection_for_leaderboard

    Retrieve all stats on a specific leaderboard for a certain game hosted on the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/leaderboards/{leaderboard_id}/stats".format(leaderboard_id='leaderboard_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_profile(client: TestClient):
    """Test case for get_stat_collection_for_profile

    Retrieve all stats for a specific profile from the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/profiles/{relic_link_id}/stats".format(relic_link_id=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_team(client: TestClient):
    """Test case for get_stat_collection_for_team

    Retrieve a list of stats for a specific team
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/teams/{team_id}/stats".format(game_id='game_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_stat_collection_for_user(client: TestClient):
    """Test case for get_stat_collection_for_user

    Retrieve all stats for a specific user profile on our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users/{user_id}/stats".format(user_id='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_status_collection_for_application(client: TestClient):
    """Test case for get_status_collection_for_application

    Retrieve only application status
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/application/status",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_team_collection(client: TestClient):
    """Test case for get_team_collection

    Retrieve all available teams
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_tournament_details_for_game(client: TestClient):
    """Test case for get_tournament_details_for_game

    Retrieve all available tournaments for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments/{game_id}".format(game_id='game_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_tournament_identifier_collection(client: TestClient):
    """Test case for get_tournament_identifier_collection

    Retrieve all available tournaments for all games available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user_collection(client: TestClient):
    """Test case for get_user_collection

    Retrieve all users of our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user_validation_details(client: TestClient):
    """Test case for get_user_validation_details

    
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users/validate",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_all_admins_for_tournament(client: TestClient):
    """Test case for partial_update_all_admins_for_tournament

    Update details of admins for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/tournaments/{tournament_id}/admins".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_all_settings_for_profile(client: TestClient):
    """Test case for partial_update_all_settings_for_profile

    Update a specific setting for a specific profile from the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/profiles/{relic_link_id}/settings".format(relic_link_id=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_all_teams(client: TestClient):
    """Test case for partial_update_all_teams

    Partial update of all teams
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_all_users(client: TestClient):
    """Test case for partial_update_all_users

    Partially update details for all user profiles
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_bracket_for_tournament(client: TestClient):
    """Test case for partial_update_bracket_for_tournament

    Partial update all brackets for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/tournaments/{tournament_id}/brackets".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_tournament_details(client: TestClient):
    """Test case for partial_update_tournament_details

    Partially update a tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/tournaments/{tournament_id}".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_tournaments(client: TestClient):
    """Test case for partial_update_tournaments

    Partial update of tournaments
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_user(client: TestClient):
    """Test case for partial_update_user

    Update details for a specific user profile on our platform if it exists
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/users/{user_id}".format(user_id='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_partial_update_user_stats(client: TestClient):
    """Test case for partial_update_user_stats

    Partially update stats for a specific user profile on our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PATCH",
        "/users/{user_id}/stats".format(user_id='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_admins_for_tournament(client: TestClient):
    """Test case for remove_all_admins_for_tournament

    Remove all admins for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/tournaments/{tournament_id}/admins".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_brackets_for_tournament(client: TestClient):
    """Test case for remove_all_brackets_for_tournament

    Remove all brackets for a specific tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/tournaments/{tournament_id}/brackets".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_settings_for_profile(client: TestClient):
    """Test case for remove_all_settings_for_profile

    Remove all settings for a specific profile from the Relic Link API
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/profiles/{relic_link_id}/settings".format(relic_link_id=56),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_teams(client: TestClient):
    """Test case for remove_all_teams

    Remove all teams
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/teams",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_tournaments(client: TestClient):
    """Test case for remove_all_tournaments

    Remove all tournaments
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/tournaments",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_user_stats(client: TestClient):
    """Test case for remove_all_user_stats

    Remove all stats for a specific user profile on our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/users/{user_id}/stats".format(user_id='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_all_users(client: TestClient):
    """Test case for remove_all_users

    Remove all users from our platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/users",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_tournament_details(client: TestClient):
    """Test case for remove_tournament_details

    Remove a tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/tournaments/{tournament_id}".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_remove_user(client: TestClient):
    """Test case for remove_user

    Remove user from our platform if it exists
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "DELETE",
        "/users/{user_id}".format(user_id='user_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_tournament_details(client: TestClient):
    """Test case for update_tournament_details

    Update details for a tournament for a specific game available on the Relic Link platform
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "PUT",
        "/tournaments/{tournament_id}".format(tournament_id='tournament_id_example'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_login(client: TestClient):
    """Test case for user_login

    
    """

    headers = {
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
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "GET",
        "/users/logout",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_user_register(client: TestClient):
    """Test case for user_register

    
    """

    headers = {
        "X-Api-Key": "special-key",
    }
    response = client.request(
        "POST",
        "/users/register",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

