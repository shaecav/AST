#SHAE'S LATEST CODE
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import numpy as np
import plotly.graph_objects as go
import plotly.figure_factory as ff
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title('Accreditation Training')
st.subheader('Applying a DEI Lens to Current Accreditation Practices')

st.sidebar.title('Navigation')
page = st.sidebar.radio('', ('1. Introduction',
                                  '2. Explore the Map',
                                  '3. Explore Institutional Data',
                                  '4. Outcomes by Accreditor',
                                  '5. Conclusion'))

if page == "1. Introduction":
    lottie_url = "https://assets5.lottiefiles.com/packages/lf20_khtt8ejx.json"
    lottie_animation = load_lottieurl(lottie_url)
    st_lottie(lottie_animation, key="animation", height=500)

    st.subheader('Are higher education accrediting agencies adding diversity, equity, and inclusion requirements to ensure colleges are advancing educational access and balance?')
    st.markdown('Accreditation is a huge investment meant to benefit students. It is estimated that 73% of full-time college students in the United States use federal subsidies to pay for college, and The Department of Education (ED) specifies that an institution must be accredited by a nationally recognized accreditor for students to receive federal student aid. At the same time, critics suggested that the current accreditation process is ineffective because accreditors focus primarily on **college inputs**, rather than **student outcomes**. ')
    st.markdown('The following training is designed for professional accreditors to reflect on current practices and current situations revolving around accreditation through the lens of diversity, equity and inclusion metrics. The data used in this training were derived from Integrated Postsecondary Education Data System (IPEDS).')

    st.subheader('Start the training by navigating the sidebar.')


schools_filtered = pd.read_csv('data/filtered_IPEDS_WebApp.csv')
IPEDS = pd.read_csv('data/IPEDS_allAccred.csv')
map_data = IPEDS.groupby(['Geographic region', 'ACCREDAGENCY'], as_index=False).agg({
    'Name':"count", 'Latitude location of institution':"mean",
    'Longitude location of institution':"mean"
})

bar_data = pd.read_csv('data/graduation_rate_summarize_group_2.csv')


