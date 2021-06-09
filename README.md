# AI_MOVIE_RECOMMENDATION<br>
This is a project in which we can recommend user movie of his/her preferences.<br>
   
<h1>Problem Statement</h1><br>
– Recommendation systems imitate this social  process to enable quick filtering of the information on the web<br>
The major Problem which we currently have are as follows:<br>
– Recommendations are not personalized as per user attributes and all users see the same recommendations irrespective of their preferences<br>
– Another problem is that the number of reviews (which reflects the number of people who have viewed the movie) will vary for each movie and hence the average star rating will have discrepancies. <br>
– The system doesn’t take into account the regional and language preferences and might recommend movies in languages that a regional dialect speaking individual might not understand<br>
 
<h1>Dataset:</h1><br>
•	We have used Movie Lens Dataset by Group Lens<br>
•	This data set consists of:<br>
•	100,000 ratings (1-5) from 610 users on 193609  movies.<br>
•	Users of Movie Lens were selected randomly.<br>
•	All users rated at least 20 movies.<br>
•	Each user represented by a unique id.<br>

<h1>How to Run?</h1><br>
<b>1)Running CollaborativeFiltering.ipynb:</b><br><br>
    a)Download the "CollaborativeFiltering.ipynb" and "datasets" on your desktop<br>
    b)You can open this file on Google-colab/jupyter notebook etc.<br>
    c)In Google Colab add the two files:"movies.csv" and "ratings.csv"  from datasets folder in the run-time.<br>
And you are good to go,you can add your own movie in the last cell and get recommended movies.<br><br>

<b>2)Running Contentbasedfiltering.ipynb:</b><br><br>
    Here we tried another approach of recommendations system called content based filtering where movies are recommended based on their <br>genres. This is less efficient approach and has some disadvantages over collaborativefiltering approach.<br>
     a)Download the "ContentbasedFiltering.ipynb" and "datasets" on your desktop<br>
     b)You can open this file on Google-colab/jupyter notebook etc.<br>
     c)In Google Colab add the two files:"movies.csv" and "ratings.csv"  from datasets folder in the run-time.<br>
And you are good to go.Here you need to enter input in different format mentioned in that cell itself.<br><br>


<b>3)Website:</b><br><br>
    Finally we integrated CollaborativeFiltering and made a website using flask where you can enter the movie and get some recommendations.<br>
    Requirements:Python,Flask etc..<br>
    a)Download the "WEB-APPLICATION" folder on your desktop<br>
    b)Navigate to the folder and run the following command:<br>
        $ python main.py<br>
Just this and you are good to go<br>
Note:If you get some error regarding module not found, please download those modules using "pip install module name"<br>
<br>
<h1>Code</h1>
<b>Google Colab</b><br>
#importing modules<br>
#importing datasets<br>
<img src="./images/1.png" alt="datasets"/><br>
#making a new dataframe where columns represent users and rows represent movies<br>
<img src="./images/2.png" alt="dataframe"/><br>
 
#replacing the NaN values by 0, here NaN means the user has not rated that movie<br>

<img src="./images/3.png" alt="NaN"/><br>
#finally using KNN<br>
<img src="./images/4.png" alt="NaN"/><br>
 
#function to recommend movie<br>
#vvimp: your movie must be present in your dataset.<br>
<img src="./images/5.png" alt="NaN"/><br>
 
<b>Output:</b><br>
<img src="./images/6.png" alt="NaN"/><br>


<br>
<h1>Website</h1><br>

We also made Interface in the form of the website for the detector. The Backend is made using Flask, whereas the frontend is normal HTML and CSS and integrated python code from Google Colab<br><br>
<img src="./images/1.1.gif" alt="NaN"/><br><br>
Movie Recommendation System <br><br>
<img src="./images/1.2.gif" alt="NaN"/><br><br>
 

Short Demo (Please Give it sometime to Load 😃)<br><br>
<img src="./images/1.3.gif" alt="NaN"/><br>
 
<h1>References</h1><br>
Dataset and Features:<br>
•	https://files.grouplens.org/datasets/movielens/ml-latest-small.zip<br>

<b>Research Papers:</b><br>
•	For  Movie Recommendation System:<br>
•	https://www.itm-conferences.org/articles/itmconf/pdf/2017/04/itmconf_ita2017_04008.pdf<br>
•	https://research.netflix.com/research-area/recommendations<br>
<b>Future Scope</b><br>
•	Integration of this service in a form of plugin in Mobile apps to Reduce user time to search movie of his/her preferences.<br>
•	Implementing more Functionality Like Hybrid MRS in order to Pull over more Justified Recommendation for User and will also working to get over better accuracy.<br>

