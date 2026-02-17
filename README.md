# CAREER-POS-tagging

## Manual POS tagging workflow

1. In [CAREER POS tagging > coding](https://uchicago.app.box.com/folder/314794154399) folder, open [CAREER manual POS file tracker](https://uchicago.app.box.com/file/2137948527819) spreadsheet.
  
2. Locate and open the associated .xlsx file (under `File URL` column) you last worked on or the next un-tagged file. If you are starting on a fresh file, add your initials to `Annotator` and today's date to `First date worked on` columns.
   
3. For each utterance in the .xlsx file:

   - Identify all nouns (including proper nouns) and verbs present.  
   - Enter each token exactly as it appears in the **`token`** column.
   - *Double check your spelling.*
   - Provide the appropriate **tag** in the corresponding column. The tags that we are using in the current workflow are 1. noun (n), 2. proper noun (n:prop), 3. plural noun (n:pt), 4. letter noun (n:let), 5. verb (v), 6. auxiliary verb (aux), and 7. modal verb (mod). See [CLAN morphology tags](https://uchicago.app.box.com/file/1781179507108) for the full list of morphological tags.
     - For some tricky cases of noun and verb tags, see [Noun/verb special cases guide](https://uchicago.app.box.com/file/2080581254184) for examples (note that bullet point 5 is irrelevant to this workflow).
   - If an utterance doesn't contain any nouns or verbs, input "0" in the last two columns. **Never leave a cell empty!**
   
4. If multiple nouns or verbs occur in a single utterance:

   - Add an additional row for each extra token (e.g., if there are 4 total nouns and verbs in one utterance, you need to add 3 additional rows below the original row).
   - In the additional row(s), copy over the first three columns (`file_name`, `speaker`, `utterance`) from the original row.
   - **You should never edit the contents in the first three columns, only copy and paste contents when needed!**

5. Repeat steps 3 & 4 until you have finished a .xlsx file. When finished, go back to the [CAREER manual POS file tracker](https://uchicago.app.box.com/file/2137948527819) spreadsheet and add today's date to `Last date worked on` column.

## Human validation of CLAN POS tagging workflow
