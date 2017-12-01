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

def find_starting_point(a):
	if a == "total":
		return find_total()
	elif a == "pop":
		return population()
	elif a == "in":
		return in_migration()
	elif a == "out":
		return out_migration()
	elif a == "net":
		return find_net()
	elif a == "rate":
		return find_rate()
	


def find_total():
	for i in range(row()):
		for j in range(column()):
			if contents[i][j]=="Total":
				return i

def population():
	for i in range(row()):
		for j in range(column()):
			if contents[i][j]=="Total population":
				return j

def in_migration():
	for i in range(row()):
		for j in range(column()):
			if contents[i][j]=="In-migration":
				return j
def out_migration():
	for i in range(row()):
		for j in range(column()):
			if contents[i][j]=="Out-migration":
				return j

def find_net():
	for i in range(row()):
		for j in range(column()):
			if contents[i][j]=="Net migration":
				return j

def find_rate():
	for i in range(row()):
		for j in range(column()):
			if contents[i][j]=="Rate of net migration\n(‰)":
				return j
	
	
	
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
		return False
	except ValueError:
		contents[row_index][column_index]=round(float(contents[row_index][column_index]),2)
		return True
#Converts whole page-data to their correct type.
def string_to_number():
	for i in range(row()):
		for j in range(column()):
			if is_number(i,j):
				make_number(i,j)
#Does the calculations for total population, total in-migration etc...
def total():
	for j in range(column()):
		if is_number(find_starting_point("total"),j):
			total=0
			for i in range(find_starting_point("total")+1,row()):
				if is_row_exists(i):
					total+=contents[i][j]
					
			contents[find_starting_point("total")][j]=total
#Does the calculations for net migrations of every provinces
def net_migration():
	for i in range(find_starting_point("total")+1,row()):
		if is_row_exists(i):
			contents[i][find_starting_point("net")]=contents[i][find_starting_point("in")]-contents[i][find_starting_point("out")]
#Does the calculations for the rate of net migrations of every provinces
def rate_of_net():
	for i in range(find_starting_point("total"),row()):
		if is_row_exists(i):
			contents[i][find_starting_point("rate")]=contents[i][find_starting_point("net")]/contents[i][find_starting_point("pop")]*1000
			contents[i][find_starting_point("rate")]=round(contents[i][find_starting_point("rate")],2)
		
#Does all calculations together
def calculate_the_cells():
	net_migration()
	total()
	rate_of_net()



string_to_number()
calculate_the_cells()
for j in range(find_rate(),column()):
	contents[find_total()][j]= round(contents[find_total()][j],2)



template="""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>%s</title>
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
        text-align: center;
        }
      .title{
        font-size:18px;
        color:#456FEA;
            }
    </style>
  </head>
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
	for j in reversed(range(column())):
		if contents[i][j]!="":
			if colspan==0:
				if i==0:
					if is_number(i,j):
						columns="        <th class=\"title\">"+"{:,}".format(contents[i][j])+"</th>\n"+columns
					else:
						columns="        <th class=\"title\">"+str(contents[i][j])+"</th>\n"+columns
				elif i<find_starting_point("total")+1:
					if is_number(i,j):
						columns="        <th>"+"{:,}".format(contents[i][j])+"</th>\n"+columns
					else:
						columns="        <th>"+str(contents[i][j])+"</th>\n"+columns
				else:
					if is_number(i,j):
						columns="        <td>"+"{:,}".format(contents[i][j])+"</td>\n"+columns
					else:
						columns="        <td>"+str(contents[i][j])+"</td>\n"+columns
			elif i==0:
				if is_number(i,j):
					columns="        <th class=\"title\" colspan=\""+str(colspan+1)+"\">"+"{:,}".format(contents[i][j])+"</th>\n"+columns
				else:
					columns="        <th class=\"title\" colspan=\""+str(colspan+1)+"\">"+str(contents[i][j])+"</th>\n"+columns
				colspan=0
			else:
				if is_number(i,j):
					columns="        <th colspan=\""+str(colspan+1)+"\">"+"{:,}".format(contents[i][j])+"</th>\n"+columns
				else:
					columns="        <th colspan=\""+str(colspan+1)+"\">"+str(contents[i][j])+"</th>\n"+columns
				colspan=0
		else:
			colspan+=1
			
			
	return columns
				
#	for j in range(column()):
#		
#		if contents[i][j]=="":
#			colspan+=1
#	for j in range(0,column()):
#		if colspan==0:
#			if i<4:
#				columns+="        <th>"+str(contents[i][j])+"</th>\n"
#			else:
#			    columns+="        <td>"+str(contents[i][j])+"</td>\n"
#			
#		else:
#			columns+="        <th class=\"title\" colspan=\""+str(colspan+1)+"\">"+str(contents[i][j])+"</th>\n"
#			break

def number_of_cities():
	count=0
	for i in range(find_starting_point("total")+1,row()):
		if is_row_exists(i):
			count+=1
	return count
def higher_than_2M():
	count=0
	for i in range(find_starting_point("total")+1,row()):
		if is_row_exists(i) and contents[i][find_starting_point("pop")]>=2000000:
			count+=1
	return count
def lower_than_200k():
	count=0
	for i in range(find_starting_point("total")+1,row()):
		if is_row_exists(i) and contents[i][find_starting_point("pop")]<=200000:
			count+=1
	return count
def average_population():
	
	average=contents[find_starting_point("total")][find_starting_point("pop")]//number_of_cities()
	return average
def avg_over_2M():
	sum=0
	for i in range(find_starting_point("total")+1,row()):
		if is_row_exists(i) and contents[i][find_starting_point("pop")]>=2000000:
			sum+=contents[i][find_starting_point("pop")]
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
		return columns%("Number of Cities","{:,}".format(number_of_cities()))
	elif i==1:
		return columns%("Number of Cities with population higher than 2M","{:,}".format(higher_than_2M()))
	elif i==2:
		return columns%("Number of Cities with population lower than 200k","{:,}".format(lower_than_200k()))
	elif i==3:
		return columns%("Average population of cities","{:,}".format(average_population()))
	elif i==4:
		return columns%("Average population of cities with population over 2M","{:,}".format(avg_over_2M()))
			
print(template %(title(),make_table(),summary_statistics%summary_table()))



		
