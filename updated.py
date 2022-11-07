import streamlit as st
import pandas as pd
import plotly.express as px


st.title('TRAINING FOR ACCREDITORS')

st.sidebar.title('Pages')
page = st.sidebar.radio('Steps', ('1. Introduction', '2. Explore the Map', '3. HBCUs', '4. Degree of Urbanization',
                                  '5. Public vs. Private Institutions', '6. Conclusion'))

schools_filtered = pd.read_csv('data/filtered_IPEDS_WebApp.csv')
map_data = schools_filtered.groupby(['Geographic region', 'ACCREDAGENCY'], as_index=False).agg({
    'Name':"count", 'Latitude location of institution':"mean",
    'Longitude location of institution':"mean"
})

#Page 2 - Explore the Map
if page == "2. Explore the Map":
    fig = px.scatter_geo(map_data, color="ACCREDAGENCY",
                         hover_name="Geographic region",
                         lon='Longitude location of institution',
                         lat='Latitude location of institution',
                         projection="natural earth",
                         size="Name")
    fig.update_geos(
        visible=False, resolution=110, scope="usa",
        showcountries=True, countrycolor="Black",
        showsubunits=True, subunitcolor="Blue"
    )
    st.plotly_chart(fig)

if page == "3. HBCUs":
    st.header("HBCUs by Accreditor")
    st.write('Higher Learning Commission')
    mask = schools_filtered['ACCREDAGENCY'] != 'Higher Learning Commission'
    schools_filtered = schools_filtered[mask]
    fig1 = px.pie(schools_filtered, names='Historically Black College or University', width=500.0)
    st.plotly_chart(fig1)

    st.write('New England Commission on Higher Education')
    mask = schools_filtered['ACCREDAGENCY'] != 'New England Commission on Higher Education'
    schools_filtered = schools_filtered[mask]
    fig3 = px.pie(schools_filtered, names='Historically Black College or University', width=500.0)
    st.plotly_chart(fig3)

    st.write('Southern Association of Colleges')
    mask = schools_filtered['ACCREDAGENCY'] != 'Southern Association of Colleges and Schools Commission on Colleges'
    schools_filtered = schools_filtered[mask]
    fig4 = px.pie(schools_filtered, names='Historically Black College or University', width=500.0)
    st.plotly_chart(fig4)




    st.number_input("What perentage of HBCUs does the Southern Association of Colleges work with?")
    st.text_input("How do the accreditation agencies differ in the types of colleges they work with?")

if page == "4. Degree of Urbanization":
    st.header("Degree of Urbanization by Accreditor")
    col13, col23 = st.columns(2)

    with col13:
        st.write('Higher Learning Commission')
        mask = schools_filtered['ACCREDAGENCY'] != 'Higher Learning Commission'
        schools_filtered = schools_filtered[mask]
        fig5 = px.pie(schools_filtered, names='Degree of urbanization (Urban-centric locale)', width=100.0)
        st.plotly_chart(fig5)

    with col23:
        st.write('Middle States Commission on Higher Education')
        mask = schools_filtered['ACCREDAGENCY'] != 'Middle States Commission on Higher Education'
        schools_filtered = schools_filtered[mask]
        fig6 = px.pie(schools_filtered, names='Degree of urbanization (Urban-centric locale)', width=100.0)
        st.plotly_chart(fig6)

    col14, col24 = st.columns(2)

    with col14:
        st.write('New England Commission on Higher Education')
        mask = schools_filtered['ACCREDAGENCY'] != 'New England Commission on Higher Education'
        schools_filtered = schools_filtered[mask]
        fig7 = px.pie(schools_filtered, names='Degree of urbanization (Urban-centric locale)', width=100.0)
        st.plotly_chart(fig7)

    with col24:
        st.write('Southern Association of Colleges')
        mask = schools_filtered[
                   'ACCREDAGENCY'] != 'Southern Association of Colleges and Schools Commission on Colleges'
        schools_filtered = schools_filtered[mask]
        fig8 = px.pie(schools_filtered, names='Degree of urbanization (Urban-centric locale)', width=100.0)
        st.plotly_chart(fig8)

if page == "5. Public vs. Private Institutions":
    st.header("Public vs Private Institutions by Accreditor")
    col15, col25 = st.columns(2)

    with col15:
        st.write('Higher Learning Commission')
        mask = schools_filtered['ACCREDAGENCY'] != 'Higher Learning Commission'
        schools_filtered = schools_filtered[mask]
        fig9 = px.pie(schools_filtered, names='Sector of institution', width=500.0)
        st.plotly_chart(fig9)

    with col25:
        st.write('Middle States Commission on Higher Education')
        mask = schools_filtered['ACCREDAGENCY'] != 'Middle States Commission on Higher Education'
        schools_filtered = schools_filtered[mask]
        fig10 = px.pie(schools_filtered, names='Sector of institution', width=500.0)
        st.plotly_chart(fig10)

    col16, col26 = st.columns(2)

    with col16:
        st.write('New England Commission on Higher Education')
        mask = schools_filtered['ACCREDAGENCY'] != 'New England Commission on Higher Education'
        schools_filtered = schools_filtered[mask]
        fig11 = px.pie(schools_filtered, names='Sector of institution', width=500.0)
        st.plotly_chart(fig11)

    with col26:
        st.write('Southern Association of Colleges')
        mask = schools_filtered[
                   'ACCREDAGENCY'] != 'Southern Association of Colleges and Schools Commission on Colleges'
        schools_filtered = schools_filtered[mask]
        fig12 = px.pie(schools_filtered, names='Sector of institution', width=500.0)
        st.plotly_chart(fig12)