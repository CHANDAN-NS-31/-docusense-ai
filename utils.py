import re

def redact_sensitive_info(text):
    text = re.sub(r'\b[\w\.-]+@[\w\.-]+\.\w+\b', '[REDACTED_EMAIL]', text)
    text = re.sub(r'\b\d{10}\b', '[REDACTED_PHONE]', text)
    text = re.sub(r'(sk-[a-zA-Z0-9]+|AIza[0-9A-Za-z-_]+)', '[REDACTED_API_KEY]', text)
    text = re.sub(r'\b[A-Z]{2,5}\d{2,}[A-Z]*\d*\b', '[REDACTED_ID]', text)
    return text
