# Codeforces_Codechef_Converter

## Introduction
**Converts the rating in between two popular competitive programming platforms- Codeforces and Codechef**
The project is currently online at this URL: https://linktr.ee/re4lvansh

#### About My Model
The "Codeforces to Codechef and Codechef to Codeforces Rating Converter" project aims to provide a reliable and user-friendly solution for converting ratings between Codeforces and Codechef, two prominent competitive programming platforms. By utilizing polynomial regression, along with popular Python libraries such as scikit-learn, matplotlib, mpld3, and NumPy, this project effectively addresses the challenge of rating conversion.

#### Project Overview
The primary goal of this project is to develop an accurate rating conversion model by leveraging polynomial regression. The conversion process involves establishing a mathematical relationship between Codeforces and Codechef ratings, taking into account the skewed data representation between higher ratings. Polynomial regression offers the advantage of capturing the non-linear correlations present in the data while avoiding the overfitting issues associated with higher-dimensional models.
![This is what our graph looks like](<Screenshot (322).png>)
#### Key Components
**Polynomial Regression:** Polynomial regression serves as the core algorithm in this project. It is chosen due to its ability to handle non-linear relationships between Codeforces and Codechef ratings. By fitting a polynomial function to the training data, the regression model can effectively estimate the conversion between the two rating scales.

**scikit-learn:** The scikit-learn library, a widely-used machine learning toolkit in Python, is employed to implement the polynomial regression model. It provides an extensive set of tools for data preprocessing, model training, evaluation, and prediction, simplifying the overall development process.

**matplotlib:** To visualize the relationship between Codeforces and Codechef ratings and provide interactive graphs, matplotlib is utilized. This powerful plotting library enables the creation of informative visualizations that aid in understanding the rating conversion process. Users can gain insights into the conversion formula and observe the trends and patterns between the two platforms.

**mpld3:** The mpld3 library is employed to seamlessly integrate the interactive matplotlib graphs into web frameworks. It enables the conversion of matplotlib plots to HTML and JavaScript, facilitating the embedding of interactive graphs into web pages. This integration enhances the user experience by allowing users to interact with the rating conversion tool directly from their browsers.

**NumPy:** NumPy, a fundamental library for numerical computing in Python, plays a crucial role in this project. It provides efficient data processing capabilities, including array operations and transformations. NumPy's array structures are employed for storing and manipulating the rating data, enabling seamless integration with scikit-learn and other components of the project.

#### Conclusion
The "Codeforces to Codechef and Codechef to Codeforces Rating Converter" project demonstrates the effectiveness of polynomial regression in accurately converting ratings between Codeforces and Codechef platforms. By incorporating scikit-learn, matplotlib, mpld3, and NumPy, the project offers an intuitive and efficient solution for competitive programmers seeking to translate their ratings between these two popular platforms.

The implementation of polynomial regression addresses the non-linear relationship between the rating scales, ensuring reliable and precise rating conversions. The interactive visualizations provided by matplotlib and mpld3 enhance the user experience, enabling users to explore and understand the rating conversion process in a more intuitive and engaging manner.

With its user-friendly interface and accurate rating conversion capabilities, this project empowers competitive programmers to compare their rankings, track their progress, and participate in contests across multiple platforms more effectively. It highlights the potential of polynomial regression and related libraries in solving real-world problems in the field of competitive programming.


## Features
#### Codeforces to Codechef rating converter:
1) The application takes as input a codeforce handle, which can be found on the profile page of any user on CodeForces platform.
2) Then it use the model to convert Codeforces rating to codechef rating following the predictions made by the model utilising polynomial regression
![Alt text](<Screenshot (323).png>)
#### Codechef to Codeforces rating converter:
1) The application takes as input a codechef handle, which can be found on the profile page of any user on the platform.
2) Then it use the model to convert Codechef rating to codeforces rating following the predictions made by the model utilising polynomial regression
![Alt text](<Screenshot (324).png>)
#### Codeforces Contest Submissions
The Codeforces User Information web application is a tool designed to fetch and display relevant information about a Codeforces user. With this application, users can enter a Codeforces username and retrieve their maximum rating, current rating, and the most recent contest submissions. The application provides a user-friendly interface that allows users to easily access and view the desired information.
![Alt text](<Screenshot (326).png>)
#### Codeclock
Keep track of upcoming four contests on Leetcode, Atcoder, Codeforces and Codechef with the Codeclock🕒
![Alt text](<Screenshot (327).png>)

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
