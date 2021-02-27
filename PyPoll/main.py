import csv
import os

input_file = os.path.join("Resources","election_data.csv")
output_file = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0
list_candidate_khan = 0
list_candidate_correy = 0
list_candidate_li = 0
list_candidate_otooley = 0
khan_percentage = 0
correy_percentage = 0
li_percetnage = 0
otooley_percentage = 0
winner =[]
CandidateList=[]

with open(input_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:

         # To find the list of candidate
        
        if row[2] not in CandidateList:
            CandidateList.append(row[2])
			
#print(CandidateList)
        total_votes += 1
        if row[2] == 'Khan':
            list_candidate_khan += 1
        if row[2] == 'Correy':
            list_candidate_correy += 1
        if row[2] == 'Li':
            list_candidate_li += 1
        if row[2] == "O'Tooley":
            list_candidate_otooley += 1

khan_percentage = round((1-((total_votes - list_candidate_khan)/total_votes))*100,0)
correy_percentage = round((1-((total_votes - list_candidate_correy)/total_votes))*100,0)
li_percentage = round((1-((total_votes - list_candidate_li)/total_votes))*100,0)
otooley_percentage = round((1-((total_votes - list_candidate_otooley)/total_votes))*100,0)

if list_candidate_khan > list_candidate_correy:
    winner = "Khan"
elif list_candidate_correy > list_candidate_li:
    winner = "Correy"
elif list_candidate_li > list_candidate_otooley:
    winner = "Li"
else:
    winner = "O'Tooley"

output = (
    f"Election Results\n"
    f"---------------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"---------------------------------\n"
    f"Khan: {khan_percentage}% ({list_candidate_khan})\n"
    f"Correy: {correy_percentage}% ({list_candidate_correy})\n"
    f"Li: {li_percentage}% ({list_candidate_li})\n"
    f"O'Tooley: {otooley_percentage}% ({list_candidate_otooley})\n"
    f"---------------------------------\n"
    f"Winner : {winner}\n"
    f"---------------------------------\n"
     )
print(output)
with open(output_file, "w") as txt_file:
    txt_file.write(output)
