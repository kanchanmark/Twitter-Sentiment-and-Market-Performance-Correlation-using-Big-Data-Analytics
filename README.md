# Twitter-Sentiment-and-Market-Performance-Correlation-using-Big-Data-Analytics

The aim of this project was to investigate the relationship between public sentiment and performance of financial markets using Big Data Analytics tools. 

Aggregation of Public Sentiment (Opinion) on companies of interest:
Implemented Twitter's public Streaming API in Python using Tweepy - open source library to connect to Twitter platform. Used Python packages - Json and TextBlob to parse JSON format data to get the labels of choice - timestamp and tweet text. 
Collected Tweets 24/7 for 2 months for 5 companies of choice and stored this data on HDFS (Hadoop distributed file system) for further processing. 

Aggregation of Financial performance data of companies of interest:
Used Yahoo API to get current as well as historical dump of stock quotes for companies of choice and stored these in HDFS.

Sentiment Analysis of tweets:
Passed each and every tweet through the VADER sentiment analysis package methods in Python (specifically attuned to sentiments expressed in social media) in order to get the sentiment score:-
1.	Positive Score: Proportion of text that falls in the positive category.
2.	Negative Score: Proportions of text that fall in the negative category.
3.	Compound Score: Computed by summing the valence scores of each word in the lexicon, adjusted according to the rules, and then normalized to be between -1 (most extreme negative) and +1 (most extreme positive).

Methods to find the correlation between the two: 
Developed script in PySpark to aggregate sentiment score for each day for each company and find out association between the public sentiments and market performance using ‘Statistical Correlation algorithms’- Pearson Correlation and Spearman Correlation.

Visualization of results: 
Developed an interactive web - application using Django framework (Jinja2 Template) and connecting it to Amazon RDS for MySQL. Visualizations developed using JavaScript (Chart.js), HTML, CSS and Tableau to help understand the correlation better.
