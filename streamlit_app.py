import re
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Evgeniy Kalinin - Data Analyst", layout="centered")

# Статика
css = Path("public/css/style.css").read_text()
js = Path("public/js/script.js").read_text()
index_html = Path("public/index.html").read_text()

# Контент из <body>
match = re.search(r"<body[^>]*>(.*)</body>", index_html, re.DOTALL)
body_html = match.group(1) if match else index_html

# HTML, который встраиваем
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
  /* Без внутренних прокруток и отступов у iframe-контента */
  html, body {{
    margin: 0;
    padding: 0;
    overflow: hidden; /* важно: исключаем внутренний скролл */
  }}
  {css}
</style>
</head>
<body>
{body_html}

<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
<script>{js}</script>

<script>
/* Автовысота без «раздувания» */
(function () {{
  var lastH = -1;
  function setHeight(h) {{
    if (!window.frameElement) return;
    var cur = parseInt(window.frameElement.style.height || "0", 10);
    // Меняем высоту только если есть реальная разница (>1px)
    if (Math.abs(cur - h) > 1 && Math.abs(lastH - h) > 1) {{
      window.frameElement.style.height = h + "px";
      lastH = h;
    }}
  }}

  function measure() {{
    // Берём высоту документа; без буферов и магии
    var h = Math.max(
      document.documentElement.scrollHeight,
      document.body ? document.body.scrollHeight : 0
    );
    setHeight(h);
  }}

  // Наблюдаем изменения размеров — без setInterval
  var ro = new ResizeObserver(function() {{ measure(); }});
  ro.observe(document.documentElement);
  if (document.body) ro.observe(document.body);

  // На загрузке — один замер
  window.addEventListener("load", measure);

  // На случай шрифтов/картинок — пару отложенных замеров
  setTimeout(measure, 100);
  setTimeout(measure, 600);
}})();
</script>
</body>
</html>
"""

# Снимаем паддинги контейнера Streamlit
st.markdown(
    """
    <style>
      .block-container { padding-top: 0rem; padding-bottom: 0rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Встраиваем: внутренний скролл запрещён, стартовая высота маленькая — дальше автоподгон
st.components.v1.html(full_html, height=200, scrolling=False)
