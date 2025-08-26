import re
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Evgeniy Kalinin - Data Analyst", layout="centered")

# Подгружаем статику
css = Path("public/css/style.css").read_text()
js = Path("public/js/script.js").read_text()
index_html = Path("public/index.html").read_text()

# Достаём контент из <body> исходного HTML
match = re.search(r"<body[^>]*>(.*)</body>", index_html, re.DOTALL)
body_html = match.group(1) if match else index_html

# Финальный HTML, который встраиваем в iframe
full_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Evgeniy Kalinin - Data Analyst</title>

<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" />

<style>
  /* Убираем внутренние отступы и любые внутренние скроллы в iframe */
  html, body {{
    margin: 0;
    padding: 0;
    overflow: visible;  /* важно: не даём iframe создавать свой скролл */
  }}
  {css}
</style>
</head>
<body>
{body_html}

<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
<script>{js}</script>

<!-- Автоподгон высоты iframe под контент -->
<script>
(function () {{
  function resize() {{
    try {{
      var h = Math.max(
        document.body.scrollHeight, document.documentElement.scrollHeight,
        document.body.offsetHeight,  document.documentElement.offsetHeight
      ) + 20; // небольшой запас
      if (window.frameElement) {{
        window.frameElement.style.height = h + "px";
        window.frameElement.style.overflow = "hidden";
      }}
    }} catch (e) {{}}
  }}

  // Обновляем высоту на загрузке и при любых изменениях верстки
  window.addEventListener("load", resize);
  new ResizeObserver(resize).observe(document.body);
  // Подстраховка на случай динамических шрифтов и др.
  setInterval(resize, 800);
}})();
</script>
</body>
</html>
"""

# Убираем внешние паддинги контейнера Streamlit
st.markdown(
    """
    <style>
      .block-container { padding-top: 0rem; padding-bottom: 0rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Встраиваем HTML: временная маленькая высота, без внутренней прокрутки
# JS внутри iframe сам выставит нужную высоту и уберёт двойной скролл.
st.components.v1.html(full_html, height=200, scrolling=False)
