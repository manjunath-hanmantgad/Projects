This project details the usage of MLOps with Azure Machine learning.
The goal of the project is to predict the weather condition and it is a classification problem to predict whether it will rain or not in the given time-frame.

Library: Scikit-learn

Machine learning Model inferencing , scoring , fit , deployment is done using Azure Machine learning Python SDK.
Dataset preprocessing is done on local compute.

The project is divided in five notebooks detailing the below steps:-

1. Loading the dataset
- Dataset is processed and then saved to Azure blob store then upload the data to the datastore
- Register the data to Azure machine learning Workspace.

2. Building Machine learning Pipeline , the steps involved are:-

- Data ingestion
- Model training
- Model testing
- Model packaging
- Model registering

For model training , I have used support vector machine and Random Forest classifier.Standard scaling has been performed.
For hyperparameter tuning I have used Grid search to get best parameters.

Using ONNX, the trained model is serialized using the skl2onnx library. The model is serialized as the file svc.onnx

Model artifacts are: svc.onnx and model-scaler.pkl

3. Model Packaging 

The steps involved in model packing include:

- Model evaluation and interpretability metrics
- Production testing methods
- Package ML models
- Inference ready models

4. Deploying ML model as web service with Azure Container Instance

Steps involved:-

- Writing a scoring script
- Deploying as a web service
- Enabling application insights
- Testing the webservice
- Testing from user (with scoring file : score.py)

5. Deploying ML model as web service with Azure Kuberenetes Service

Steps are repeated , inplace of ACI create a Kuberenetes cluster ( using inference cluster , auto-scaling, AKSCompute)


Post the model deployment stage I have enabled CI/CD using Azure DevOps ( with integration of Azure Repos , Azure Release Pipelines , Azure trigger (Git trigger , Schedule trigger and action trigger)


ML model can be served as Real time or as Batch service. I am using FastAPI to serve the users.

For model monitoring following is done:

- Register the target dataset ( to use for inferencing)
- Create a data drift monitor
- Perform data drift analysis
- Perform feature drift analysis
- Create and perfrom Model drift analysis
- Application performance ( using Azure application insights)


