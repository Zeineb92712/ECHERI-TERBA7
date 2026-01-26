import pdfplumber
import pytesseract

PDF_PATH = "ai/data/pdfs/Decathlon.pdf"

def extract_text(pdf_path: str) -> str:
    print("[START] PDF LOADER")
    full_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        print(f"[INFO] Number of pages: {len(pdf.pages)}")

        for i, page in enumerate(pdf.pages):
            print(f"[INFO] Processing page {i+1}")

            text = page.extract_text()
            if text:
                full_text += text + "\n"

            for img in page.images:
                try:
                    cropped = page.crop(
                        (
                            max(img["x0"], 0),
                            max(img["top"], 0),
                            min(img["x1"], page.width),
                            min(img["bottom"], page.height),
                        )
                    )
                    image = cropped.to_image().original
                    ocr_text = pytesseract.image_to_string(image)
                    full_text += ocr_text + "\n"
                except Exception as e:
                    print(f"[WARN] OCR skipped: {e}")

    print("[DONE] Extraction finished")
    return full_text


if __name__ == "__main__":
    text = extract_text(PDF_PATH)
    print(f"[RESULT] Total characters: {len(text)}")
