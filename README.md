I have made this project to help the government to identify ‘wanted criminals’ roaming  freely at any  public place. Smart cameras will be installed at various public places, whenever it finds any person matching  with the dataset record, it will send notification to security center.
For this I have mainly used OpenCV library in Python and SQL.
I have divided this project into 3 parts-
1.	Creating dataset
2.	Train the recognizer
3.	Detector 
For creating dataset, either I can use my camera or previous pictures of that criminal that I am already having. For every criminal, I have given some ID no. and to increase the accuracy I have captured 20 frames per criminal. Frames that I captured are colored therefore to decrease memory usage I have converted that colored frames into Gray scale.
For training, I have used LBPH Face Recognizer and I train it such that it automatically maps the particular face with the corresponding  Face ID. Now,Trained Recognizer has been saved as yml file so that I can use it later during detection.
In the detecting phase, I have used already trained yml recognizer to get the corresponding  ID for the given face. 
Now it was time to use database (I named it as FaceBase). In that database I have made a table named ‘People’ and mark ‘ID’ attribute as Primary Key. Other attributes that I used were ‘Name’, ‘gender’, ‘Age’, ‘Criminal Records’.
Then I went back to the dataset phase and added some lines of code such that it takes ID and Name as input from user before it starts capturing. For this I have used concept of cursors in SQL.
After this, I added one method named getProfile() to detector program which will match the face to the corresponding ID and through that ID it will provide us with the Criminal Record information as I have already connected it to my FaceBase.
