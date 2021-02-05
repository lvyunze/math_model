from sklearn.svm import SVC
model_svm= SVC(class_weight='balanced')
model_svm.fit(x,y)