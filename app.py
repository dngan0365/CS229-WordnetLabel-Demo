import streamlit as st
from pyswip import Prolog
from utils import nl_to_prolog

# ----------------------------
# Khởi tạo Prolog
# ----------------------------
prolog = Prolog()
prolog.consult("assets/knowledge2.pl")

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
# Chú thích ký hiệu
# ----------------------------
st.subheader("📝 Chú thích các ký hiệu")
st.markdown(
    "**ngan**: Ngan | **nguyen**: Nguyen | **thao**: Thao | "
    "**uit**: University of Information Technology | "
    "**gl**: Gia Lai | **vt**: Vung Tau | **bh**: Beach | "
    "**td**: Thao's dad | **tm**: Thao's mom | "
    "**nd**: Ngan's dad | **nm**: Ngan's mom | "
    "**ld**: Nguyen's dad | **lm**: Nguyen's mom"
)

# ----------------------------
# Section 1: Facts ngắn gọn
# ----------------------------
@st.cache_data
def get_facts_list(predicate):
    p = Prolog()
    p.consult("assets/knowledge.pl")
    return [f["X"] for f in p.query(f"{predicate}(X)")]

@st.cache_data
def get_relation_list(predicate):
    p = Prolog()
    p.consult("assets/knowledge.pl")
    return [(f["X"], f["Y"]) for f in p.query(f"{predicate}(X,Y)")]

with st.expander("📜 Xem facts ngắn gọn", expanded=True):
    if st.button("Load facts ngắn gọn"):
        st.subheader("Con người")
        st.info(", ".join(get_facts_list("person")))

        st.subheader("Sinh viên UIT")
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
        all_facts = [
            f"{f['P']}/{f['A']}"
            for f in prolog.query("current_predicate(P/A)")
        ]
        st.code("\n".join(all_facts))

# =====================================================
# Section 3: NL → Prolog → Run (UX chuẩn)
# =====================================================
st.subheader("🔍 Thực hiện Query Prolog")

# Init session state
if "prolog_query" not in st.session_state:
    st.session_state.prolog_query = ""

# Toggle NLP
use_nl = st.toggle("🤖 Dùng ngôn ngữ tự nhiên để tạo Prolog?", value=False)

# ----------- Ngôn ngữ tự nhiên -----------
if use_nl:
    st.markdown("### 🤖 Câu hỏi ngôn ngữ tự nhiên")
    nl_question = st.text_input(
        "Ví dụ: Bố của Thảo có phải là ngư dân không?",
        key="nl_question"
    )

    if st.button("✨ Tạo câu lệnh Prolog"):
        if nl_question.strip():
            generated = nl_to_prolog(nl_question)
            if generated:
                st.session_state.prolog_query = generated
                st.success("✅ Đã tạo Prolog – bạn có thể chỉnh sửa bên dưới")
            else:
                st.error("❌ Không thể chuyển câu hỏi sang Prolog")

# ----------- Ô nhập Prolog (CHUẨN STATE) -----------
st.markdown("### 🧩 Câu lệnh Prolog")

st.text_input(
    "Nhập hoặc chỉnh sửa câu lệnh Prolog:",
    key="prolog_query"
)

# ----------- Run Query -----------
if st.button("▶️ Run Query"):
    query = st.session_state.prolog_query

    if query.strip():
        results = query_prolog(query.strip())

        if isinstance(results, bool):
            st.success(f"✅ Result: {results}")
        elif isinstance(results, list):
            st.write("📋 Kết quả:")
            st.dataframe(results)
        elif isinstance(results, dict) and "error" in results:
            st.error(f"❌ Error: {results['error']}")
        else:
            st.write(results)
    else:
        st.warning("⚠️ Vui lòng nhập câu lệnh Prolog")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown("Ứng dụng được xây dựng bằng **Streamlit** và **SWI-Prolog**.")
