import re
import streamlit as st

def redact_sensitive_info(text):
    # If user turned off redaction, return original
    if not st.session_state.get("enable_redaction", True):
        return text

    # Redact email addresses
    text = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', '[REDACTED_EMAIL]', text)

    # Redact Indian phone numbers (10 digits, with or without country code)
    text = re.sub(r'\b(\+91[-\s]?)?\d{10}\b', '[REDACTED_PHONE]', text)

    # Redact Aadhaar numbers (format: 1234 5678 9123 or 123456789123)
    text = re.sub(r'\b\d{4}\s?\d{4}\s?\d{4}\b', '[REDACTED_AADHAAR]', text)

    # Redact PAN numbers (format: ABCDE1234F)
    text = re.sub(r'\b[A-Z]{5}[0-9]{4}[A-Z]\b', '[REDACTED_PAN]', text)

    # Redact Government ID formats (e.g., DL-0420211234567, Passport, etc.)
    text = re.sub(r'\b[A-Z]{2}-\d{2,}[A-Z0-9]*\b', '[REDACTED_GOV_ID]', text)

    # Redact College/Student IDs (simple alphanumeric patterns like ENG22CS0038)
    text = re.sub(r'\b[A-Z]{2,}\d{2,}[A-Z]{0,}\d{0,}\b', '[REDACTED_STUDENT_ID]', text)

    # Redact numeric Student Application Numbers (e.g., 8–12 digit numbers)
    text = re.sub(r'\b\d{8,12}\b', '[REDACTED_APPLICATION_ID]', text)

    # Redact generic account or reference numbers (long numeric sequences)
    text = re.sub(r'\b\d{9,}\b', '[REDACTED_NUMBER]', text)

    # Redact dates of birth (various formats)
    text = re.sub(r'\b(?:\d{1,2}[-/\s])?(?:\d{1,2}[-/\s])?\d{2,4}\b', '[REDACTED_DOB]', text)

    # Redact names with patterns like Mr./Ms./Dr. followed by capitalized name
    text = re.sub(r'\b(?:Mr|Ms|Mrs|Dr|Prof)\.\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', '[REDACTED_NAME]', text)

    return text