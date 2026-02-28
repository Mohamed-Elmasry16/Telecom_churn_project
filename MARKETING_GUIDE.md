# 🤖 How to Use the Churn Prediction Chatbot

Welcome! This guide is designed to help the Marketing Team get the most out of our AI-powered assistant. Simply type your questions in plain English, and the bot will analyze our database to tell you how many customers are likely to leave (churn).

---

## 🌐 Getting Started
Access the chatbot through your web browser at:
**`http://localhost:8501`**



---

## ✅ How to Ask Good Questions
The bot is powered by a Large Language Model (LLM) that understands everyday language. However, it provides the most accurate results when you use the **keywords** found in our customer data.

### ✔️ Use These Keywords:

| Category | Keywords to Use |
| :--- | :--- |
| **Customer Profile** | `male`, `female`, `senior citizen`, `married`, `dependents` |
| **Services** | `phone service`, `DSL`, `fiber optic`, `online security`, `tech support`, `streaming TV`, `streaming movies` |
| **Contract** | `month-to-month`, `one year`, `two year` |
| **Payment** | `electronic check`, `mailed check`, `bank transfer`, `credit card` |
| **Tenure** | `tenure > 24`, `tenure < 12` (Use symbols like `>`, `<`, `>=`, `<=`) |
| **Charges** | `monthly charges > 70`, `total charges < 1000` |

### ❌ Avoid:
* **Vague descriptions:** Instead of "elderly," use `senior citizen`.
* **Overcomplicating:** Try to stick to 2–3 filters per question for the best clarity.

---

## 💬 Example Queries
Type these directly into the chat box to see how the system responds:

* **Scenario A:** *"Show me senior citizens with monthly charges above 70 and fiber optic internet."*
* **Scenario B:** *"Find female customers who are married, have dependents, and monthly charges below 50."*
* **Scenario C:** *"Customers with no internet service and no phone service."*
* **Scenario D:** *"List customers paying with electronic check and having a month-to-month contract."*


---

## 📩 Understanding Your Results
After you send a message, the bot will provide a summary:

1.  **High Risk Found:** *"There are 12 customers likely to churn out of 260 matching your criteria."*
2.  **Low Risk Found:** *"None of the customers matching your description are predicted to churn."*
3.  **No Matches:** *"No customers match your criteria."* (This means no one in the database fits your filters).
4.  **Error:** *"Sorry, I couldn't understand the request."* (Try rephrasing using the keywords in the table above).

---

## 💡 Pro Tips for Power Users
* **Range Filtering:** You can use mathematical symbols for numbers, e.g., `tenure >= 6` and `tenure <= 12`.
* **Service Presence:** For any service, you can just say "with" or "without," such as *"customers without tech support."*
* **Start Simple:** Start with a broad question like *"monthly charges > 100"* and then narrow it down by adding more details.

---
*Generated for the Telecom Marketing Department PoC.*
