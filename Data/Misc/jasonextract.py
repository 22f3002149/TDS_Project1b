# write python script that runs through all json files in '02b_DiscoursePostsJson' and from all posts in 'post_stream' and create a markdown file for each json file as below:
# First line for each post "Topic:" + collect 'topic_id' from post and from 'Misc/Topics.csv' file get 'title' for the topic_id
# Second line for each post "Topic URL:" + create URL as 'https://discourse.onlinedegree.iitm.ac.in/t/' + 'topic_slug' + '/' + 'topic_id'
# Third line for each post "Post URL:" + create URL as 'https://discourse.onlinedegree.iitm.ac.in/t/' + 'topic_slug' + '/' + 'topic_id' + '/' + 'post_number'
# Fourth line for each post "Post:" + collect 'cooked' from post and remove '<aside>' tag and its content from 'cooked' where class name for aside is 'group-ds-students' or 'group-faculty' and remove all HTML tags from 'cooked' content
# Save the text file with the same name as the json file as markdown file with .md extension in 'Misc/01' directory
import os
import json
import csv
def load_topics(file_path):
    topics = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            topics[row['topic_id']] = {
                'title': row['title'],
                'slug': row['slug']
            }
    return topics
def clean_cooked_content(cooked):
    # Remove <aside> tags with specific class names and their content
    cleaned = cooked
    cleaned = cleaned.replace('<aside class="group-ds-students">', '').replace('</aside>', '')
    cleaned = cleaned.replace('<aside class="group-faculty">', '').replace('</aside>', '')
    # Remove all HTML tags
    #cleaned = ''.join(cleaned.split('<')).split('>')[0::2]
    return cleaned
def process_json_files(directory, topics):
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                try:
                    data = json.load(file)
                    posts = data.get("post_stream", {}).get('posts', [])
                    markdown_content = []
                    for post in posts:
                        topic_id = str(post.get('topic_id'))
                        if topic_id in topics:
                            topic = topics[topic_id]
                            topic_title = topic['title']
                            topic_slug = topic['slug']
                            post_number = post.get('post_number')
                            cooked_content = clean_cooked_content(post.get('cooked', ''))
                            
                            markdown_content.append(f"Topic: {topic_title}")
                            markdown_content.append(f"Topic URL: https://discourse.onlinedegree.iitm.ac.in/t/{topic_slug}/{topic_id}")
                            markdown_content.append(f"Post URL: https://discourse.onlinedegree.iitm.ac.in/t/{topic_slug}/{topic_id}/{post_number}")
                            markdown_content.append(f"Post: {cooked_content}\n")
                    
                    # Save to markdown file
                    md_filename = os.path.splitext(filename)[0] + '.md'
                    md_file_path = os.path.join('Misc/01', md_filename)
                    with open(md_file_path, 'w', encoding='utf-8') as md_file:
                        md_file.write('\n'.join(markdown_content))
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from file: {file_path}")

topics_file_path = 'Misc/Topics.csv'
json_directory = '02b_DiscoursePostsJson'
    
# Load topics from CSV file
topics = load_topics(topics_file_path)
    
# Process JSON files and create markdown files
process_json_files(json_directory, topics)
