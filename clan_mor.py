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
        'v': 'verb'
    }
    base_tag = tag.split('-')[0]
    return clan_categories.get(base_tag, tag)

def process_clan_file(input_file):
    """ 
    Reads a .cha file, extracts morphological analyses, and writes results to an Excel file
    with columns: original file name, speaker, full utterance, token, tag
    """
    filename = os.path.basename(input_file)
    
    with open(input_file, 'r', encoding='utf-8') as cha_f:
        lines = cha_f.readlines()
    
    # Data to store in the Excel file
    data = {
        'file_name': [],
        'line_number': [],
        'speaker': [],
        'utterance': [],
        'token': [],
        'tag': [],
        'readable_tag': []
    }
    
    i = 0
    while i < len(lines):
        # Check for speaker utterance lines
        if lines[i].startswith('*'):
            speaker = lines[i][1:4]  # Extract speaker ID
            
            if speaker != "CAR": # Non-speaker rows excluded
                # Extract the full utterance (remove speaker code, timestamp, and clean up)
                utterance_parts = lines[i].split('%snd:')[0].strip()
                utterance = utterance_parts[5:].strip()  # Remove '*XXX:' prefix
                
                # Look for corresponding morphological analysis
                if i + 1 < len(lines) and lines[i + 1].startswith('%mor:'):
                    mor_line = lines[i + 1][6:].strip()  # Remove '%mor:' prefix
                    
                    # Handle multi-line morphological analyses
                    j = i + 2
                    while j < len(lines) and lines[j].startswith('\t'):
                        mor_line += ' ' + lines[j].strip()
                        j += 1
                    
                    # Process morphological tokens
                    mor_tokens = mor_line.split()
                    for mor_token in mor_tokens:
                        # Split token into word and tag
                        # "tag|word", others would be punctuations, not coded so skip
                        if '|' in mor_token:
                            tag, word = mor_token.split('|', 1)
                            readable_tag = get_readable_category(tag)
                        
                            # Add data to our dictionary
                            data['file_name'].append(filename)
                            data['line_number'].append(i + 1)
                            data['speaker'].append(speaker)
                            data['utterance'].append(utterance)
                            data['token'].append(word)
                            data['tag'].append(tag)
                            data['readable_tag'].append(readable_tag)
            
        i += 1
    
    # Create and return dataframe
    df = pd.DataFrame(data)
    return df

def extract_nouns_verbs(df, output_file):
    NOUN_VERB_TAGS = {"n", "n:prop", "n:let", "n:pt", "v", "aux", "mod"}
    df_nouns_verbs = df[df["tag"].isin(NOUN_VERB_TAGS)]
    df_nouns_verbs.to_excel(output_file, engine='xlsxwriter')

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 clan_mor.py <input_file> <output_file>")
        sys.exit(1)
    
    # Ensure output file has .xlsx extension
    output_file = sys.argv[2]
    if not output_file.endswith('.xlsx'):
        output_file += '.xlsx'
    
    df = process_clan_file(sys.argv[1])
    extract_nouns_verbs(df, output_file)