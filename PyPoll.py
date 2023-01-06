# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import csv
import os

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:
# Write the three counties to the file.
    txt_file.write("Counties in the Election\n-----------------------------\nArapahoe\nDenver\nJefferson")
    