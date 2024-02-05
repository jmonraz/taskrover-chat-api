import spacy

# load spacy model
nlp = spacy.load('en_core_web_sm')

department_keywords = {
    'IT':
        ['login', 'password', 'email', 'computer', 'account', 'locked', 'software', 'hardware', 'integration',
         'compatibility', 'network', 'setup', 'data', 'installation', 'software', 'display', 'error'],
    'Accounting': ['billing', 'invoice', 'payment', 'account', 'credit', 'debit', 'balance', 'refund', 'tax', 'prices',
                   'charge', 'charged', 'bill', 'money', 'dollar', 'dollars', 'payroll', 'pay', 'paid', 'owe', 'owed', 'due', 'financial', 'asset', 'income', 'balance'],
    'Customer Service': ['order', 'delivery', 'return', 'shipping', 'cancel', 'exchange', 'status', 'ticket', 'shipped',
                         'cancellation', 'shipped', 'ship', 'tracking']
}


# method to assign department and category
def assign_department_and_category(subject, description):
    text = subject + ' ' + description
    doc = nlp(text)

    for department, keywords in department_keywords.items():
        if any(keyword in doc.text.lower() for keyword in keywords):
            return department, determine_category(department, doc.text)

    return 'Other', 'Other'


def determine_category(department, text):
    text = text.lower()

    if department == "IT Support":
        if "password" in text or "login" in text:
            return "Account Issues"
        elif "email" in text:
            return "Email Problems"
        elif "computer" in text or "hardware" in text:
            return "Hardware Support"
        else:
            return "General IT Support"

    elif department == "Accounting":
        if "billing" in text or "invoice" in text:
            return "Billing"
        elif "payment" in text or "refund" in text:
            return "Payment"
        else:
            return "General Accounting"

    elif department == "Customer Service":
        if "order" in text or "delivery" in text:
            return "Order Issues"
        elif "return" in text or "exchange" in text:
            return "Return/Exchange"
        else:
            return "General Customer Service"

    else:
        return "Other"
