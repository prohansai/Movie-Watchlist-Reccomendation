# Movie-Watchlist-Recommendation
Movie Watchlist Manager is a Python-based command-line tool that allows users to create, manage, and interact with a personalized movie watchlist. The program uses Python's pickle module for efficient data serialization, enabling users to store their movie lists and retrieve them in future sessions.

Features
Add Movies to Watchlist:
Users can add multiple movies to their watchlist, each categorized by genre. The list is saved to a file associated with the user, allowing for easy retrieval.

View Watchlist:
Users can view all the movies in their watchlist along with their associated genres.

Remove Movies from Watchlist:
Users can remove specific movies from their watchlist by providing the movie names. This helps in managing the list by removing watched or unwanted movies.

Suggest a Movie:
Users can either get a random movie suggestion from their watchlist or choose a movie suggestion based on a specified genre.

Change User:
The tool supports multiple users. By switching users, each user can manage their own watchlist independently without affecting others.

Exit the Program:
The user can exit the program, with all data saved for future sessions.

How It Works
Data Persistence: The movie data is stored using the pickle module, which serializes the watchlist to a binary file. This allows the user's data to be securely saved and retrieved whenever needed.
User Interaction: The program is interactive and provides a simple menu for the user to choose different options to manage their watchlist.
User-Friendly Interface: The tool is designed to be easy to use, with prompts guiding the user through each step of the process.
Usage
Run the Program:
Start the program and enter your username to begin.

Add Movies:
Select the option to add movies, then enter the movie names and their genres.

View and Manage Watchlist:
View the entire watchlist, remove movies, or get movie suggestions from the watchlist.

Switch Users:
If more than one person uses the program, switch users to manage separate watchlists.

Exit:
When done, simply exit the program. Your watchlist will be saved automatically.
