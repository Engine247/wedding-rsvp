import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define Colors
gold_color = "#B8860B"  # Gold text color
box_color_1 = "#0ADA7F"  # Light Engine Green
box_color_2 = "#0B9959"  # Medium Engine Green
box_color_3 = "#0E6037"  # Dark Engine Green

# === CHANGED SECTION: Updated CSS to Adjust Fonts & Alignment ===
st.markdown(f"""
    <style>
        body {{
            background-color: #2E2E2E !important;
            text-align: center;
        }}

        .title {{
            font-size: 36px;
            font-weight: bold;
            text-align: center;
        }}

        .names {{
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
            text-align: center;
        }}

        .divider-thick {{
            border-bottom: 5px solid {gold_color};
            margin: 15px auto;
            width: 60%;
        }}

        .divider-thin {{
            border-bottom: 2px solid {gold_color};
            margin: 10px auto;
            width: 50%;
        }}

        .event-container, .form-container {{
            max-width: 50%;
            margin: auto;
            text-align: center;
        }}

        .event-title {{
            font-size: 26px;
            font-weight: bold;
            text-align: center;
            color: {gold_color};
        }}

        .event-details {{
            font-size: 20px;
            text-align: center;
            color: white;
        }}

        /* === CHANGED: Adjusted Input Box Width and Alignment === */
        .stTextInput, .stTextArea, .stButton, .stRadio {{
            width: 60% !important;
            margin: auto !important;
        }}

        /* === CHANGED: Increased Font Size for Radio Buttons === */
        .stRadio label {{
            font-size: 18px !important;
            font-weight: bold;
            color: white !important;
        }}

        .stTextInput > div > div > input {{
            border: 2px solid {gold_color} !important;
            border-radius: 5px;
            width: 100%;
        }}

        .stTextInput > div > div > input:hover {{
            border-color: {gold_color} !important;
        }}

        /* === REMOVE THE EXTRA BOX BELOW THE TEXT AREA === */
        .stTextArea > div {{
            border: none !important;  /* Removes wrapper div border */
            box-shadow: none !important;  /* Removes extra box shadow */
            background: transparent !important;
            padding: 0 !important;
            margin: 0 !important;
        }}

        /* === FIX: Ensure Additional Comments Box Matches Other Fields === */
        .stTextArea > div > textarea {{
            border: 2px solid {gold_color} !important; /* Keeps correct border */
            border-radius: 5px !important;
            background-color: #1E1E1E !important;
            color: white !important;
            padding: 8px !important;
            width: 100% !important;
        }}

        .stButton > button {{
            background-color: {box_color_1} !important;
            color: white !important;
            border: 2px solid {box_color_3} !important;
            width: 35% !important;
        }}

        .stButton > button:hover {{
            background-color: {box_color_2} !important;
            border: 2px solid {box_color_1} !important;
        }}
    </style>
""", unsafe_allow_html=True)

# Title and Names (Centered)
st.markdown('<div class="title">WEDDING | RSVP</div>', unsafe_allow_html=True)
st.markdown('<div class="names">Heather & Rob</div>', unsafe_allow_html=True)

# Double Gold Line (Thick then Thin)
st.markdown('<div class="divider-thick"></div>', unsafe_allow_html=True)
st.markdown('<div class="divider-thin"></div>', unsafe_allow_html=True)

# Wedding Details (Centered)
st.markdown('<div class="event-container">', unsafe_allow_html=True)
st.markdown('<div class="event-title">The Venetian</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details">546 River Dr, Garfield, NJ 07026</div>', unsafe_allow_html=True)
st.markdown('<div class="divider-thin"></div>', unsafe_allow_html=True)
st.markdown('<div class="event-title">April 12, 2025</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details"><strong>6:00 PM</strong> - Arrival</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details"><strong>6:30 PM</strong> - Ceremony</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details"><strong>7:00 PM</strong> - Cocktails</div>', unsafe_allow_html=True)
st.markdown('<div class="divider-thin"></div>', unsafe_allow_html=True)
st.markdown('<div class="divider-thick"></div>', unsafe_allow_html=True)

# === CHANGED: RSVP Section Now Matches Width and Font Styling ===
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="names">* * * GUEST DETAILS * * *</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# === CHANGED: Centered Radio Buttons to 60% Width ===
st.markdown("<div style='width: 60%; margin: auto;'>", unsafe_allow_html=True)
num_guests = st.radio("Number of Guests Attending", options=[1, 2, "Unable to attend"], index=0, horizontal=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="event-title">Your Details</div>', unsafe_allow_html=True)
guest1_name = st.text_input("Your Name", placeholder="Enter your full name").strip().title()
guest1_email = st.text_input("Your Email Address", placeholder="Enter your email")

if num_guests in [1, 2]:
    if num_guests == 2:
        st.markdown('<div class="event-title">Additional Guest Details</div>', unsafe_allow_html=True)
        guest2_name = st.text_input("Additional Guest Name", placeholder="Enter full name").strip().title()
    else:
        guest2_name = "N/A"

    st.markdown('<div class="event-title">Additional Comments</div>', unsafe_allow_html=True)
    comments = st.text_area("Questions | Comments | Concerns", placeholder="(e.g., dietary restrictions, family considerations, etc.)")

st.markdown('</div>', unsafe_allow_html=True)  # Close form container

# Submit Button (Green)
submitted = st.button("Submit")

# === CHANGED: Submit Button is Now Centered and Matches Width of Form ===

# === CHANGED: Adjusted Email Function to Align with Updates ===
def send_email(to_email, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("rob.haddad.222@gmail.com", "yzmj yhno npkd oxvz")

        msg = MIMEMultipart()
        msg["From"] = '"Heather & Rob | April-12-2025" <rob.haddad.222@gmail.com>'
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "html", "utf-8"))

        server.sendmail("rob.haddad.222@gmail.com", [to_email, "heathervictoria412@gmail.com"], msg.as_string())
        server.quit()
    except Exception as e:
        st.error(f"Failed to send email: {e}")

if submitted:
    if num_guests in [1, 2] and (not guest1_name or not guest1_email):
        st.error("Please complete all required fields.")
    elif num_guests == 2 and not guest2_name:
        st.error("Please enter the name of your additional guest.")
    else:
        st.success("RSVP Confirmed! Check your email for details.")
