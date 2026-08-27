import easyocr


class OCREngine:

    def __init__(self):
        print("Loading OCR engine...")

        self.reader = easyocr.Reader(
            ['en'],
            gpu=False
        )

        print("OCR engine ready.")

    def extract_text(self, image_path):

        results = self.reader.readtext(str(image_path))

        extracted_text = []

        for _, text, confidence in results:

            extracted_text.append({
                "text": text,
                "confidence": float(confidence)
            })

        return extracted_text


# if __name__ == "__main__":

#     print("OCR module initialized successfully.")

if __name__ == "__main__":

    engine = OCREngine()

    image_path = input("Enter screenshot path: ").strip()

    results = engine.extract_text(image_path)

    print("\n========== OCR RESULT ==========")

    for item in results:
        print(
            f"Text: {item['text']} | "
            f"Confidence: {item['confidence']:.2f}"
        )

    print("================================")