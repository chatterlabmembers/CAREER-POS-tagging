# CAREER POS Tagging File Prep Workflow

The following steps walk you through how to convert transcribed .eaf files to .xlsx files that are ready for human validation of CLAN's automatic POS tags.

## part 1: .eaf to .cha conversion

1.  Download [CLAN](https://dali.talkbank.org/clan/) via CHILDES.
2.  Have all .eaf files to be analyzed saved locally on your device in one folder.
3.  Open CLAN, locate "working" and set the directory to where all .eaf files are stored.
4.  In the command console, type command `elan2chat @`. This will trigger a "File In" button. Click on the "File In" button and select all .eaf files to be converted to .cha files.
5.  Run the command in step 4. The output .cha files should be saved in the same directory as all input .eaf files.

## part 2: clean up .cha outputs

1.  Keep all output .cha files from **part 1** in one folder.
2.  Run `clean_cha_tiers.py` script on all output .cha files to remove all speaker tiers that do not fit the 3-character speaker tiers format (as indicated by \* at the beginning of each line).
    - NOTE: Speaker tiers that do *not* follow 3-character format cause CLAN's morphology processing to crash.

## part 3: adding %mor tier in .cha files

1.  Keep all cleaned .cha files in one folder.
2.  Open CLAN, locate "working" and set the directory to where all cleaned .cha files are stored.
3.  In the command console, type command `mor @`. This will trigger a "File In" button. Click on the "File In" button and select all *and only all* cleaned .cha files to be tagged for word morphology.
4.  Once CLAN finishes processing all .cha files, it outputs an .ulx.cex file that documents all tokens the `mor @` function did not recognize.
    - NOTE: Most of the times, the tokens that go unrecognized are 1) any incomplete speech indicated by hyphens, 2) noun phrases connected via underscores, 3) select compound nouns, and 4) any misspelled tokens. These unrecognized tokens' tag shows up as a question mark — you may want to do a screening of those tokens to make sure there aren't any systematic errors.
5.  Need help navigating CLAN? Check out a somewhat outdated but beginner-friendly guide written by speech pathologists (thus primarily serving the speech pathology community) on using CLAN [here](https://hesp.umd.edu/sites/hesp.umd.edu/files/SLPCLANGuide_August2015_Final.pdf).

## part 4: .cha to .xlsx conversion

1.  Run `cha2xlsx.py` script on all morphology-tagged .cha files. This script should extract all tokens of our study's interests from the .cha files and input them in the output .xlsx files, along with associated identifying information (e.g., file name, line number, timestamp, etc.).
    - This script will extract all tokens that the `mor @` function did not recognize in **part 3** (i.e., any tokens with a morphological tag of a question mark) so human validators can assign the correct morphological tags to the unrecognized tokens.
    - This script also looks for embedded morphological tags documented [here](https://uchicago.app.box.com/file/2360514577838) (see pp.5-7 for details). Need access to view the document? Contact the Lab Manager for access!
