import csv

from os import walk


def order_players_by_stat(tournament_name, stat_name):
    dir_name = "csv/" + tournament_name
    _, _, filenames = next(walk(dir_name))

    player_name_to_score = {}
    for filename in filenames:
        with open(dir_name + "/" + filename, "r") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["Name"] not in player_name_to_score:
                    player_name_to_score[line["Name"]] = 0
                player_name_to_score[line["Name"]] += float(line[stat_name])

    return dict(sorted(player_name_to_score.items(), key=lambda item: -1 * item[1]))


def write_ranking_to_csv(tournament_name, stat_name):
    sorted_dict = order_players_by_stat(tournament_name, stat_name)
    csv_file_name = "rankings/" + tournament_name + "/" + stat_name + "_ranking.csv"
    with open(csv_file_name, "w") as csv_file:
        writer = csv.writer(csv_file)
        for key, value in sorted_dict.items():
            writer.writerow([key, value])
