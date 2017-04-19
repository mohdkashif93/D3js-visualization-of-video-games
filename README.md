# Data Visualization Project
# Udacity Data Analyst Nanodegree
#### By Mohammed Kashif

## Summary

I wish to demonstrate the growth of Video Game sales over the past 10 years for different genres of video games over different gaming platforms . To demonstrate the sales , I have created a Sales Dashboard using D3.js for the dataset containing information regarding the video game sales over the past decade .

## Design
By comparing the sales over different platforms , it thus makes it easy for us to compare the sales of a particular genre of games over different gaming consoles available in the market . The performance of that particular genre can be viewed through a separate graph , making it easier for us to analyse the trends for that particular genre . 

####Dataset collection
The data set made available through [Kaggle](https://www.kaggle.com/) and can be accesse through [this link](https://www.kaggle.com/gregorut/videogamesales) . I had to extract the data of last 10 years from this complete dataset and perform different analysis to come up with the final design . 

####Visualization design
I decided to make to highlight the key features and take away points that could be analysed through this dataset . The first was grouping the sales based on genre of video games . Secondly, how well a particular genre performs over different gaming platforms available in the market . Finally , I also wanted to visualize the trends for a particular genre over the decade .

### Initial Design
Initial design was to show a pie chart of global sales based on the genre of each video game and corresponding to each genre I wish to know the global sales of video game’s platform which will be a bar chart. I had the sales breakdown based on year as well. And hence I decided to add a line plot of sales breakup group by year. I included last 10 years data to keep the visualization concise. This was thought a dashboard for video game sales analysis.

### Coded Sketch - Take 1
My first sketch was as I planned, i.e. a dashboard showing sales based on genre in a pie chart, sales grouped by platform in a bar graph and  Yearly sales in a line plot.
![Take 1](https://github.com/mohdkashif93/D3js-visualization-of-video-games/blob/master/TAKE1.png)


(Interactive Version: http://bl.ocks.org/mohdkashif93/8a5f5b42c886ceb2144296ef80afa50b)


### Coded Sketch - Take 2
After one self-reflection and taking feedback from discussion forum, I feel my visualization fails to clarify the platform names (x labels of bar chart) due to its small size. I made the following changes:

- Increased the size of charts to make most of the browser screen.
- Changed the font-weight to bold where-ever possible.

![Take 2](https://github.com/mohdkashif93/D3js-visualization-of-video-games/blob/master/TAKE2.png)

(Interactive Version: http://bl.ocks.org/mohdkashif93/raw/ebc80a782bbe6d52ed85f6fa62282e10/)

### Coded Sketch - Take 3
This version involved following major changes:
Increased the size of pie chart to make all labels clearly visible.
Placed the y labels above bar chart in order to make it clearly visible.
Updated necessary label and title, including units for sales.
A major change in this version is in the line plot. I re-arrange the key points in order of year (which i missed in previous versions :( )
For more details on the data, I included the dataset link as well.

![Take 3](https://github.com/mohdkashif93/D3js-visualization-of-video-games/blob/master/TAKE3.png)

(Interactive Version: http://bl.ocks.org/mohdkashif93/raw/a5e345a126c889a1379c8ef1b18c5a3a)

## Feedback

### Friend 1 Feedback

#### Friend 1 provided the following feedback after reviewing Take 1:
"You should improve the readability of the graph . Especially the one showing the sales at the top . It is not clear exactly what the line graph is representing "

### Friend 2 Feedback

#### Friend 2 provided the following feedback after reviewing Take 2:
"The points on the line graph should be displayed when we hover it . Also the units on the bar chart should be displayed on top of the bar for better readability .”


### Udacity Forum Feedback
(Details: https://discussions.udacity.com/t/p6-seeking-feedback-for-d3js-visualization/240993)

####Review 1
I posted my take 1 visualization on Udacity Forum and "mohammad_48426351372" provided the following feedback:

"Hi,

It is looking interesting to me. As the visualization is very interactive. It would be better if you would have include the unit for the score. Also show the x axis labels of the bar plot is not readable."

### Future Work
I am glad that my friends were able to clearly understand correlations I am trying to portray in the visualization. Although I do understand that there is huge scope for improvement . I can add region wise sales or even add a simple timeline bar at the top that controls the sales over different years .

##### I will definitely work on a new visualization as my future work. 

## Resources

https://www.kaggle.com/
https://github.com/d3/d3/wiki/Gallery
https://www.kaggle.com/gregorut/videogamesales
https://bl.ocks.org/mbostock/3885304
Udacity’s course on Data Visualization helped me a lot in understanding the nuts and bolts of D3.js . 
