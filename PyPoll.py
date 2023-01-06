# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. THe winner of the election based on popular vote.

file_to_load = 'C:\Users\Upt0w\Election-Analysis\Resources\election_results.csv'
with open("C:\Users\Upt0w\Election-Analysis\Resources\election_results.csv", 'r') as election_data:
    print(election_data)