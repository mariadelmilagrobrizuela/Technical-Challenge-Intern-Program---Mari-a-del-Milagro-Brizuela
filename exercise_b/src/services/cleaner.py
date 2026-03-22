from models.Episode import Episode


def clean_episodes(episodes):
    cleaned_episodes = []
    cleaner_stats = {
        'total': len(episodes),
        'discarded': 0,
        'corrected': 0
    }

    for episode in episodes:
        original = episode.__dict__.copy()

        episode.normalize()
        episode.clean()

        if episode.is_discardable():
            cleaner_stats['discarded'] += 1
            continue

        if episode.__dict__ != original:
            cleaner_stats['corrected'] += 1

        cleaned_episodes.append(episode)

    return cleaned_episodes, cleaner_stats