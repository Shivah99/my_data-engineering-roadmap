# Day 9 — Python Operators, Variables, and Meaning

### Day 9 is about:
```
- operators
- keywords
- mutability
- truthy / falsy values
- `None`
```

## 📁 Project Structure

```
operators/
├── README.md
├── day2_precision_drills.py
├── day2_error_reasoning.py
└── day2_mini_project/
    └── operator_playground.py
```
---

## 🧩 PART 1 — Precision Drills (Foundation)

Create a .py file:

### Q1. Expressions vs Statements

Write **6 separate lines** of code.

Rules:
- Exactly **3 expressions**
- Exactly **3 statements**
- Comment each line as:
  - `# expression`
  - `# statement`
- At least **one line must look like an expression but actually be a statement**

The goal is precision, not memorization.

---

### Q2. Operator Identification

Rewrite **one line per operator category** and comment it clearly.

#### Operator categories to use:
```
- arithmetic
- comparison
- assignment
- logical
- membership
```
Each line must include:
- valid Python code
- a comment naming the operator category

---

### Q3. Keywords Trap

Write **three illegal lines of code**.

Each line must violate a **different rule**:

1. Using a Python keyword as a variable name
2. Assigning to a literal value
3. Assignment inside a function call

For **each line**, add a comment explaining **why Python rejects it**.

Do not fix the errors.  
Understanding rejection is the point.

---

## 🧠 PART 2 — Error Reasoning (No Running First)

Create the file:

```
day2_error_reasoning.py
```

For **each snippet below**, do the following:

1. Predict one of:
   - `SyntaxError`
   - `TypeError`
   - `NameError`
   - `Runs fine`
2. Explain **why**
3. Then run the code
4. Confirm or correct your explanation

### Snippet A

```python
print(not True == False)
```

### Snippet B

```python
x = 5
print(x = 3)
```

### Snippet C

```python
a = None
print(a + 1)
```

### Snippet D

```python
x = [1, 2, 3]
y = x
y[0] = 99
print(x)
```

If your prediction is wrong, fix your comment.  
Do not move on until you understand why.

---

## 🔬 PART 3 — Mini Project (Very Important)

Create the folder:

```
day2_mini_project/
```

Inside it, create:

```
operator_playground.py
```

### Required Header

```python
"""
Day 2 Mini Project
Goal: Prove understanding of Python operators and data behavior
"""
```

---

### Project Goal

This script must **prove**, not claim, that you understand:

- operators
- data types
- mutability
- `None`
- truthy / falsy behavior
- identity vs equality

---

### Mandatory Requirements

Your script must:

1. Define at least:
   - one `int`
   - one `list`
   - one `dict`
   - one `None`
2. Use **all** operator categories at least once:
   - arithmetic
   - comparison
   - assignment
   - logical
   - membership
   - identity
3. Include **at least 3 deliberate mistakes**
   - commented out
   - each with an explanation of why it is wrong
4. Print outputs that **prove behavior**, not just values

Examples of behaviors to demonstrate (not solutions):

- `is` vs `==`
- list mutation through shared references
- `None` failing in arithmetic
- truthy and falsy values in logical operations

---

## 🧪 How You Should Work

For **every file**:

1. Predict what will happen
2. Write comments first
3. Run the code
4. Adjust comments if your prediction was wrong



---

