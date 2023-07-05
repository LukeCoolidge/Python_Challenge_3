import csv
import os
csvpath=os.path.join("Resources","election_data.csv")

#open CSV File

with open(csvpath,"r") as file:

    #Read CSV 

    csv_reader = csv.reader(file)

    header = next(csv_reader)

    #Set up variables

    total_votes = 0
    candidates = {}
    
    # Look Thru CSV
    for row in csv_reader:
        #Total votes
        total_votes += 1
        
        # Canditate in row 2
        candidate = row[2]
        
        # See if cindidate is listed
        if candidate in candidates:
            # Increment the vote count for the candidate
            candidates[candidate] += 1
        else:
            # Add the candidate to the dictionary with an initial vote count of 1
            candidates[candidate] = 1
    
    # Winner calculation
    winner = ""
    max_votes = 0
    
    # Print results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    
    output = f"Election Results\n"
    output += f"-------------------------\n"
    output += f"Total Votes: {total_votes}\n"
    output += f"-------------------------\n"

    # Candidates and calculate their vote percentage
    for candidate, votes in candidates.items():
        vote_percentage = (votes / total_votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
        output +=f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        
        # Check if the current candidate has the most votes
        if votes > max_votes:
            max_votes = votes
            winner = candidate
    
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    output += f"-------------------------\n"
    output += f"Winner: {winner}\n"
    output += f"-------------------------\n"
   


    output_file = os.path.join("analysis","election_data.text")

    with open(output_file, "w") as f:
        f.write(output)

    print(f'Financial analysis has been experted to{output_file} successfully')