# app.py (Minimal changes to use new templates and result page)

from flask import Flask, url_for, render_template, request # Added request
from forms import InputForm # Your forms.py
import pandas as pd
import joblib

# Use __name__ for Flask app
app = Flask(__name__, static_folder='static')
# Keep your original secret key for now, but CHANGE LATER
app.config['SECRET_KEY'] = "secret_key" # REMEMBER TO CHANGE THIS

# Load Model (Keep as is)
# Add a basic check in case loading fails - app will crash if model is None later otherwise
try:
    model = joblib.load("model.joblib")
except Exception as e:
    print(f"CRITICAL ERROR: Could not load model.joblib: {e}")
    model = None # Or exit, as prediction will fail

@app.route('/')
@app.route('/home')
def home():
    # Use the new template name
    return render_template("home_simple_zillow.html", title="Home")

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    form = InputForm()
    # We won't use the 'message' variable in the same way
    # Errors will be handled by WTForms field validators displayed in the template

    # Check if model loaded before proceeding
    if model is None:
        # Render the form page with an error message if model didn't load
        # Using 'output' variable name like in predict_simple_zillow.html
        return render_template("predict_simple_zillow.html", title="Predict", form=form, output="Error: Prediction Model Failed to Load.")

    if form.validate_on_submit():
        # --- Form is valid, PREDICT ---
        # Keep your original data preparation
        x_new = pd.DataFrame(dict(
            location=[form.location.data],
            total_sqft=[form.total_sqft.data],
            bath=[form.bath.data],
            balcony=[form.balcony.data],
            BHK=[form.BHK.data]
        ))

        # Keep your original prediction call
        # Assume prediction works and returns a number, otherwise it will error here
        prediction_raw = model.predict(x_new)[0]

        # Format the result simply
        # (No check here for negative/non-numeric as requested, will error if prediction_raw is bad)
        prediction_lakhs = prediction_raw 
        prediction_result_text = f"{prediction_lakhs:,.2f} Lakh INR"

        # --- RENDER THE NEW RESULT PAGE ---
        # Instead of rendering predict.html with a message, render the result page
        return render_template(
            "result_simple_zillow.html", # Render the result template
            title="Prediction Result",
            predicted_price=prediction_result_text, # Pass the formatted price
            input_details=x_new.iloc[0].to_dict() # Pass input details
        )
    # else: (Implicitly handles GET request or failed POST validation)
    # If GET request OR form.validate_on_submit() is False on POST:
    # Re-render the prediction form.
    # WTForms automatically passes errors to the form object for display in template.
    return render_template("predict_simple_zillow.html", title="Predict", form=form, output=None) # output=None for initial load


@app.route('/contact')
def contact():
    # Use the new template name
    return render_template("contact_simple_zillow.html", title="Contact")

# Corrected the main execution block condition
if __name__ == '__main__':
    app.run(debug=True)