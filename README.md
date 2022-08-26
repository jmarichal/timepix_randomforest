# Random forest for particle identification with MiniPIX-Timepix detector
\
MiniPIX-Timepix is a novel silicon-based detector that enables online visualization and recording of pixel tracks drawn by the particles hitting its sensitive area.
\
\
A random forest classification model has been trained to determine the particle type (electrons and photons, protons or alpha particles) of a pixel cluster. It is saved in the pickled file random_forest.pkl.
\
\
The file Deploy_model.py shows a little code in Python that deploys the model and uses it on some data from Timepix measurements. 
\
\
You will need the PyCaret library to run this code. You can easily install it with pip:
```
pip install pycaret
```
See the [PyCaret installation page](https://pycaret.readthedocs.io/en/stable/installation.html) for more information.
\
\
To directly see the results, please check the notebook file Deploy_model.ipynb.
