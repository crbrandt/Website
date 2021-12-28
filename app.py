#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st

import html5lib

import webbrowser

from datetime import date
from datetime import datetime


# In[ ]:


##Updating Page Logo and Tab Title
st.set_page_config(page_title='Cole Brandt',
                   page_icon='https://media-exp1.licdn.com/dms/image/C5603AQFnSHiUxeXpVw/profile-displayphoto-shrink_800_800/0/1595044910016?e=1646265600&v=beta&t=081oEk-qqeM0dkpDQ6jwFLdqQTQnQMffaWtRN1IptL4',
                   layout="wide")



##Creating Functions
def highlight(text):
     st.markdown(f'<p style="text-align: center;color:#013369;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
def teamcolor(text):
     if 'Arizona' in text:
         st.markdown(f'<p style="text-align: center;color:#97233F;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Atlanta' in text:
         st.markdown(f'<p style="text-align: center;color:#A71930;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Baltimore' in text:
         st.markdown(f'<p style="text-align: center;color:#241773;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Buffalo' in text:
         st.markdown(f'<p style="text-align: center;color:#00338D;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Carolina' in text:
         st.markdown(f'<p style="text-align: center;color:#0085CA;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Chicago' in text:
         st.markdown(f'<p style="text-align: center;color:#C83803;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Cincinnati' in text:
         st.markdown(f'<p style="text-align: center;color:#FB4F14;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Cleveland' in text:
         st.markdown(f'<p style="text-align: center;color:#FF3C00;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Dallas' in text:
         st.markdown(f'<p style="text-align: center;color:#003594;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Denver' in text:
         st.markdown(f'<p style="text-align: center;color:#FB4F14;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Detroit' in text:
         st.markdown(f'<p style="text-align: center;color:#0076B6;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Green Bay' in text:
         st.markdown(f'<p style="text-align: center;color:#203731;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Houston' in text:
         st.markdown(f'<p style="text-align: center;color:#A71930;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Indianapolis' in text:
         st.markdown(f'<p style="text-align: center;color:#002C5F;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Jacksonville' in text:
         st.markdown(f'<p style="text-align: center;color:#006778;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Kansas City' in text:
         st.markdown(f'<p style="text-align: center;color:#E31837;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Las Vegas' in text:
         st.markdown(f'<p style="text-align: center;color:#A5ACAF;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Chargers' in text:
         st.markdown(f'<p style="text-align: center;color:#0080C6;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Rams' in text:
         st.markdown(f'<p style="text-align: center;color:#003594;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Miami' in text:
         st.markdown(f'<p style="text-align: center;color:#008E97;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Minnesota' in text:
         st.markdown(f'<p style="text-align: center;color:#4F2683;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'New England' in text:
         st.markdown(f'<p style="text-align: center;color:#002244;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'New Orleans' in text:
         st.markdown(f'<p style="text-align: center;color:#D3BC8D;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Giants' in text:
         st.markdown(f'<p style="text-align: center;color:#0B2265;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Jets' in text:
         st.markdown(f'<p style="text-align: center;color:#125740;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Eagles' in text:
         st.markdown(f'<p style="text-align: center;color:#004C54;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Steelers' in text:
         st.markdown(f'<p style="text-align: center;color:#FFB612;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'San Francisco' in text:
         st.markdown(f'<p style="text-align: center;color:#AA0000;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Seahawks' in text:
         st.markdown(f'<p style="text-align: center;color:#69BE28;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Buccaneers' in text:
         st.markdown(f'<p style="text-align: center;color:#D50A0A;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Titans' in text:
         st.markdown(f'<p style="text-align: center;color:#4B92DB;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     elif 'Washington' in text:
         st.markdown(f'<p style="text-align: center;color:#773141;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
     else:
         st.markdown(f'<p style="text-align: center;color:#575757;font-size:26px;border-radixus:2%;">{text}</p>', unsafe_allow_html=True)
def color(text):
     st.markdown(f'<p style="color:#013369;font-size:20px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)
def accuracy(text):
     st.markdown(f'<p style="color:#013369;font-size:15px;border-radius:2%;">{text}</p>', unsafe_allow_html=True)


# In[2]:


current_date = date.today()

resume_url = 'https://drive.google.com/file/d/1hcbLlZ1DqYs6hHQeBNta0lnkDmFnlYvj/view?usp=sharing'
nfl_url = 'bit.ly/colebrandt_nfl'


# In[ ]:


col_title, col_logo = st.beta_columns([4,1])
with col_title:
  st.title('Cole Brandt')
  st.markdown(' ## Analyst')
with col_logo:
  st.image("https://media-exp1.licdn.com/dms/image/C5603AQFnSHiUxeXpVw/profile-displayphoto-shrink_800_800/0/1595044910016?e=1646265600&v=beta&t=081oEk-qqeM0dkpDQ6jwFLdqQTQnQMffaWtRN1IptL4")
st.write("#")


# In[ ]:


st.write('Forward-thinking and skilled analyst with a B.A. in Business Administration and concentrations in Information Systems and Finance, along with a specialization in Market Analytics.') 

st.write('Also has earned a Master of Science in Data Science from Northwestern University.')

st.write('Self-driven with a passion for analytics, process improvement, and all things data.')





if st.button('View Resume'):
    webbrowser.open_new_tab('https://drive.google.com/file/d/1hcbLlZ1DqYs6hHQeBNta0lnkDmFnlYvj/view?usp=sharing')

    
webbrowser.open_new_tab('resume_url')
    

#Resume: https://drive.google.com/file/d/1hcbLlZ1DqYs6hHQeBNta0lnkDmFnlYvj/view?usp=sharing

