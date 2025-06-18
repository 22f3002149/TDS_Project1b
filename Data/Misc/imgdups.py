# write a python script that runs through all .md files in 'Misc/02' directory and if any file name contains '_2_' then make a copy of this file in 'Misc/04' directory with the same name but without the content of the name starts with '_2_'
import os
import shutil
def copy_files_with_condition(input_directory, output_directory):
    """Copy files from input directory to output directory based on naming condition."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    for filename in os.listdir(input_directory):
        if filename.endswith('.md') and '_2_' in filename:
            # Create new filename without '_2_' part
            new_filename = filename.replace('_2_', '!')
            new_filename = new_filename.split('!')[0] + '.md'
            source_path = os.path.join(input_directory, filename)
            destination_path = os.path.join(output_directory, new_filename)
            shutil.copyfile(source_path, destination_path)
            print(f"Copied {filename} to {new_filename} in {output_directory}")
if __name__ == "__main__":
    input_dir = 'Misc/02'
    output_dir = 'Misc/04'
    copy_files_with_condition(input_dir, output_dir)
    print("Files copied based on naming condition.")


