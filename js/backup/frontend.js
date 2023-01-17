document.addEventListener('DOMContentLoaded', () => {
  // Send a GET request to the /questions endpoint
  fetch('http://127.0.0.1:5000/questions', { mode: 'no-cors' })
    .then(response => {
      // Check if the response was successful
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      // If the response was successful, return the response as JSON
      return response.json();
    })
    .then(questions => {
      // Generate HTML for the survey form using the questions
      const formHTML = generateFormHTML(questions);

      // Insert the HTML into the page
	  
      document.querySelector('.survey-container').innerHTML = formHTML;
    })
    .catch(error => {
      // Log any errors that occurred
      console.error(error);

    });
});

function generateFormHTML(questions) {
  console.log('generateFormHTML() called');
  let formHTML = '<form>';

  for (const question of questions) {
    formHTML += `
      <div class="question">
        <p>${question.text}</p>
        <label for="${question.id}">${question.prompt}</label>
        <input type="${question.type}" min="${question.min}" max="${question.max}" id="${question.id}" name="${question.id}">
      </div>
    `;
  }

  formHTML += '<input type="submit" value="Submit" class="blue-submit-button"></form>';
  console.log('formHTML:', formHTML);
  return formHTML;
}


