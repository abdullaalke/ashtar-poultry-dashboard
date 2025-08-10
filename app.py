import streamlit as st
import pandas as pd

# بيانات المنتجات
PRODUCTS = [
    {
        "id": "AMR-01",
        "name": "Ameraucana",
        "purpose": "إنتاج بيض",
        "origin": "أمريكا",
        "egg_color": "أزرق سماوي",
        "weight_kg": "2.0–2.7",
        "temperament": "هادئ",
        "price_aed": 180,
        "stock": 24,
        "availability": "متوفر",
        "image": "",
        "notes": "خط بيض أزرق ثابت، تحمل جيد للحرارة.",
        "wa": "+971500000000"
    },
    {
        "id": "AST-02",
        "name": "Australorp",
        "purpose": "مزدوج الغرض",
        "origin": "أستراليا",
        "egg_color": "بني فاتح",
        "weight_kg": "2.5–3.1",
        "temperament": "هادئ/نشِط",
        "price_aed": 160,
        "stock": 12,
        "availability": "متوفر",
        "image": "",
        "notes": "أداء ممتاز في إنتاج البيض مع نمو لحمي جيد.",
        "wa": "+971500000000"
    },
    {
        "id": "ORP-03",
        "name": "Orpington (Buff)",
        "purpose": "مزدوج الغرض",
        "origin": "المملكة المتحدة",
        "egg_color": "كريمي",
        "weight_kg": "3.0–3.6",
        "temperament": "أليف",
        "price_aed": 220,
        "stock": 8,
        "availability": "محدود",
        "image": "",
        "notes": "شكل جذاب وحجم كبير، مناسب للأسر.",
        "wa": "+971500000000"
    },
    {
        "id": "COC-04",
        "name": "Cochin",
        "purpose": "زينة",
        "origin": "الصين",
        "egg_color": "بني",
        "weight_kg": "3.2–4.2",
        "temperament": "لطيف",
        "price_aed": 250,
        "stock": 5,
        "availability": "محدود",
        "image": "",
        "notes": "ريش غزير وأرجل مكسوّة، مظهر استعراضي.",
        "wa": "+971500000000"
    },
    {
        "id": "SLK-05",
        "name": "Silkie",
        "purpose": "زينة",
        "origin": "الصين",
        "egg_color": "كريمي",
        "weight_kg": "0.8–1.1",
        "temperament": "حنون",
        "price_aed": 200,
        "stock": 18,
        "availability": "متوفر",
        "image": "",
        "notes": "ريش حريري، أمومة ممتازة للتفريخ.",
        "wa": "+971500000000"
    },
    {
        "id": "BRH-06",
        "name": "Brahma (Light)",
        "purpose": "مزدوج الغرض",
        "origin": "أمريكا",
        "egg_color": "بني",
        "weight_kg": "3.5–5.0",
        "temperament": "هادئ",
        "price_aed": 260,
        "stock": 7,
        "availability": "محدود",
        "image": "",
        "notes": "أحجام عملاقة ومنظر مهيب، متحمل للبرد.",
        "wa": "+971500000000"
    },
    {
        "id": "SUS-07",
        "name": "Sussex (Speckled)",
        "purpose": "مزدوج الغرض",
        "origin": "المملكة المتحدة",
        "egg_color": "كريمي",
        "weight_kg": "2.7–3.2",
        "temperament": "ودود",
        "price_aed": 170,
        "stock": 15,
        "availability": "متوفر",
        "image": "",
        "notes": "سلالة متوازنة وسهلة التربية للمبتدئ.",
        "wa": "+971500000000"
    },
    {
        "id": "LEH-08",
        "name": "Leghorn (White)",
        "purpose": "إنتاج بيض",
        "origin": "إيطاليا",
        "egg_color": "أبيض",
        "weight_kg": "1.8–2.4",
        "temperament": "نشِط",
        "price_aed": 140,
        "stock": 20,
        "availability": "متوفر",
        "image": "",
        "notes": "إنتاج بيض مرتفع وكفاءة علف ممتازة.",
        "wa": "+971500000000"
    },
    {
        "id": "WYN-09",
        "name": "Wyandotte (Silver Laced)",
        "purpose": "مزدوج الغرض",
        "origin": "أمريكا",
        "egg_color": "بني فاتح",
        "weight_kg": "2.5–3.2",
        "temperament": "متوازن",
        "price_aed": 210,
        "stock": 9,
        "availability": "محدود",
        "image": "",
        "notes": "لون ريش مميز وإنتاج جيد.",
        "wa": "+971500000000"
    },
    {
        "id": "AYA-10",
        "name": "Ayam Cemani",
        "purpose": "زينة",
        "origin": "إندونيسيا",
        "egg_color": "كريمي",
        "weight_kg": "1.5–2.0",
        "temperament": "حيوي",
        "price_aed": 750,
        "stock": 3,
        "availability": "نادر",
        "image": "",
        "notes": "تلون ميلانيني أسود كامل ومطلوب لهواة الزينة.",
        "wa": "+971500000000"
    }
]

