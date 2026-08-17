import sys
import os
import re
import pandas as pd
import xlsxwriter

def get_readable_category(tag):
    clan_categories = {
        'adj': 'adjective',
        'adj:pred': 'adjective',
        'adv': 'adverb',
        'adv:tem': 'adverb (temporal)',
        'aux': 'auxiliary verb',
        'co': 'communicator',
        'comp': 'complementizer',
        'conj': 'conjunction',
        'coord': 'coordinator',
        'cop': 'copula',
        'det:art': 'article',
        'det:dem': 'demonstrative',
        'det:int': 'interrogative determiner',
        'det:num': 'number',
        'det:poss': 'possessive determiner',
        'inf': 'infinitive',
        'mod': 'modal verb',
        'n': 'noun',
        'n:prop': 'proper noun',
        'n:let': 'letter noun',
        'n:pt': 'plural noun',
        'neg': 'negative',
        'on': 'onomatopoeia',
        'part': 'particle',
        'prep': 'preposition',
        'pro:dem': 'demonstrative pronoun',
        'pro:exist': 'existential pronoun',
        'pro:indef': 'indefinite pronoun',
        'pro:int': 'interrogative pronoun',
        'pro:obj': 'object pronoun',
        'pro:per': 'personal pronoun',
        'pro:poss': 'possessive pronoun',
        'pro:rel': 'relative pronoun',
        'pro:sub': 'subject pronoun',
        'v': 'verb',
        '?': 'unknown'    # for all unrecognized tokens
    }
    base_tag = tag.split('-')[0]
    return clan_categories.get(base_tag, tag)

def get_extraction_tag(mor_token):
    # determines whether a token should be extract and what mor tag it has

    # leading tags that should always be extracted
    leading_tags = {
        'n',
        'v',
        'n:prop',
        'n:let',
        'n:pt',
        'aux',
        'mod',
        'cop',
        'part',
        '?'
    }

    # check the leading tag first
    if '|' in mor_token:
        leading_tag = mor_token.split('|', 1)[0]

        if leading_tag in leading_tags:
            return leading_tag

    # check for additional embedded mor structure for contractions, etc.
    if '~aux' in mor_token:
        return 'aux'

    if '~mod' in mor_token:
        return 'mod'

    if '~cop' in mor_token:
        return 'cop'

    if '#n' in mor_token:
        return '?'

    if '&dn-POSS' in mor_token:
        return 'adj'

    # token is not one of the interested mor categories
    return None

def extract_utterance_text(lines, start_index):
    first_line = lines[start_index]

    # remove the 3-character speaker code from the first line
    utterance = first_line[5:].rstrip('\n')

    current_index = start_index + 1

    # continue collecting lines until reaching a dependent tier
    while current_index < len(lines):
        line = lines[current_index]

        if line.startswith('%'):
            break

        # continued lines begin with whitespace
        if line.startswith('\t') or line.startswith(' '):
            utterance += ' ' + line.strip()
            current_index += 1
        else:
            break

    return utterance.strip(), current_index

def extract_mor_tier(lines, start_index):

    current_index = start_index

    # find the %mor: tier associated with this utterance
    if current_index >= len(lines) or not lines[current_index].startswith('%mor:'):
        return None, start_index

    # remove '%mor:' from the first line
    mor_line = lines[current_index][5:].strip()
    current_index += 1

    # collect continued %mor lines
    while current_index < len(lines):
        line = lines[current_index]

        if line.startswith('\t') or line.startswith(' '):
            mor_line += ' ' + line.strip()
            current_index += 1
        else:
            break

    return mor_line, current_index

def process_clan_file(input_file):
    # reads a .cha file and extracts relevant mor info to .xlsx outputs

    filename = os.path.basename(input_file)

    with open(input_file, 'r', encoding='utf-8') as cha_f:
        lines = cha_f.readlines()

    data = {
        'file_name': [],
        'line_number': [],
        'speaker': [],
        'utterance': [],
        'token': [],
        'tag': [],
        'readable_tag': [],
        'is_correct_tag': [],
        'corrected_tag': []
    }

    i = 0

    while i < len(lines):

        # look for speaker tiers
        if lines[i].startswith('*'):

            # extract the 3-character speaker code
            speaker = lines[i][1:4]

            # make sure this is actually a valid speaker tier
            if (
                len(lines[i]) >= 5
                and lines[i][4] == ':'
                and re.match(r'^[A-Za-z0-9]{3}$', speaker)
            ):

                # save the physical line number of the speaker tier
                line_number = i + 1

                # extract the complete utterance
                utterance, mor_start = extract_utterance_text(
                    lines,
                    i
                )

                # find the associated mor tier
                mor_line, mor_end = extract_mor_tier(
                    lines,
                    mor_start
                )

                # only process utterances that have mor info
                if mor_line is not None:

                    # split the mor tier into individual mor tokens
                    mor_tokens = mor_line.split()

                    for mor_token in mor_tokens:

                        extraction_tag = get_extraction_tag(
                            mor_token
                        )

                        if extraction_tag is not None:

                            data['file_name'].append(filename)
                            data['line_number'].append(line_number)
                            data['speaker'].append(speaker)
                            data['utterance'].append(utterance)
                            data['token'].append(mor_token)
                            data['tag'].append(extraction_tag)
                            data['readable_tag'].append(
                                get_readable_category(
                                    extraction_tag
                                )
                            )

                            # blank columns for human validation
                            data['is_correct_tag'].append('')
                            data['corrected_tag'].append('')

                    # jump past the mor tier
                    i = mor_end
                    continue

        i += 1

    return pd.DataFrame(data)

def save_results(df, output_file):
    df.to_excel(
        output_file,
        index=False,
        engine='xlsxwriter'
    )

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print(
            "Usage: python3 clan_mor.py "
            "<input_file> <output_file>"
        )
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # ensure the output file has an .xlsx extension
    if not output_file.endswith('.xlsx'):
        output_file += '.xlsx'

    df = process_clan_file(input_file)

    save_results(df, output_file)

    print(f"Extracted {len(df)} morphological tokens.")
    print(f"Saved results to: {output_file}")
