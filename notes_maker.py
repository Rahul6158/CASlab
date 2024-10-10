import streamlit as st

# HTML Template
html_template = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Data Structures</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: Verdana, Geneva, Tahoma, sans-serif; background-color: #f4f4f4; color: #333; }}
        .sidebar {{ width: 250px; background-color: #3a6cf4; height: 100vh; padding-top: 20px; position: fixed; top: 0; left: 0; box-shadow: 2px 0 5px rgba(0, 0, 0, 0.2); overflow-y: auto; transition: width 0.3s ease; }}
        .sidebar h2 {{ color: white; text-align: center; margin-bottom: 15px; font-size: 24px; font-family: cursive; }}
        .sidebar ul {{ list-style: none; padding-left: 0; }}
        .sidebar ul li {{ margin: 10px 0; }}
        .sidebar ul li a {{ color: white; text-decoration: none; padding: 10px; display: block; font-size: 16px; transition: background-color 0.3s ease; border-radius: 5px; }}
        .sidebar ul li a:hover {{ background-color: #ffffff; color: #3a6cf4; }}
        .content {{ margin-left: 260px; padding: 30px; transition: margin-left 0.3s ease; }}
        section {{ display: none; margin-bottom: 50px; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); }}
        section.active {{ display: block; }}
        section h2 {{ font-size: 28px; margin-bottom: 10px; color: #3a6cf4; text-align: center; }}
        section p {{ font-size: 16px; line-height: 1.6; margin-top: 10px; }}
        section img {{ max-width: 100%; height: auto; margin: 20px 0; }}
    </style>
</head>

<body>
    <!-- Sidebar -->
    <div class="sidebar">
        <h2>{heading}</h2>
        <ul>
            <li><a href="#" onclick="showSection('intro1')">{section1}</a></li>
            <li><a href="#" onclick="showSection('intro2')">{section2}</a></li>
            <li><a href="#" onclick="showSection('impl1')">{section3}</a></li>
        </ul>
    </div>

    <!-- Main Content -->
    <div class="content">
        <section id="intro1" class="active">
            <h2>{section1_title}</h2>
            <p>{section1_content}</p>
        </section>

        <section id="intro2">
            <h2>{section2_title}</h2>
            <p>{section2_content}</p>
        </section>

        <section id="impl1">
            <h2>{section3_title}</h2>
            <p>{section3_content}</p>
        </section>
    </div>
</body>

</html>
"""

# Streamlit input fields
st.title('Dynamic HTML Structure Generator')

# Get inputs for dynamic content
heading = st.text_input('Enter the heading for the sidebar:')
section1 = st.text_input('Enter text for Section 1 link:')
section2 = st.text_input('Enter text for Section 2 link:')
section3 = st.text_input('Enter text for Section 3 link:')
section1_title = st.text_input('Enter the title for Section 1:')
section1_content = st.text_area('Enter content for Section 1:')
section2_title = st.text_input('Enter the title for Section 2:')
section2_content = st.text_area('Enter content for Section 2:')
section3_title = st.text_input('Enter the title for Section 3:')
section3_content = st.text_area('Enter content for Section 3:')

# When the user clicks 'Generate HTML'
if st.button('Generate HTML'):
    # Replace placeholders with user input
    structured_html = html_template.format(
        heading=heading,
        section1=section1,
        section2=section2,
        section3=section3,
        section1_title=section1_title,
        section1_content=section1_content,
        section2_title=section2_title,
        section2_content=section2_content,
        section3_title=section3_title,
        section3_content=section3_content
    )

    # Display the structured HTML
    st.code(structured_html, language='html')

    # Option to download the generated HTML
    st.download_button('Download HTML', data=structured_html, file_name='structured.html', mime='text/html')
 
