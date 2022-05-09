# Py CSV JSON Converter CLI App

CSV and JSON Converter CLI app build with [Python Fire library](https://github.com/google/python-fire)

CLI app included in distribution folder (dist/py-csv-json-cli.exe)

![](https://github.com/afif-dev/py-csv-json-cli/blob/main/py-csv-json-cli-ss.png)


## Basic Usage
1. Help
```
py py-csv-json-cli --
py py-csv-json-cli --help
* Note: close help with key 'q'
```
2. Covert CSV to JSON
```
py py-csv-json-cli csvtojson car-models.csv

* Note: example of csv file is car-models.csv 
```
3. Covert JSON to CSV
```
py py-csv-json-cli jsontocsv csvtojson-1652043963.json

* Note: example of json file is csvtojson-1652043963.json
```

## Setup for Local Development

1. Creating a virtual environment
```
py -m venv venv
```
2. Activate the environment
```
.\venv\Scripts\activate
```
3. Install all of the packages using requirements.txt
```
pip install -r requirements.txt
```
4. Run cli application 
```
py py-csv-json-cli.py
```
5. Build cli output (more refer to : https://pyinstaller.org/en/stable/usage.html)
```
pyinstaller py-csv-json-cli.spec
```
6. Export a list of all installed packages (Optional)
```
pip freeze > requirements.txt
```
7. Leaving the environment
```
deactivate
```

## Reference Links
- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
- https://docs.python.org/3/library/index.html
- https://docs.python.org/3/library/datetime.html
- https://docs.python.org/3/library/json.html
- https://docs.python.org/3/library/csv.html
- https://github.com/google/python-fire
- https://pyinstaller.org/en/stable/usage.html
- https://www.geeksforgeeks.org/convert-csv-to-json-using-python/
- https://www.geeksforgeeks.org/convert-json-to-csv-in-python/