#Page 2 - Explore the Map
if page == "2. Explore the Map":
    st.subheader('Explore the Map')
    st.write("_This map represents the largest accreditation agencies in the U.S. by region._")
    fig = px.scatter_geo(map_data, color="ACCREDAGENCY",
                         hover_name="Geographic region",
                         lon='Longitude location of institution',
                         lat='Latitude location of institution',
                         projection="natural earth",
                         size="Name",
                         locationmode='USA-states',
                         )

    states_geojson = requests.get(
        "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_1_states_provinces_lines.geojson"
    ).json()
    fig.update_layout(height=200, margin={"r": 10, "t": 10, "l": 10, "b": 0},
                      width=900,
                      legend_itemclick="toggleothers")
    fig.update_traces(legendwidth=10, selector = dict(type='scattergeo'))
    fig.add_trace(
        go.Scattergeo(
            lat=[
                v
                for sub in [
                    np.array(f["geometry"]["coordinates"])[:, 1].tolist() + [None]
                    for f in states_geojson["features"]
                ]
                for v in sub
            ],
            lon=[
                v
                for sub in [
                    np.array(f["geometry"]["coordinates"])[:, 0].tolist() + [None]
                    for f in states_geojson["features"]
                ]
                for v in sub
            ],
            line_color="black",
            line_width=1,
            mode="lines",
            showlegend=False,
        )
    )

    fig.update_geos(fitbounds="locations",  visible=True, resolution=110,
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Black")

    st.plotly_chart(fig)

    st.write("In the map legend, click on the name of an accreditation agency to see only that one appear on the map.")
    q1 = st.radio(
        "Based on what you see here, do you think most schools are accredited regionally or nationally?",
        ('', 'Regionally', 'Nationally'))

    if q1!= '':
        labels = ['Regionally Accredited College or University', 'Nationally Accredited College or University']
        values = [85, 15]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig = px.pie(labels=labels, values=values, width=500.0,
                  color_discrete_sequence=px.colors.sequential.RdBu)

        st.plotly_chart(fig)

        st.subheader("85% of Colleges and Universities are Accredited Regionally.")
        st.write('The majority of schools are accredited **regionally**. In the regional accreditation process, each '
                     'agency reviews institutions in their own geographic areas. These schools also tend to be more '
                     'selective than nationally accredited schools.')
        st.text_input('Do you think there is value in a regional vs. national accreditation process? Why or why not?',
                  "Your response here.")

        if st.button("Submit"):
            st.write(
            "Thank you, your responses have been recorded. Please head to the next page using the sidebar to keep reflecting.")

#Page 3 HBCUs
if page == "3. Explore Institutional Data":
    visualization=st.sidebar.radio('View Institutional Data',
    options=['HBCUs',
    'Degree of Urbanization',
    'Public vs. Private Institutions'])

    if visualization== 'HBCUs':
        st.header("HBCUs by Accreditor")

        select_accred = st.selectbox('Select Accreditation Agency:',(schools_filtered['ACCREDAGENCY'].unique()))

        st.write('You selected:', select_accred)

        mask = schools_filtered['ACCREDAGENCY'] !=select_accred
        schools_filtered = schools_filtered[mask]

        fig1 = px.pie(schools_filtered, names='Historically Black College or University', width=500.0,
                      color_discrete_sequence=px.colors.sequential.RdBu)
        st.plotly_chart(fig1)

        st.number_input("What percentage of HBCUs does the New England Commission on Higher Education work with?")
        st.radio("Which agency accredits the fewest HBCUs?", ('Higher Learning Commission',
                                                          'New England Commission on Higher Education',
                                                          'Southern Association of Colleges',
                                                          'Middle States Commission on Higher Education'))
        st.text_input("As an accreditation agency employee, what does it mean to you when you see an accreditation agency working with more HBCUs?")
        if st.button("Submit"):
            st.write("Thank you, your responses have been recorded. Please head to the next page using the sidebar to keep reflecting.")

#Page 4 Degree of Urbanzation

    if visualization == 'Degree of Urbanization':
        st.header("Degree of Urbanization by Accreditor")

        select_accred = st.selectbox('Select Accreditation Agency:',
                                     (schools_filtered['ACCREDAGENCY'].unique()))

        st.write('You selected:', select_accred)

        mask = schools_filtered['ACCREDAGENCY'] != select_accred
        schools_filtered = schools_filtered[mask]

        fig5 = px.pie(schools_filtered, names='Degree of urbanization (Urban-centric locale)', width=500.0)
        st.plotly_chart(fig5)
#QUESTIONS
        st.number_input("What percentage of colleges accredited by the Southern Association of Colleges are located in large suburbs?")
        st.multiselect("Colleges accredited by these four agencies are most likely to be located in which of the following?", ('City: Large', 'Rural: Remote', 'Suburb: Midsize', 'Suburb: Large'))
        st.text_input(
        "What are the factors resulting in fewer accredited colleges in rural communities and what does this mean for students from these communities?")
        if st.button("Submit"):
            st.write(
            "Thanks for submitting. Your responses have been recorded. Continue your evidence-based reflections by jumping to the next page using the sidebar.")

#Page 5 Public vs. Private Institutions
    if visualization == 'Public vs. Private Institutions':
        st.header("Public vs Private Institutions by Accreditor")

        select_accred = st.selectbox('Select Accreditation Agency:',
                                     (schools_filtered['ACCREDAGENCY'].unique()))

        st.write('You selected:', select_accred)

        mask = schools_filtered['ACCREDAGENCY'] != select_accred
        schools_filtered = schools_filtered[mask]

        fig9 = px.pie(schools_filtered, names='Sector of institution', width=500.0)
        st.plotly_chart(fig9)

#QUESTIONS
        st.radio("Which type of institution are colleges accredited by these agencies more likely to be?",('Private', 'Public'))
        st.slider("Private institutions represent over what percentage of accredited colleges for all three agencies?", min_value=0, max_value=100)
        st.text_input("Are there any concerns about the higher accreditation rates of private institutions? Why do you think the rates are higher?")
        if st.button("Submit"):
            st.write("Thank you for your reflections. Please head to Section 4.")


if page == '4. Outcomes by Accreditor':
    st.header('Graduation Rates for a Bachelors Degree in 4 Years by Accreditor')
    fig = px.bar(bar_data, x='ACCREDAGENCY', y='Graduation rate - Bachelor degree within 4 years, total', width=800)
    fig.update_layout(
        xaxis_tickfont_size=10,
        yaxis=dict(
            title='Avg Percentage of Students who Graduate with a Bachelors Degree in 4 Years',
            titlefont_size=10,
            tickfont_size=11,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    st.plotly_chart(fig)

    st.write("Critics have suggested that the accreditation process is ineffective because "
             "accreditors focus primarily on college inputs rather than student outcomes.")
    st.text_input("What is one thing your organization could do to more closely examine student outcomes?")

    if st.button("Submit"):
        st.write("Thank you for submitting your responses. Now, we will conclude the training.")


if page == "5. Conclusion":
    st.title("You've completed the training!")
    lottie_url2 = "https://assets5.lottiefiles.com/private_files/lf30_atlgj83i.json"
    lottie_json = load_lottieurl(lottie_url2)
    st_lottie(lottie_json, height=350)

    st.markdown("Remember that this training wasn’t designed to criticize current accreditation practices, but to spark"
                " self reflection and critical thinking. As you look back at the findings and insights that you have "
                "just observed and the answers you submitted, we hope that you will also think about the kind of "
                "education system that you would hope to see in the future - and the changes that we would have to make "
                "to get there.")
    st.subheader("Additional resources on diversity, equity and inclusion through the lens of college accreditation:")
    resource1, resource2, resource3 = st.columns(3)

    with resource1:
        st.markdown("[![Foo](https://i.dell.com/is/image/DellContent/content/dam/uwaem/production-design-assets/en/services/Support-services/Networking/Campus-Branch-Switches/thumbnail-256x256.jpg?wid=640&fit=constrain)]"
                    "(https://www.higheredtoday.org/2021/01/13/refocusing-diversity-equity-inclusion-pandemic-beyond-lessons-community-practice/)")
        st.caption('Refocusing on DEI During the Pandemic and Beyond from Higher Education Today')

    with resource2:
        st.markdown("[![Foo](https://d26oc3sg82pgk3.cloudfront.net/files/media/edit/image/33032/square_thumb%402x.jpg)]"
                    "(https://www.chea.org/diversity-equity-and-inclusion-and-accreditation)")
        st.caption('Accrediation in the News by CHEA (Council for Higher Education Accrediation)')

    with resource3:
        st.markdown("[![Foo](https://www.usnews.com/dims4/USNEWS/68b0f1d/17177859217/thumbnail/256x256/quality/85/?url=https%3A%2F%2Fmedia.beam.usnews.com%2Fa0%2F84%2F03561d8d4c458238d4c477b3d3e0%2F210521-submitted.17__9.jpg)]"
                    "(https://www.insightintodiversity.com/do-u-s-accrediting-agencies-do-enough-to-assess-diversity-efforts-2/)")
        st.caption('Do U.S. Accrediting Agencies Do Enough to Assess Diversity Efforts? by Insights to Diversity')


