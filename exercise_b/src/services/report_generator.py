import csv
from pathlib import Path


OUTPUT_DIR = Path("data/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)  # Crea la carpeta si no existe


def generate_clean_csv(unique_episodes, filename="episodes_clean.csv"):
    output_path = OUTPUT_DIR / filename

    with open(output_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        writer.writerow(["SeriesName", "SeasonNumber", "EpisodeNumber", "EpisodeTitle", "AirDate"])
        
        for episode in unique_episodes:
            writer.writerow([
                episode.series_name,
                episode.season_number,
                episode.episode_number,
                episode.episode_title,
                episode.air_date
            ])
    
    return output_path


def generate_data_quality_report(
        total_input,
        total_cleaned,
        discarded,
        corrected,
        duplicates_removed,
        filename="report.md"
    ):
    
    output_path = OUTPUT_DIR / filename
    
    with open(output_path, mode="w", encoding="utf-8") as f:
        f.write("# DATA QUALITY REPORT\n\n")
        
        f.write("## Stats\n\n")
        f.write(f"- Total input records: {total_input}\n")
        f.write(f"- Total output records: {total_cleaned}\n")
        f.write(f"- Number of discarded entries: {discarded}\n")
        f.write(f"- Number of corrected entries: {corrected}\n")
        f.write(f"- Number of duplicates detected: {duplicates_removed}\n\n")

        f.write("## Deduplication Strategy\n\n")
        f.write(
            "Episodes must be considered duplicates when they refer to the same:\n\n"
            "(SeriesName_normalized, SeasonNumber, EpisodeNumber) or\n"
            "(SeriesName_normalized, SeasonNumber, EpisodeNumber) or\n"
            "(SeriesName_normalized, SeasonNumber, EpisodeNumber)\n\n"
            "When duplicates existed, the following priority was used to retain the best record:\n\n"
            "1. Episodes with a valid AirDate over 'Unknown'\n"
            "2. Episodes with a known EpisodeTitle over 'Untitled Episode'\n"
            "3. Episodes with valid SeasonNumber and EpisodeNumber\n"
            "4. If tied, the first entry encountered was retained"
        )
    
    return output_path