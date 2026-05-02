import streamlit as st
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Kamus Saku Pemasyarakatan", page_icon="⚖️")

st.info("Ini adalah edisi pertama Kamus Pemasyarakatan bahasa Indonesia - Inggris yang dibuat oleh Wendy Nahaklay selaku peserta magang di bidang Penerjemah")

# --- DATA LOADING ---
def load_data():
    # Remove "data/" so it looks in the root folder
    path = "kamus_pemasyarakatan.json" 
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# --- UI ---
st.title("⚖️ Kamus Saku Pemasyarakatan")
st.caption("Digital Glossary for Correctional Terminology")

# --- SEARCH FUNCTION ---
search = st.text_input("🔍 Search Term (Indonesian or English)", placeholder="e.g. Warga Binaan")

if search:
    found = False
    for category, terms in db.items():
        for item in terms:
            # We unpack 3 values now: indo, eng, and the new definition
            indo, eng, definition = item[0], item[1], item[2]
            
            if search.lower() in indo.lower() or search.lower() in eng.lower():
                st.info(f"**{indo}** = *{eng}*")
                st.write(f"**Definisi:** {definition}") # Added definition display
                st.caption(f"Category: {category}")
                st.divider()
                found = True
    if not found:
        st.warning("No matches found.")

# --- BROWSE BY CATEGORY ---
st.divider()
st.subheader("📚 Browse by Category")
for category, terms in db.items():
    with st.expander(category):
        for item in terms:
            # Unpacking 3 values here as well to avoid the ValueError
            indo, eng, definition = item[0], item[1], item[2]
            st.write(f"**{indo}**: {eng}")
            st.caption(definition) # Showing definition in the browse view
            st.write("") 


# --- ADD NEW TERM (Updated for 3 values) ---
with st.expander("➕ Add New Term to Dictionary"):
    with st.form("add_form"):
        new_cat = st.selectbox("Category", list(db.keys()))
        new_indo = st.text_input("Indonesian Term")
        new_eng = st.text_input("English Translation")
        new_def = st.text_area("Definition") # Added a text area for definition
        
        if st.form_submit_button("Add to Library"):
            if new_indo and new_eng and new_def:
                # We save all 3 as a single list entry
                db[new_cat].append([new_indo, new_eng, new_def])
                save_data(db)
                st.success(f"Added {new_indo} to {new_cat}!")
                st.rerun()