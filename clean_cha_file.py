import os
import re
import argparse

def clean_cha_file(input_file, output_file):
    """ Removes word-final hyphens in .cha files to prevent CLAN crashes. """
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        if line.startswith("*"):
            # Regex for catching:
            # 1. Hyphens followed by spaces: "word- "
            # 2. Hyphens followed by punctuation: "word-."
            # 3. Hyphens followed by word boundaries
            cleaned_line = re.sub(r"(\b\w+)-(?=[\s\.,;:!?]|$)", r"\1", line)
        else:
            cleaned_line = line
        cleaned_lines.append(cleaned_line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

def process_all_cha(input_folder, output_folder):
    """ Processes all .cha files in a folder, cleaning word-final hyphens. """
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".cha"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            print(f"Cleaning {input_path} -> {output_path}")
            clean_cha_file(input_path, output_path)

def main():
    parser = argparse.ArgumentParser(description="Remove word-final hyphens in .cha files.")
    parser.add_argument("input_folder", help="Path to the folder containing .cha files.")
    parser.add_argument("output_folder", help="Path to save cleaned .cha files.")
    args = parser.parse_args()
    
    process_all_cha(args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()