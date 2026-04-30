from sklearn.model_selection import train_test_split,GridSearchCV,RandomizedSearchCV,KFold,cross_val_score
import mlflow
import dagshub
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from logger import logging
import joblib
from sklearn.pipeline import Pipeline

df=pd.read_csv("D:\\Loan_aproval\\Loan_aproval_model\\data\\preprocessed.csv",index_col=0)
y=df["loan_status"]
x=df.drop(columns="loan_status")

x_train,x_test,y_train,y_test=train_test_split(x,y)



#Logistic Regression
model=LogisticRegression()
try:
    model.fit(x_train,y_train)
    logging.info("logistic regression model fitted succesfully")
except Exception:
    logging.info("Logistic regression not fitted succesfully")
y_pred=model.predict(x_test)

accuracy_score(y_test,y_pred)
con=classification_report(y_test,y_pred,output_dict=True)

#connect with dagshub
dagshub.init(repo_owner='MasudMallik', repo_name='Loan_aproval_model', mlflow=True)


#track logistic regression in mlflow
mlflow.set_tracking_uri("https://dagshub.com/MasudMallik/Loan_aproval_model.mlflow")
mlflow.set_experiment("Loan_Approval_models_")
with mlflow.start_run(run_name="logistic"):
    mlflow.log_metrics({
        "precision":con["weighted avg"]["precision"],
        "recall":con["weighted avg"]["recall"],
        "f1 score":con["weighted avg"]["f1-score"],
        "accuracy":con["accuracy"]
    })
    mlflow.set_tag("model name","logistic regression")
mlflow.sklearn.log_model(model,"logistic")



#DecisionTree Classifier
decision_model=DecisionTreeClassifier(random_state=42,)

param={
    "criterion":["gini","entropy","log_loss"],
    "max_depth":[10,25,20,25],
}
cross=KFold(n_splits=5,random_state=42,shuffle=True)


#finding best parameter using gridsearchcv
decision_tree=GridSearchCV(
    estimator=decision_model,
    param_grid=param,
    n_jobs=-1,
    scoring="accuracy",
    cv=cross,
    refit=True
)
try:
    decision_tree.fit(x_train,y_train)
    logging.info("Decision Tree model fitted succesfully")
except Exception:
    logging.info("decision tree model not loaded succesfully")

y_pred=decision_tree.predict(x_test)
des_con=(classification_report(y_test,y_pred,output_dict=True))


#track decision tree experiment in dagshub(mlflow)
mlflow.set_tracking_uri("https://dagshub.com/MasudMallik/Loan_aproval_model.mlflow")
mlflow.set_experiment("Loan_Approval_models_")
with mlflow.start_run(run_name="DecisionTree"):
    mlflow.log_metrics({
        "precision":des_con["weighted avg"]["precision"],
        "recall":des_con["weighted avg"]["recall"],
        "f1 score":des_con["weighted avg"]["f1-score"],
        "accuracy":des_con["accuracy"]
    })
    mlflow.log_params(decision_tree.best_params_)
    mlflow.set_tag("model name","DEcisionTreeClassifier")
mlflow.sklearn.log_model(decision_tree.best_estimator_,"DEcisiontree")



#randomforest
random=RandomForestClassifier(random_state=42,)
param={
    "criterion":["gini","entropy","log_loss"],
    "max_depth":[10,15,20,30,40],
    "n_estimators":[10,20,30]
}

random_model=GridSearchCV(
    estimator=random,
    param_grid=param,
    cv=cross,
    n_jobs=-1,
    scoring="accuracy",
)

try:
    random_model.fit(x_train,y_train)
    logging.info("randomforest model loaded succesfully")
except Exception:
    logging.info("randomforest model not loaded succesfully")
y_pred=random_model.predict(x_test)
rand_con=classification_report(y_test,y_pred,output_dict=True)

