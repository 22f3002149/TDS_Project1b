# wrtie a python script that reads all .md files in 'Misc/01' directory and remove all html formatting & HTML tags without losing the text content and save the cleaned .md files in 'Misc/03' directory which should be ready for chuking and text embedding using openai API
import os
import re
from bs4 import BeautifulSoup

def clean_html_tags(content):
    """Remove HTML tags and formatting from the content."""
    # Remove HTML tags but keep all hyperlinks and text content
    clean = re.compile('<.*?>')
    content = re.sub(clean, '', content)
    # Remove extra whitespace
    #content = re.sub(r'\s+', ' ', content).strip()
    return content

def clean_html_keep_links_and_alt(html):
    soup = BeautifulSoup(html, "html.parser")
    result = []
    for elem in soup.recursiveChildGenerator():
        if elem.name == "a" and elem.has_attr("href"):
            # Keep link text and URL
            result.append(f"{elem.get_text()} ({elem['href']})")
        elif elem.name == "img" and elem.has_attr("alt"):
            # Keep alt text for images
            result.append(elem["alt"])
        elif elem.string and not elem.name:
            # Keep plain text
            result.append(elem.string)
    return " ".join(result)

def process_markdown_files(input_directory, output_directory):
    """Process all markdown files in the input directory and save cleaned content to the output directory."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.endswith('.md'):
            file_path = os.path.join(input_directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                cleaned_content = clean_html_keep_links_and_alt(content)
                
                # Save cleaned content to new file
                output_file_path = os.path.join(output_directory, filename)
                with open(output_file_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(cleaned_content)
            print(f"Processed {filename} and saved cleaned content to {output_file_path}")
if __name__ == "__main__":
    input_dir = 'Misc/01'
    output_dir = 'Misc/03'
    process_markdown_files(input_dir, output_dir)
    print("All markdown files processed and cleaned content saved.")
# This script will read all markdown files in 'Misc/01', clean them by removing HTML tags and formatting, and save the cleaned content to 'Misc/03'. It ensures that the text content is preserved without any HTML formatting, making it suitable for further processing like chunking and text embedding.
# Make sure to run this script in an environment where the specified directories exist and contain the markdown files you want to process. Adjust the input and output directory paths as necessary based on your project structure.                        