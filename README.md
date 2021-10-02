# **Election Analysis**

## **Overview of Election Audit**
The purpose of this election audit analysis was to read through a large set of data using python to create a clearer picture of who won the election in Colorado. 

## **Election-Audit Results** 
An overview of the election results can be found [here](https://github.com/tutran90/Election_Analysis/blob/main/analysis/election_analysis.txt).

- **How many votes were cast in this congressional election?**

    - There was a total of 369,711 votes in this congressional election. In order to find the total number of votes, the csv file had to be opened and read using python. A code was then created to tell the system to read through the headers in the. The following code can be found [here](https://github.com/tutran90/Election_Analysis/blob/main/PyPoll_Challenge.py) from lines 35-90.

- **A  breakdown of the number of votes and the percentage of total votes for each county in the precint:**

    - County votes was summarized by county name in the following [file](https://github.com/tutran90/Election_Analysis/blob/main/analysis/election_analysis.txt) from lines 7-10. 

    - A breakdown of this code can be found in the [python](https://github.com/tutran90/Election_Analysis/blob/main/PyPoll_Challenge.py) document from lines 97-107. Basically, a code was created to loop through the columns and count the total number of votes. 
    
- **Which county had the largest number of votes?** 

    - Denver County had a total of 306,055 votes which was 82.8% of total votes; making it the county with the largest number of votes. A summary of the number of votes & percentages per county can be found [here](https://github.com/tutran90/Election_Analysis/blob/main/analysis/election_analysis.txt) from lines 7-10.

- **A breakdown of the number of votes and the percentage of the total votes each candidate received**

    - In order to find the number of votes for each candidate followed by the percentage from the total votes. The candidates were first itereated to see exactly how many candidates were in the large file. 

    - Second, based on the candidates' name that would appear on the file, a code was created to continue the count of each vote that appeared with the corresponding name.

    - Third, this number was then divided by the total number of votes (which is 369,711) then multiplied by 100 to get the percentage. 
    - The code can be viewed [here](https://github.com/tutran90/Election_Analysis/blob/main/PyPoll_Challenge.py) from lines 42-154.

- **Summary of the winning candidate:**
    - The winning candidate of this election was Diana DeGette who has a total of 272, 892 votes, which was 73.8% of the total votes. A summary of each candidate election results can be found [here](https://github.com/tutran90/Election_Analysis/blob/main/analysis/election_analysis.txt) from lines 14-16

## **Election-Audit Summary**

-   Overall, if one were to analyze the results using Excel, it would take quite some time to decifer through a large set of data. Python, definitely is superior when trying to analyze a large set of data without having to create multiple pivot tables, charts, etc. in order to obtain the same information.

- This script could be helpful for future candidates and their election campagins. For example, the script could be modified to find out what the total number of registered voters are and population for that county. Some counties may carry more votes since there is a higher population rate. In this case, we don't have enough information to make this conclusion, but Denver could have a higher population compared to Arapahoe and Jefferson. It would definitely be benefical to know this so one could plan where they should focus more. 

- The script could also be modified to show the dominating party in a certain county. If this data was collected, we could break down the count to see how many republicans or democrats voted for certain candidates. This would also tie in with the first example, finding out which county is heavily populated with would be a factor to pay attention to for any future campaings. 