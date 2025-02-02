import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# # # # # # # # # # # # 

# **Define Engine Green Colors**
box_color_1 = "#0ADA7F"  # Light Engine Green (used for focus outlines)
box_color_2 = "#0B9959"  # Medium Engine Green (used for buttons & borders)
box_color_3 = "#0E6037"  # Dark Engine Green (used for button hover)

# # # # # # # # # # # # 



# **Custom CSS for Streamlit UI**
st.markdown(f"""
    <style>
        body {{
            background-color: #2E2E2E !important; /* Dark Gray */
        }}

        /* SOLID GREEN LINES */
        .line-green {{
            border-bottom: 5px solid {box_color_2}; /* Medium Green 5pt */
            margin: 20px 0;
        }}

        /* SOLID GOLD LINES */
        .line-gold-thick {{
            border-bottom: 5px solid #B8860B; /* Gold 5pt */
            margin-top: 40px;
        }}

        .line-gold-thin {{
            border-bottom: 2px solid #B8860B; /* Gold 2pt */
            margin-top: 5px;
        }}

        /* Make Input Fields Appear Side by Side */
        .input-container {{
            display: flex;
            justify-content: space-between;
        }}

        .input-container > div {{
            width: 48%;  /* Adjust width for spacing */
        }}

        /* Change Input Field Outline to Light Green or Gold on Focus */
        input:focus, textarea:focus {{
            outline: 3px solid {box_color_1} !important; /* Light Engine Green */
            border-color: {box_color_1} !important;
        }}

div.stButton > button {{
    background-color: #B8860B !important; /* Gold */
    color: white !important;
    border-radius: 8px !important;
    border: none !important;
    padding: 10px 20px !important;
    font-size: 16px !important;
    font-weight: bold !important;
}}

div.stButton > button:hover {{
    background-color: #A6760B !important; /* Slightly Darker Gold on Hover */
}}

        div.stButton > button:hover {{
            background-color: {box_color_3} !important; /* Dark Engine Green on Hover */
        }}

        /* Make Input Fields & Text Areas Outline Light Green on Focus */
        input:focus, textarea:focus {{
            outline: 3px solid {box_color_1} !important; /* Light Engine Green Outline */
            border-color: {box_color_1} !important;
        }}
    </style>
""", unsafe_allow_html=True)


# # # # # # # # # # 


# **Sender Email Configuration**
sender_email_1 = "rob.haddad.222@gmail.com"  # NEW  
sender_email_2 = "heathervictoria412@gmail.com" # NEW 
sender_password = "yzmj yhno npkd oxvz"  # Google App Password // NEW

### sender_email_1 = "rob.haddad.46@gmail.com"  # OLD
### sender_password = "auox mtis ikrb ihmm"  # Google App Password // OLD



# **Function to Send Email**
def send_email(to_email, subject, body):
    try:
        # Setup SMTP Server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email_1, sender_password)

        # Email Setup
        msg = MIMEMultipart()
        msg["From"] = f'"Heather & Rob | April-12-2025" <{sender_email_1}>, <{sender_email_2}>'
        msg["To"] = to_email
        msg["Subject"] = subject

        # Attach HTML Content
        msg.attach(MIMEText(body, "html", "utf-8"))

        # Send Email
        server.sendmail(sender_email_1, [to_email, sender_email_2], msg.as_string())
        server.quit()

    except Exception as e:
        st.error(f"Failed to send email: {e}")


# # # # # # # # # # 


### **Insert Green Line at the Top**
### st.markdown('<div class="line-green"></div>', unsafe_allow_html=True)

# **Insert Thin Gold Line Below**
st.markdown('<div class="line-gold-thin"></div>', unsafe_allow_html=True)

### **Insert Thick Gold Line**
### st.markdown('<div class="line-gold-thick"></div>', unsafe_allow_html=True)

st.title("Wedding Invitation | RSVP")
st.write("Let's celebrate! Please RSVP below.")

### **Insert Second Green Line Below Title**
### st.markdown('<div class="line-green"></div>', unsafe_allow_html=True)

# **Insert Thick Gold Line**
st.markdown('<div class="line-gold-thick"></div>', unsafe_allow_html=True)

# **Insert Thin Gold Line Below**
st.markdown('<div class="line-gold-thin"></div>', unsafe_allow_html=True)


# # # # # # # # # # 


# **Step 1: Ask for Number of Guests (Includes "Cannot Attend")**
num_guests = st.radio(
    "Number of Guests Attending", 
    options=[1, 2, "Unable to attend"],  
    index=0,  # Default selection is 1
    horizontal=True
)

# **Step 2: Guest 1 Details (Always Visible)**
st.subheader("Your Details")
guest1_name = st.text_input("Your Name", placeholder="Enter your full name").strip().title()
guest1_email = st.text_input("Your Email Address", placeholder="Enter your email")



