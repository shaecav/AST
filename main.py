import streamlit as st
import pandas as pd
import plotly.express as px

st.title('TRAINING FOR ACCREDITORS')

st.sidebar.title('Pages')
page = st.sidebar.radio('Steps', ('1. Introduction', '2. Explore the Map', '3. Agency Profiles', '4. Conclusion'))

schools = pd.read_csv('data/schools.csv')
schools_filtered = pd.read_csv('data/schools_filtered.csv')

st.write(schools_filtered)

if page == "3. Agency Profiles":
    tab1, tab2, tab3 = st.tabs(["HBCUs", "Degree of Urbanization", "Public vs. Private Institutions"])

    with tab1:
        st.header("HBCUs by Accreditor")
        col1, col2 = st.columns(2)

        with col1:
            st.write('Higher Learning Commission')
            mask = schools_filtered['ACCREDAGENCY'] != 'Higher Learning Commission'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Historically Black College or University', width=500.0)
            st.plotly_chart(fig)

        with col2:
            st.write('Middle States Commission on Higher Education')
            mask = schools_filtered['ACCREDAGENCY'] != 'Middle States Commission on Higher Education'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Historically Black College or University', width=500.0)
            st.plotly_chart(fig)

        col1, col2 = st.columns(2)

        with col1:
            st.write('New England Commission on Higher Education')
            mask = schools_filtered['ACCREDAGENCY'] != 'New England Commission on Higher Education'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Historically Black College or University', width=500.0)
            st.plotly_chart(fig)

        with col2:
            st.write('Southern Association of Colleges')
            mask = schools_filtered[
                       'ACCREDAGENCY'] != 'Southern Association of Colleges and Schools Commission on Colleges'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Historically Black College or University', width=500.0)
            st.plotly_chart(fig)

    with tab2:
        st.header("Degree of Urbanization")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.write('Higher Learning Commission')
            mask = schools_filtered['ACCREDAGENCY'] != 'Higher Learning Commission'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Degree of urbanization (Urban-centric locale)', width=500.0)
            st.plotly_chart(fig)

        with col2:
            st.write('Middle States Commission on Higher Education')
            mask = schools_filtered['ACCREDAGENCY'] != 'Middle States Commission on Higher Education'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Degree of urbanization (Urban-centric locale)', width=500.0)
            st.plotly_chart(fig)

        col1, col2 = st.columns(2)

        with col1:
            st.write('New England Commission on Higher Education')
            mask = schools_filtered['ACCREDAGENCY'] != 'New England Commission on Higher Education'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Degree of urbanization (Urban-centric locale)', width=500.0)
            st.plotly_chart(fig)

        with col2:
            st.write('Southern Association of Colleges')
            mask = schools_filtered['ACCREDAGENCY'] != 'Southern Association of Colleges and Schools Commission on Colleges'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Degree of urbanization (Urban-centric locale)', width=500.0)
            st.plotly_chart(fig)

    with tab3:
        st.header("Public vs Private Institutionsr")
        col1, col2 = st.columns(2)
        with col1:
            st.write('Higher Learning Commission')
            mask = schools_filtered['ACCREDAGENCY'] != 'Higher Learning Commission'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Sector of institution', width=500.0)
            st.plotly_chart(fig)

        with col2:
            st.write('Middle States Commission on Higher Education')
            mask = schools_filtered['ACCREDAGENCY'] != 'Middle States Commission on Higher Education'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Sector of institution', width=500.0)
            st.plotly_chart(fig)

        col1, col2 = st.columns(2)

        with col1:
            st.write('New England Commission on Higher Education')
            mask = schools_filtered['ACCREDAGENCY'] != 'New England Commission on Higher Education'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Sector of institution', width=500.0)
            st.plotly_chart(fig)

        with col2:
            st.write('Southern Association of Colleges')
            mask = schools_filtered['ACCREDAGENCY'] != 'Southern Association of Colleges and Schools Commission on Colleges'
            schools_filtered = schools_filtered[mask]
            fig = px.pie(schools_filtered, names='Sector of institution', width=500.0)
            st.plotly_chart(fig)

