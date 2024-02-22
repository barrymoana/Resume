from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Barry Rerecich"
PAGE_ICON = ":wave:"
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
NAME = "Barry Rerecich"
DESCRIPTION = """
Graduate Software Engineer Specializing Machine Learning
"""
EMAIL = "barry@xander.co.nz \n :phone: +6427243227"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/barry-rerecich-5b2b68195/",
    "GitHub": "https://github.com/barrymoana",
    
}
PROJECTS = {
    "🏆 PDF GPT Chat - Upload PDF & Chat With It": "https://github.com/barrymoana/PDFChatter",
    "🏆 Dog Cat Classifer - Tensorflow CNN Classifier": "https://github.com/barrymoana/CNN_CatDog",
    "🏆 Fruit Classifier - Instance Segmentation Model": "https://github.com/barrymoana/FruitClassifier",
}








# --- LOAD CSS, PDF 
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)



#Hero Section
st.title(NAME)
st.write(DESCRIPTION)
st.write("📫", EMAIL)



# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")




# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas)
- 📊 Data Visualization: Streamlit, Plotly
- 📚 Modeling: Experience with Supervised Learning (Logistic Regression, Decision Trees), Unsupervised Learning, and familiarity with Neural Networks, including Convolutional Neural Networks (CNNs)
- 🗄️ Data-Preprocessing: Handling Missing Data, Data Cleaning, Feature Scaling with Python libraries like Numpy, and Scikit-learn
- 🤖 Computer Vision: Experience with OpenCV for image processing, TensorFlow, and Keras for building and training neural network models, understanding of convolutional neural networks (CNNs)   
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.markdown(f'<span style="color: red;">{project}</span> [GitHub Link]({link})', unsafe_allow_html=True)





# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Software Engineer | Yelavich Transport**")
st.write("12/2022 - 02/2023")
st.write(
    """
- ► Developed and implemented a computer vision system for license plate detection at gate entries using OpenCV, TensorFlow, and Keras.
- ► Designed a user-friendly UI for the system using Python and Streamlit, enhancing usability for security personnel.
- ► Conducted system testing under varied scenarios to ensure robustness and reliability.
- ► Collaborated with the security team to refine the system based on feedback, improving user satisfaction.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Manager | Under Armour - Westgate**")
st.write("05/2019 - 01/2020")
st.write(
    """
- ► Provided training, incentives, mentoring, and feedback to associates to meet and exceed sales goals
- ► Developed opening and closing procedures and daily store operations, including cash handling, inventory count, deposits, crisis management, and shift procedures to improve efficiency 
- ► Scheduled employees for shifts, considering shift preferences and availability to increase employee satisfaction
- ► Tracked inventory, and ordered merchandise and supplies according to corporate guidelines to maximize sales and maintain store appearance
"""
)




# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")
st.write("---")

# --- Uni 2
st.write(":books:","**Bachelor of Software Engineering Artificial Intelligence | Media Design School | AKL, NZ**")
st.write("02/2020 - 11/2023")
st.write(
    """
- ► Networking & Database Systems
- ► Human Centred Design
- ► Natural Language Processing & Speech Recognition
- ► Computer Vision
- ► Machine Learning
- ► Data Mining & Visualisation
"""
)

# --- Uni 2
st.write(":books:", "**Bachelor of Business Management | Campbellsville University | KY, USA**")
st.write("08/2016 - 06/2019")
st.write(
    """
- ► Management
- ► Accounting
- ► Marketing
- ► Economics
"""
)


# --- References ---
st.write('\n')
st.subheader("References")
st.write("---")

st.write("Dr.Ranpreet Kaur - Lecturer @ MDS")
st.write("📫","ranpreet.kaur@mediadesignschool.com")
st.write("---")

st.write("Logan Yelavich - Owner @ Yelavich Transport")
st.write("📫","loganyel@gmail.com")
