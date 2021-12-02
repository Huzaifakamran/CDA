import streamlit as st
import pymongo
import pandas as pd
#from streamlit_pandas_profiling import st_profile_report
#from pandas_profiling import ProfileReport
from pandas_profiling import ProfileReport
from streamlit_metrics import metric, metric_row
from streamlit_pandas_profiling import st_profile_report
karachiAI = "https://scontent.fkhi22-1.fna.fbcdn.net/v/t39.30808-6/219696940_538744634235861_2620116542391875630_n.png?_nc_cat=108&_nc_rgb565=1&ccb=1-5&_nc_sid=09cbfe&_nc_ohc=XlRl-xOa_s8AX9UUxL9&_nc_ht=scontent.fkhi22-1.fna&oh=a464c8554a85a70b212a31c7a6a7db04&oe=61AD3C0C"
client = pymongo.MongoClient("mongodb+srv://huzaifa:huzaifa123@cluster0.lbsdo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.customer_complaints
cursor_items = db.complaints.find()

all_records = []
for item in cursor_items:
    del item['_id']
    all_records.append(item)
df = pd.DataFrame(all_records)
# df1 = df['state'].agg('sum')
# #
# states = db.complaints.distinct('state').length
# print(states)
st.set_page_config(layout="wide")

st.title('CDA BATCH 1 FINAL PROJECT(Consumer Financial Protection Bureau)')
st.text("")
with st.container():
    col1, col2,col3,col4 = st.columns((1,1,1,1))
    col1.image(karachiAI,width = 200)
    st.text("")
    col2.metric("Total Complaints", cursor_items.count())
    col3.metric("Timely Done Complaints", db.complaints.count_documents({ "timely": "Yes"}))
    col4.metric("Timely Not Done", db.complaints.count_documents({ "timely": {"$ne":"Yes"}}))

    # col5, col6,col7,col8 = st.columns(4)

    # col6.metric("Total States", db.complaints.count_documents({"state":{}}))
    # col7.metric("Timely Not Done", db.complaints.count_documents({ "timely": {"$ne":"Yes"}}))
    # col8.metric("Timely Not Done", db.complaints.count_documents({ "timely": {"$ne":"Yes"}}))
with st.container():
   profile = ProfileReport(df,

                        title="Financial Consumer Data",

        dataset={

        "description": "This is the Demo of AI Summit 21",
        "Demo URL": "https://github.com/mustafaali96/AISummit21"

    }
)
st_profile_report(profile)


