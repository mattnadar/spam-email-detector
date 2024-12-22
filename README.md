# spam-email-detector
Email Spam Detector

This project is a machine learning-based email spam detector. It allows users to check whether an email is spam or not via a web interface, powered by a Flask backend and a simple frontend hosted using Python's built-in HTTP server. 

Features:

    Trains an ML model to classify emails as spam or not.
    Flask backend to process predictions.
    Simple web interface for user interactions.

Steps to use:

After cloning the repository, run "pip install -r requirements.txt" to download the requiremtns. Then, do the following:

1. Train the model (Kind of optional because I have a model in the github I think):
	run 'python model.py'

2. Start flask backend
	run 'python app.py'

3. Start the front end
	run 'python -m http.server'
it will be hosted on localhost:8000

4. Now input a sample email and it will make a prediction.

Moving forward, I'd like to somehow integrate this as some sort of extension on a web browser.
