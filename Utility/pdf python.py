import pdfplumber
import re

INPUT_PDF = "input.pdf"
OUTPUT_RTF = "output.rtf"

def clean_text(text):
text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
text = re.sub(r'[ \t]+', ' ', text)
text = re.sub(r'\n{2,}', '\n\n', text)
return text.strip()

def rtf_escape(text):
return text.replace('\\', r'\\').replace('{', r'\{').replace('}', r'\}')

content = []

with pdfplumber.open(INPUT_PDF) as pdf:
for page in pdf.pages:
t = page.extract_text()
if t:
content.append(t)

cleaned = clean_text("\n\n".join(content))

rtf_body = rtf_escape(cleaned).replace("\n\n", r"\par\par ")

rtf = r"""{\rtf1\ansi\deff0
{\fonttbl{\f0 Times New Roman;}}
\f0\fs24
""" + rtf_body + "\n}"

with open(OUTPUT_RTF, "w", encoding="utf-8") as f:
f.write(rtf)

print("Saved:", OUTPUT_RTF)