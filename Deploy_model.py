#!/usr/bin/env python
# coding: utf-8

# python libraries imports
import pandas as pd
import pycaret
from pycaret.classification import *

# Load data
events = pd.read_csv('events_lists/opf100B2.csv',delimiter=';')

# Display to check importation
events.head()

# Import the random forest
rf = load_model('random_forest')

# Predict particle type with random forest classifier
events_classified = predict_model(rf, data=events)
        
#Correct for one-pixels-photons
events_classified.loc[events_classified['Size'] < 2, 'Label'] = 'photon'

# Check 'label' and 'score' column are added
events_classified.head()

# Save file
file_name = 'events_lists/opf100B0_classified.csv'
events_classified.to_csv(file_name, sep=';')