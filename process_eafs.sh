# ensure necessary directories exist
mkdir -p clan_output cleaned_cha eafs_cha

# get rid of cut-off hyphens in cha files
python3 clean_cha_file.py eafs_cha cleaned_cha

# run clan_mor.py on the cleaned .cha files
for file in cleaned_cha/*.cha; do
    filename=$(basename -- "$file" .cha)
    echo "Running clan_mor.py on $file"
    python3 clan_mor.py "$file" "clan_output/${filename}-clan.txt"
done