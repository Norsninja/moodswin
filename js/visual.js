
$(document).ready(function() {

    // Make an AJAX request to the /results/all endpoint to get the survey results
    $.ajax({
        url: 'http://127.0.0.1:5000/results/all',
        type: 'GET',
        success: function(data) {
// Create the variables
			var events = [];
            var appetite = [],
			exercise = [],
			embarrassmentPride = [],
			extroversionIntroversion = [],
			sleep = [],
			intestinalPain = [],
			mentalConfidence = [],
			physicalConfidence = [],
			color = [],
			datesSubmitted = []
			
		for (var i = 0; i < data.length; i++) {
				appetite.push(data[i].Appetite);
				exercise.push(data[i]["Did you exercise yesterday (15+ minutes or more)"]);
				embarrassmentPride.push(data[i]["Embarrassment and Shame vs Pride and Self-Love"]);
				extroversionIntroversion.push(data[i]["Feeling of Extroversion vs Introversion"]);
				sleep.push(data[i]["How did you sleep last night?"]);
				intestinalPain.push(data[i]["Intestinal Pain"]);
				mentalConfidence.push(data[i]["Mental Confidence"]);
				physicalConfidence.push(data[i]["Physical Confidence"]);
				datesSubmitted.push(data[i]["date_submitted"]);
				color.push(data[i]["Pick a Color"]);
				events.push({
							start: data[i].date_submitted,
							end: data[i].date_submitted,
							color: data[i]["Pick a Color"]
				});

			}

            var trace1 = {
                x: datesSubmitted,
                y: mentalConfidence,
                type: 'scatter',
                name: 'Mental Confidence',
                marker: {
                    color: 'rgb(49,130,189)'
                }
            };

            var trace2 = {
                x: datesSubmitted,
                y: physicalConfidence,
                type: 'scatter',
                name: 'Physical Confidence',
                marker: {
                    color: 'rgb(204,204,204)'
                }
            };

            var trace3 = {
                x: datesSubmitted,
                y: embarrassmentPride,
                type: 'scatter',
                name: 'Embarrassment and Shame vs Pride and Self-Love',
                marker: {
                    color: 'rgb(255,153,51)'
                }
            };

            var trace4 = {
                x: datesSubmitted,
                y: extroversionIntroversion,
                type: 'scatter',
                name: 'Feeling of Extroversion vs Introversion',
                marker: {
                    color: 'rgb(153,255,51)'
                }
            };

            var trace5 = {
                x: datesSubmitted,
                y: appetite,
                type: 'scatter',
                name: 'Appetite',
                marker: {
                    color: 'rgb(255,51,153)'
                }
            };

            var trace6 = {
                x: datesSubmitted,
                y: intestinalPain,
                type: 'scatter',
                name: 'Intestinal Pain',
                marker: {
                    color: 'rgb(255,0,0)'
                }
            };

            var trace7 = {
                x: datesSubmitted,
                y: exercise,
                type: 'scatter',
                name: 'Did you exercise yesterday (15+ minutes or more)',
                marker: {
                    color: 'rgb(153,51,255)'
                }
            };

            var trace8 = {
                x: datesSubmitted,
                y: sleep,
                type: 'scatter',
                name: 'How did you sleep last night?',
                marker: {
                    color: 'rgb(51,255,153)'
                }
            };

            var data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8];

            var layout = {
                title: 'Survey Results',
                xaxis: {
                    title: 'Date Submitted',
                    titlefont: {
                        size: 18,
                        color: '#7f7f7f'
                    }
                },
                yaxis: {
                    title: 'Rating (1-10)',
                    titlefont: {
                        size: 18,
                        color: '#7f7f7f'
                    }
                }
            };
			
			var config = {responsive: true}
			
			
			
	$("#chart-type-selector").change(function() {
      var selectedType = $(this).val();
      // update the type property of each trace
      data.forEach(function(trace) {
        trace.type = selectedType;
      });
      // re-render the chart with the updated data
      Plotly.newPlot('fig', data, layout, config);
    });
	
	

            // Generate the visualization with the survey results as input data
            Plotly.newPlot('fig', data, layout, config);
        },
		
		
		
        error: function(xhr, status, error) { 
            console.log('Error retrieving survey results'); 
            console.log(xhr); 
            console.log(status); 
            console.log(error); 

            alert('Error retrieving survey results'); 

        }
		
		});	

		});