import scrape_round

NUMBER_OF_ROUNDS = 7


def generate_file_name(round_number):
    return "round_" + str(round_number) + "_ids.txt"


if __name__ == "__main__":
    for index in [number + 1 for number in range(NUMBER_OF_ROUNDS)]:
        scrape_round.write_round_to_csv(generate_file_name(index))