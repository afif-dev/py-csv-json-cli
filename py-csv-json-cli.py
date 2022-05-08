import fire   

class ConvertCsvJson(object):

    def __init__(self):
        import datetime

        curr_dt = datetime.datetime.now()
        self._timestamp = int(round(curr_dt.timestamp()))
    

    def jsontocsv(self,jsonFilePath):
        import csv
        import json

        if not jsonFilePath.endswith('.json'):
            return "Error: Invalid JSON file!"

        csvOutputFile = "jsontocsv-{timestamp}.csv".format(timestamp=self._timestamp)
        
        with open(jsonFilePath) as jsonf:
            jsondata = json.load(jsonf)
        
        data_file = open(csvOutputFile, 'w', newline='')
        csv_writer = csv.writer(data_file)
        
        count = 0
        for data in jsondata:
            
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(data.values())
        
        data_file.close()

        return "Successfully created {output}".format(output=csvOutputFile)


    def csvtojson(self,csvFilePath):
        import csv
        import json
        
        if not csvFilePath.endswith('.csv'):
            return "Error: Invalid CSV file!"
        
        jsonOutputFile = "csvtojson-{timestamp}.json".format(timestamp=self._timestamp)
        data = []

        with open(csvFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
            for rows in csvReader:
                data.append(rows)

        with open(jsonOutputFile, 'a', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))

        return "Successfully created {output}".format(output=jsonOutputFile)


if __name__ == '__main__':
  fire.Fire(ConvertCsvJson)
