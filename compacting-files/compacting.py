import os
from pathlib import Path
import shutil
from zipfile import ZipFile

# Creating the archive to be compacted

PATHWAY = Path(__file__).parent
PATHWAY_CONTENT = PATHWAY / 'content'
CONTENT_ZIPPED = PATHWAY / 'content.zip'
CONTENT_UNZIPPED = PATHWAY / 'content_unzipped'

shutil.rmtree(PATHWAY_CONTENT, ignore_errors=True)
Path.unlink(CONTENT_ZIPPED, missing_ok=True)
shutil.rmtree(str(CONTENT_ZIPPED).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(CONTENT_UNZIPPED, ignore_errors=True)

# raise Exception()

PATHWAY_CONTENT.mkdir(exist_ok=True)

def make_file(qtd: int, zip_dir: Path):
    for i in range(qtd):
        text = 'archive_%s' % i
        with open(zip_dir / f'{text}.txt', 'w') as file:
            file.write(text)

make_file(10, PATHWAY_CONTENT)

# packing the content file
with ZipFile(CONTENT_ZIPPED, 'w') as zip:
    for root, dirs, files in os.walk(PATHWAY_CONTENT):
        for file in files:
            zip.write(os.path.join(root, file), file)

# reading zip file
with ZipFile(CONTENT_ZIPPED, 'r') as zip:
    for archive in zip.namelist():
        print(archive)

# unpacking file
with ZipFile(CONTENT_ZIPPED, 'r') as zip:
    zip.extractall(CONTENT_UNZIPPED)
