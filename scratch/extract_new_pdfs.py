import pypdf
import sys

def extract_text(pdf_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for i in range(len(reader.pages)):
            text += f"--- Page {i+1} ---\n"
            text += reader.pages[i].extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error reading {pdf_path}: {e}"

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding='utf-8')
    print("### BAOCAO.PDF ###")
    print(extract_text("k:\\CTU\\THLT\\DoAnNhom\\Me\\Baocao\\BaoCao.pdf"))
    print("\n\n### RPG_DEMO.PDF ###")
    print(extract_text("k:\\CTU\\THLT\\DoAnNhom\\Me\\Baocao\\RPG_demo.pdf"))
