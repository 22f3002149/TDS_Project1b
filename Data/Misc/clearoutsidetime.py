# write a python script that runs through all json files in '02b_DiscoursePostsJson' and extract all posts in 'post_stream' and identify the ones which are 'created_at' and 'updated_at' outside the time range of 2025-01-01 to 2025-04-15. List these posts in a new JSON file saved as 'Misc/clearoutsidetime.json'
import os
import json
from datetime import datetime
def extract_posts_outside_time_range(directory, output_file, start_date, end_date):
    posts_outside_time = []
    start_dt = datetime.strptime(start_date, '%Y-%m-%d')
    end_dt = datetime.strptime(end_date, '%Y-%m-%d')

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    for post in data.get("post_stream", {}).get('posts', []):
                        created_at = datetime.strptime(post['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
                        updated_at = datetime.strptime(post['updated_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
                        if not (start_dt <= created_at <= end_dt) or not (start_dt <= updated_at <= end_dt):
                            posts_outside_time.append(post)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {file_path}")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(posts_outside_time, outfile, indent=4)
if __name__ == "__main__":
    extract_posts_outside_time_range(
        '02b_DiscoursePostsJson',
        'Misc/clearoutsidetime.json',
        '2025-01-01',
        '2025-04-14'
    )
    print("Extraction complete. Check 'Misc/clearoutsidetime.json' for results.")
