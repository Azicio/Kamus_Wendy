import streamlit as st
import json
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Kamus Saku Pemasyarakatan", page_icon="⚖️")

# --- CUSTOM THEME (background & heading colors) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #243887; /* Light gray background */
    }
    h1 {
        color: #b9cef0; /* Deep blue for the main title */
    }
    </style>
    """, unsafe_allow_html=True)

# --- DATA LOADING & SAVING ---
def load_data():
    path = "kamus_pemasyarakatan.json"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_data(data):
    path = "kamus_pemasyarakatan.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

db = load_data()

# --- UI ---
st.title("⚖️ Kamus Saku Pemasyarakatan")
st.info(
    "Ini adalah edisi pertama Kamus Pemasyarakatan bahasa Indonesia - Inggris "
    "yang dibuat oleh Wendy Nahaklay selaku peserta magang di bidang Penerjemah."
)

if not db:
    st.error("⚠️ Database file (kamus_pemasyarakatan.json) not found in the root directory.")
else:
    # --- SEARCH FUNCTION ---
    search = st.text_input("🔍 Search Term (Indonesian or English)", placeholder="e.g. Warga Binaan")

    if search:
        found = False
        for category, terms in db.items():
            for item in terms:
                indo, eng, definition = item[0], item[1], item[2]
                if search.lower() in indo.lower() or search.lower() in eng.lower():
                    st.info(f"**{indo}** = *{eng}*")
                    st.write(f"**Definisi:** {definition}")
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
                indo, eng, definition = item[0], item[1], item[2]
                st.write(f"**{indo}**: {eng}")
                st.caption(definition)
                st.write("")

    # --- ADD NEW TERM ---
    with st.expander("➕ Add New Term to Dictionary"):
        with st.form("add_form"):
            new_cat = st.selectbox("Category", list(db.keys()))
            new_indo = st.text_input("Indonesian Term")
            new_eng = st.text_input("English Translation")
            new_def = st.text_area("Definition")
            
            if st.form_submit_button("Add to Library"):
                if new_indo and new_eng and new_def:
                    db[new_cat].append([new_indo, new_eng, new_def])
                    save_data(db)
                    st.success(f"Added {new_indo} to {new_cat}!")
                    st.rerun()