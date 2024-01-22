# Note to self:
# Reviewed notes in Python class 1 - 3 before start
# Total of vote: use vote counter +=
# Individual vote count: Create a list for the Candidate names, if the Candidate name is not on the list, add his/her name to the list, along with a vote for his/her name.
# But if he/she is already on the list, then simply add a vote count under his/her name
# In previous Module 2, If Not Equal (<>) in VBA is utilized to check if we are still within the same ticker, and it played an important role during the For Loop value searches.
# To find out if Python has conditional statements like "if not", I looked up online and found W3Schools Python Tutorial: https://www.w3schools.com/python/gloss_python_if_not.asp


import os
import csv

# Path to the CSV file
pypoll_csv = os.path.join('Resources', 'election_data.csv')

# Open and read csv
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read and print CSV header
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    # Initialize variables for candidate analysis
    Candidate = []
    vote_count = []
    vote_percentage = []
    total_vote = 0

    for row in csv_reader:
        # Total vote-counter
        total_vote += 1

        # Check if the Candidate is already in the list, and if not add the Candidate to the list with an initial vote count of 1
        candidate_name = row[2]
        if candidate_name not in Candidate:
            Candidate.append(candidate_name)
            vote_count.append(1)

        # If the candidate is already in the list, increase the vote count for that candidate
        else:
            index = Candidate.index(candidate_name)
            vote_count[index] += 1

    # Add to vote_percentage list
    for votes in vote_count:
        percentage = (votes/total_vote) * 100
        percentage = round(percentage, 3)
        vote_percentage.append(percentage)

    # Find the winning candidate
    winner_votes = max(vote_count)
    index = vote_count.index(winner_votes)
    winner = Candidate[index]

    # Displaying results
    print("Election Results")
    print("--------------------------")
    print(f"Total Votes: {total_vote}")
    print("--------------------------")
    for i in range(len(Candidate)):
        print(f"{Candidate[i]}: {vote_percentage[i]}% ({vote_count[i]})")
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

    output_path = os.path.join('Analysis', 'pypoll_result_1.txt')
    with open(output_path, 'w') as text:
        text.write("Election Results\n")
        text.write("--------------------------\n")
        text.write(f"Total Votes: {str(total_vote)}\n")
        text.write("--------------------------\n")
        for i in range(len(Candidate)):
            text.write(f"{Candidate[i]}: {vote_percentage[i]}% ({vote_count[i]})\n")
        text.write("--------------------------\n")
        text.write(f"Winner: {winner}\n")
        text.write("--------------------------\n")





