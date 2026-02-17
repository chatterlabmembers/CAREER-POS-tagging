# Running CLAN POS tagger for human validation

### exporting .eaf files as .cha files with CLAN
1. have .eaf files in a directory
2. set "working" on command window for clan to the directory
3. from clan, run `elan2chat @` to create .cha files for all .eaf files in the same directory

### adding %mor tier with CLAN
1. have .cha files in a directory
2. set “working” on command window for clan to the directory
3. from clan, file —> get mor grammar —> English
4. run “mor *.cha” to run MOR, POST, POSMORTEM, and MEGRASP in sequence —> adds %mor and %gra to files

## clean_cha_file.py
### correcting for cut-offs with - not getting recognized
- USE: python3 clean_cha_file.py cha cleaned_cha
- NOTE: have cha files in `eafs_cha` directory first
- OUTPUT: iterates through cha files and removes word-final dashes; saves output in `cleaned_cha` folder

## clan_mor.py
### getting cha file to a readable form with tags
- INPUT: takes a .cha file as input
    - have to add %mor tier first
- NOTES: finds the %mor lines and corresponding speaker; output is in chronological order
- OUTPUT: file_name  line_number speaker utterance   token   tag readable_tag    correct_tag corrected_tag
- sample output lines:

`COU_DI46_030001_10800000_11100000_random-20.cha	18	CHI	I want to xxx . 	want	v	verb`
`COU_DI46_030001_10800000_11100000_random-20.cha	21	MA1	it's not in there Bud . 	there	n	noun`
