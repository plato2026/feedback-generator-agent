"""
parser.py — Student Submission Parser
======================================
Parses uploaded text to extract individual student submissions.
Supports multiple delimiter patterns for flexibility.
"""

import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass


@dataclass
class StudentSubmission:
    """Represents a single parsed student submission."""
    name: str
    text: str
    word_count: int
    char_count: int


# Delimiter patterns ordered from most specific to most general.
# The parser tries each and picks the one with the most matches.
DELIMITER_PATTERNS = [
    (r"^Student:\s*(.+)$",          "Student: [Name]"),
    (r"^Name:\s*(.+)$",             "Name: [Name]"),
    (r"^Submission by:?\s*(.+)$",   "Submission by: [Name]"),
    (r"^---\s*([A-Z][a-z]+ [A-Z].+?)\s*---$", "--- Name ---"),
    (r"^##\s*([A-Z][a-z]+ [A-Z].+)$",          "## Name"),
]


def parse_students(raw_text: str) -> Tuple[List[StudentSubmission], Optional[str], Optional[str]]:
    """
    Parse raw text to extract student submissions.

    Args:
        raw_text: The full text content of the uploaded file.

    Returns:
        Tuple of (list of StudentSubmission, error_message, pattern_used)
        If parsing succeeds, error_message is None.
        If parsing fails, the list is empty and error_message explains why.
    """
    if not raw_text or len(raw_text.strip()) < 20:
        return [], "The uploaded file appears to be empty or too short to contain student submissions.", None

    # Try each delimiter pattern and keep the one with the most matches
    best_matches = []
    best_label = ""

    for pattern, label in DELIMITER_PATTERNS:
        matches = list(re.finditer(pattern, raw_text, re.MULTILINE | re.IGNORECASE))
        if len(matches) > len(best_matches):
            best_matches = matches
            best_label = label

    if not best_matches:
        return [], (
            "**Could not detect student delimiters.**\n\n"
            "Please ensure each student's submission is separated by a clear header line. "
            "The recommended format is:\n\n"
            "```\n"
            "Student: Jane Doe\n"
            "[Jane's complete submission text here...]\n\n"
            "Student: John Smith\n"
            "[John's complete submission text here...]\n"
            "```"
        ), None

    # Extract individual submissions
    students = []
    for i, match in enumerate(best_matches):
        name = match.group(1).strip().rstrip(":-_").strip()
        start_idx = match.end()
        end_idx = best_matches[i + 1].start() if i < len(best_matches) - 1 else len(raw_text)
        body = raw_text[start_idx:end_idx].strip()

        # Validate: name should be reasonable length, body should have content
        if 1 < len(name) < 80 and len(body) > 10:
            words = len(body.split())
            students.append(StudentSubmission(
                name=name,
                text=body,
                word_count=words,
                char_count=len(body),
            ))

    if not students:
        return [], (
            "Delimiters were detected but no valid student submissions could be extracted. "
            "Please check that each student header is followed by submission text."
        ), best_label

    return students, None, best_label


def extract_text_from_docx(file_bytes: bytes) -> str:
    """
    Extract plain text from a .docx file using mammoth.

    Falls back to python-docx if mammoth is unavailable.
    """
    try:
        import mammoth
        result = mammoth.extract_raw_text(mammoth.documents.DocumentConverter(), file_bytes)
        # mammoth's API: use convert_to_raw_text with BytesIO
        import io
        result = mammoth.extract_raw_text(io.BytesIO(file_bytes))
        return result.value
    except Exception:
        pass

    # Fallback: python-docx
    try:
        from docx import Document
        import io
        doc = Document(io.BytesIO(file_bytes))
        return "\n\n".join(para.text for para in doc.paragraphs if para.text.strip())
    except Exception as e:
        raise ValueError(f"Could not read .docx file: {e}")
