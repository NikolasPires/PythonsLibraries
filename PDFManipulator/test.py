from pathlib import Path
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

ROOT = Path(__file__).parent
ORIGINALS_PATHWAY = ROOT / 'original_pdf'
NEW_FILE = ROOT / 'new_files'

BACEN_RELATORY =  ORIGINALS_PATHWAY / 'R20230303.pdf'

NEW_FILE.mkdir(exist_ok=True)

reader = PdfReader(BACEN_RELATORY)

page0 = reader.pages[0]
image0 = page0.images[0]

# print(page0.extract_text())
# with open(NEW_FILE / image0.name, 'wb') as fp:
#     fp.write(image0.data)


for i, page in enumerate(reader.pages):
        writer = PdfWriter()       
        with open(NEW_FILE / f'page{i}.pdf', 'wb') as arquivo:
            writer.add_page(page)
            writer.write(arquivo)
