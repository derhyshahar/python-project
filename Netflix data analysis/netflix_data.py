import pandas as pd 
import numpy as np 
import plotly.express as px
from textblob import TextBlob 
#import the data
raw_data_csv = pd.read_csv("C:/Users/shaha/Desktop/workspace/env/netflix_titles.csv")
raw_data_csv.shape #the data has 8807 rows and 12 columns
#lets check the column names:
raw_data_csv.columns
#('show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added',
# 'release_year', 'rating', 'duration', 'listed_in', 'description')
# we want to check which rating is most common among the platform
z = raw_data_csv.groupby(['rating']).size().reset_index(name = 'counts')
pie_chart = px.pie(z, values = 'counts',
                   names = 'rating',
                   title = 'Distribution of content rating on Netflix',
                   color_discrete_sequence= px.colors.qualitative.Set3)
pie_chart.show() 
# The chart shows that the majority of content on Netflix is categorized as "TV-MA", which means that most of the content is intended for mature & adult audiences.
# Now - lets see whos the top 5 successfull directors on the platform
# lets fill the null values before
raw_data_csv['director'].fillna('no director specified') #fills any missing values with the string 'no director specified'
filtered_directors = pd.DataFrame() #creats empty DataFrame
filtered_directors=raw_data_csv['director'].str.split(',',expand=True).stack() #'direcror' column split by ","
filtered_directors=filtered_directors.to_frame() #converts to DataFrame
filtered_directors.columns=['Director'] #assign the column name to the DataFrame
directors=filtered_directors.groupby(['Director']).size().reset_index(name='Total Content') # we want to find the number of times each director appears in the original DataFrame
directors=directors[directors.Director !='No Director Specified'] #filters the DataFrame where the 'Director' has no value ('no director specified') and removes them
directors=directors.sort_values(by=['Total Content'],ascending=False) #the 'total content' column in the DataFrame is sorted in a descending order
directorsTop5=directors.head()    # new DataFrame that contains the top 5 rows of the 'directors' DataFrame
directorsTop5=directorsTop5.sort_values(by=['Total Content']) #sort the data in ascending order
fig1=px.bar(directorsTop5,x='Total Content',y='Director',title='Top 5 Directors on Netflix') #create the Bar chart
fig1.show()
 # from this chart we can see the top 5 directors are:
 # 1 - Rajiv Chilaka 
 # 2 - Jan Suter
 # 3 - Raul Campos
 # 4 - Marcus Raboy
 # 5 - Suhas Kadav
 # now we will look for the top 5 Actors -
raw_data_csv['cast'] = raw_data_csv['cast'].fillna('No Cast Specified') # filling missing values with the str - 'no cast specified'
filterd_cast = pd.DataFrame #creating an empty DataFrame
filterd_cast = raw_data_csv['cast'].str.split(',', expand=True).stack() #split the values in the 'cast' column
filterd_cast = filterd_cast.to_frame() #converts to DataFrame
filterd_cast.columns = ['Actor']
actors = filterd_cast.groupby(['Actor']).size().reset_index(name= 'Total Content') #To find the number of times each actor appears in the original DataFrame
actors = actors[actors.Actor != 'No Cast Specified']
actors = actors.sort_values(by=['Total Content'], ascending=False)
actorsTop5 = actors.head()
actorsTop5 = actorsTop5.sort_values(by = ['Total Content'])
fig2=px.bar(actorsTop5, x= 'Total Content', y = 'Actor', title = 'Top 5 Actors on Netflix')
fig2.show()
#from this chart we can see that top 5 actors on Netflix are -
# 1 - Anupam Kher
# 2 - Rupa Bhimani
# 3 - Takashiro Sakurai
# 4 - Julie Tejwani
# 5 - Om Puri
#The next thing to analyze from the Data is the trend of production over the years on Netflix
df1= raw_data_csv[['type', 'release_year']] #create new DataFrame by selecting only the 'type' and 'release_year' columns from 'raw_data_csv' DF
df1 = df1.rename( columns={"release_year" : "Release Year"}) #change the name gor better visualization
df2 = df1.groupby(['Release Year', 'type']).size().reset_index(name= 'Total Content')
df2 = df2[df2['Release Year']>=2010] #we will analyse only the movies that released at 2010 and further
fig3 = px.line(df2, x= "Release Year", y = "Total Content", color= 'type', title = 'Trend of content produced since 2010 on Netflix')
fig3.show()
#the graph shows that there has been a decline in the production of the content of both movies and shows since 2020.
# at last - to conclude our analysis, well analyze the sentiment of content on Netflix (positive/negative/neutral)
dfx = raw_data_csv[['release_year', 'description']] #create the DF
dfx = dfx.rename(columns={'release_year':'Release Year'}) 
for index,row in dfx.iterrows():    
    z = row['description']
    testimonial = TextBlob(z)
    p = testimonial.sentiment.polarity
    if p==0:
        sent = 'Neutral'
    elif p>0:
        sent = 'Positive'
    else:
        sent = 'Negative'
    dfx.loc[[index,2],'Sentiment'] = sent # adds a new column called 'Sentiment' that assigns the value of sent to the 'Sentiment' column in the DataFrame dfx for the current row and the column index 2. 
dfx = dfx.groupby(['Release Year', 'Sentiment']).size().reset_index(name='Total Content') 
dfx = dfx[dfx['Release Year']>=2010] #since 2010
fig4 = px.bar(dfx, x ='Release Year', y= 'Total Content', color= 'Sentiment', title = 'Sentiment of content on Netflix')  
fig4.show()
# the graph shows that the overall positive content is always greater than the neutral and negative content combined


