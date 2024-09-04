document.addEventListener('DOMContentLoaded', function() {
  const button = document.getElementById('randomPoemBtn');
  const randomPoemDiv = document.getElementById('randomPoem');
  const authorSpan = document.querySelector('.author');
  const readMoreLink = document.querySelector('.readMoreLink');

  if (button && randomPoemDiv && authorSpan && readMoreLink) {
    button.addEventListener('click', function() {
      fetch('/poem-list.json')
        .then(response => response.json())
        .then(data => {
          // Get a random poem
          const randomIndex = Math.floor(Math.random() * data.gedichte.length);
          const randomPoem = data.gedichte[randomIndex];

          // Update HTML elements
          randomPoemDiv.innerHTML = `
            ${randomPoem.excerpt}
          `;
          authorSpan.textContent = `Author: ${randomPoem.author || 'Unknown'}`; // Assuming you have an author field
          readMoreLink.href = randomPoem.url;
          readMoreLink.textContent = randomPoem.title;
        })
        .catch(error => console.error('Error fetching JSON:', error));
    });
  }
});
