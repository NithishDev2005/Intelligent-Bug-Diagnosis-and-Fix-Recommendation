import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000/diagnose"


st.set_page_config(
    page_title="Smart Bug Analysis",
    page_icon="🐞",
    layout="wide",
)


st.title("🐞 Smart Bug Analysis")
st.write(
    "AI-powered bug diagnosis using multi-agent analysis and RAG."
)

st.divider()


st.subheader("Submit a Bug Report")

title = st.text_input(
    "Bug Title",
    placeholder="Example: NullPointerException in User Profile",
)

description = st.text_area(
    "Description",
    placeholder="Describe what happens when the bug occurs...",
)

error_type = st.text_input(
    "Error Type",
    placeholder="Example: NullPointerException",
)

stack_trace = st.text_area(
    "Stack Trace",
    placeholder="Paste the stack trace here...",
    height=150,
)

component = st.text_input(
    "Component",
    placeholder="Example: User Service",
)

technologies = st.text_input(
    "Technologies",
    placeholder="Example: Java, Spring Boot",
)


if st.button("🔍 Analyze Bug", type="primary"):

    if not title or not description:
        st.error("Bug Title and Description are required.")

    else:

        bug = {
            "title": title,
            "description": description,
            "error_type": error_type,
            "stack_trace": stack_trace,
            "component": component,
            "technologies": technologies,
        }

        with st.spinner("AI is analyzing the bug..."):

            try:
                response = requests.post(
                    API_URL,
                    json=bug,
                    timeout=300,
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Bug analysis completed!")

                    st.divider()

                    st.subheader("Diagnosis Result")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.metric(
                            "Severity",
                            result.get("severity", "N/A"),
                        )

                    with col2:
                        st.metric(
                            "Priority",
                            result.get("priority", "N/A"),
                        )

                    st.write(
                        "**Failure Point:**",
                        result.get("failure_point", "N/A"),
                    )

                    st.write(
                        "**Error Type:**",
                        result.get("error_type", "N/A"),
                    )

                    st.write(
                        "**Similar Bugs:**",
                        ", ".join(
                            result.get("similar_bugs", [])
                        ),
                    )

                    st.subheader("Root Cause")

                    st.info(
                        result.get(
                            "probable_root_cause",
                            "N/A",
                        )
                    )

                    st.write(
                        "**Confidence:**",
                        result.get("confidence", "N/A"),
                    )

                    st.subheader("Recommended Fix")

                    st.success(
                        result.get(
                            "recommended_fix",
                            "N/A",
                        )
                    )

                    st.subheader("Preventive Action")

                    st.warning(
                        result.get(
                            "preventive_action",
                            "N/A",
                        )
                    )

                else:

                    st.error(
                        f"API Error: {response.status_code}"
                    )

                    st.write(response.text)

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to the backend. "
                    "Please start the FastAPI server first."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The diagnosis took too long. "
                    "Please try again."
                )

            except Exception as e:

                st.error(
                    f"Unexpected error: {str(e)}"
                )