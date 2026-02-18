# CAREER-POS-tagging

## Brief overview

This project supports analyses of noun and verb distributions in the CAREER corpus. To ensure accuracy in part-of-speech (POS) classification, we are using two complementary workflows:

1. Human validation of CLAN’s automated POS tagging across the full corpus.
2. Manual POS tagging of a subset of files.

The first workflow evaluates the accuracy of CLAN’s automated token recognition and morphological tagging processes. The second workflow provides a reliability check on the number of missed tokens that should have been tagged by CLAN’s automated process. Together, these procedures allow us to quantify tagging accuracy and reliability for downstream analyses.

### What’s here

This document contains:

1. Step-by-step instructions for **human validation of CLAN POS tagging**
2. Step-by-step instructions for **manual POS tagging**
3. Links to all relevant trackers and reference guides

Follow the appropriate workflow depending on which phase of the project you are assigned to.

## Human validation of CLAN POS tagging workflow

1. In [CAREER POS tagging > coding](https://uchicago.app.box.com/folder/314794154399) folder, open [CAREER POS tagging file tracker](https://uchicago.app.box.com/file/1822376572544) spreadsheet.
  
2. Locate and open the associated .xlsx file (under `Tagged tokens URL` column) you last worked on or the next un-tagged file. If you are starting on a fresh file, add your initials to `Annotator` and today's date to `First date worked on` columns.

3. In the .xlsx file, most columns are pre-filled. The two columns that you will be filling out are `is_correct_tag` and `corrected_tag`.

4. For each token tagged in the .xlsx file:

   - Determine if the `tag` produced by the automated process is correct by using context clues and reading the full utterance in the `utterance` column. If correct, input "y" in `is_correct_tag` column and "0" or leave empty in `corrected_tag` column.
   - If `tag` is not correct, input "n" in `is_correct_tag` column and the correct tag shorthand in `corrected_tag` column. The tags that we are using in the current workflow are 1. noun (n), 2. proper noun (n:prop), 3. plural noun (n:pt), 4. letter noun (n:let), 5. verb (v), 6. auxiliary verb (aux), and 7. modal verb (mod). See [CLAN morphology tags](https://uchicago.app.box.com/file/1781179507108) for the full list of morphological tags.
     - For some tricky cases of noun and verb tags, see [Noun/verb special cases guide](https://uchicago.app.box.com/file/2080581254184) for examples.
   - In the case that the correct morphological tag of a token cannot be inferred from context clues, input "u" in in `is_correct_tag` column and "0" or leave empty in `corrected_tag` column. **Please use this option sparingly!**
   - *Double check your spelling.*

5. Work through the entire .xlsx file via step 4. When finished, go back to the [CAREER POS tagging file tracker](https://uchicago.app.box.com/file/1822376572544) spreadsheet and add today's date to `Last date worked on` column. Add comments if needed.

## Manual POS tagging workflow

1. In [CAREER POS tagging > coding](https://uchicago.app.box.com/folder/314794154399) folder, open [CAREER manual POS file tracker](https://uchicago.app.box.com/file/2137948527819) spreadsheet.
  
2. Locate and open the associated .xlsx file (under `File URL` column) you last worked on or the next un-tagged file. If you are starting on a fresh file, add your initials to `Annotator` and today's date to `First date worked on` columns.
   
3. For each utterance in the .xlsx file:

   - Identify all nouns (including proper nouns) and verbs present.  
   - In the `token` column, enter each token exactly as it appears in the original utterance.
   - *Double check your spelling.*
   - Provide the appropriate **tag** in the corresponding `tag` column. The tags that we are using in the current workflow are 1. noun (n), 2. proper noun (n:prop), 3. plural noun (n:pt), 4. letter noun (n:let), 5. verb (v), 6. auxiliary verb (aux), and 7. modal verb (mod). See [CLAN morphology tags](https://uchicago.app.box.com/file/1781179507108) for the full list of morphological tags.
     - For some tricky cases of noun and verb tags, see [Noun/verb special cases guide](https://uchicago.app.box.com/file/2080581254184) for examples (note that bullet point 5 is irrelevant to this workflow).
   - If an utterance doesn't contain any nouns or verbs, input "0" in the last two columns. **Never leave a cell empty!**
   
4. If multiple nouns or verbs occur in a single utterance:

   - Add an additional row for each extra token (e.g., if there are 4 total nouns and verbs in one utterance, you need to add 3 additional rows below the original row).
   - In the additional row(s), copy over the first three columns (`file_name`, `speaker`, `utterance`) from the original row.
   - **You should never edit the contents in the first three columns, only copy and paste contents when needed!**

5. Repeat steps 3 & 4 until you have finished a .xlsx file. When finished, go back to the [CAREER manual POS file tracker](https://uchicago.app.box.com/file/2137948527819) spreadsheet and add today's date to `Last date worked on` column.
