import streamlit as st
import requests

st.set_page_config(
    page_title="YouTube Content Copilot",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 YouTube Content Copilot")

st.write(
    "Create, edit and manage your YouTube content with AI."
)

st.divider()

st.header("Create New Content")

topic = st.text_input(
    "Enter your YouTube topic",
    placeholder="Example: மனிதர்கள் பணம் வந்ததும் ஏன் மாறுகிறார்கள்?"
)

language = st.selectbox(
    "Language",
    ["English", "Tamil", "Tanglish"]
)

content_type = st.selectbox(
    "Content Type",
    ["Long Video", "Shorts"]
)

audience = st.text_input(
    "Target Audience",
    placeholder="Example: பொதுவான தமிழ் பார்வையாளர்கள்"
)

tone = st.selectbox(
    "Tone",
    ["Friendly", "Professional", "Educational", "Storytelling"]
)

duration = st.selectbox(
    "Video Duration",
    ["1-3 minutes", "5-10 minutes", "10-15 minutes", "15-30 minutes"]
)

if st.button("🚀 Create Content", type="primary"):

    if not topic:
        st.warning("Please enter a topic first.")

    else:

        data = {
            "topic": topic,
            "language": language,
            "content_type": content_type,
            "audience": audience,
            "tone": tone,
            "duration": duration
        }

        try:

            response = requests.post(
                "http://127.0.0.1:8000/content/create",
                json=data
            )

            if response.status_code == 200:

                result = response.json()

                st.success("✅ AI content generated successfully!")

                st.divider()

                st.subheader("📝 Generated Content")

                st.write(
                    result["generated_content"]
                )

            else:

                st.error(
                    f"Backend error: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to FastAPI. "
                "Please make sure the backend is running."
            )