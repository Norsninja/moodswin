$(document).ready(function() {
function createInputElement(question) {
  switch (question.inputType) {
    case 'range':
      // create a range input element
      var input = document.createElement('input');
      input.type = 'range';
	  input.name = question.question; // add name attribute
      input.min = question.min;
      input.max = question.max;
	  input.value = 5;
      return input;
    case 'color':
      // create a color input element
      var input = document.createElement('input');
      input.type = 'color';
	  input.name = question.question; // add name attribute
      return input;
    case 'yesno':
      // create a radio button group for yes/no
      var container = document.createElement('div');
      ['Yes', 'No'].forEach(function(label) {
        var input = document.createElement('input');
        input.type = 'radio';
		input.name = question.question; // add name attribute
        input.value = label.toLowerCase();
        var labelElement = document.createElement('label');
        labelElement.appendChild(document.createTextNode(label));
        container.appendChild(input);
        container.appendChild(labelElement);
      });
      return container;
    default:
      // create a text input element as a fallback
      var input = document.createElement('input');
      input.type = 'text';
	  input.name = question.question; // add name attribute
      return input;
  }
}

// Make an AJAX request to the /questions endpoint to retrieve the list of questions
var xhr = new XMLHttpRequest();
xhr.open('GET', 'http://127.0.0.1:5000/questions');
xhr.onload = function() {
  if (xhr.status === 200) {
    // Retrieve the list of questions from the response
    var questions = JSON.parse(xhr.responseText);
    
    // Get the form element
    var form = document.getElementById('survey-form');
    
	var submitButton = document.createElement("button");
	submitButton.innerHTML = "Submit";
	submitButton.className = "button";
		form.appendChild(submitButton);
	
    // Iterate through the list of questions
    questions.forEach(function(question) {
      // Create a label element for the question
      var label = document.createElement('label');
      label.innerHTML = question.question;
      
      // Create an input element for the question
      var input = createInputElement(question);
      
      // Append the label and input elements to the form
      form.appendChild(label);
      form.appendChild(input);
	  form.appendChild(document.createElement("br"));
	  
    });
	
	var buttonContainer = document.createElement("div");
	buttonContainer.className = "buttonContainer";
	buttonContainer.appendChild(submitButton);
	form.appendChild(buttonContainer);

  }
  else {
    console.error(xhr.responseText);
  }
};
xhr.send();

// Get the form element
var form = document.getElementById('survey-form');

// Attach a submit event listener to the form
form.addEventListener('submit', function(event) {
  // Prevent the form from being submitted
  event.preventDefault();

  // Create a new FormData object to hold the form data
  var data = new FormData(form);

  // Make an AJAX request to the /submit endpoint to send the form data
  var xhr = new XMLHttpRequest();
  xhr.open('POST', 'http://127.0.0.1:5000/submit');
  xhr.onload = function() {
    if (xhr.status === 200) {
      console.log('Form data sent successfully');
      // Redirect the user to the "survey complete" page
      window.location.href = 'results.html';
      // OR use window.location.replace('/survey-complete'); to replace the current page
    }
    else {
      console.error(xhr.responseText);
    }
  };
  xhr.send(data);
});


function submitForm() {
  // Get the form data
  var formData = new FormData(document.getElementById('survey-form'));

  // Send a POST request to the server to store the form data
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/submit');
  xhr.send(formData);
}
		});
