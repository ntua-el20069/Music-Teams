import os
import fileinput

directory = 'music_teams_src/lib/prototype/'  # Replace with your directory path

def replace_padding(file_path):
    with fileinput.FileInput(file_path, inplace=True) as file:
        for line in file:
            print(line.replace("double baseWidth = ",
                               "double baseWidth = 450; //"), end='')

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.dart'):
                file_path = os.path.join(root, file_name)
                replace_padding(file_path)

process_directory(directory)
