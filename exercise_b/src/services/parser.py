import csv
from models.Episode import Episode


def parse_csv(file_path):
    episodes = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for parts in reader:
            if len(parts) != 5:
                continue

            series_name, season_number, episode_number, episode_title, air_date = parts

            episode = Episode(
                series_name,
                season_number,
                episode_number,
                episode_title,
                air_date
            )

            episodes.append(episode)

    return episodes