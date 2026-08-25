import os
import re
import argparse


def clean_cha_file(input_file, output_file):

    # removes invalid speaker tiers and their continuation lines from .cha files
    # keeps only speaker tiers of the form *XXX:
    # any illegal speaker tier and all following continuation lines are removed
    # until the next legal speaker tier is reached

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    cleaned_lines = []

    # tracks whether inside an illegal speaker tier
    removing = False

    for line in lines:

        # a new speaker tier starts with *
        if line.startswith("*"):

            # check whether this is a legal 3-character speaker tier
            if re.match(r"^\*[A-Za-z0-9]{3}:", line):

                # legal tier: keep it
                removing = False
                cleaned_lines.append(line)

            else:

                # illegal tier: remove it and all continuation lines
                # until the next legal speaker tier
                removing = True
                print(f"Removing tier: {line.strip()}")

        else:
            
            # keep the line if not from illegal speaker tier
            if not removing:
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
        description="Remove invalid speaker tiers and their continuation lines from .cha files."
    )

    parser.add_argument(
        "input_folder",
        help="Folder containing .cha files."
    )

    parser.add_argument(
        "output_folder",
        help="Folder for cleaned .cha files."
    )

    args = parser.parse_args()

    process_all_cha(args.input_folder, args.output_folder)


if __name__ == "__main__":
    main()