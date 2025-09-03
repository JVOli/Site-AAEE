import base64
import pathlib
import streamlit as st
import streamlit.components.v1 as components
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(page_title="AAEE", layout="wide")

project_root = pathlib.Path(__file__).parent
html_path = project_root / "index.html"
css_path = project_root / "styles.css"
seal_path = project_root / "Selo1.png"

css = ""
if css_path.exists():
  css = css_path.read_text(encoding="utf-8")

html = html_path.read_text(encoding="utf-8")

# Remove link externo ao CSS e injeta o conteúdo inline
html = html.replace('<link rel="stylesheet" href="styles.css" />', f"<style>{css}</style>")

# Embute Selo.png como data URI (cobre variações comuns)
if seal_path.exists():
  seal_b64 = base64.b64encode(seal_path.read_bytes()).decode("utf-8")
  for needle in [
    'src="Selo.png"',
    "src='Selo.png'",
    'src="Selo1.png"',
  ]:
    html = html.replace(needle, f'src="data:image/png;base64,{seal_b64}"')
else:
  st.warning("Arquivo Selo.png não encontrado ao lado do app.py.")

# Tela cheia: remove paddings/header/footer do Streamlit
st.markdown(
  """
  <style>
    .block-container { padding: 0; }
    header[data-testid=\"stHeader\"] { display: none; }
    footer { visibility: hidden; }
  </style>
  """,
  unsafe_allow_html=True,
)

# Altura do viewport (full screen)
vh = streamlit_js_eval(js_expressions="window.innerHeight", key="get_vh")
try:
  height = int(vh) if vh else 700
except Exception:
  height = 700

# Renderização sem scroll, ocupando a altura do viewport
components.html(html, height=height, scrolling=False)


