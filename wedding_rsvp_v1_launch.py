import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define Colors
gold_color = "#B8860B"  # Gold text color
box_color_1 = "#0ADA7F"  # Light Engine Green
box_color_2 = "#0B9959"  # Medium Engine Green
box_color_3 = "#0E6037"  # Dark Engine Green

# === CUSTOM FORMAT: Updated CSS to Adjust Fonts & Alignment ===
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

        body {{
            background-color: #2E2E2E !important;
            text-align: center;
            font-family: 'Georgia Pro', Georgia, serif !important;
        }}

        /* Whimsical Wedding Title */
        .wedding-title {{
            font-size: 55px;
            font-weight: bold;
            text-align: center;
            font-family: 'Great Vibes', cursive;
            color: {gold_color};
            margin-bottom: 10px;
        }}

        .names {{
            font-size: 26px;
            font-weight: bold;
            margin-bottom: 10px;
            text-align: center;
            font-family: 'Georgia Pro', Georgia, serif;
        }}

        .divider-thick {{
            border-bottom: 4px solid {gold_color};
            margin: 5px auto;
            width: 55%;
        }}

        .divider-thin {{
            border-bottom: 2px solid {gold_color};
            margin: 5px auto;
            width: 55%;
        }}

        .event-container, .form-container {{
            max-width: 50%;
            margin: auto;
            text-align: center;
            font-family: 'Georgia Pro', Georgia, serif;
        }}

        .event-title {{
            font-size: 26px;
            font-weight: bold;
            text-align: center;
            color: {gold_color};
            font-family: 'Georgia Pro', Georgia, serif;
        }}

        .event-details {{
            font-size: 18px;
            text-align: center;
            font-family: 'Georgia Pro', Georgia, serif;
        }}

        /* Input fields */
        .stTextInput, .stTextArea, .stButton, .stRadio {{
            width: 60% !important;
            margin: auto !important;
        }}

        .stTextInput > div > div > input {{
            border: 2px solid {gold_color} !important;
            border-radius: 5px;
            width: 100%;
            font-family: 'Georgia Pro', Georgia, serif;
        }}

        .stTextArea > div > textarea {{
            border: 2px solid {gold_color} !important;
            border-radius: 5px !important;
            background-color: #1E1E1E !important;
            color: white !important;
            padding: 8px !important;
            width: 100% !important;
            font-family: 'Georgia Pro', Georgia, serif;
        }}

        /* Button Styling */
        .stButton > button {{
            background-color: {box_color_1} !important;
            color: white !important;
            border: 2px solid {box_color_3} !important;
            width: 35% !important;
            font-family: 'Georgia Pro', Georgia, serif;
        }}

        .stButton > button:hover {{
            background-color: {box_color_2} !important;
            border: 2px solid {box_color_1} !important;
        }}
    </style>
