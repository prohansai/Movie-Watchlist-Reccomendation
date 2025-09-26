# Movie-Watchlist-Recommendation 🎬

Movie Watchlist Manager is a Python-based command-line tool that allows users to create, manage, and interact with a personalized movie watchlist. The program uses Python's `pickle` module for efficient data serialization, enabling users to store their movie lists and retrieve them in future sessions.

---

## ✨ Features

* **Add Movies:** Add multiple movies to your watchlist, each categorized by genre.
* **View Watchlist:** Display all the movies in your watchlist along with their associated genres.
* **Remove Movies:** Easily remove specific movies from your list after you've watched them.
* **Get Suggestions:** Receive a random movie suggestion from your entire list or get a suggestion based on a specific genre you choose.
* **Multi-User Support:** Switch between user profiles to manage separate watchlists for different people.
* **Data Persistence:** All data is automatically saved when you exit, ready for your next session.

---

## 🛠️ Prerequisites

Before you begin, ensure you have Python installed on your system.
* **Python:** Version 3.6 or higher. You can verify your installation by running `python --version` or `python3 --version` in your terminal.

---

## ⚙️ Installation and Running

To get a local copy up and running, follow these simple steps.

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/prohansai/Movie-Watchlist-Recommendation.git](https://github.com/prohansai/Movie-Watchlist-Recommendation.git)
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd Movie-Watchlist-Recommendation
    ```
3.  **Run the application:**
    ```sh
    python movie.py
    ```

---

## ⚙️ How It Works

* **Data Persistence:** The movie data is stored using the `pickle` module, which serializes the watchlist to a binary file. This allows each user's data to be securely saved and retrieved whenever needed.
* **User Interaction:** The program is fully interactive and provides a simple menu for the user to choose different options to manage their watchlist.
* **User-Friendly Interface:** The tool is designed to be easy to use, with clear prompts guiding the user through each step of the process.

---

## 🚀 Usage

1.  **Run the Program:** Start the program and enter your username to begin or load your existing list.
2.  **Add Movies:** Select the option to add movies, then enter the movie names and their genres.
3.  **View and Manage:** Choose options to view the entire watchlist, remove movies, or get movie suggestions.
4.  **Switch Users:** If more than one person uses the program, simply switch users to manage separate watchlists.
5.  **Exit:** When you're done, exit the program. Your watchlist will be saved automatically.

---

## 💡 Future Improvements

This project serves as a great base for a more advanced system. Future enhancements could include:

* **API Integration:** Connect to a movie database API (like TMDb or OMDb) to automatically fetch movie details like summaries, ratings, and release dates.
* **Improved Recommendations:** Implement a more sophisticated recommendation algorithm based on user ratings or viewing history.
* **GUI or Web Interface:** Build a graphical user interface (GUI) with a library like Tkinter or PyQt, or turn it into a web application using Flask or Django.
* **Database Storage:** Replace pickle files with a more robust database system like SQLite for better data management and scalability.
