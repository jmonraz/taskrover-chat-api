import spacy

# load spacy model
nlp = spacy.load('en_core_web_sm')

department_keywords = {
    'IT Support':
    ['login', 'password', 'email', 'computer', 'account', 'locked', 'software', 'hardware', 'integration'],
    'Accounting': ['billing', 'invoice', 'payment', 'account', 'credit', 'debit', 'balance', 'refund', 'tax', 'prices', 'charge', 'charged'],
    'Customer Service': ['order', 'delivery', 'return', 'shipping', 'cancel', 'exchange', 'status', 'ticket', 'shipped'],
    'Sales': ['quote', 'pricing', 'discount', 'promotion', 'sales', 'revenue', 'commission', 'quota', 'target'],
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

    elif department == "HR":
        if "salary" in text or "payroll" in text:
            return "Payroll"
        elif "leave" in text or "vacation" in text:
            return "Leave Requests"
        elif "benefits" in text:
            return "Benefits and Compensation"
        elif "hiring" in text or "recruitment" in text:
            return "Recruitment"
        else:
            return "General HR Inquiries"

    # Add more departments and categories as needed

    else:
        return "General Inquiry"


def calculate_compound():

    base_salary = 115,000
    rate = 0.07
    new_salary = 0
    # write a for loop to iterate from range 1 to 5
    for i in range(1, 6):
        new_salary = base_salary + (base_salary * rate)

    print(new_salary)
