from services.parser import parse_csv
from services.cleaner import clean_episodes
from services.deduplicator import deduplicate_episodes
from services.report_generator import generate_clean_csv, generate_data_quality_report


def main():
    episodes = parse_csv("data/input/catalog.csv")
    
    cleaned_episodes, cleaner_stats = clean_episodes(episodes)
    
    unique_episodes, deduplicator_stats = deduplicate_episodes(cleaned_episodes)
    
    generate_clean_csv(unique_episodes)
    
    generate_data_quality_report(
        total_input=cleaner_stats["total"],
        total_cleaned=len(unique_episodes),
        discarded=cleaner_stats["discarded"],
        corrected=cleaner_stats["corrected"],
        duplicates_removed=deduplicator_stats["duplicates_removed"]
    )

if __name__ == "__main__":
    main()