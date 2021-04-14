import argparse
import csv
import scrape_stats

BASE_URL = "https://itp.infosys-platforms.com/api/rg/stats-plus/v1/keystats/year/2020/eventId/520/matchId/"
CSV_COLUMNS = [
    "Aces",
    "Break Points Won",
    "Double Faults",
    "First Serve",
    "Name",
    "Net Points Won",
    "Receiving Points Won",
    "Total Points Won",
    "Unforced Errors",
    "Win On 1st Serve",
    "Win On 2nd Serve",
    "Winners",
    "Max Speed",
    "1st Serve Average Speed",
    "2nd Serve Average Speed",
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("matches_file", help="File with match ids to scrap.")
    args = parser.parse_args()
    match_stats = scrape_round("match_ids/french2020/" + args.matches_file)
    write_match_stats_to_csv(
        match_stats, "csv/" + args.matches_file.split(".")[0] + ".csv"
    )
