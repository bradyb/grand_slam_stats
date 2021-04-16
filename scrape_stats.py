import argparse
import csv
import pprint
import requests

# https://itp.infosys-platforms.com/api/rg/stats-plus/v1/keystats/year/2020/eventId/520/matchId/SM076


def get_percentage_from_str(stat_str):
    return stat_str.split("%")[0].split("(")[1]


def fill_match_stat_for_player(stat_dict, player_index, stats_array):
    stat_name = stat_dict["name"]
    raw_value = stat_dict["player" + player_index]
    player_dict = stats_array[("player" + player_index)]
    if stat_name == "Break Points Won":
        player_dict[stat_name] = raw_value.split("/")[0]
    elif stat_name == "Receiving Points Won":
        player_dict["Receiving Points Won Pct"] = get_percentage_from_str(raw_value)
    elif stat_name == "Win On 2nd Serve":
        player_dict["Win On 2nd Serve Pct"] = get_percentage_from_str(raw_value)
    else:
        player_dict[stat_name] = raw_value


def fill_match_stat(stat_dict, stats_array):
    if not stat_dict:
        return
    fill_match_stat_for_player(stat_dict, "1", stats_array)
    fill_match_stat_for_player(stat_dict, "2", stats_array)


def set_player_names(players, stats_of_interest):
    for player, stats in stats_of_interest.items():
        stats["Name"] = players[player]


def verify_stats(stats_of_interest):
    assert "player1" in stats_of_interest
    assert "player2" in stats_of_interest


def get_match_stats(url):
    page = requests.get(url)
    json = page.json()

    players = {
        "player1": json["players"][0]["player1name"],
        "player2": json["players"][1]["player1name"],
    }
    pprint.pprint(players)

    stats_array = json["setStats"]["set0"]
    stats_of_interest = {"player1": {}, "player2": {}}

    for stat_dict in stats_array:
        fill_match_stat(stat_dict, stats_of_interest)

    set_player_names(players, stats_of_interest)

    verify_stats(stats_of_interest)
    return stats_of_interest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url to get")
    args = parser.parse_args()
    get_match_stats(args.url)
