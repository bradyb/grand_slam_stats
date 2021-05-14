import argparse
import csv
import scrape_stats
import tournament_constants


def get_url(match_id_line):
    return tournament_constants.BASE_URL + match_id_line.rstrip()


def scrape_round(match_ids_file_name):
    match_ids_file = open(match_ids_file_name, "r")
    match_ids = match_ids_file.readlines()

    match_stats = []
    for match_id in match_ids:
        match_stats.append(scrape_stats.get_match_stats(get_url(match_id)))
    return match_stats


def write_match_stats_to_csv(match_stats, csv_file_name):
    with open(csv_file_name, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=tournament_constants.CSV_COLUMNS)
        writer.writeheader()
        for match_stat in match_stats:
            writer.writerow(match_stat["player1"])
            writer.writerow(match_stat["player2"])


def write_round_to_csv(round_ids_file_name, tournament_name):
    match_stats = scrape_round("match_ids/french2020/" + round_ids_file_name)
    write_match_stats_to_csv(
        match_stats,
        "csv/" + tournament_name + "/" + round_ids_file_name.split(".")[0] + ".csv",
    )
