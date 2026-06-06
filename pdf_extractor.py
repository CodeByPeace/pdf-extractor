import pdfplumber
import pandas as pd
import os
pdf_path = 'sample.pdf'
data = []
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            data.append({'Page': i + 1, 'Content': text.strip().replace('\n', ' ')})
df = pd.DataFrame(data)
print(df)
df.to_csv("output.csv", index=False)
print("saved")