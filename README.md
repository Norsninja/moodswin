# MoodSwing
MoodSwing is a web-based tool for tracking and visualizing changes 
in mood and physical health over time. It is designed to allow users 
to complete a daily survey consisting of questions about various aspects 
of their mood, physical health, and well-being. The responses to the 
survey are stored in a database and can be used to generate data 
visualizations, such as line graphs and bar charts, which can help users 
identify patterns and trends in their mood and physical health. 
By completing the daily survey and viewing the data visualizations, 
users can gain insights into their moods and physical health and 
potentially identify factors that may affect them. This information 
can be helpful in managing and improving one's mental and physical 
health and well-being.

## Moodswing Actual:
This is a work in progress project that aims to visualize survey results collected using the MoodSwinger survey tool. The project is built using Flask for the backend, and JavaScript and HTML frontend.

## Installation
To run this project on your local machine, you will need to have Python and MongoDB installed. You will also need to install the dependencies listed in the requirements.txt file by running the following command:

### Copy code
pip install -r requirements.txt
Usage
To run the project, start the MongoDB server and then start the Flask app by running the following command:

### Copy code
python app.py
The app will be available at http://192.168.0.17/moodswing/index.html

## Current functionality
Currently, the project has the following functionality:

### Submit survey answers
Submit survey form

### Retrieve survey results
Retrieve most recent survey results
Retrieve all survey results

### Visualize results using Plotly
The project also uses Plotly to generate a scatter plot of the survey results, with the x-axis showing the date the survey was submitted and the y-axis showing the survey results.

### Note
This project is still a work in progress and I am unsure of the results. It works on my local machine, yet it may not work as expected on your machine.

### To Do
Improve the FullCalendar functionality to display the chosen colors.
Convert project to Django with user-specific data storage and visualization, using everything I have learned from this project. I want to use web3 to authenticate users and maybe charge some crypto (big brand, or maybe a token) to use it.


Please let me know if you have any issues running the project.