# تحويل البيانات لـ DataFrame
df = pd.DataFrame(PRODUCTS)

st.set_page_config(page_title="لوحة منتجات مزرعة عشتار", layout="wide")

st.title("🐓 لوحة منتجات مزرعة عشتار")
st.markdown("عرض تفاعلي لمنتجات دواجن الزينة والسلالات العالمية مع بحث وفلاتر.")

# فلاتر
col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
search = col1.text_input("بحث سريع")
purpose_filter = col2.selectbox("الغرض", [""] + sorted(df["purpose"].unique()))
origin_filter = col3.selectbox("المنشأ", [""] + sorted(df["origin"].unique()))
sort_by = col4.selectbox("ترتيب حسب", ["الاسم", "السعر (تصاعدي)", "السعر (تنازلي)", "المتوفر أولا"])

min_price, max_price = st.slider("نطاق السعر (درهم)", 0, int(df["price_aed"].max()), (0, int(df["price_aed"].max())))

# تطبيق الفلاتر
filtered = df.copy()
if search:
    filtered = filtered[filtered.apply(lambda row: search.lower() in " ".join(map(str, row)).lower(), axis=1)]
if purpose_filter:
    filtered = filtered[filtered["purpose"] == purpose_filter]
if origin_filter:
    filtered = filtered[filtered["origin"] == origin_filter]
filtered = filtered[(filtered["price_aed"] >= min_price) & (filtered["price_aed"] <= max_price)]

# ترتيب
if sort_by == "الاسم":
    filtered = filtered.sort_values("name")
elif sort_by == "السعر (تصاعدي)":
    filtered = filtered.sort_values("price_aed")
elif sort_by == "السعر (تنازلي)":
    filtered = filtered.sort_values("price_aed", ascending=False)
elif sort_by == "المتوفر أولا":
    filtered = filtered.sort_values("stock", ascending=False)

# عرض النتائج
st.write(f"العناصر المعروضة: {len(filtered)} / {len(df)} — متوسط السعر: {round(filtered['price_aed'].mean(), 2) if len(filtered) else '—'} درهم")

for _, row in filtered.iterrows():
    with st.container():
        cols = st.columns([1, 3])
        with cols[0]:
            st.image(row["image"] or "https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?q=80&w=1200&auto=format&fit=crop", use_column_width=True)
        with cols[1]:
            st.subheader(row["name"])
            st.write(f"**الغرض:** {row['purpose']} — **المنشأ:** {row['origin']}")
            st.write(f"**لون البيض:** {row['egg_color']} — **الوزن (كجم):** {row['weight_kg']}")
            st.write(f"**الطبع:** {row['temperament']}")
            st.write(f"**ملاحظات:** {row['notes']}")
            st.write(f"**السعر:** {row['price_aed']} درهم — **المتوفر:** {row['stock']}")
            wa_link = f"https://wa.me/{row['wa'].replace('+','').replace(' ','')}?text=مرحباً، أود الاستفسار عن السلالة: {row['name']} (معرّف: {row['id']})."
            st.markdown(f"[💬 تواصل عبر واتساب]({wa_link})", unsafe_allow_html=True)
    st.markdown("---")
