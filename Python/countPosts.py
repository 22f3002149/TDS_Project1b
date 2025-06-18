# wirte python script to count the number of posts in all json files in a given directory
import os
import json
def count_posts_in_json_files(directory):
    total_posts = 0
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    total_posts += len(data["post_stream"]['posts'])
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {file_path}")
    return total_posts

count = count_posts_in_json_files('02b_DiscoursePostsJson')
print(f'Total number of posts in all JSON files: {count}')