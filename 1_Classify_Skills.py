import streamlit as st
import random
from scripts import classify_interface as ci

def iterator_session(iterator:iter):
    st.session_state.iterator = iterator


def render_page():
    st.title('Labeling')
    classifier = ci.LabelingInterface('/data/skills_dataset.parquet', '/skills_classified.parquet', current_dir='.')
    unclassified_skills = classifier.get_unclassified_skills()

    row = unclassified_skills[0]
    job, skill = row.job, row.skill
    
    st.write(job)
    st.write(skill)
    label = st.text_input('Give the label')
    
    new_label = [list(row.values) + [label]]
    classifier.save_new_classifications(new_label)
    

if __name__ == '__main__':
    render_page()