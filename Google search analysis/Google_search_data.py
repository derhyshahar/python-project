#3.5 billion searches are performed on Google daily, which means that approximately 40,000 searches are performed every second on Google. So Google search is a great use case for analyzing data based on search queries.
#For using Google data about daily search queries we will use Google Trends API
#The API known as pytrends
import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()
trends.build_payload(kw_list=["Machine Learning"]) #The keyword list is "Machine Learning"
data = trends.interest_by_region() #We want to categorize them by region
data = data.sort_values(by="Machine Learning", ascending = False)
data = data.head(10)
print(data)
# China                     100
# Ethiopia                   48
# Singapore                  47
# India                      37
# Tunisia                    27
# Pakistan                   26
# Hong Kong                  25
# Sri Lanka                  23
# South Korea                22
# Nepal                      22
# according to the above results, the search queries based on "Machine learning are mostly done in China"
# lets view it via Bar chart
data.reset_index().plot(x="geoName",
                        y= "Machine Learning",
                        figsize= (15,12), kind = "bar")
plt.style.use('fivethirtyeight')
plt.show() 

data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Machine Learning'])
data = data.interest_over_time() #returns a DataFrame containing the historical popularity of the search term "Machine Learning" over time.
fig, ax = plt.subplots(figsize = (15,12))
data['Machine Learning'].plot()
plt.style.use('fivethrityeight')
plt.title('Total Google Searches for Maching Learning',
          fontweight = 'bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()