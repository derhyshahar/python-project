import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv("billionaire_list_20yrs.csv")
data.isnull().sum() #the missing values :
# last_name                 10850
# gender                    11892
# permanent_country         47691
# company                   25500
# wealth_source_details     10922
# industry                     49
# state                    193179
# headquarters             218714
data = data.dropna()
df = data.sort_values( by= ["annual_income"], ascending = False)
df = df.drop_duplicates("name").head(10) # we got the top 10 billionaires in the world by annual income
# Elon Musk
# Jeff Bezos
# Bill Gates
# Warren Buffet
# Larry Page
# Sergey Brin
# Larry Ellison
# Mark Zuckerberg
# Steve Ballmer
# Michael Bloomberg
plt.figure (figsize = (10,8))
plt.pie(df['annual_income'],
       labels = df['name'].values,
       textprops = {'size' : 'small',
                    'fontweight' : 'bold',
                    'rotation' : 'horizontal'})
plt.show()

a = df["main_industry"].value_counts().head(5)
index = a.index
a.drop_duplicates 
source = a.values
costume_colors = ["skyblue", "green", "red", "pink", "yellow"]
plt.figure(figsize = (5,5))
plt.pie(source, labels=index, colors = costume_colors)
central_circle = plt.Circle((0,0), 0.5, color = 'white')
plt.gca().add_artist(central_circle)
plt.rc('font', size = 12)
plt.title("Top 5 domains to become a Billionaire", fontsize = 20)
plt.show() 




 
