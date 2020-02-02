mkdir $1
cd $1
python ../readme_parser.py $1 > README.md
touch "p$1".py