#tracking randomforest model using mlflow
mlflow.set_tracking_uri("https://dagshub.com/MasudMallik/Loan_aproval_model.mlflow")
mlflow.set_experiment("Loan_Approval_models_")
with mlflow.start_run(run_name="Randomforest"):
    mlflow.log_metrics({
        "precision":rand_con["weighted avg"]["precision"],
        "recall":rand_con["weighted avg"]["recall"],
        "f1 score":rand_con["weighted avg"]["f1-score"],
        "accuracy":rand_con["accuracy"]
    })
    mlflow.log_params(random_model.best_params_)
    mlflow.set_tag("model name","RandomForestClassifier")
mlflow.sklearn.log_model(random_model.best_estimator_,"RandomForest")


#svm
svc_model=SVC(random_state=42)
try:
    svc_model.fit(x_train,y_train)
    logging.info("Svm model fitted succesfully")
except Exception:
    logging.info("svm model not fitted succesfully")
y_pred=svc_model.predict(x_test)
svm_con=(classification_report(y_test,y_pred,output_dict=True))

#svm model tracking using mlflow
mlflow.set_tracking_uri("https://dagshub.com/MasudMallik/Loan_aproval_model.mlflow")
mlflow.set_experiment("Loan_Approval_models_")
with mlflow.start_run(run_name="svm"):
    mlflow.log_metrics({
        "precision":svm_con["weighted avg"]["precision"],
        "recall":svm_con["weighted avg"]["recall"],
        "f1 score":svm_con["weighted avg"]["f1-score"],
        "accuracy":svm_con["accuracy"] 
    })
    mlflow.set_tag("model name","support vector")
mlflow.sklearn.log_model(svc_model,"SVM")


#gaussiannb

bayes=GaussianNB()
try:
    bayes.fit(x_train,y_train)
    logging.info("gaussian naive bayes model loaded succesfully")
except Exception:
    logging.info("Gaussian naive bayes model not loaded succesfully")
y_pred=bayes.predict(x_test)
gauss_con=(classification_report(y_test,y_pred,output_dict=True))

#tracking gaussian naive bayes using mlflow
mlflow.set_tracking_uri("https://dagshub.com/MasudMallik/Loan_aproval_model.mlflow")
mlflow.set_experiment("Loan_Approval_models_")
with mlflow.start_run(run_name="gaussianNb"):
    mlflow.log_metrics({
        "precision":gauss_con["weighted avg"]["precision"],
        "recall":gauss_con["weighted avg"]["recall"],
        "f1 score":gauss_con["weighted avg"]["f1-score"],
        "accuracy":gauss_con["accuracy"]
    })
    mlflow.set_tag("model name","Gaussian Naive Bayes")
mlflow.sklearn.log_model(bayes,"GNB")


#xgb
xgb=XGBClassifier()
try:
    xgb.fit(x_train,y_train)
    logging.info("xgboost model fitted succesfully")
except Exception:
    logging.info("xgboost model not fitted succesfully")
y_pred=xgb.predict(x_test)
xgb_con=(classification_report(y_test,y_pred,output_dict=True))

#xgboost tracking using mlflow
mlflow.set_tracking_uri("https://dagshub.com/MasudMallik/Loan_aproval_model.mlflow")
mlflow.set_experiment("Loan_Approval_models_")
with mlflow.start_run(run_name="XGB"):
    mlflow.log_metrics({
        "precision":xgb_con["weighted avg"]["precision"],
        "recall":xgb_con["weighted avg"]["recall"],
        "f1 score":xgb_con["weighted avg"]["f1-score"],
        "accuracy":xgb_con["accuracy"]
    })
    mlflow.set_tag("model name","XGBClassifier")
mlflow.xgboost.log_model(xgb,"XGB")

#register model
mlflow.register_model("run:/30a7f73c94c84affab263f66007cc67b/XGB","xgbclassifier",tags={"stage":"production"})


#in mlflow we see that xgboost is giving 93 % accuracy 
file_name="loan_predict.joblib"
with open(file_name,"wb") as f:
    joblib.dump(xgb,f)
