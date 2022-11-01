import csv

#def get_highest_gdp(data, year):`  
 # This function will return the name of the state had the highest GDP for a specified year. It takes in a string `year` as an argument. `data` will be a `DictReader` object containing data.  

#`def get_lowest_gdp(data, year):`  
 # This function will return the name of the state had the lowest GDP for a specified year. It takes in a string `year` as an argument. `data` will be a `DictReader` object containing data.  

#def get_state_gdp(data, state, year):`  
 # This function will return gdp value of some specific state for some specific year column. The name of the state will be passed in `state`, and the year will be passed in via `year`.

def get_highest_gdp(data, year):
    state=data[0]["GeoName"]
    max_gdp=float(data[0][year])
    
    for row in data:
        val=float(row[year])
        if val>max_gdp:
            max_gdp=val
            state=row["GeoName"]
    return state

def get_lowest_gdp(data, year):
    state=data[0]["GeoName"]
    min_gdp=float(data[0][year])
    
    for row in data:
        val=float(row[year])
        if val<min_gdp:
            min_gdp=val
            state=row["GeoName"]
    return state

def get_state_gdp(data, state, year):
    for row in data:
        if state==row["GeoName"]:
            return row[year]

#this appends all rows as dictionaries to list_data
# save each row into a list (TODO: change to your path!)
list_data = []
with open("state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)


highest=get_highest_gdp(list_data, '2020')
lowest=get_lowest_gdp(list_data, '2020')

print(highest,lowest)

prev = get_state_gdp(list_data, "New York", "2019")
new = get_state_gdp(list_data, "New York", "2020")

#print(prev,new)
print(float(new) - float(prev))