import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Customer Support Dashboard")

st.title("AI Customer Support Dashboard")

st.header("Create Ticket")

customer_name = st.text_input("Customer Name")

issue = st.text_area("Describe Issue")

if st.button("Submit Ticket"):

    payload = {
        "customer_name": customer_name,
        "issue": issue
    }

    try:

        response = requests.post(
            f"{API_URL}/tickets",
            json=payload
        )

        if response.status_code == 200:

            data = response.json()

            st.success("Ticket Created Successfully")

            st.subheader("AI Analysis")

            st.write("Category:", data["category"])
            st.write("Priority:", data["priority"])
            st.write("Sentiment:", data["sentiment"])
            st.write("Department:", data["department"])
            st.write("Escalation:", data["escalation"])
            st.write("Resolution:", data["resolution"])
            st.write("SLA:", data["sla"])

        else:
            st.error("Failed to create ticket")

    except Exception as e:
        st.error(f"Connection Error: {e}")

st.divider()

st.header("All Tickets")

try:

    response = requests.get(f"{API_URL}/tickets")

    if response.status_code == 200:

        tickets = response.json()

        for ticket in tickets:

            st.subheader(f"Ticket ID: {ticket['id']}")

            st.write("Customer:", ticket["customer_name"])
            st.write("Issue:", ticket["issue"])
            st.write("Category:", ticket["category"])
            st.write("Priority:", ticket["priority"])
            st.write("Sentiment:", ticket["sentiment"])
            st.write("Department:", ticket["department"])
            st.write("Escalation:", ticket["escalation"])
            st.write("Resolution:", ticket["resolution"])
            st.write("SLA:", ticket["sla"])

            st.divider()

except Exception as e:
    st.error(f"Connection Error: {e}")