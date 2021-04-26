import argparse
import csv
import scrape_stats

BASE_URL = "https://itp.infosys-platforms.com/api/rg/stats-plus/v1/keystats/year/2020/eventId/520/matchId/"
CSV_COLUMNS = [
    "Aces",
    "Break Points Won",
    "Break Points Saved",
    "Break Points Lost",
    "Double Faults",
    "First Serve",
    "Name",
    "Net Points Won",
    "Receiving Points Won Pct",
    "Total Points Won",
    "Unforced Errors",
    "Win On 1st Serve",
    "Win On 2nd Serve Pct",
    "Winners",
    "Max Speed",
    "1st Serve Average Speed",
    "2nd Serve Average Speed",
    "Break Points Won Raw",
]


def get_url(match_id_line):
    return BASE_URL + match_id_line.rstrip()


def scrape_round(match_ids_file_name):
    match_ids_file = open(match_ids_file_name, "r")
    match_ids = match_ids_file.readlines()

    match_stats = []
    for match_id in match_ids:
        match_stats.append(scrape_stats.get_match_stats(get_url(match_id)))
    return match_stats


def write_match_stats_to_csv(match_stats, csv_file_name):
    with open(csv_file_name, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for match_stat in match_stats:
            writer.writerow(match_stat["player1"])
            writer.writerow(match_stat["player2"])


def write_round_to_csv(round_ids_file_name):
    match_stats = scrape_round("match_ids/french2020/" + round_ids_file_name)
    write_match_stats_to_csv(
        match_stats, "csv/" + round_ids_file_name.split(".")[0] + ".csv"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("round_ids", help="File with match ids from a round to scrape.")
    args = parser.parse_args()
    write_round_to_csv(args.round_ids)
