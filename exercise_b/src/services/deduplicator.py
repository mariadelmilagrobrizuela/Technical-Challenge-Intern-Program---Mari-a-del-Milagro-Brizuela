def is_better_episode(new_episode, existing_episode):
    if new_episode.air_date != "Unknown" and existing_episode.air_date == "Unknown":
        return True
    if new_episode.air_date == "Unknown" and existing_episode.air_date != "Unknown":
        return False

    if new_episode.episode_title != "Untitled Episode" and existing_episode.episode_title == "Untitled Episode":
        return True
    if new_episode.episode_title == "Untitled Episode" and existing_episode.episode_title != "Untitled Episode":
        return False

    new_valid = new_episode.season_number > 0 and new_episode.episode_number > 0
    existing_valid = existing_episode.season_number > 0 and existing_episode.episode_number > 0

    if new_valid and not existing_valid:
        return True
    if not new_valid and existing_valid:
        return False

    return False


def deduplicate_episodes(cleaned_episodes):
    unique_episodes = []
    deduplicator_stats = {
        'total': len(cleaned_episodes),
        'duplicates_removed': 0
    }

    for episode in cleaned_episodes:
        duplicate_found = False

        for i, existing in enumerate(unique_episodes):

            rule_1 = (
                episode.series_name == existing.series_name and
                episode.season_number == existing.season_number and
                episode.episode_number == existing.episode_number
            )

            rule_2 = (
                episode.series_name == existing.series_name and
                episode.episode_number == existing.episode_number and
                episode.episode_title == existing.episode_title and
                (episode.season_number == 0 or existing.season_number == 0)
            )

            rule_3 = (
                episode.series_name == existing.series_name and
                episode.season_number == existing.season_number and
                episode.episode_title == existing.episode_title and
                (episode.episode_number == 0 or existing.episode_number == 0)
            )

            if rule_1 or rule_2 or rule_3:
                duplicate_found = True

                if is_better_episode(episode, existing):
                    unique_episodes[i] = episode

                deduplicator_stats['duplicates_removed'] += 1
                break

        if not duplicate_found:
            unique_episodes.append(episode)

    return unique_episodes, deduplicator_stats