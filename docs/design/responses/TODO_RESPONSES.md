# Responses that need to be designed

## TODO

- GET /application/status
- GET /dumps/{timeframe}
- GET /users/validate
- GET /games/{game_id}/definitions
- GET /games/{game_id}/info

### Blocking

- GET /games
- GET /games/{game_id}
- GET /games/{game_id}/matches
- GET /games/{game_id}/leaderboards
- GET /games/matches/{match_uuid}
- GET /profiles
- GET /profiles/{relic_link_id}
- GET /profiles/{relic_link_id}/matches
- GET /profiles/{relic_link_id}/ledger
- GET /leaderboards
- GET /leaderboards/{leaderboard_id}
- GET /leaderboards/{leaderboard_id}/matches

## Done

- GET /profiles/{profile_id}/matches?single_match=
- GET /profiles/search?steam_id
- GET /profiles/search?alias

## Notes

- do we need ranks/percentiles in ratinghistory, so people can use that to create a graph of profiles also for their ranking at a certain moment in time? (-> Coolio)
