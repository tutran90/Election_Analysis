#The data we need to retrieve
#Assign a variable for the file to load and the path: CSV file is located in the Election_Analysis folder, direct path:
#file_to_load = "election_results.csv"
#indirect path to load 
#Add our dependencies
import csv
import os 

#assign a varialbe to load a file from a path
file_to_load = os.path.join('election_results.csv')
#Create a filename variable to driect or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file
#election_data = open(file_to_load, 'r') one way to open and read the file with open() and close()
with open(file_to_load) as election_data:

#To Do: perform analysis
    #print(election_data)

#using the open() function wit the "w" mode we will write data to the file. We created a folder "analysis" and now there is a txt file created in it
#open(file_to_save, "w")

#using the with statement open file as a text file.
#outfile = open(file_to_save, "w")
#using the "with" statement instead of open/close()
#with open(file_to_save, "w") as txt_file:
#write some data to the file.
#outfile.write("Hello World")
#txt_file.write("Hello World")

    #To do: read & analyze the data here.
    file_reader = csv.reader(election_data)

    #print the header row.
    headers = next(file_reader)
    print(headers)

#print each row in the CSV file.
    #for row in file_reader:
    #    print(row)

#write 3 counties to the file. there are no spaces if it is written this way. 
#to have spaces, need to add a comma and a space
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson")
#to add all three counties to one line: will have the same output as the previous one all on one line
    #txt_file.write("Arapahoe, Denver, Jefferson")
#to write each county line on a separate line, add the "newline escape" sequence to the end of each county name
#\n<name>, to add a line of dashes between the headers use \n after the title then use print('-'*#)
    #txt_file.write("Counties in the Election\n")
    #txt_file.write('-'*80)
    #txt_file.write("\nArapahoe\nDenver\nJefferson")

#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received 
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#Close the file. Close the file is not needed when using a with statement to open the file
#election_data.close()
#outfile.close()
