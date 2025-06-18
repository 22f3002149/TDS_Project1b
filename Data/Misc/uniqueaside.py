# Write python script that lists all class names inside '<aside' tags in all json files in '02b_DiscoursePostsJson' directory and saves them to a file called 'Misc/unique_aside_classes.txt'.
import os
import json
def extract_unique_aside_classes(directory='02b_DiscoursePostsJson', output_file='Misc/unique_aside_classes.txt'):
    unique_classes = set()
    
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    for post in data.get("post_stream", {}).get('posts', []):
                        if 'cooked' in post:
                            cooked_content = post['cooked']
                            # Find all <aside> tags and extract class names
                            start = 0
                            while True:
                                start = cooked_content.find('<aside', start)
                                if start == -1:
                                    break
                                end = cooked_content.find('>', start)
                                if end == -1:
                                    break
                                aside_tag = cooked_content[start:end]
                                # Extract class names from the tag
                                if 'class="' in aside_tag:
                                    class_start = aside_tag.find('class="') + len('class="')
                                    class_end = aside_tag.find('"', class_start)
                                    class_names = aside_tag[class_start:class_end].split()
                                    unique_classes.update(class_names)
                                start = end + 1
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {file_path}")
    # Save unique class names to a file
    with open(output_file, 'w', encoding='utf-8') as output:
        for class_name in sorted(unique_classes):
            output.write(f"{class_name}\n")
    print(f"Unique class names extracted and saved to {output_file}")
extract_unique_aside_classes()