""", unsafe_allow_html=True)


# === Wedding Header Section ===
st.markdown('<div class="wedding-title">The Wedding</div>', unsafe_allow_html=True)
st.markdown('<div class="divider-thick"></div>', unsafe_allow_html=True)



# === Wedding Details Section (Centered) ===
st.markdown('<div class="event-container">', unsafe_allow_html=True) # OPEN event container
st.markdown('<div class="event-title">The Venetian</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details">546 River Dr, Garfield, NJ 07026</div>', unsafe_allow_html=True)
### st.markdown('<div class="divider-thin"></div>', unsafe_allow_html=True)
### st.markdown('</div>', unsafe_allow_html=True)  # CLOSE event-container

# === Date Container
### st.markdown('<div class="event-container">', unsafe_allow_html=True) # OPEN event container
st.markdown('<div class="event-title">April 12, 2025</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details"><strong>6:00 PM</strong> - Arrival</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details"><strong>6:30 PM</strong> - Ceremony</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details"><strong>7:00 PM</strong> - Cocktails</div>', unsafe_allow_html=True)
### st.markdown('<div class="divider-thin"></div>', unsafe_allow_html=True)
### st.markdown('</div>', unsafe_allow_html=True)  # CLOSE event-container


# === RSVP FORM CONTAINER (Re-Added) ===
st.markdown('<div class="event-container">', unsafe_allow_html=True) # OPEN event container
st.markdown('<div class="divider-thin"></div>', unsafe_allow_html=True)
st.markdown('<div class="names">* * * RSVP * * *</div>', unsafe_allow_html=True)
st.markdown('<div class="divider-thick"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # CLOSE event-container

### st.markdown('<div class="divider-thick"></div>', unsafe_allow_html=True)
### st.markdown('<div class="divider-thin"></div>', unsafe_allow_html=True)


### st.markdown('<div class="form-container">', unsafe_allow_html=True)
### st.markdown('<div class="divider-thin"></div>', unsafe_allow_html=True)
### st.markdown('<div class="event-title">* * * RSVP * * *</div>', unsafe_allow_html=True)
### st.markdown('</div>', unsafe_allow_html=True)  # CLOSE event-container


### st.markdown('<div class="divider-thick"></div>', unsafe_allow_html=True)

# === Guest Selection (Fixed Centering) ===
st.markdown("<div style='width: 60%; margin: auto;'>", unsafe_allow_html=True)
num_guests = st.radio("Please make your selection", options=[1, 2, "Unable to attend"], index=0, horizontal=True)
st.markdown("</div>", unsafe_allow_html=True)


# === Primary Guest Input Fields ===
st.markdown('<div class="event-title">Your Details</div>', unsafe_allow_html=True)
guest1_name = st.text_input("Your Name", placeholder="Enter your full name").strip().title()
guest1_email = st.text_input("Your Email Address", placeholder="Enter your email")

# === Guest 2 Details (Only If Selected) ===
if num_guests in [1, 2]:
    if num_guests == 2:
        st.markdown('<div class="event-title">Additional Guest Details</div>', unsafe_allow_html=True)
        guest2_name = st.text_input("Additional Guest Name", placeholder="Enter full name").strip().title()
    else:
        guest2_name = "N/A"

    st.markdown('<div class="event-title">Additional Comments</div>', unsafe_allow_html=True)
    comments = st.text_area("Questions | Comments | Concerns", placeholder="(e.g., dietary restrictions, family considerations, etc.)")

st.markdown('</div>', unsafe_allow_html=True)  # Close form-container

# === Submit Button ===
submitted = st.button("Submit")

# === Email Function (No Change) ===
def send_email(to_email, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("rob.haddad.222@gmail.com", "yzmj yhno npkd oxvz")

        msg = MIMEMultipart()
        msg["From"] = '"Heather & Rob | April-12-2025" <rob.haddad.222@gmail.com>'
        msg["To"] = to_email
        msg["Subject"] = subject


        # HTML-Formatted Email Body
        confirmation_body = f"""
        <html>
        <head>
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
                
                body {{
                    font-family: 'Georgia Pro', Georgia, serif;
                    color: #444;
                    background-color: #f8f8f8;
                    padding: 20px;
                }}
                .container {{
                    max-width: 600px;
                    margin: auto;
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    text-align: center;
                    font-family: 'Great Vibes', cursive;
                    color: {gold_color};
                    font-size: 40px;
                }}
                h2 {{
                    color: #444; 
                    text-align: center;
                    font-size: 22px;
                    font-family: 'Georgia Pro', Georgia, serif;
                }}
                p {{
                    font-size: 16px;
                    line-height: 1.5;
                    text-align: center;
                }}
                .details {{
                    font-size: 18px;
                    font-weight: bold;
                    color: #444;
                    text-align: left;
                }}
                .footer {{
                    margin-top: 20px;
                    text-align: center;
                    font-size: 14px;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Thank you for your RSVP!</h1>
                <h2>Wedding Details</h2>

                <hr>
                <div class="details">
                    <p><strong>Date:</strong> April 12, 2025</p>
                    <p><strong>The Venetian |</strong> Garfield, NJ</p>
                    <p><strong>6:00 PM:</strong> Arrival</p>
                    <p><strong>6:30 PM:</strong> Ceremony</p>
                    <p><strong>7:00 PM:</strong> Cocktails</p>
                </div>
                <hr>

                <p class="footer">We are excited to celebrate with you!</p>

                <p class="footer">With Love,<br> Heather & Rob</p>
            </div>
        </body>
        </html>
        """



        msg.attach(MIMEText(body, "html", "utf-8"))

        server.sendmail("rob.haddad.222@gmail.com", [to_email, "heathervictoria412@gmail.com"], msg.as_string())
        server.quit()
    except Exception as e:
        st.error(f"Failed to send email: {e}")




# === Handle Submission ===
if submitted:
    if num_guests in [1, 2] and (not guest1_name or not guest1_email):
        st.error("Please complete all required fields.")
    elif num_guests == 2 and not guest2_name:
        st.error("Please enter the name of your additional guest.")
    else:
        st.success("RSVP Confirmed! Check your email for details.")
