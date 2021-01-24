import random
import pandas as pd 
import plotly.express as px
import plotly.figure_factory as ff



counter=[]
dice_ans=[]

for i in range(1,100):
    d1=random.randint(1,6)
    d2=random.randint(1,6)

    dice_ans.append(d1+d2)
    counter.append(i)

fig=ff.create_distplot([dice_ans],['result'])
#fig=px.bar(x=dice_ans, y=counter)
fig.show()
