# MoodSwinger Results Visualization
This is a work in progress project that aims to visualize survey results collected using the MoodSwinger survey tool. The project is built using Flask for the backend, and JavaScript (jQuery, Plotly.js) for the frontend.

## Installation
To run this project on your local machine, you will need to have Python and MongoDB installed. You will also need to install the dependencies listed in the requirements.txt file by running the following command:

### Copy code
pip install -r requirements.txt
Usage
To run the project, start the MongoDB server and then start the Flask app by running the following command:

### Copy code
python app.py
The app will be available at http://localhost:5000/moodswing/index.html

## Current functionality
Currently, the project has the following functionality:

### Submit survey answers
Submit survey form

### Retrieve survey results
Retrieve most recent survey results
Retrieve all survey results

### Visualize results using Plotly
The project also uses Plotly.js to generate a scatter plot of the survey results, with the x-axis showing the date the survey was submitted and the y-axis showing the survey results.

### Note
This project is still a work in progress and I am unsure of the results. It works on my local machine, yet it may not work as expected on your machine.

### To Do
Improve the FullCalendar functionality.
Please let me know if you have any issues running the project.
