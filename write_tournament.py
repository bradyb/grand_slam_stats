import scrape_round

NUMBER_OF_ROUNDS = 7


def generate_file_name(round_number):
    return "round_" + str(round_number) + "_ids.txt"


if __name__ == "__main__":
    for index in range(1, NUMBER_OF_ROUNDS + 1):
        scrape_round.write_round_to_csv(generate_file_name(index))