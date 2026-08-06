import os
import re
import argparse

def clean_cha_file(input_file, output_file):

    # removes invalid speaker tiers from .cha files
    # keeps only speaker tiers of the form *XXX:
    # other speaker tier structures would cause CLAN to crash when tagging morphologies

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = []

    for line in lines:
        if line.startswith("*"):
            # keeps only 3-character tiers like *CHI:, *FA1:, *MA1:, etc.
            if re.match(r"^\*[A-Za-z0-9]{3}:", line):
                cleaned_lines.append(line)
            else:
                print(f"Removing tier: {line.strip()}")
        else:
            # keeps all other lines
            cleaned_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as f:
        f.writelines(cleaned_lines)


def process_all_cha(input_folder, output_folder):
    # processes all .cha files in a folder

    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".cha"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            print(f"Cleaning {filename}")
            clean_cha_file(input_path, output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Remove invalid speaker tiers from .cha files."
    )

    parser.add_argument("input_folder",
                        help="Folder containing .cha files.")
    parser.add_argument("output_folder",
                        help="Folder for cleaned .cha files.")

    args = parser.parse_args()

    process_all_cha(args.input_folder, args.output_folder)


if __name__ == "__main__":
    main()