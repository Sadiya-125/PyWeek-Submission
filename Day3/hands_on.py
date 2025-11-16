import pandas as pd

data = pd.read_csv(r"C:\Users\Sadiya Maheen\Desktop\PyWeek-Submission\Day3\ipl-matches.csv")

print(data.head())

# Number of Rows and Columns
print(data.shape)

# List All Unique Seasons and Teams
print(data['Season'].unique())
print(data['Team1'].unique())

# How Many Matches Were Played in Each Season
matches_per_season = data['Season'].value_counts()
print(matches_per_season)

# Which Team Won the Most Matches Overall
most_wins = data['WinningTeam'].value_counts().idxmax()
print(f"Team with most wins: {most_wins}")

# Show Matches where 'Mumbai Indians' were the Winning Team
mumbai_wins = data[data['WinningTeam'] == 'Mumbai Indians']
print(mumbai_wins)

# Show All Matches that Went to Super Over
super_over_matches = data[data['SuperOver'] == 'Y']
print(super_over_matches)

# Show Matches Played at 'Eden Gardens'
eden_gardens_matches = data[data['Venue'] == 'Eden Gardens']
print(eden_gardens_matches)

# How Many Super Over Finishes Have Occurred
super_over_count = data['SuperOver'].value_counts().get('Y', 0)
print(f"Number of Super Over finishes: {super_over_count}")

# Check if Toss Winner is Also the Match Winner in Percentage of Matches
toss_winner_matches = data[data['TossWinner'] == data['WinningTeam']]
percentage_toss_winner_wins = (len(toss_winner_matches) / len(data)) * 100
print(f"Percentage of matches where toss winner is also match winner: {percentage_toss_winner_wins:.2f}%")