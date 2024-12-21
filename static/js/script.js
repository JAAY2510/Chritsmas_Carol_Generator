

const form = document.querySelector('form');
const carolDisplay = document.getElementById('carol-display');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const response = await fetch('/generate', {
    method: 'POST',
    body: formData,
  });

  if (response.ok) {
    const data = await response.json();
    carolDisplay.innerHTML = `<p>${data.carol}</p>`; 
  } else {
    carolDisplay.innerHTML = '<p>An error occurred while generating the carol.</p>';
  }
});