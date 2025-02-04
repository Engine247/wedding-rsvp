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
            border-radius: 5px;
            width: 100%;
            font-family: 'Georgia Pro', Georgia, serif;
        }}

        .stTextArea > div > textarea {{
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
st.markdown('</div>', unsafe_allow_html=True)  # CLOSE event-container

# === Date Container
st.markdown('<div class="event-container">', unsafe_allow_html=True) # OPEN event container
st.markdown('<div class="event-title">April 12, 2025</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details"><strong>6:00 PM : </strong> Arrival</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details"><strong>6:30 PM : </strong>Ceremony</div>', unsafe_allow_html=True)
st.markdown('<div class="event-details"><strong>7:00 PM : </strong>Cocktails</div>', unsafe_allow_html=True)
### st.markdown('<div class="divider-thin"></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # CLOSE event-container


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
if num_guests in [1, 2, "Unable to attend"]:
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



###  <<< Email Function >>>

# **Sender Email Configuration**
sender_email_1 = "rob.haddad.222@gmail.com"  
sender_email_2 = "heathervictoria412@gmail.com"
sender_password = "yzmj yhno npkd oxvz"  # Google App Password (replace with env variable later)

# **Function to Send Email**
def send_email(to_email, subject, body):
    try:
        # Setup SMTP Server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email_1, sender_password)

        # Email Setup
        msg = MIMEMultipart()
        msg["From"] = f'"Heather & Rob | April-12-2025" <{sender_email_1}>'
        msg["To"] = to_email
        msg["Subject"] = subject

        # Attach HTML Content
        msg.attach(MIMEText(body, "html", "utf-8"))

        # Send Email to RSVP Submitter
        server.sendmail(sender_email_1, [to_email, sender_email_2], msg.as_string())

        # **Send Notification Email to Hosts with ALL Details**
        host_subject = f"New RSVP Submission from {to_email}"
        host_body = f"""
        <html>
        <body>
            <h2>New RSVP Submission</h2>
            <p><strong>Guest Name:</strong> {guest1_name}</p>
            <p><strong>Email:</strong> {guest1_email}</p>
            <p><strong>Number of Guests:</strong> {num_guests}</p>
            {"<p><strong>Additional Guest:</strong> " + guest2_name + "</p>" if num_guests == 2 else ""}
            <p><strong>Comments:</strong> {comments if comments else "No additional comments provided"}</p>
        </body>
        </html>
        """

        msg_host = MIMEMultipart()
        msg_host["From"] = f'"Heather & Rob | RSVP System" <{sender_email_1}>'
        msg_host["To"] = sender_email_2
        msg_host["Subject"] = host_subject
        msg_host.attach(MIMEText(host_body, "html", "utf-8"))

        # Send Email to Host
        server.sendmail(sender_email_1, sender_email_2, msg_host.as_string())

        # Close SMTP Server
        server.quit()

    except Exception as e:
        st.error(f"Failed to send email: {e}")



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
                .hotel-links a {{
                    color: {gold_color};
                    text-decoration: none;
                    font-weight: bold;
                }}
                .hotel-links a:hover {{
                    text-decoration: underline;
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

                <h2>Hotel Recommendations</h2>
                <div class="hotel-links">
                    <p><strong>GLENPOINTE | TEANECK, NJ</strong></p>
                    <p><a href="https://www.marriott.com" target="_blank">Marriott (Reservations)</a></p>
                    <p><a href="https://www.hilton.com/en/hotels/tetnwhw-homewood-suites-teaneck-glenpointe" target="_blank">Homewood Suites by Hilton (Reservations)</a></p>
                    <p><a href="https://www.hilton.com/en/hotels/tetnwhx-hampton-inn-teaneck-glenpointe/" target="_blank">Hampton Inn & Suites (Reservations)</a></p>
                </div>

                <hr>

                <p class="footer">We are excited to celebrate with you!</p>

                <p class="footer">With Love,<br> Heather & Rob</p>
            </div>
        </body>
        </html>
        """


        msg.attach(MIMEText(body, "html", "utf-8"))

        server.sendmail("rob.haddad.222@gmail.com", [to_email, "heathervictoria412@gmail.com", "rob.haddad.222@gmail.com"], msg.as_string())
        server.quit()
    except Exception as e:
        st.error(f"Failed to send email: {e}")




# === Handle Submission ===


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

                        <div class="details">
                            <h3><strong>Guest Details</strong></h3>
                            <p><strong>Your Name:</strong> {guest1_name}</p>
                            {"<p><strong>Guest Name:</strong> " + guest2_name + "</p>" if num_guests == 2 else ""}
                            {"<p><strong>Comments:</strong> " + comments + "</p>" if comments.strip() else ""}
                        </div>
                        <hr>

                        <div class="details">
                            <h3>We are excited to celebrate with you!</p
                            <h2>With Love,<br> Heather & Rob</p>
                        </div>

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



        else:  # **If "Unable to attend", Send an Email Instead of Just Displaying a Message**
            
            unable_subject = "Wedding RSVP | April-12-2025 | Unable to Attend"
            
            unable_body = f"""
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
                    <h1>Thank You for Your RSVP</h1>
                    
                    <p>We're sorry you won't be able to attend, but we truly appreciate your response.</p>
                    
                    <hr>
                                        
                    <p class="footer">With Love,</p>
                    <p class="footer">Heather & Rob</p>

                    <hr>
                    <hr>

                    <h3><strong>Guest Details</strong></h3>
                    <p><strong>Name:</strong> {guest1_name}</p>
                    <p><strong>Email:</strong> {guest1_email}</p>
                    
                    {"<p><strong>Additional Comments:</strong> " + comments + "</p>" if comments.strip() else ""}
                    
                    <hr>


                </div>
            </body>
            </html>
            """

            # Send Confirmation Email to Guest & Notification to Hosts
            send_email(guest1_email, unable_subject, unable_body)  # Send Email to Guest
            send_email(sender_email_1, f"Unable to Attend RSVP from {guest1_name}", unable_body)  # Notify Hosts
            
            # Display On-Screen Message for Guest
            st.markdown(
                f"""
                <div style='text-align: center; margin-top: 30px;'>
                    <h2 style='color: #B8860B;'>Thank you for your RSVP</h2>
                    <p style='font-size: 16px; color: #DDD;'>That's unfortunate news, but we understand and appreciate your response.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
