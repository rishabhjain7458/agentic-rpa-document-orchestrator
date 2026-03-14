import json
import os
import sys

DOCUMENT_KEYWORDS = {

    "invoice": [
        "invoice",
        "invoice number",
        "gst",
        "bill to",
        "amount due",
        "total"
    ],

    "resume": [
        "experience",
        "education",
        "skills",
        "curriculum vitae",
        "linkedin",
        "profile",
        "employment history"
    ],

    "requirements_doc": [
        "requirements",
        "software requirements",
        "functional requirements",
        "system overview",
        "scope",
        "system requirements specification"
    ],

    "purchase_order": [
        "purchase order",
        "po number",
        "vendor",
        "order date",
        "delivery",
        "purchase order number"
    ],

    "contract": [
        "agreement",
        "contract",
        "terms and conditions",
        "party of the first part",
        "effective date",
        "legal agreement"
    ],

    "report": [
        "report",
        "summary",
        "analysis",
        "findings",
        "conclusion",
        "executive summary"
    ],

    "bank_statement": [
        "account number",
        "statement period",
        "opening balance",
        "closing balance",
        "transaction",
        "bank statement"
    ],

    "receipt": [
        "receipt",
        "payment received",
        "transaction id",
        "paid amount",
        "payment method"
    ],

    "cover_letter": [
        "dear hiring manager",
        "cover letter",
        "application for",
        "sincerely",
        "regards"
    ]
}


def classify_document(text: str):

    text_lower = text.lower()
    scores = {}

    for doc_type, keywords in DOCUMENT_KEYWORDS.items():
        score = 0

        for word in keywords:
            if word in text_lower:
                score += 1

        scores[doc_type] = score

    best_type = max(scores, key=scores.get)
    best_score = scores[best_type]

    if best_score == 0:
        return {
            "document_type": "unknown",
            "confidence": 0.0
        }

    confidence = best_score / len(DOCUMENT_KEYWORDS[best_type])

    return {
        "document_type": best_type,
        "confidence": round(confidence, 2)
    }


def main():

    try:

        if len(sys.argv) < 2:
            print("ERROR: No input file provided.")
            return

        input_file = sys.argv[1]

        print("Input file received:", input_file)

        if not os.path.exists(input_file):
            print("ERROR: File does not exist:", input_file)
            return

        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()

        result = classify_document(text)

        output_file = os.path.splitext(input_file)[0] + "_result.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(json.dumps(result, indent=4))

        print("Classification result:", result)
        print("Result written to:", output_file)

    except Exception as e:
        print("ERROR:", str(e))


if __name__ == "__main__":
    main()