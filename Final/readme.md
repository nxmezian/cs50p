   # SPORTSWEIGHT
    #### Video Demo:  <URL HERE>
    #### Description:
SportsWeight is a simple tracker for a user’s running statistics and weight. A user inputs the aforementioned data and is able to see them plotted in a graph.

In project.py the user will find the main function, this is the only file directly accessible to users. When the main.py is passed through the Python interpreter,
the first screen that is loaded is the intro screen. The first print statement includes “Welcome to Sportsweight!”. For some users “Welcome back to SportsWeight”
might make more sense, however, due to the complexity ,time effort involved in coding this statement and the additional code required for a minor improvement, no distinction is made between first-time users and regular users.

The intro() function contains a while-True loop that takes in input that directs the user to the menu of their choice. While-True loop can be “expensive”, but because of the importance of only allowing valid input and allowing for users to retry after their input was rejected, the loop is essential. In fact, almost all other functions have a similar loop that prompts the user to either return to the main menu, return to the beginning of the current menu or to exit the program altogether. In the intro(), users can choose to log in, create a new account or to use a temporary account that is not meant to store information.

In credentials(), create_username(), create_password(), the user creates a unique username of four characters or more and a password of eight characters or more that includes numbers and letters, these credentials are saved in a CSV file named credentials.csv. As of yet, these passwords are stored in plain text. Good practice would be to hash these passwords. In login(), users enter their credentials which are compared to the username and password that are stored in credentials.csv.

From main_menu(), the user input running statistics and weight progression. These statistics are saved in different files that are created with the OS module and are guaranteed to be stored in a unique file as the filename contains the username, which must be unique. The statistics can be visualized with help of the Pandas module, which shows the user a graph of their previously inputted data. The user also has a personal profile, which provides the additional benefit of calculating the user’s BMI.

Possible improvements for the current program include the previously mentioned hashing of passwords. Furthermore, the stored BMI could also be visualized in a graph. Lastly, as the current software is a command-line program, it would be interesting to experiment with implementing a GUI for a future iteration. For now, the lightweight aspect of the program and the fact that the program can help users motivate them to achieve their fitness goals make it a working prototype.
