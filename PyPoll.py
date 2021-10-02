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

#1.Initialize total votes counter
total_votes = 0

#Candidate options
candidate_options = []

#Declaring an empty dictionary for candidate votes:
candidate_votes = {}

#Declaring the winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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

    #Read & print the header row.
    headers = next(file_reader)
    #print(headers)

#print each row in the CSV file.
    for row in file_reader:
        #2. Add to the total vote count.
        total_votes += 1

        #Print the candidate name from each row.
        candidate_name = row[2]

        #if the candidate does not match any exiting candidate... using "if ... not in" statement 
        if candidate_name not in candidate_options:   

            #Add the candidate name to the candidate list/options.
            candidate_options.append(candidate_name)

            #Begin tracking the candidate's vote count
            candidate_votes[candidate_name] = 0          

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1  

    #Determine the % of votes for each candidate by looping thru the counts
    #1. Iterate through the candidate list. 
    for candidate_name in candidate_votes:
        #2 Retrieve vote cont of a candidate. candidate_votes[candidate_name] is calling for the values
        #candidate_name is the key in the candidate_votes dictionary. therefore votes = the candidate_name value
        votes = candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        #vote_percentage is a new variable taking votes/total votes (**where did total votes come from)
        vote_percentage = float(votes) / float(total_votes) * 100 
        #print the candidate name and percentage of votes.
        #pringt out the candidate name (need to make sure there is a : or it won't work. )
        #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote")

        #Determine if the vote count is greater than the winning_count
        #1. If the vote count is > winning_count and percentage is > winning_percentage 
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            #2. set the winning_count = votes and set winning_percentage = vote_percentage 
            winning_count = votes
            winning_percentage = vote_percentage 

            #3. set the winning_count = candidate_name in the for loop
            winning_candidate = candidate_name
        #Print out each candidate's name, vote count, & percentage of votes to the terminal
        ##need to make sure that this is in line with the if statement or else it will not print everything
        ##prints out the value for the candidate_name and the vote_percentage to 1 decimal place
        ##and votes, separating each candidate by a new line \n
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    ##how does this know which one has the highest score already
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")
    print(winning_candidate_summary)


#3. Print the total votes.
#print(total_votes)

#print the candidate list.
#print(candidate_options)

#print the candidate vote dictionary 
#print(candidate_votes)

#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received 
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#Close the file. Close the file is not needed when using a with statement to open the file
#election_data.close()
#outfile.close()
