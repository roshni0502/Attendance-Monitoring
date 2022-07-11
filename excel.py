import csv 
import pandas as pd   
# field names 
fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    
# data rows of csv file 
rows = [ ['Nikhil', 'COE', '2', '9.0'], 
         ['Sanchit', 'COE', '2', '9.1'], 
         ['Aditya', 'IT', '2', '9.3'], 
         ['Sagar', 'SE', '1', '9.5'], 
         ['Prateek', 'MCE', '3', '7.8'], 
         ['Sahil', 'EP', '2', '9.1']] 
    
# name of csv file 
filename = "university_records.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)


df = pd.read_csv (f'{filename}')
#df.to_csv('/path/to/file.csv')
#print (df)
from smart_open import open 
with open(f'{filename}', 'w') as fout: 
   for line in open(f'{filename}', 'r'): 
 
      fout.write(line) 