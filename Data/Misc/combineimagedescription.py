# write python script that runs through all .md files in 'Misc/03' directory. For every image in the markdown file, add a description after the image link. The description the the content from  corresponding file as image filename but with .md extension from the 'Misc/02' directory. export the modified markdown file to 'Misc/05' directory. a status report file should be created in 'Misc' folder with the name 'image_description_status.txt' that contains the number of files processed, number of images found, and number of images with descriptions added, list of images wihout descriptions, and list of images with descriptions added.
import os
import re
def add_image_descriptions(md_directory, desc_directory, output_directory):
    status_report = {
        'files_processed': 0,
        'images_found': 0,
        'images_with_descriptions': [],
        'images_without_descriptions': []
    }

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(md_directory):
        if filename.endswith('.md'):
            status_report['files_processed'] += 1
            md_file_path = os.path.join(md_directory, filename)
            with open(md_file_path, 'r', encoding='utf-8') as md_file:
                content = md_file.read()

            # Find all image links in the markdown file (Markdown and custom format)
            image_links = re.findall(r'!\[.*?\]\((.*?)\)|\((https?://[^\s)]+\.(?:png|jpe?g|webp))\)', content, re.IGNORECASE)
            # Also match bare URLs in parentheses (custom format)
            image_links += re.findall(r'\((https?://[^\s)]+\.(?:png|jpe?g|webp))\)', content, re.IGNORECASE)
            # Flatten and deduplicate
            image_links = list(set([i if isinstance(i, str) else (i[0] or i[1]) for i in image_links if i or (isinstance(i, tuple) and (i[0] or i[1]))]))
            status_report['images_found'] += len(image_links)

            # Replace each image link with itself plus the description (if available)
            def add_description_to_image(match):
                image_link = match.group(2) or match.group(4)
                if not image_link:
                    return match.group(0)
                # Extract last two parts of the URI path (without extension) and join with '_'
                from urllib.parse import urlparse
                parsed = urlparse(image_link)
                path_parts = [p for p in parsed.path.split('/') if p]
                if len(path_parts) >= 2:
                    part1 = os.path.splitext(path_parts[-2])[0]
                    part2 = os.path.splitext(path_parts[-1])[0]
                    image_name = f"{part1}_{part2}"
                else:
                    image_name = os.path.splitext(path_parts[-1])[0] if path_parts else "unknown"
                desc_file_path = os.path.join(desc_directory, f"{os.path.splitext(image_name)[0]}.md")
                if os.path.exists(desc_file_path):
                    with open(desc_file_path, 'r', encoding='utf-8') as desc_file:
                        description = desc_file.read().strip()
                    status_report['images_with_descriptions'].append(image_name)
                    return f"{match.group(0)}\n\n{description}\n"
                else:
                    status_report['images_without_descriptions'].append(image_name)
                    return match.group(0)

            # Update content in-place for both Markdown and custom format
            content = re.sub(r'(!\[.*?\]\((.*?)\))|(\((https?://[^\s)]+\.(?:png|jpe?g|webp))\))',
                            lambda m: add_description_to_image(m), content, flags=re.IGNORECASE)

            # Write the modified content to the output directory
            output_file_path = os.path.join(output_directory, filename)
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(content)

    # Write the status report
    status_report_path = os.path.join('Misc', 'image_description_status.txt')
    with open(status_report_path, 'w', encoding='utf-8') as report_file:
        report_file.write(f"Files Processed: {status_report['files_processed']}\n")
        report_file.write(f"Images Found: {status_report['images_found']}\n")
        report_file.write(f"Images with Descriptions: {len(status_report['images_with_descriptions'])}\n")
        report_file.write(f"Images without Descriptions: {len(status_report['images_without_descriptions'])}\n")
        report_file.write(f"List of Images with Descriptions: {status_report['images_with_descriptions']}\n")
        report_file.write(f"List of Images without Descriptions: {status_report['images_without_descriptions']}\n")

md_directory = 'Misc/06'
desc_directory = 'Misc/07'
output_directory = 'Misc/08'
add_image_descriptions(md_directory, desc_directory, output_directory)
