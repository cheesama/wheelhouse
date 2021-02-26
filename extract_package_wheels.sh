#sh ./extract_package_wheels.sh package_name
pip install pipdeptree
pipdeptree --package $1 -f > $1_req.txt
pip wheel -w $1_wheels -r $1_req.txt
rm $1_req.txt
