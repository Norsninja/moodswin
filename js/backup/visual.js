$(document).ready(function() {
    // Make an AJAX request to the /visualization endpoint to get the visualization JSON data
    $.ajax({
        url: 'http://127.0.0.1:5000/visualization',
        type: 'GET',
        success: function(json) {
            // Generate the visualization with the survey results as input data
            Plotly.plot('fig', json, {x : ['Appetite', 'Embarrassment and Shame vs Pride and Self-Love', 'Feeling of Extroversion vs Introversion'], y : ['Mental Confidence', 'Physical Confidence', 'Sleep Quality'], labels : {x : 'Question', y : 'Response'}});  
        },
        error: function(xhr, status, error) { 
            console.log('Error retrieving survey results'); 
            console.log(xhr); 
            console.log(status); 
            console.log(error); 

            alert('Error retrieving survey results'); 

        }  										    });   });
		
		