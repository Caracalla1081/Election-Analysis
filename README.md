# Election-Analysis

## Overview of Election Audit
The puprose of this election audit is to ensure to produce an automated process that can produce the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote.

The opportunity was also taken to provide analysis that gave more details on voter turnout by county and the county with the highest voter turnout.

Overall, if this process is successful, it will lay the foundation for an automated process that can be repeated for other congressional districts, senatorial districts, and local elections.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- Counties where votes were cast and included in this audit:
  - Jefferson County
  - Denver County
  - Arapahoe County
- Voter turnout results by county were:
  - Jefferson County had 10.5% of total voter turnout; with 38,855 of total votes cast.
  - Denver County had 82.8% of total voter turout; with 306,055 of total votes cast.
  - Arapahoe County had 6.7% of total voter turnout; with 24,801 ot total votes cast.
- County with the highest voter turnout:
  - Denver county with 82.8% of total voter turnout; with 306,055 of total votes cast.
- The candidates were:
  - Diana DeGette
  - Charles Casper Stockham
  - Raymon Anthony Doane
- The Candidate results were:
  - Diane DeGette received 73.8%  of the vote and 272,892 votes.
  - Charlest Casper Stockham received 23.0 of the vote and 85,213 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 of the votes.
- The winner of the election was:
  - Diane DeGette who received 73.8%  of the vote and 272,892 votes.

## Election Audit Summary
Having concluded the election audit, it is my recommendation that this code (see attached "PyPoll_Challenge.py" file) can be used for local, county, and state senate elections because of its ability to be modified to fit the needs and specifics of an audit at various election levels. This code allows for more efficient and accurate results when running the audit; tabulating vote counts and vote percentages based on key metrics by candidate or votong block (county, precinct, district, etc).

 For instance, instead of utilizing "county_name" to tabulate votes in a state senate contest, one could utilize "district_name" data that should be provided for a state  senate contest. By similar means, to use the code for a local contest, one could replace "county_name" with "precinct_name" or any other identifying structure that is utilized to breakdown local elections voting groups by location.

 Also, assuming the vote data is public record, the code could also be modified to provide a breakout of each candidates vote perfromance, by county. For example, we could look at how Diana DeGette perfomed in reference to total votes and/or percentage of vote, by county. This could prove useful for candidates, get out the vote operations, or future targeted fundraising for campaigns; as any of these entities would gain a better understanding of where to commit finite resources.

 The uses of this code in election auditing can be expanded upon even further, but even in its current state it would prove an invaluable resource for accurate, efficient, and repeatable election auditing movign forward.
  
