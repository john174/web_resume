import streamlit as st

st.set_page_config(
    page_title="John Doe - Resume",
    page_icon=":briefcase:",
    layout="wide",
)

# Apply a custom font and background color
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    .stApp {background-color: #f5f5f5;}
    html, body, [class*="css"]  {font-family: 'Roboto', sans-serif;}
    </style>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.image("https://www.gravatar.com/avatar/?d=mp&s=200", width=160)
    st.markdown("## Contact")
    st.markdown(
        """
        **Email:** john.doe@example.com  
        **Phone:** +1 555 123 4567  
        **LinkedIn:** [linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)
        """
    )
    st.download_button(
        "Download as PDF",
        data=b"",
        file_name="resume.pdf",
        disabled=True,
        help="Add a resume.pdf file to enable downloads",
    )

st.title("John Doe")
st.caption("Data Scientist")

about, experience, education, skills, projects = st.tabs(
    ["About", "Experience", "Education", "Skills", "Projects"]
)

with about:
    st.write(
        "Experienced data scientist with a passion for deriving insights from data and deploying machine learning models to production."
    )

with experience:
    exp1 = st.container()
    with exp1:
        left, right = st.columns([3, 1])
        with left:
            st.subheader("Senior Data Scientist, Acme Corp")
            st.caption("2022 - Present")
            st.write(
                """- Built machine learning pipelines to predict customer churn.
- Led a team of five engineers.
"""
            )
        with right:
            st.markdown("San Francisco, CA")
    exp2 = st.container()
    with exp2:
        left, right = st.columns([3, 1])
        with left:
            st.subheader("Data Analyst, Globex")
            st.caption("2020 - 2022")
            st.write(
                """- Analyzed sales data to uncover trends.
- Created dashboards for leadership.
"""
            )
        with right:
            st.markdown("Remote")

with education:
    edu = st.container()
    with edu:
        st.subheader("B.S. in Computer Science")
        st.caption("University of Example, 2016 - 2020")

with skills:
    st.write("Hover to view a summary of skill categories.")
    with st.popover("Skills overview"):
        st.write(
            "Proficient in machine learning, data engineering, and visualization."
        )
    skills_data = {
        "Python": 0.9,
        "Machine Learning": 0.85,
        "Data Visualization": 0.8,
        "SQL": 0.75,
    }
    for skill, score in skills_data.items():
        st.write(skill)
        st.progress(score)

with projects:
    project = st.container()
    with project:
        st.subheader("Awesome Project")
        st.write("A project showcasing advanced analytics.")
        st.page_link(
            "https://github.com/johndoe/awesome-project",
            label="GitHub Repo",
            icon=":material/github:",
        )