# **Only Show Additional Fields If Attending (1 or 2 guests)**
if num_guests in [1, 2]:

    # **Step 3: Guest 2 Fields (Only If User Selects 2 Guests)**
    guest2_name = "N/A"
    if num_guests == 2:
        st.subheader("Additional Guest Details")
        guest2_name = st.text_input("Additional Guest Name", placeholder="Enter full name").strip().title()

    # **Step 4: Optional Notes & Comments (Only If Attending)**
    st.subheader("Additional Comments")
    family_notes = st.text_area("Any questions or concerns?", placeholder="i.e., family considerations, dietary restrictions, etc.")
    ### general_commentary = st.text_area("Additional Comments", placeholder="Any questions or concerns?")


### **Step 3: Guest 2 Fields (Only if User Selects 2 Guests)**
##guest2_name = "N/A"
##if num_guests == 2:
##    st.subheader("Additional Guest Details")
##    guest2_name = st.text_input("Additional Guest Name", placeholder="Enter full name").strip().title()

### **Step 4: Optional Notes & Comments**
##family_notes = st.text_area("Family Considerations", placeholder="Dietary restrictions, children, etc.")
##general_commentary = st.text_area("Additional Comments", placeholder="Any questions or concerns?")


### st.markdown('</div>', unsafe_allow_html=True)  # Close inner box
st.markdown('</div>', unsafe_allow_html=True)  # Close main box

# **Step 5: Submit Button**
submitted = st.button("Submit")


if submitted:
    if num_guests in [1, 2] and (not guest1_name or not guest1_email):
        st.error("Please complete all required fields.")
    elif num_guests == 2 and not guest2_name:
        st.error("Please enter the name of your additional guest.")
    elif num_guests == "Unable to attend" and (not guest1_name or not guest1_email):
        st.error("Please complete all required fields.")
    else:
        if num_guests in [1, 2]:  # **If Attending, Send Confirmation Email**
            try:
                confirmation_subject = "Wedding RSVP | April-12-2025 | Confirmed!"
                confirmation_body = f"""
                <html>
                <head>
                    <style>
                        body {{
                            font-family: 'Georgia', serif;
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
                            color: #B8860B; /* Gold */
                        }}
                        h2 {{
                            color: #444;
                            text-align: center;
                            font-size: 18px;
                        }}
                        h3 {{
                            color: #B8860B; /* Gold */ 
                            text-align: center;
                            font-size: 20px;
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
                        <h1>Thank you for your RSVP</h1>
                        <p><p>
                        <h2>WEDDING DETAILS</h2>

                        <hr>
                        <div class="details">
                            <h3><strong>The Venetian</strong></h3>
                            <p>546 River Dr, Garfield, NJ 07026</p>
                            <p>___________________<p>
                            <h3><strong>April 12, 2025</strong> </h3>
                            <p><strong>6:00 PM  </strong> Arrival</p>
			   <p><strong>  6:30 PM  </strong> Ceremony</p>
			   <p><strong> 7:00 PM  </strong> Cocktails</p>
                        </div>
                        <hr>

                 <hr>
                        <div class="details">
            		   <h3><strong>Hotel Recommendations</strong></h3>
            		   <h2><strong>GLENPOINTE | TEANECK, NJ</strong></h2>
			   <p><strong>Marriott </strong> (<a href="https://www.marriott.com/en-us/hotels/ewrgp-teaneck-marriott-at-glenpointe/overview/" target="_blank">Reservations</a>)</p>
			   <p><strong>Hampton Inn & Suites </strong> (<a href="https://www.hilton.com/en/hotels/ewrtehx-hampton-suites-teaneck-glenpointe/" target="_blank">Reservations</a>)</p>
			   <p><strong>Homewood Suites by Hilton </strong> (<a href="https://www.hilton.com/en/hotels/ewrtghw-homewood-suites-teaneck-glenpointe/" target="_blank">Reservations</a>)</p>
                        </div>
                        <hr>


                        <p class="footer">We are excited to celebrate with you!</p>	

                        <p class="footer">With Love,<br> Heather & Rob</p>
                    </div>
                </body>
                </html>
                """

                send_email(guest1_email, confirmation_subject, confirmation_body)

                st.markdown(
                    f"""
                    <div style='text-align: center; margin-top: 20px;'>
                        <h3 style='color: #B8860B;'>RSVP Confirmed | Check your Email for Details!</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"An error occurred: {e}")

        else:  # **If "Unable to attend", Show a Message Instead of Sending an Email**
            st.markdown(
                f"""
                <div style='text-align: center; margin-top: 30px;'>
                    <h2 style='color: #B8860B;'>Thank you for your RSVP</h2>
                    <p style='font-size: 16px; color: #DDD;'>That's unfortunate news, but we understand and appreciate your response.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

