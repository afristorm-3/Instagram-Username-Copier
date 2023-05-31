import instaloader

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()

# Replace with your Instagram credentials
username = ""
password = ""

# Login to authenticate the requests
bot.login(username, password)


# Provide the search query here
search_query = 'music'

# Retrieve the top search results for profiles
search_results_profiles = instaloader.TopSearchResults(bot.context, search_query).get_profiles()

# Create a file to store the usernames and URLs
filename = 'usernames.txt'
with open(filename, 'w') as file:

# Iterate over the extracted profiles and write the username and URL to the file

    for profile in search_results_profiles:
	username = profile.username
	profile_url = f"https://www.instagram.com/{username}/"
	file.write(f"{username}: {profile_url}\n")

print(f"Usernames and URLs saved to {filename}.")
