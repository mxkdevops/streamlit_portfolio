try:
    import streamlit as st
    from PIL import Image
except ModuleNotFoundError as e:
    raise ImportError("Required module(s) missing. Please ensure 'streamlit' and 'Pillow' are installed.") from e

# Setting the page configuration
def configure_page():
    st.set_page_config(page_title="Mohammad Kamruzzaman - Portfolio", page_icon=":man_technologist:", layout="wide")

def main():
    configure_page()

    # Custom Styling using Streamlit's built-in features
    st.markdown(
        """
        <style>
        body {background-color: #f9f9f9;}
        .header {background-color: #003566; color: white; padding: 20px; text-align: center; border-radius: 10px;}
        .sub-header {color: #0077cc; text-align: center; margin-top: -10px;}
        .section-title {color: #003566; font-size: 24px; margin-top: 20px;}
        .card {background-color: white; padding: 15px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px;}
        .card:hover {box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.2);}
        .footer {text-align: center; margin-top: 30px; color: gray; font-size: 14px;}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header Section
    st.markdown("<div class='header'><h1>Mohammad Kamruzzaman</h1></div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'><h3>Consultant | IT Support Specialist</h3></div>", unsafe_allow_html=True)

    st.markdown(
        """
        Welcome to my portfolio website! I specialize in:
        - **IT Support**
        - **Microsoft 365 Setup**
        - **Power Automation**
        - **Excel Expertise**
        - **Dynamic Website Development**
        - **WordPress Website Design**
        - **AWS Setup**
        - **Hosting & DNS Configuration**

        I have extensive skills in Linux, Windows, and Web Server management.
        """
    )

    # About Section
    st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'>I am an experienced IT consultant with a passion for helping businesses streamline their operations through technology. "
        "Whether you need help setting up a new cloud environment, automating workflows, or building a professional website, I have the expertise to deliver solutions tailored to your needs.</div>",
        unsafe_allow_html=True
    )

    # Services Section
    st.markdown("<div class='section-title'>Services</div>", unsafe_allow_html=True)
    services = [
        "Microsoft 365 Setup",
        "Power Automation",
        "Excel and Data Analysis",
        "Dynamic Website Development",
        "WordPress Website Design",
        "AWS Cloud Setup",
        "Hosting Account and DNS Setup",
        "Linux and Windows Server Management",
    ]
    
    for service in services:
        st.markdown(f"<div class='card'>- {service}</div>", unsafe_allow_html=True)

    # Skills Section
    st.markdown("<div class='section-title'>Skills</div>", unsafe_allow_html=True)
    skills = {
        "Operating Systems": ["Linux", "Windows"],
        "Web Servers": ["Apache", "Nginx"],
        "Automation Tools": ["Power Automate"],
        "Cloud Platforms": ["AWS"],
        "Web Development": ["Dynamic Websites", "WordPress"],
    }

    for category, items in skills.items():
        st.markdown(f"<div class='card'><strong>{category}:</strong> {', '.join(items)}</div>", unsafe_allow_html=True)

    # Contact Section
    st.markdown("<div class='section-title'>Get in Touch</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card'>If you're interested in working with me or have any questions, feel free to reach out.</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div class='card'><strong>Email:</strong> mohammad.k@example.com</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><strong>Phone:</strong> +123 456 7890</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><strong>LinkedIn:</strong> <a href='https://linkedin.com/in/mohammad-kamruzzaman'>linkedin.com/in/mohammad-kamruzzaman</a></div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"An error occurred: {e}")
