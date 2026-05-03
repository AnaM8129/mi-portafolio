import streamlit as st
 
# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Portafolio · ML & AI Apps",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed",
)
 
# ── Global CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Boogaloo&family=Nunito:wght@400;700;900&family=Space+Mono:wght@700&display=swap');
 
/* ── Reset & base ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #fdf6e3 !important;
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { display: none; }
footer { display: none; }
 
/* ── Hero ── */
.hero {
    position: relative;
    text-align: center;
    padding: 3rem 1rem 2rem;
    overflow: hidden;
}
.hero-title {
    font-family: 'Boogaloo', cursive;
    font-size: clamp(4rem, 12vw, 9rem);
    line-height: 0.9;
    letter-spacing: -2px;
    color: #1a1a2e;
    margin: 0;
}
.hero-title .p  { color: #e63946; }
.hero-title .o1 { color: #2196f3; }
.hero-title .r  { color: #ff9800; }
.hero-title .t  { color: #e63946; }
.hero-title .f  { color: #4caf50; }
.hero-title .o2 { color: #9c27b0; }
.hero-title .l  { color: #2196f3; }
.hero-title .i  { color: #ff9800; }
.hero-title .o3 { color: #4caf50; }
 
.hero-subtitle {
    font-family: 'Space Mono', monospace;
    font-size: 1rem;
    color: #fff;
    background: #1a1a2e;
    display: inline-block;
    padding: 6px 20px;
    border-radius: 30px;
    margin-top: 1rem;
    letter-spacing: 2px;
    text-transform: uppercase;
}
 
/* ── Floating decorative blobs ── */
.blob {
    position: absolute;
    border-radius: 50%;
    opacity: 0.18;
    pointer-events: none;
}
.blob-1 { width:180px; height:180px; background:#e63946; top:-40px; left:-40px; border-radius:60% 40% 70% 30% / 50% 60% 40% 50%; }
.blob-2 { width:120px; height:120px; background:#2196f3; top:10px; right:60px; border-radius:30% 70% 40% 60% / 60% 30% 70% 40%; }
.blob-3 { width:90px;  height:90px;  background:#ff9800; bottom:0; right:200px; border-radius:50%; }
.blob-4 { width:70px;  height:70px;  background:#4caf50; bottom:-10px; left:180px; border-radius:50%; }
 
/* ── Decorative badges ── */
.badge-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin: 1.5rem auto 2.5rem;
}
.badge {
    font-family: 'Nunito', sans-serif;
    font-weight: 900;
    font-size: 0.8rem;
    padding: 5px 16px;
    border-radius: 999px;
    letter-spacing: 1px;
    text-transform: uppercase;
    border: 2px solid currentColor;
}
.badge-red    { color:#e63946; border-color:#e63946; }
.badge-blue   { color:#2196f3; border-color:#2196f3; }
.badge-green  { color:#4caf50; border-color:#4caf50; }
.badge-orange { color:#ff9800; border-color:#ff9800; }
.badge-purple { color:#9c27b0; border-color:#9c27b0; }
 
/* ── Section title ── */
.section-title {
    font-family: 'Boogaloo', cursive;
    font-size: 2.4rem;
    color: #1a1a2e;
    margin: 1rem 0 0.3rem;
    display: flex;
    align-items: center;
    gap: 12px;
}
.section-line {
    height: 4px;
    border-radius: 4px;
    margin-bottom: 2rem;
}
 
/* ── Project card ── */
.card-wrap {
    margin-bottom: 1.4rem;
}
.card {
    border-radius: 18px;
    padding: 1.4rem 1.5rem;
    border: 3px solid #1a1a2e;
    position: relative;
    overflow: hidden;
    transition: transform 0.18s ease, box-shadow 0.18s ease;
    cursor: pointer;
}
.card:hover {
    transform: translate(-4px, -4px);
    box-shadow: 8px 8px 0 #1a1a2e;
}
.card-accent {
    position: absolute;
    top: -18px; right: -18px;
    width: 70px; height: 70px;
    border-radius: 50%;
    opacity: 0.25;
}
.card-emoji {
    font-size: 2rem;
    margin-bottom: 0.4rem;
    display: block;
}
.card-title {
    font-family: 'Boogaloo', cursive;
    font-size: 1.35rem;
    color: #1a1a2e;
    margin: 0 0 0.3rem;
}
.card-desc {
    font-family: 'Nunito', sans-serif;
    font-size: 0.88rem;
    color: #444;
    margin: 0 0 0.9rem;
    line-height: 1.5;
}
.card-link {
    font-family: 'Space Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    color: #fff;
    padding: 6px 14px;
    border-radius: 999px;
    text-decoration: none;
    display: inline-block;
    border: none;
    letter-spacing: 0.5px;
}
.card-link:hover { opacity: 0.88; }
.card-tag {
    font-family: 'Nunito', sans-serif;
    font-size: 0.7rem;
    font-weight: 900;
    padding: 2px 10px;
    border-radius: 999px;
    display: inline-block;
    margin-top: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #1a1a2e;
}
 
/* ── Footer ── */
.footer {
    text-align: center;
    padding: 3rem 1rem 2rem;
    font-family: 'Nunito', sans-serif;
    color: #888;
    font-size: 0.85rem;
}
.footer strong {
    font-family: 'Boogaloo', cursive;
    font-size: 1.2rem;
    color: #1a1a2e;
}
 
/* ── Deco shapes in header area ── */
.deco-star {
    display: inline-block;
    font-size: 1.8rem;
    animation: spin 8s linear infinite;
}
@keyframes spin { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }
 
.zigzag {
    display: block;
    width: 100%;
    height: 12px;
    background: repeating-linear-gradient(
        90deg,
        #e63946 0, #e63946 20px,
        #ff9800 20px, #ff9800 40px,
        #2196f3 40px, #2196f3 60px,
        #4caf50 60px, #4caf50 80px,
        #9c27b0 80px, #9c27b0 100px
    );
    margin: 0 0 2rem;
    border-radius: 4px;
}
</style>
""", unsafe_allow_html=True)
 
# ── Data ──────────────────────────────────────────────────────────────────────
projects = [
    {
        "emoji": "🤖",
        "title": "Chat-bot",
        "desc": "Asistente conversacional inteligente con procesamiento de lenguaje natural.",
        "url": "https://chatbot222.streamlit.app/",
        "color": "#e63946",
        "bg": "#fff5f5",
        "tag": "NLP",
        "tag_color": "#ffd6d6",
    },
    {
        "emoji": "📝",
        "title": "Respuestas a Oraciones",
        "desc": "Genera respuestas automáticas a oraciones en inglés usando modelos de lenguaje.",
        "url": "https://respuestasoraciones.streamlit.app/",
        "color": "#2196f3",
        "bg": "#f0f7ff",
        "tag": "NLP · English",
        "tag_color": "#c8e4ff",
    },
    {
        "emoji": "😊",
        "title": "Análisis de Emociones",
        "desc": "Detecta y clasifica emociones en texto usando modelos de sentiment analysis.",
        "url": "https://sentimentoapp.streamlit.app/",
        "color": "#ff9800",
        "bg": "#fff8f0",
        "tag": "Sentiment",
        "tag_color": "#ffe0b2",
    },
    {
        "emoji": "☁️",
        "title": "Word Cloud",
        "desc": "Visualización creativa de frecuencia de palabras en nubes interactivas.",
        "url": "https://wordcloud22.streamlit.app/",
        "color": "#9c27b0",
        "bg": "#faf0ff",
        "tag": "Visualización",
        "tag_color": "#e1bee7",
    },
    {
        "emoji": "👤",
        "title": "Reconocimiento de Rostro",
        "desc": "Detecta y reconoce rostros humanos en imágenes usando visión por computador.",
        "url": "https://conana-sinana.streamlit.app/",
        "color": "#4caf50",
        "bg": "#f0fff4",
        "tag": "Computer Vision",
        "tag_color": "#c8f0d0",
    },
    {
        "emoji": "🔍",
        "title": "Detección de Objetos",
        "desc": "Identifica y etiqueta objetos dentro de imágenes con modelos de deep learning.",
        "url": "https://reconocimiento-imagen.streamlit.app/",
        "color": "#e63946",
        "bg": "#fff5f5",
        "tag": "Computer Vision",
        "tag_color": "#ffd6d6",
    },
    {
        "emoji": "🌱",
        "title": "Mi Primera App",
        "desc": "Primera aplicación construida en Streamlit — el punto de partida del viaje.",
        "url": "https://holaquemas.streamlit.app/",
        "color": "#2196f3",
        "bg": "#f0f7ff",
        "tag": "Debut",
        "tag_color": "#c8e4ff",
    },
    {
        "emoji": "📌",
        "title": "Primera App · Versión Profe",
        "desc": "Versión mejorada de la primera app, incorporando feedback del profesor.",
        "url": "https://estaesunaurl.streamlit.app/",
        "color": "#ff9800",
        "bg": "#fff8f0",
        "tag": "Iteración",
        "tag_color": "#ffe0b2",
    },
    {
        "emoji": "🔊",
        "title": "Texto a Audio",
        "desc": "Convierte texto escrito a voz sintética con distintas opciones de idioma.",
        "url": "https://texto-a-audio-profe-egbafxjujxxpaeqtpcy2jd.streamlit.app/",
        "color": "#9c27b0",
        "bg": "#faf0ff",
        "tag": "TTS",
        "tag_color": "#e1bee7",
    },
    {
        "emoji": "🎙️",
        "title": "OCR + Audio",
        "desc": "Extrae texto de imágenes (OCR) y lo convierte en audio de forma automática.",
        "url": "https://ocr-audio-8129.streamlit.app/",
        "color": "#4caf50",
        "bg": "#f0fff4",
        "tag": "OCR · Audio",
        "tag_color": "#c8f0d0",
    },
    {
        "emoji": "🖌️",
        "title": "App de Dibujo",
        "desc": "Lienzo interactivo para dibujar directamente en el navegador con herramientas creativas.",
        "url": "https://dibujoapp.streamlit.app/",
        "color": "#e63946",
        "bg": "#fff5f5",
        "tag": "Interactivo",
        "tag_color": "#ffd6d6",
    },
    {
        "emoji": "✍️",
        "title": "Handwriting",
        "desc": "Reconoce y analiza escritura a mano usando modelos de visión artificial.",
        "url": "https://handwriting-a.streamlit.app/",
        "color": "#2196f3",
        "bg": "#f0f7ff",
        "tag": "Computer Vision",
        "tag_color": "#c8e4ff",
    },
    {
        "emoji": "📊",
        "title": "Tablero de Datos",
        "desc": "Dashboard interactivo para visualización y análisis de conjuntos de datos.",
        "url": "https://tablero2-8.streamlit.app/",
        "color": "#ff9800",
        "bg": "#fff8f0",
        "tag": "Dashboard",
        "tag_color": "#ffe0b2",
    },
]
 
# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="blob blob-1"></div>
  <div class="blob blob-2"></div>
  <div class="blob blob-3"></div>
  <div class="blob blob-4"></div>
 
  <p class="hero-title">
    <span class="p">P</span><span class="o1">O</span><span class="r">R</span><span class="t">T</span><span class="f">F</span><span class="o2">O</span><span class="l">L</span><span class="i">I</span><span class="o3">O</span>
  </p>
  <p class="hero-subtitle">✦ ML &amp; AI Apps ✦ Streamlit ✦</p>
</div>
""", unsafe_allow_html=True)
 
# ── Badges ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="badge-strip">
  <span class="badge badge-red">NLP</span>
  <span class="badge badge-blue">Computer Vision</span>
  <span class="badge badge-green">Deep Learning</span>
  <span class="badge badge-orange">Text to Speech</span>
  <span class="badge badge-purple">Dashboards</span>
  <span class="badge badge-red">OCR</span>
  <span class="badge badge-blue">Sentiment Analysis</span>
  <span class="badge badge-green">Interactive Apps</span>
</div>
<div class="zigzag"></div>
""", unsafe_allow_html=True)
 
# ── Section header ────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-title">
  🚀 Proyectos
</div>
<div class="section-line" style="background: linear-gradient(90deg,#e63946,#ff9800,#2196f3,#4caf50,#9c27b0);"></div>
""", unsafe_allow_html=True)
 
# ── Cards grid ────────────────────────────────────────────────────────────────
cols_per_row = 3
rows = [projects[i:i+cols_per_row] for i in range(0, len(projects), cols_per_row)]
 
for row in rows:
    cols = st.columns(len(row), gap="medium")
    for col, project in zip(cols, row):
        with col:
            st.markdown(f"""
            <div class="card-wrap">
              <div class="card" style="background:{project['bg']};">
                <div class="card-accent" style="background:{project['color']};"></div>
                <span class="card-emoji">{project['emoji']}</span>
                <p class="card-title">{project['title']}</p>
                <p class="card-desc">{project['desc']}</p>
                <a class="card-link" href="{project['url']}" target="_blank"
                   style="background:{project['color']};">
                  Abrir app ↗
                </a>
                <br>
                <span class="card-tag" style="background:{project['tag_color']};">{project['tag']}</span>
              </div>
            </div>
            """, unsafe_allow_html=True)
 
# ── Divider ───────────────────────────────────────────────────────────────────
st.markdown('<div class="zigzag" style="margin-top:2rem;"></div>', unsafe_allow_html=True)
 
# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <strong>🎨 Portafolio ML & AI</strong><br>
  Construido con ❤️ usando <strong>Streamlit</strong> · Python<br>
  <span style="font-size:0.75rem;margin-top:6px;display:block;">
    Todos los proyectos fueron desarrollados como parte de un proceso de aprendizaje continuo.
  </span>
</div>
""", unsafe_allow_html=True)
 
