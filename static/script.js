document.getElementById('pdfForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(this);

    fetch('/', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('questionDisplay').textContent = data.question;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('textForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const text = document.getElementById('text_input').value;

    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'text_input=' + encodeURIComponent(text),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('questionDisplay').textContent = data.question;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});