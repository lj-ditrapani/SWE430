# Run with sh zip_website.sh
name="swe430.zip"
rm -f ${name}
cd website
zip -r ../${name} .
