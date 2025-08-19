import re
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Evgeniy Kalinin - Data Analyst", layout="centered")

# Load static assets
css = Path("public/css/style.css").read_text()
js = Path("public/js/script.js").read_text()
index_html = Path("public/index.html").read_text()

# Extract body content from the static HTML
match = re.search(r"<body[^>]*>(.*)</body>", index_html, re.DOTALL)
body_html = match.group(1) if match else index_html

# Combine everything into a single HTML document
full_html = f"""
<!DOCTYPE html>
<html lang=\"en\">
<head>
<meta charset=\"UTF-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
<title>Evgeniy Kalinin - Data Analyst</title>
<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
<link href=\"https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap\" rel=\"stylesheet\" />
<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css\" />
<style>{css}</style>
</head>
<body>
{body_html}
<script src=\"https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js\"></script>
<script>{js}</script>
</body>
</html>
"""

# Render the HTML inside the Streamlit app
height = len(body_html.splitlines()) * 18
st.components.v1.html(full_html, height=height, scrolling=False)
