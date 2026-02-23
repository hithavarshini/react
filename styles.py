def get_custom_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* Black & White Theme */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    background: #ffffff;
    color: #000000;
}

.main {
    background: #ffffff;
}

.block-container {
    padding-top: 2rem !important;
    max-width: 1400px !important;
}

/* Hero Section */
.hero-container {
    background: #ffffff;
    padding: 80px 60px;
    margin: -2rem -4rem 3rem -4rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12), 0 2px 8px rgba(0, 0, 0, 0.08);
    position: relative;
}

.hero-title {
    font-size: 56px;
    font-weight: 900;
    color: #000000;
    margin-bottom: 20px;
    letter-spacing: -0.03em;
}

.hero-subtitle {
    font-size: 18px;
    color: #374151;
    font-weight: 400;
    line-height: 1.7;
    max-width: 700px;
}

.hero-badge {
    display: inline-block;
    background: #000000;
    color: #ffffff;
    padding: 8px 20px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    margin-bottom: 24px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

/* Cards */
.enterprise-card {
    background: #ffffff;
    border-radius: 8px;
    padding: 32px;
    margin: 20px 0;
    border: 1px solid #e5e7eb;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;
}

.enterprise-card:hover {
    box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
    transform: translateY(-4px);
}

/* Section Headers */
.section-header {
    font-size: 28px;
    font-weight: 800;
    color: #000000;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 3px solid #000000;
    letter-spacing: -0.02em;
}

.metric-label {
    font-size: 11px;
    font-weight: 700;
    color: #6b7280;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 40px;
    font-weight: 900;
    color: #000000;
    line-height: 1;
}

/* Buttons */
button[kind="primary"], .stButton > button {
    background: #000000 !important;
    color: #ffffff !important;
    padding: 16px 36px !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    border: none !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25) !important;
    transition: all 0.3s ease !important;
    font-size: 15px !important;
    letter-spacing: 0.5px !important;
}

button[kind="primary"]:hover, .stButton > button:hover {
    background: #1a1a1a !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35) !important;
    transform: translateY(-2px) !important;
}

.stButton > button p {
    color: #ffffff !important;
}

.stButton > button:hover p {
    color: #ffffff !important;
}

/* File Uploader */
.stFileUploader {
    background: #fafafa !important;
    border: 2px dashed #d1d5db !important;
    border-radius: 8px !important;
    padding: 48px !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04) !important;
    transition: all 0.3s ease !important;
}

.stFileUploader:hover {
    border-color: #000000 !important;
    background: #ffffff !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08) !important;
}

.stFileUploader label {
    color: #000000 !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}

/* Selectbox */
.stSelectbox > div > div {
    background: #ffffff !important;
    border: 1px solid #d1d5db !important;
    border-radius: 6px !important;
    color: #000000 !important;
    font-weight: 500 !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05) !important;
}

.stSelectbox label {
    color: #000000 !important;
    font-weight: 600 !important;
    font-size: 15px !important;
}

.stSelectbox div[data-baseweb="select"] > div {
    color: #000000 !important;
}

.stSelectbox option {
    color: #000000 !important;
}

/* Chat Messages */
.stChatMessage {
    background: #ffffff !important;
    border-radius: 8px !important;
    border: 1px solid #e5e7eb !important;
    padding: 24px !important;
    margin: 16px 0 !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) !important;
}

.stChatMessage[data-testid="user-message"] {
    background: #fafafa !important;
    border-color: #d1d5db !important;
    box-shadow: 0 3px 12px rgba(0, 0, 0, 0.08) !important;
}

.stChatMessage[data-testid="assistant-message"] {
    background: #ffffff !important;
    border: 2px solid #000000 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
}

.stChatMessage p {
    color: #000000 !important;
}

/* Chat avatars */
.stChatMessage [data-testid="chatAvatarIcon-user"],
.stChatMessage [data-testid="chatAvatarIcon-assistant"] {
    background: #000000 !important;
}

.stChatMessage svg {
    color: #ffffff !important;
}

/* Chat Input */
.stChatInput > div {
    background: #ffffff !important;
    border: 2px solid #e5e7eb !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) !important;
}

.stChatInput input {
    color: #000000 !important;
    font-size: 15px !important;
}

.stChatInput > div:focus-within {
    border-color: #000000 !important;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12) !important;
}

/* Expander */
.streamlit-expanderHeader {
    background: #fafafa !important;
    border-radius: 8px !important;
    border: 1px solid #e5e7eb !important;
    color: #000000 !important;
    font-weight: 600 !important;
    padding: 18px 24px !important;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05) !important;
}

.streamlit-expanderHeader:hover {
    background: #ffffff !important;
    border-color: #000000 !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
}

/* Sidebar */
.css-1d391kg, [data-testid="stSidebar"] {
    background: #fafafa !important;
    border-right: 1px solid #e5e7eb !important;
}

/* Info/Success boxes */
.stSuccess {
    background: #ffffff !important;
    border: 1px solid #e5e7eb !important;
    border-left: 4px solid #000000 !important;
    border-radius: 6px !important;
    color: #000000 !important;
    padding: 16px 20px !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) !important;
}

.stSuccess [data-testid="stMarkdownContainer"] p {
    color: #000000 !important;
}

.stInfo {
    background: #fafafa !important;
    border: 1px solid #e5e7eb !important;
    border-left: 4px solid #6b7280 !important;
    border-radius: 6px !important;
    color: #000000 !important;
    padding: 16px 20px !important;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06) !important;
}

.stInfo [data-testid="stMarkdownContainer"] p {
    color: #000000 !important;
}

/* Status Badge */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #000000;
    color: #ffffff;
    padding: 8px 20px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    text-transform: uppercase;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.status-badge::before {
    content: '';
    width: 8px;
    height: 8px;
    background: #ffffff;
    border-radius: 50%;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

::-webkit-scrollbar-track {
    background: #fafafa;
}

::-webkit-scrollbar-thumb {
    background: #d1d5db;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #9ca3af;
}

/* Typography */
h1, h2, h3 {
    color: #000000 !important;
}

p {
    color: #374151 !important;
    line-height: 1.7 !important;
}
</style>
"""
