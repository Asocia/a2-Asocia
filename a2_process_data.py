#######################################################
### Please ignore the lines of code in this section.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do not need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################
#Counts and returns number of columns
def column():
	count=i=0
	while (True):
		try:
			column=contents[0][i]
			count+=1
			i+=1
		except IndexError:
			return count
#Counts and returns number of rows
def row():
	count=i=0
	while (True):
		try:
			column=contents[i][0]
			count+=1
			i+=1
		except IndexError:
			return count
#Checks whether the row is empty
def is_row_exists(row_index):
	for i in range(column()):
		if contents[row_index][i]=="":
			continue
		return True
	return False
#Checks whether the cell is real number
def is_number(row_index,column_index):
	try:
		float(contents[row_index][column_index])
		return True
	except ValueError:
		return False
#Converts the string to an integer or a floating number
def make_number(row_index,column_index):
	try:
		contents[row_index][column_index]=int(contents[row_index][column_index])
	except ValueError:
		contents[row_index][column_index]=float(contents[row_index][column_index])
#Converts whole page-data to their correct type.
def string_to_number():
	for i in range(row()):
		for j in range(column()):
			if is_number(i,j):
				make_number(i,j)
#Does the calculations for total population, total in-migration etc...
def total():
	for j in range(column()):
		if is_number(3,j):
			total=0
			for i in range(4,row()):
				total+=contents[i][j]
			contents[3][j]=total
#Does the calculations for net migrations of every provinces
def net_migration():
	for i in range(4,row()):
		contents[i][4]=contents[i][2]-contents[i][3]
#Does the calculations for the rate of net migrations of every provinces
def rate_of_net():
	for i in range(3,row()):
		contents[i][5]=contents[i][4]/contents[i][1]*1000
		contents[i][5]=round(contents[i][5],2)
#Does all calculations together
def calculate_the_cells():
	net_migration()
	total()
	rate_of_net()

string_to_number()
calculate_the_cells()
template="""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>%s</title>
  </head>
  <style>
    body{
      font-family:Calibri, sans-serif;
      background-color:azure;
        }
    th{
      font-size:18px;
      color:#000000;
      
      }
    table, tr,th,td{
      border: 2px solid;
      border-color: blue;
      border-collapse:collapse;
      padding:4px 5px 4px 4px;
      }
    .title{
      font-size:18px;
      color:#456FEA;
          }
  </style>
  <body>
    %s
    %s
  </body>
</html>
"""
def title():
	return "Turkey Population Analysis"

def make_table():
	return "<table>\n"+make_row()+"\n    </table>"
def make_row():
	rows=""
	for i in range(row()):
		if is_row_exists(i):
			rows+="      <tr>\n"+make_column(i)+"      </tr>\n"
	return rows
def make_column(i):
	columns=""
	colspan=0
	for j in range(column()):
		
		if contents[i][j]=="":
			colspan+=1
	for j in range(0,column()):
		if colspan==0:
			if i<4:
				columns+="        <th>"+str(contents[i][j])+"</th>\n"
			else:
			    columns+="        <td>"+str(contents[i][j])+"</td>\n"
			
		else:
			columns+="        <th class=\"title\" colspan=\""+str(colspan+1)+"\">"+str(contents[i][j])+"</th>\n"
			break
	return columns
def number_of_cities():
	count=0
	for i in range(4,row()):
		count+=1
	return count
def higher_than_2M():
	count=0
	for i in range(4,row()):
		if contents[i][1]>=2000000:
			count+=1
	return count
def lower_than_200k():
	count=0
	for i in range(4,row()):
		if contents[i][1]<=200000:
			count+=1
	return count
def average_population():
	average=contents[3][1]//number_of_cities()
	return average
def avg_over_2M():
	sum=0
	for i in range(4,row()):
		if contents[i][1]>=2000000:
			sum+=contents[i][1]
	average=sum//higher_than_2M()
	return average
summary_statistics="""
%s
"""
def summary_table():
	return "    <br><br>\n    <table>\n"+summary_rows()+"    </table>"
def summary_rows():
	rows=""
	for i in range(5):
		rows+="      <tr>\n"+summary_columns(i)+"      </tr>\n"
	return rows
def summary_columns(i):
	columns=""
	for j in range(2):
		columns+="        <td>%s\n        </td>\n"
	if i==0:
		return columns%("Number of Cities",str(number_of_cities()))
	elif i==1:
		return columns%("Number of Cities with population higher than 2M",str(higher_than_2M()))
	elif i==2:
		return columns%("Number of Cities with population lower than 200k",str(lower_than_200k()))
	elif i==3:
		return columns%("Average population of cities",str(average_population()))
	elif i==4:
		return columns%("Average population of cities with population over 2M",str(avg_over_2M()))
			

print(template %(title(),make_table(),summary_statistics%summary_table()))



		
