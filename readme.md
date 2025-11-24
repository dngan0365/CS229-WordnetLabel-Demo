# 🧩 Prolog Query App

A **Streamlit** application that allows users to query a **Prolog knowledge base** in an interactive and user-friendly way.

---

## Features

- View **facts** in a concise format.
- View **all predicates** in the Prolog knowledge base.
- Execute **custom Prolog queries**.
- Highlighted **notations** and symbols for easier understanding of entities.
- Clean and interactive UI using **Streamlit components**.

---

## Installation

1. Clone this repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```
2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install streamlit pyswip

```

4. Make sure you have SWI-Prolog installed and accessible in your PATH.

5. Place your Prolog knowledge base file as knowledge.pl in the project folder.

---

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

1. The app interface provides:

Chú thích các ký hiệu
Explains short symbols used in the knowledge base, for example:
- ngan: Ngan
- thao: Thao
- uit: University of Information Technology
- etc.

2. Một số mệnh đề (Quickly view):
- People
- Students at UIT
- Friends
- Cities
- Jobs

3. All Facts
View all predicates in the knowledge base.

4. Query Prolog
Input a custom Prolog query and view the results:
- Boolean results
- Dictionaries
- Lists
- Errors

---

## Example Queries
```bash
person(X).
student(X).
friend(X,Y).
job(X,Y).
fisherman(td).
```

---

## Screenshots




## License

This project is open source and available under the MIT License.


---

If you want, I can also make a **shorter version** suitable for a GitHub repo that includes **badge support and installation commands** in a clean one-page layout.  

Do you want me to do that?