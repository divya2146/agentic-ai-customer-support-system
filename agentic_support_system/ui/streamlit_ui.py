# app.py
# Agentic AI Customer Support Platform (FULL FIXED VERSION)
# Run: streamlit run app.py

import streamlit as st
import pandas as pd
import os
import json
from datetime import datetime

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="AI Support Platform",
    page_icon="🎫",
    layout="wide"
)

# =====================================================
# FILE
# =====================================================
DATA_FILE = "tickets.json"

# =====================================================
# LOAD DATA
# =====================================================
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return pd.DataFrame(data)

    # default sample data
    sample = [
        {"id":1,"user_id":"1001","issue":"fraud","department":"Security","priority":"High","status":"Open"},
        {"id":2,"user_id":"1002","issue":"payment failed","department":"Billing","priority":"High","status":"Open"},
        {"id":3,"user_id":"1003","issue":"login issue","department":"Technical","priority":"Medium","status":"Open"},
        {"id":4,"user_id":"1004","issue":"refund request","department":"Billing","priority":"Medium","status":"Open"},
        {"id":5,"user_id":"1005","issue":"fraud detected","department":"Security","priority":"High","status":"Open"},
        {"id":6,"user_id":"1006","issue":"payment pending","department":"Billing","priority":"Medium","status":"Open"},
        {"id":7,"user_id":"1007","issue":"technical error","department":"Technical","priority":"Low","status":"Open"},
        {"id":8,"user_id":"1008","issue":"refund delayed","department":"Billing","priority":"Medium","status":"Open"},
        {"id":9,"user_id":"1009","issue":"product missing","department":"Support","priority":"Low","status":"Open"},
        {"id":10,"user_id":"1010","issue":"page hanging","department":"Technical","priority":"Medium","status":"Open"},
    ]
    return pd.DataFrame(sample)

# =====================================================
# SAVE DATA
# =====================================================
def save_data(df):
    with open(DATA_FILE, "w") as f:
        json.dump(df.to_dict(orient="records"), f, indent=4)

# =====================================================
# AGENTIC LOGIC
# =====================================================
def predict_department(issue):
    issue = issue.lower()

    if "payment" in issue or "refund" in issue or "bill" in issue:
        return "Billing"

    elif "fraud" in issue or "hack" in issue:
        return "Security"

    elif "login" in issue or "error" in issue or "page" in issue or "technical" in issue:
        return "Technical"

    elif "product" in issue or "missing" in issue:
        return "Support"

    return "General"


def predict_priority(issue):
    issue = issue.lower()

    if "fraud" in issue or "payment failed" in issue:
        return "High"

    elif "refund" in issue or "login" in issue or "page" in issue:
        return "Medium"

    return "Low"


def suggested_resolution(issue):
    issue = issue.lower()

    if "payment" in issue:
        return "Verify card/bank balance and retry."

    elif "refund" in issue:
        return "Refund request forwarded to billing."

    elif "fraud" in issue:
        return "Freeze account and escalate."

    elif "login" in issue:
        return "Reset password and clear cache."

    elif "page" in issue:
        return "Try browser refresh / technical team notified."

    return "Support team will contact user."

# =====================================================
# LOAD
# =====================================================
df = load_data()

# =====================================================
# SIDEBAR
# =====================================================
st.sidebar.title("🚀 Navigation")
page = st.sidebar.radio(
    "Go To",
    ["Dashboard", "Create Ticket", "Manage Tickets", "Search Tickets"]
)

# =====================================================
# TITLE
# =====================================================
st.title("🎫 Agentic AI Customer Support Platform")

# =====================================================
# DASHBOARD
# =====================================================
if page == "Dashboard":

    st.subheader("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Tickets", len(df))
    col2.metric("Open Tickets", len(df[df["status"]=="Open"]))
    col3.metric("Closed Tickets", len(df[df["status"]=="Closed"]))

    st.write("### Department Wise")
    st.bar_chart(df["department"].value_counts())

    st.write("### Priority Wise")
    st.bar_chart(df["priority"].value_counts())

# =====================================================
# CREATE TICKET (FIXED USER ID)
# =====================================================
elif page == "Create Ticket":

    st.subheader("📝 Create Ticket")

    # IMPORTANT FIX:
    # text_input keeps exact entered value
    user_id = st.text_input("User ID", key="create_uid")

    issue = st.text_input("Enter Issue", key="create_issue")

    if issue.strip() != "":
        dept = predict_department(issue)
        priority = predict_priority(issue)
        resolution = suggested_resolution(issue)

        st.info(f"Predicted Department: {dept}")
        st.success(f"Predicted Priority: {priority}")
        st.warning(f"Suggested Resolution: {resolution}")

    if st.button("Create Ticket"):

        # FIXED VALIDATION
        if user_id.strip() == "" or issue.strip() == "":
            st.error("Please enter User ID and Issue")

        else:
            new_id = int(df["id"].max()) + 1 if len(df) > 0 else 1

            new_row = {
                "id": new_id,
                "user_id": user_id.strip(),   # EXACT VALUE ENTERED BY USER
                "issue": issue.strip(),
                "department": predict_department(issue),
                "priority": predict_priority(issue),
                "status": "Open"
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            save_data(df)

            st.success(f"Ticket Created Successfully for User ID {user_id}")

# =====================================================
# MANAGE TICKETS
# =====================================================
elif page == "Manage Tickets":

    st.subheader("📂 Manage Tickets")

    st.dataframe(df, use_container_width=True)

    ticket_id = st.number_input("Enter Ticket ID", min_value=1, step=1)

    if st.button("Close Ticket"):

        index = df[df["id"] == ticket_id].index

        if len(index) > 0:
            df.loc[index, "status"] = "Closed"
            save_data(df)
            st.success("Ticket Closed Successfully")

        else:
            st.error("Ticket ID Not Found")

# =====================================================
# SEARCH (FIXED USER ID SEARCH)
# =====================================================
elif page == "Search Tickets":

    st.subheader("🔎 Search Tickets")

    keyword = st.text_input("Enter keyword / user id / ticket id")

    if keyword.strip() == "":
        result = df

    else:
        key = keyword.strip().lower()

        result = df[
            df["issue"].astype(str).str.lower().str.contains(key) |
            df["user_id"].astype(str).str.lower().str.contains(key) |
            df["id"].astype(str).str.contains(key) |
            df["department"].astype(str).str.lower().str.contains(key) |
            df["priority"].astype(str).str.lower().str.contains(key) |
            df["status"].astype(str).str.lower().str.contains(key)
        ]

    st.dataframe(result, use_container_width=True)

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption("Built with Streamlit + Python + Agentic AI Logic")