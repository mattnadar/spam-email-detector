async function checkSpam() {
    const message = document.getElementById('message').value;

    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message }),
    });

    const data = await response.json();
    document.getElementById('result').innerText = `Prediction: ${data.prediction}`;
}
