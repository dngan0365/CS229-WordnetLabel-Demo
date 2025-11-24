import streamlit as st
from pyswip import Prolog

# ----------------------------
# Khởi tạo Prolog
# ----------------------------
prolog = Prolog()
prolog.consult("knowledge.pl")  # load file .pl

# ----------------------------
# Hàm query Prolog
# ----------------------------
def query_prolog(query_str):
    try:
        results = list(prolog.query(query_str))
        if not results:
            return False
        if all(isinstance(r, dict) and len(r) == 0 for r in results):
            return True
        return results
    except Exception as e:
        return {"error": str(e)}

# ----------------------------
# Streamlit UI
# ----------------------------
st.set_page_config(page_title="Prolog Query App", layout="wide")
st.title("🧩 Prolog Query App")
st.markdown("Ứng dụng cho phép bạn query knowledge base bằng **Prolog**.")

# ----------------------------
# Chú thích các ký hiệu
# ----------------------------
st.subheader("📝 Chú thích các ký hiệu")
st.markdown("**ngan**: Ngan | **nguyen**: Nguyen | **thao**: Thao | **uit**: University of Information Technology | **gl**: Gia Lai | **vt**: Vung Tau | **bh**: Beach | **td**: Thao's dad | **tm**: Thao's mom | **nd**: Ngan's dad | **nm**: Ngan's mom | **ld**: Nguyen's dad | **lm**: Nguyen's mom")

# ----------------------------
# Section 1: Facts ngắn gọn (dùng caching)
# ----------------------------
@st.cache_data
def get_facts_list(predicate):
    return [f['X'] for f in list(prolog.query(f"{predicate}(X)"))]

@st.cache_data
def get_relation_list(predicate):
    return [(f['X'], f['Y']) for f in list(prolog.query(f"{predicate}(X,Y)"))]

with st.expander("📜 Xem facts ngắn gọn", expanded=True):
    if st.button("Load facts ngắn gọn"):
        st.subheader("Con người")
        st.info(", ".join(get_facts_list("person")))

        st.subheader("Sinh viên ở UIT")
        st.success(", ".join(get_facts_list("student")))

        st.subheader("Bạn bè")
        friends = get_relation_list("friend")
        st.warning(", ".join([f"{x}-{y}" for x, y in friends]))

        st.subheader("Thành phố")
        st.info(", ".join(get_facts_list("city")))

        st.subheader("Nghề nghiệp")
        jobs = get_relation_list("job")
        st.success(", ".join([f"{x}-{y}" for x, y in jobs]))

# ----------------------------
# Section 2: Tất cả facts
# ----------------------------
with st.expander("📜 Xem tất cả facts trong Knowledge Base"):
    if st.button("Load tất cả facts"):
        all_facts = [f"{f['P']}/{f['A']}" for f in list(prolog.query("current_predicate(P/A)"))]
        st.code("\n".join(all_facts))

# ----------------------------
# Section 3: Query Prolog
# ----------------------------
st.subheader("🔍 Thực hiện query Prolog")
query = st.text_input("Nhập câu lệnh Prolog:", "fisherman(td)")

if st.button("Run Query") and query.strip() != "":
    results = query_prolog(query.strip())
    if isinstance(results, bool):
        st.success(f"✅ Result: {results}")
    elif isinstance(results, list):
        if results and all(isinstance(r, dict) for r in results):
            st.write("📋 Kết quả:")
            st.dataframe(results)
        else:
            st.write("Result:", results)
    elif isinstance(results, dict) and "error" in results:
        st.error(f"❌ Error: {results['error']}")
    else:
        st.write("Result:", results)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown("Ứng dụng được xây dựng bằng **Streamlit** và **SWI-Prolog**.")