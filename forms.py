# forms.py (Your Original - No Changes)

from flask_wtf import FlaskForm
import pandas as pd
from wtforms import SelectField,FloatField,IntegerField,SubmitField
from wtforms.validators import DataRequired,NumberRange

# Keep your data loading as is - ensure paths are correct
try:
    train=pd.read_csv("Dataset/train_data.csv")
    test=pd.read_csv("Dataset/test_data.csv")
    # Combine to get all unique locations for the dropdown
    X_data=pd.concat([train,test],axis=0).drop(columns="price", errors='ignore')
    location_choices = sorted(X_data['location'].unique().tolist())
except Exception as e:
    print(f"Warning: Could not load data for form locations: {e}")
    location_choices = []


class InputForm(FlaskForm):
    location=SelectField(
        label="Location",
        choices=location_choices,
        validators=[DataRequired(message="Please select a location.")] # Added message
    )
    total_sqft=FloatField(
        label="Total Sqft",
        validators=[DataRequired(message="Square footage is required.")] # Added message
    )
    bath=IntegerField(
        label="Bath Rooms",
        validators=[DataRequired(message="Number of bathrooms is required.")] # Added message
    )
    balcony=IntegerField(
        label="Balcony",
       # Consider InputRequired if 0 is valid and required
       validators=[DataRequired(message="Number of balconies is required (enter 0 if none)."),
                   NumberRange(min=0, message="Balcony must be 0 or greater")]
    )
    BHK=IntegerField(
        label="BHK",
        validators=[DataRequired(message="BHK count is required.")] # Added message
    )
    submit=SubmitField("Predict Price") # Changed text slightly