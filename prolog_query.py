from pyswip import Prolog

# Khởi tạo Prolog
prolog = Prolog()
prolog.consult("knowledge.pl")  # load file .pl

def query_prolog(query_str):
    """
    query_str: str, ví dụ 'grandparent(john, Who)'
    
    Trả về:
    - True/False nếu query không bind biến
    - List dict nếu query có bind biến
    - Dict lỗi nếu có exception
    """
    try:
        results = list(prolog.query(query_str))
        
        if not results:
            # Không có kết quả -> mệnh đề false
            return False
        
        # Nếu kết quả là dict rỗng (True) -> mệnh đề đúng
        if all(isinstance(r, dict) and len(r) == 0 for r in results):
            return True
        
        # Nếu có bind biến -> trả list kết quả
        return results
    
    except Exception as e:
        return {"error": str(e)}
