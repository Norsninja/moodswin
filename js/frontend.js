document.addEventListener('DOMContentLoaded', () => {
  // Send a GET request to the /questions endpoint
  fetch('http://192.168.0.17:5000/questions', { mode: 'no-cors' })
    .then(response => {
      // Check if the response was successful
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      // If the response was successful, return the response as JSON
      return response.json();
    })
    .then(data => {
      // Loop through the questions
    data.forEach(question => {
      // Create the HTML elements for the question
      let questionDiv = document.createElement('div');
      let promptLabel = document.createElement('label');
      let inputElement = document.createElement('input');
 
      // Set the attributes for the elements
      promptLabel.setAttribute('for', question.id);
      inputElement.setAttribute('type', question.type);
      inputElement.setAttribute('min', question.min);
      inputElement.setAttribute('max', question.max);
      inputElement.setAttribute('id', question.id);
      inputElement.setAttribute('name', question.id);
 
      // Add the question text to the label element
      promptLabel.innerText = question.prompt;
 
      // Append the elements to the div
      questionDiv.appendChild(promptLabel);
      questionDiv.appendChild(inputElement);
 
      // Append the div to the survey container
      document.querySelector('.survey-container').appendChild(questionDiv);
    });
  });
});

