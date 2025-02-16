// script.js

document.getElementById('report-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the form from refreshing the page

  // Get form values
  const itemName = document.getElementById('item-name').value;
  const itemDescription = document.getElementById('item-description').value;
  const contactInfo = document.getElementById('contact-info').value;

  // Create a new lost item entry
  const lostItem = document.createElement('div');
  lostItem.classList.add('lost-item');
  lostItem.innerHTML = `
    <h3>${itemName}</h3>
    <p>${itemDescription}</p>
    <p>Contact: ${contactInfo}</p>
  `;

  // Add the new lost item entry to the list
  document.getElementById('lost-items-list').appendChild(lostItem);

  // Clear the form
  document.getElementById('report-form').reset();
});

