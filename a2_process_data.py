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

#print(contents)
#print(contents[0])
#print(contents[0][0])
#print(type(contents))
#print(type(contents[0]))
#print(type(contents[0][0]))
#print(contents[10][1])
#print(type(contents[10][1]))
#print(contents[2][0])
#The following part evaluates the total population.
i=total_population=0
while(True):
    try:
        next=contents[i+4][1]
        total_population+=int(next)
        i+=1
    except IndexError:
        break
#print("Total population is:",total_population)
#The following part counts the number of cities
#with population over 2 million and list them.
cities=[]
i=4
count=0
while(True):
    try:
        if int(contents[i][1])>=2000000:
            cities+=[contents[i][0]]
            count+=1
        i+=1
    except IndexError:
        break
#print("Number of cities with population higher than 2M:",count)
#print("These cities are:",*cities)
#Try to calculate a mean average 
#of some variables and save the result in a variable.
i=4
sum=count_2=0
while(True):
    try:
        if int(contents[i][1])>=2000000:
            sum+=int(contents[i][1])
            count_2+=1
        i+=1
    except IndexError:
        break
average=sum//count_2
#Print the variables that you have saved.
#print("Average population of cities with population over 2M is:",average)
#See what happens if you try to print variables 
#that don't exist, such as contents["chickenchicken"].
#print(contents["cdf"])
#This is a TypeError because list indices must be integers or slices
#not string!
#print(contents[5161][46546])
#This is an IndexError because list index is out of range.

#Concatenate some of the strings and print the result.
#print("My name is"+" Şahin Akkaya")
#See what happens when you try to concatenate a number and a string.
#age=18
#print("My name is"+" Şahin Akkaya. I'm "+age)
#This is a TypeError.

#See what happens when you try to multiply a number with a string.
#print("Aşkım seni ç"+"o"*3+"k seviyorum :)")

#Print the types of the results of these calculations.
#print(type(average))
#print(type(count))
#print(type(":)"))

#Run the help() function on some of the variables you have created.
#help(average)

#STEP 3
#Output HTML from your Python program


#print("-----------------------------------------------------------")
#print("This assignment (assignment 2) almost has been finished.")
#print("But all it can do is calculating some stupid things that you would never want to use:")
#print("Cell at index 0,0:")
#print(contents[0][0]+" (... But who cares?)")
#print("Type of the index at 0,1:")
#print(type(contents[0][1])," (... Still doesn't make any sense.)")
#print("HTML output for the calculated values"+"  (... Wait, what?? Are you serious?",end=" ")
#print("I must confess... I'm really impressed now! Let's see then :) )",end="\n\n")
templete="""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf­8">
    <title>%s</title>
    </head>
  <body>
    <p>Total population is:%d</p>
    <p>Number of cities with population higher than 2M:%d</p>
    <p>These cities are: %s</p>
    <p>Average population of cities with population over 2M is: %d</p>
  </body>
</html>
"""
title="Turkey Population Analysis"
print(templete %(title,total_population,count,cities,average))
