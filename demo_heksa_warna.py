import streamlit as st

# ── PAGE CONFIG ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Demo Heksadesimal — Warna RGB",
    page_icon="🎨",
    layout="centered"
)

# ── LOGO ─────────────────────────────────────────────────────────────────────
LOGO_B64 = "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"

# ── STYLE ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stApp { background-color: #f8f9fa; }

    .header-box {
        background: #1a1a2e;
        color: white;
        padding: 20px 28px;
        border-radius: 10px;
        margin-bottom: 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
    }
    .header-text { flex: 1; }
    .header-box h2 { color: white; margin: 0 0 4px 0; font-size: 22px; }
    .header-box p  { color: #aab4d4; margin: 0; font-size: 13px; }
    .header-logo {
        background: white;
        border-radius: 8px;
        padding: 8px 12px;
        display: flex;
        align-items: center;
        flex-shrink: 0;
    }
    .header-logo img { height: 40px; width: auto; display: block; }

    .swatch-box {
        width: 100%;
        height: 120px;
        border-radius: 10px;
        margin: 16px 0;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        font-weight: 700;
        font-family: monospace;
        letter-spacing: 2px;
        border: 1px solid rgba(0,0,0,0.08);
    }

    .comp-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        padding: 16px 12px;
        text-align: center;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    }
    .comp-label { font-size: 12px; color: #888; margin-bottom: 4px; }
    .comp-dec   { font-size: 26px; font-weight: 700; margin: 0; }
    .comp-hex   { font-family: monospace; font-size: 18px; font-weight: 600; }
    .comp-bin   { font-family: monospace; font-size: 11px; color: #888; letter-spacing: 1px; margin-top: 4px; }

    .code-box {
        background: #1a1a2e;
        color: #e0e0e0;
        border-radius: 8px;
        padding: 16px 20px;
        font-family: 'Courier New', monospace;
        font-size: 14px;
        line-height: 2;
        margin-top: 16px;
    }
    .code-kw  { color: #aab4d4; }
    .code-at  { color: #79b8ff; }
    .code-val { color: #85e89d; }

    .info-box {
        background: #e8f0fe;
        border-left: 4px solid #4A4E6B;
        border-radius: 6px;
        padding: 12px 16px;
        margin-top: 16px;
        font-size: 14px;
        color: #1a1a2e;
    }

    .footer {
        text-align: center;
        color: #aaa;
        font-size: 12px;
        margin-top: 40px;
        padding-top: 16px;
        border-top: 1px solid #ddd;
    }
</style>
""", unsafe_allow_html=True)

# ── HEADER ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="header-box">
    <div class="header-text">
        <h2>🎨 Demo Heksadesimal — Warna RGB</h2>
        <p>Arsitektur dan Organisasi Komputer</p>
    </div>
    <div class="header-logo">
        <img src="data:image/jpeg;base64,{LOGO_B64}" alt="ITech Logo">
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("**Setiap warna di layar komputer disimpan sebagai 3 byte (24 bit). Heksadesimal adalah cara paling ringkas untuk menuliskannya.**")
st.caption("💡 Geser slider R, G, B dan perhatikan bagaimana nilai desimal, heksadesimal, dan biner berubah.")

st.divider()

# ── SLIDER INPUT ──────────────────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
with col1:
    r = st.slider("🔴 Red", 0, 255, 255, key="r")
with col2:
    g = st.slider("🟢 Green", 0, 255, 87, key="g")
with col3:
    b = st.slider("🔵 Blue", 0, 255, 51, key="b")

# ── KALKULASI ─────────────────────────────────────────────────────────────────
hex_r = format(r, '02X')
hex_g = format(g, '02X')
hex_b = format(b, '02X')
hex_color = f"#{hex_r}{hex_g}{hex_b}"

bin_r = format(r, '08b')
bin_g = format(g, '08b')
bin_b = format(b, '08b')

# Warna teks otomatis (putih/hitam tergantung kecerahan)
brightness = (r * 299 + g * 587 + b * 114) / 1000
text_color = "#ffffff" if brightness < 128 else "#1a1a2e"

# ── SWATCH ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="swatch-box" style="background:{hex_color}; color:{text_color};">
    {hex_color}
</div>
""", unsafe_allow_html=True)

# ── KARTU KOMPONEN ────────────────────────────────────────────────────────────
st.markdown("#### Representasi per komponen (masing-masing 8 bit)")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="comp-card">
        <div class="comp-label">Red</div>
        <div class="comp-dec" style="color:#cc2200;">{r}</div>
        <div class="comp-hex" style="color:#cc2200;">= {hex_r}<sub>16</sub></div>
        <div class="comp-bin">{bin_r}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="comp-card">
        <div class="comp-label">Green</div>
        <div class="comp-dec" style="color:#1a7a30;">{g}</div>
        <div class="comp-hex" style="color:#1a7a30;">= {hex_g}<sub>16</sub></div>
        <div class="comp-bin">{bin_g}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="comp-card">
        <div class="comp-label">Blue</div>
        <div class="comp-dec" style="color:#0055cc;">{b}</div>
        <div class="comp-hex" style="color:#0055cc;">= {hex_b}<sub>16</sub></div>
        <div class="comp-bin">{bin_b}</div>
    </div>
    """, unsafe_allow_html=True)

# ── KODE PROGRAM ─────────────────────────────────────────────────────────────
st.markdown("#### Kode program")
st.markdown(f"""
<div class="code-box">
    <span class="code-kw">/* CSS — 2 cara menulis warna yang sama */</span><br>
    <span class="code-at">color</span>: <span class="code-val">{hex_color}</span>;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="code-kw">/* heksadesimal */</span><br>
    <span class="code-at">color</span>: <span class="code-val">rgb({r}, {g}, {b})</span>;&nbsp;&nbsp;&nbsp;&nbsp;<span class="code-kw">/* desimal */</span><br><br>
    <span class="code-kw">/* Disimpan komputer sebagai 24 bit: */</span><br>
    <span style="color:#e0e0e0; font-size:13px; letter-spacing:1px;">{bin_r} {bin_g} {bin_b}</span>
</div>
""", unsafe_allow_html=True)

# ── INFO BOX ─────────────────────────────────────────────────────────────────
total_bits = 24
total_colors = 2 ** total_bits

st.markdown(f"""
<div class="info-box">
    <strong>Kenapa hex?</strong><br>
    Setiap channel (R, G, B) = <strong>1 byte = 8 bit = 2 digit hex</strong>.
    Menulis <code>{hex_color}</code> jauh lebih ringkas dari <code>rgb({r}, {g}, {b})</code>
    — dan langsung terbaca sebagai 3 pasang byte.<br><br>
    Total kombinasi warna: 2<sup>24</sup> = <strong>{total_colors:,}</strong> warna berbeda.
</div>
""", unsafe_allow_html=True)

# ── CONTOH WARNA POPULER ─────────────────────────────────────────────────────
st.divider()
st.markdown("#### Contoh warna populer di web")

presets = [
    ("Merah tombol", "#E74C3C", 231, 76, 60),
    ("Biru link",    "#3498DB", 52, 152, 219),
    ("Hijau sukses", "#2ECC71", 46, 204, 113),
    ("Abu netral",   "#95A5A6", 149, 165, 166),
    ("Hitam teks",   "#2C3E50", 44, 62, 80),
    ("Putih bg",     "#FFFFFF", 255, 255, 255),
]

cols = st.columns(len(presets))
for i, (nama, hx, pr, pg, pb) in enumerate(presets):
    br = (pr * 299 + pg * 587 + pb * 114) / 1000
    tc = "#ffffff" if br < 128 else "#1a1a2e"
    with cols[i]:
        st.markdown(f"""
        <div style="background:{hx}; color:{tc}; border-radius:8px; padding:12px 8px;
                    text-align:center; font-size:11px; border:1px solid rgba(0,0,0,0.1);
                    font-weight:600; line-height:1.8;">
            {hx}<br>
            <span style="font-weight:400; opacity:0.8;">{nama}</span>
        </div>
        """, unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Arismunandar, M.T.I. &nbsp;·&nbsp; Arsitektur dan Organisasi Komputer &nbsp;·&nbsp; STTI NIIT Jakarta
</div>
""", unsafe_allow_html=True)
