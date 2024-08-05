// Extract the username from the URL
const urlParts = window.location.pathname.split('/');
const username = urlParts[urlParts.length - 1];

// Fetch the rating history using Codeforces API
fetch(`https://codeforces.com/api/user.rating?handle=${username}`)
  .then(response => response.text())  // Use text() to get raw response
  .then(text => {
    console.log('API response:', text); // Log raw response for debugging

    try {
      const data = JSON.parse(text); // Parse the response as JSON
      if (data.status === "OK") {
        // Extract the ratings from the response
        let ratings = data.result.map(rating => rating.newRating);
        let maxRating = Math.max(...ratings); // Find the max rating
        let last5Ratings = ratings.slice(-5); // Get the last 5 ratings
        
        // Create an array with max rating and last 5 ratings
        let ratingsArray = [maxRating, ...last5Ratings];

        let predictedRating=predictCF(ratingsArray);

        updateProfile(predictedRating);
      } else {
        console.error('Error fetching ratings:', data.comment);
      }
    } catch (e) {
      console.error('Failed to parse JSON:', e);
    }
  })
  .catch(error => {
    console.error('Error fetching the user rating:', error);
  });


function predictCF(ratings) {
    const meanCF=[
        1825.4548387096775, 1746.483870967742, 1724.2967741935483,
        1706.7290322580645, 1687.8451612903225, 1673.1129032258063,
        3320132.9870967744, 3240073.1806451613, 3176540.212903226,
        3130736.206451613, 3096066.0935483873, 6850075030.780645,
        6621022125.341935, 6433519863.67742, 6358146350.793549,
        6273432344.7709675
    ];
    const stdCF=[
        543.2954963330126, 520.385074682782, 517.4335555948994,
        514.2658362044735, 531.8150655756895, 545.6369605454041,
        2059428.3109835437, 2037699.2440900842, 2006880.7417028772,
        2065441.2197304103, 2061161.943143167, 6700464578.839158,
        6604386290.136724, 6451091061.063176, 6696797797.619845,
        6607289433.721786
    ];
    const weightCF=[
        274.22418375460137, -205.5520544698708, -45.58081432031249,
        -62.044452546476826, 177.53208142169393, -211.88277700228528,
        353.8130129282163, 261.3225120036117, 464.60006971036586,
        -717.2342251541672, 467.7974294325564, -121.17488309021998,
        -222.8771810004437, -390.53114724576795, 474.5415221581281,
        -174.86475939264045
    ];

    let rawInput = [
        parseInt(ratings[0]), 
        parseInt(ratings[1]), 
        parseInt(ratings[2]),
        parseInt(ratings[3]), 
        parseInt(ratings[4]),
        parseInt(ratings[5]),
        parseInt(ratings[1] ** 2), 
        parseInt(ratings[2] ** 2),
        parseInt(ratings[3] ** 2), 
        parseInt(ratings[4] ** 2),
        parseInt(ratings[5] ** 2),
        parseInt(ratings[1] ** 3),
        parseInt(ratings[2] ** 3),
        parseInt(ratings[3] ** 3),
        parseInt(ratings[4] ** 3),
        parseInt(ratings[5] ** 3)
    ];

    for (let index = 0; index < rawInput.length; index++) {
        const element = rawInput[index];
        rawInput[index]=(element-meanCF[index])/stdCF[index];
    }

    var result=2046.8668984593405;
    for (let index = 0; index < rawInput.length; index++) {
        const element = rawInput[index];
        result+=(element*weightCF[index]);
    }

    return Math.max(parseInt(result),0);
}

function colorPicker(predictedRating){
    // Dynamically set the color based on the predictedRating value
    if (predictedRating >= 2500) {
        return 'rgb(208,1,27)'; //7*
    }
    else if (predictedRating >= 2200) {
        return 'rgb(255,127,0)'; // 6*
    }
    else if (predictedRating >= 2000) {
        return 'rgb(255,191,0)'; // 5*
    } 
    else if (predictedRating >= 1800) {
        return 'rgb(104,66,115)'; // 4*
    } 
    else if (predictedRating >= 1600) {
        return 'rgb(51,102,204)'; // 3*
    }
    else if (predictedRating >= 1400) {
        return 'rgb(30,125,34)'; // 2*
    }
    else {
        return '#666666'; // 1*
    }
}

function getStarHTML(rating) {
    let starsHTML = '';
    let numStars = 0;
    let starColor = colorPicker(rating); // Default color

    // Determine the number of stars and color based on rating
    if (rating >= 2500) {
        numStars = 7;
    } 
    else if (rating >= 2200) {
        numStars = 6;
    } 
    else if (rating >= 2000) {
        numStars = 5;
    } 
    else if (rating >= 1800) {
        numStars = 4;
    } 
    else if (rating >= 1600) {
        numStars = 3;
    } 
    else if (rating >= 1400) {
        numStars = 2;
    }
    else{
        numStars = 1;
    }

    // Generate star HTML
    for (let i = 0; i < Math.floor(numStars); i++) {
        starsHTML += `<span style="color:${starColor}; font-size:18px;">&#9733;</span>`; // Solid star
    }

    return starsHTML;
}


function updateProfile(predictedRating) {
    // Select the .main-info div
    const mainInfoDiv = document.querySelector('.info');

    if (mainInfoDiv) {
        // Find the <ul> element inside .main-info
        const ulElement = mainInfoDiv.querySelector('ul');

        if (ulElement) {
            // Create a new <li> element for the predicted CodeChef rating
            const predictedRatingElement = document.createElement('li');

            // Create the image element
            const ratingImage = document.createElement('img');
            ratingImage.src = 'https://codeforces.org/s/55478/images/icons/rating-24x24.png';
            ratingImage.alt = 'Predicted CodeChef rating';
            ratingImage.style.verticalAlign = 'middle';
            ratingImage.style.marginRight = '0.5em';

            // Create the text element for the label
            const ratingLabelText = document.createElement('span');
            ratingLabelText.textContent = 'Predicted CodeChef Rating: ';
            ratingLabelText.style.marginLeft = '5px';

            // Create the text element for the predicted rating
            const ratingValueText = document.createElement('span');
            ratingValueText.textContent = predictedRating;
            ratingValueText.style.fontWeight = 'bold';
            ratingValueText.style.marginBottom = '2px';

            // Create the opening bracket
            const openBracket=document.createElement('span');
            openBracket.textContent='(';
            openBracket.style.marginLeft='4px';
            ratingValueText.style.color = colorPicker(predictedRating);
            ratingValueText.style.fontSize = '14px';

            //For dynamic number of stars
            const starsElement = document.createElement('span');
            starsElement.innerHTML = getStarHTML(predictedRating);

            // Create the closing bracket
            const closeBracket=document.createElement('span');
            closeBracket.textContent=')';
            // closeBracket.style.marginLeft='4px';

            // Append the image, label, and rating value to the new <li> element
            predictedRatingElement.appendChild(ratingImage);
            predictedRatingElement.appendChild(ratingLabelText);
            predictedRatingElement.appendChild(ratingValueText);
            predictedRatingElement.appendChild(openBracket);
            predictedRatingElement.appendChild(starsElement);
            predictedRatingElement.appendChild(closeBracket);

            // Insert the new <li> element as the second child of the <ul>
            const secondChild = ulElement.children[1]; // Get the second child, if it exists
            if (secondChild) {
                ulElement.insertBefore(predictedRatingElement, secondChild);
            } else {
                // If there is no second child, append it as the last item
                ulElement.appendChild(predictedRatingElement);
            }
        }
    }
}