// Make an AJAX request to the /results endpoint to retrieve the most recent survey results
      var xhr = new XMLHttpRequest();
      xhr.open('GET', 'http://127.0.0.1:5000/results');
      xhr.onload = function() {
        if (xhr.status === 200) {
          // Retrieve the survey results from the response
          var results = JSON.parse(xhr.responseText);
          
          // Get the results element
          var resultsElement = document.getElementById('results');
          
          // Iterate through the list of results
          for (var key in results) {
            // Create an li element for the result
            var resultElement = document.createElement('li');
            
    
            // If this is the color result, render a swatch sample instead
           
if (key === 'Appetite') {
				resultElement.innerHTML = key + ' &#x1F354;&#x1F35F;&#x1F355;&#x1F313' + ': ' + results[key];
			} else if (key === 'Embarrassment and Shame vs Pride and Self-Love') {
				resultElement.innerHTML = key + ' &#x1F926;&#x1F937;&#x1F61E;&#x1F604' + ': ' + results[key];
			} else if (key === 'Feeling of Extroversion vs Introversion') {
				resultElement.innerHTML = key + ' &#x1F92B;&#x1F507;&#x1F509;&#x1F3A4' + ': ' + results[key];
			} else if (key === 'How did you sleep last night?') {
				resultElement.innerHTML = key + ' &#x1F6CC;&#x1F62A;&#x1F6CC;&#x1F6CF' + ': ' + results[key];
			} else if (key === 'Intestinal Pain') {
				resultElement.innerHTML = key  + ' &#x1F92E;&#x1F915;&#x1F4A9;&#x1F321' + ': ' + results[key];
			} else if (key === 'Mental Confidence') {
				resultElement.innerHTML = key + ' &#x1F4AD;&#x1F914;&#x1F9E0;&#x1F4AA' + ': ' + results[key];
			} else if (key === 'Physical Confidence') {
				resultElement.innerHTML = key + ' &#x1F3CB;&#x26F9;&#x1F3C3;&#x1F3C3' + ': ' + results[key];
			} else if (key === 'Pick a Color') {
				var colorElement = document.createElement('div');
				colorElement.style.backgroundColor = results[key];
				colorElement.style.width = '50px';
				colorElement.style.height = '50px';
				colorElement.style.display = 'inline-block';
				resultElement.innerHTML = key + ' &#x1F308;&#x1F3C6;&#x1F304;&#x1F303' + ': ';
				resultElement.appendChild(colorElement);
			} else {
				resultElement.innerHTML = key + ': ' + results[key];
			}
            // Append the result element to the results element
            resultsElement.appendChild(resultElement);
          }
        }
        else {
          console.error(xhr.responseText);
        }
      };
      xhr.send();
	  
