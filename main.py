###Read and open CSV files using pandas###
#Import Modules 
import os
import pandas as pd

#set path for file
PyBankCSV = os.path.join("PyBank", "Resources", "budget_data.csv")
PyPollCSV = os.path.join("PyPoll", "Resources", "election_data.csv")

#Read CSV files
PyBankCSVfile = pd.read_csv(PyBankCSV)
PyPollCSVfile = pd.read_csv(PyPollCSV)

#Print CSV files
print(PyBankCSVfile)
print(PyPollCSVfile)

###Pybank Analysis###
#Calculate total number of monts icluded in the dataset for PyBank 
TotalMonths = PyBankCSVfile["Date"].count()
print("Total Months:" + str(TotalMonths))

#Calculate the net total amout of "Profit/Losses" over the entier period for PyBank 
TotalPL = PyBankCSVfile["Profit/Losses"].sum()
print("Total: $" + str(TotalPL))

#Calculate changes in "Profit/Losses" over the entire period, and then the average of those changes 
AvgChange = PyBankCSVfile["Profit/Losses"].mean()
print("Average Change: $" + str(AvgChange))

#Calculate The greatest increase/Decrease in profits (date and amount) over the entire period for PyBank
GreatestIncrease = PyBankCSVfile["Profit/Losses"].max()
GreatestDecrease = PyBankCSVfile["Profit/Losses"].min()

print("Greatest Increase in Profits:" + str(GreatestIncrease))
print("Greatest Decrease in Profits:" + str(GreatestDecrease))

#Export PyPoll text file with the results
output_path_PyPoll = os.path.join("PyPoll", "Resources", "PyPoll_Analysis.txt")
with open(output_path_PyPoll, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Total Months: " + str(TotalMonths) + "\n")
    txtfile.write("Total: $" + str(TotalPL) + "\n")
    txtfile.write("Average Change: $" + str(AvgChange) + "\n")
    txtfile.write("Greatest Increase in Profits:" + str(GreatestIncrease) + "\n")
    txtfile.write("Greatest Decrease in Profits:" + str(GreatestDecrease) + "\n")

#Seperate the projects 
print("##########################")

###PyPoll Analysis###
#Calulate the total number of votes cast and print header
TotalVotes = PyPollCSVfile["Ballot ID"].count()
print("Ekection Results")
print("-------------------------")
print("Total Votes:" + str(TotalVotes))

#Make a complete list of candidates who received votes
CanadidateList = PyPollCSVfile["Candidate"].unique()

#Calculate the total number of votes each candidate won
CharlesCasperStockhamCount = PyPollCSVfile["Candidate"].value_counts()["Charles Casper Stockham"]
DianaDeGetteCount = PyPollCSVfile["Candidate"].value_counts()["Diana DeGette"]
RaymonAnthonyDoaneCount = PyPollCSVfile["Candidate"].value_counts()["Raymon Anthony Doane"]

#Calculate the percentage of votes each candidate won
CCSPercent = (CharlesCasperStockhamCount/TotalVotes)*100
DDGPercent = (DianaDeGetteCount/TotalVotes)*100
RADPercent = (RaymonAnthonyDoaneCount/TotalVotes)*100

#Calculate the winner of the election based on popular vote
Winner = PyPollCSVfile["Candidate"].value_counts().idxmax()

#Create a Dictionary to display the results
VoteDict = {"Candidate": ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"],
            "Percent of Votes": [CCSPercent, DDGPercent, RADPercent],
            "Total Votes": [CharlesCasperStockhamCount, DianaDeGetteCount, RaymonAnthonyDoaneCount]}

#Convert the dictionary to a DataFrame
VoteDF = pd.DataFrame(VoteDict)

#Apply formatting, print the DataFrame and winner 
VoteDF["Percent of Votes"] = VoteDF["Percent of Votes"].apply(lambda x: "{:.2f}%".format(x))
VoteDF["Total Votes"] = VoteDF["Total Votes"].apply(lambda x: "{:,}".format(x))
print(VoteDF)
print("-------------------------")
print("And the Winner Is........")
print(Winner + "!")

###print the analysis to the terminal and export a text file with the results.###
#export PyBank text file with the results
output_path_PyBank = os.path.join("PyBank", "Resources", "PyBank_Analysis.txt")
with open(output_path_PyBank, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Total Months: " + str(TotalMonths) + "\n")
    txtfile.write("Total: $" + str(TotalPL) + "\n")
    txtfile.write("Average Change: $" + str(AvgChange) + "\n")
    txtfile.write("Greatest Increase in Profits:" + str(GreatestIncrease) + "\n")
    txtfile.write("Greatest Decrease in Profits:" + str(GreatestDecrease) + "\n")
    txtfile.write("##########################\n")
    txtfile.write("Ekection Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Total Votes:" + str(TotalVotes) + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write(VoteDF.to_string(index=False) + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write("And the Winner Is........\n")
    txtfile.write(Winner + "!\n")
    txtfile.write("-------------------------\n")