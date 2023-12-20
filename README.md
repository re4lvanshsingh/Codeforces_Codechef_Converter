# Codeforces_Codechef_Converter

## Introduction
**Converts the rating in between two popular competitive programming platforms- Codeforces and Codechef**
The project is currently online at this URL: https://linktr.ee/re4lvansh

#### About My Model
The "Codeforces to Codechef and Codechef to Codeforces Rating Converter" project aims to provide a reliable and user-friendly solution for converting ratings between Codeforces and Codechef, two prominent competitive programming platforms. Over 20 models are compared , using statistical methods of root mean square error, r2 score and other metrics for comparing the fields. Initially, we start out with simple methods like Lasso Regression, ElasticNet regression and ridge regression after utilizing a heatmap to decipher related features. Then, we move on to more complicated models like Decision Tree Regressor, LGMRegressor, Isotonic Regressor and so on. Finally, we settle at the Huber Regression model, with  R2 Score: 0.91 (approximately). 
The Huber regressor is a type of robust regression model used in statistics and machine learning. It is designed to be less sensitive to outliers in the data compared to traditional least squares regression. The Huber loss function is a compromise between the mean squared error (MSE) used in ordinary least squares regression and the mean absolute error (MAE) used in L1 regularization.The Huber regressor aims to minimize the sum of these Huber loss values for all data points. It is particularly useful when dealing with datasets that contain outliers, as it provides a balance between the robustness of L1 regularization (MAE) and the efficiency of L2 regularization (MSE).

#### Project Overview
The primary goal of this project is to develop an accurate rating conversion model by leveraging polynomial regression. The conversion process involves establishing a mathematical relationship between Codeforces and Codechef ratings, taking into account the skewed data representation between higher ratings. We compare results from over 20 models and use R2 score as metric for calculating Codeforces and Codechef ratings, while also reducing overfitting.

BeautifulSoup library is used to design web scrapers which fetch data from Codechef,Leetcode and Atcoder about their next four contests. Additionally, we also use Codeforces API for fetching information  on next four coding contests there. Codeclock supports competitive coders keep track of contests from top platforms, and the Rating Converter helps them to compare their ratings and evaluate progress.

Overall, the project also aims to show the increased importance of machine learning to compare stats for competitive programmers across a variety of prominent platforms.


#### Conclusion
The "Codeforces to Codechef and Codechef to Codeforces Rating Converter" project demonstrates the effectiveness of hubet regression in accurately converting ratings between Codeforces and Codechef platforms. By incorporating scikit-learn, matplotlib, mpld3, and NumPy, the project offers an intuitive and efficient solution for competitive programmers seeking to translate their ratings between these two popular platforms.

The implementation of huber regression addresses the non-linear relationship between the rating scales, ensuring reliable and precise rating conversions. The interactive visualizations provided by matplotlib and mpld3 enhance the user experience, enabling users to explore and understand the rating conversion process in a more intuitive and engaging manner.

With its user-friendly interface and accurate rating conversion capabilities, this project empowers competitive programmers to compare their rankings, track their progress, and participate in contests across multiple platforms more effectively. 


## Features
#### Codeforces to Codechef rating converter:
1) The application takes as input a codeforce handle, which can be found on the profile page of any user on CodeForces platform.
2) Then it use the model to convert Codeforces rating to codechef rating following the predictions made by the model utilising huber regression
3) It compares users' last 5 ratings to avoid overfitting and calculate the rating more accurately
![Alt text](<Screenshot (330)-1.png>) 
#### Codechef to Codeforces rating converter:
1) The application takes as input a codechef handle, which can be found on the profile page of any user on the platform.
2) Then it use the model to convert Codechef rating to codeforces rating following the predictions made by the model utilising huber regression
3) It compares users' last 5 ratings to avoid overfitting and calculate the rating more accurately
#### Codeforces Contest Submissions
The Codeforces User Information web application is a tool designed to fetch and display relevant information about a Codeforces user. With this application, users can enter a Codeforces username and retrieve their maximum rating, current rating, and the most recent contest submissions. The application provides a user-friendly interface that allows users to easily access and view the desired information.
![Alt text](<Screenshot (326).png>)
#### Codeclock
Keep track of upcoming four contests on Leetcode, Atcoder, Codeforces and Codechef with the Codeclock🕒. Beautiful Soup library is used for web scraping to gather information of next four contests from Leetcode, Atcoder and Codechef. For codeforces, we have used their API to gather information on the same
Gathers relevant user data from the Codechef website.
![Alt text](<Screenshot (331).png>)

## Installation
> git  clone re4lvanshsingh/Codeforces_Codechef_Converter
> cd Codeforces_Codechef_Converter

## Usage
Just visit the website and avail the features at your dispersal. As a Codechef user, having a hard time keeping up with discussions on ratings on Codeforces?Use our tool to get your projected rank and approach questions based on ranking and difficulty. 
Use the status tool to keep in check with contests , submissions and ratings, without the hassle of having to log in
**Missing Out contest reminders?!**
Fear Not! Codeclock is here to help you stay in sync with the latest updates on new rounds from top coding sites with dates! Happy coding , people!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests. Once the issue is assigned to you, only then do you start working on it. 
*To make sure updates are up to date:*
> git fetch upstream
> git merge upstream/main
> git checkout -b <feature-name> (to create and work on new branch)
> git switch <feature-name> (to work on specific branch)
> git add .
> git commit -m <meaningful-remark>
> git push
