from PIL import Image
from PIL.ExifTags import TAGS
import pandas as pd

def get_exif_data(image_path):
    with Image.open(image_path) as img:
        exif_data = img._getexif()
        if exif_data:
            exif = {
                TAGS.get(tag, tag): value
                for tag, value in exif_data.items()
                if TAGS.get(tag, tag) != "MakerNote"
            }
            return exif
        else:
            return None

image_path = "caminho_da_imagem.jpg"
exif = get_exif_data(image_path)
if exif:
    df = pd.DataFrame.from_dict(exif, orient="index")
    writer = pd.ExcelWriter("dados_exif.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Dados EXIF")
    writer.save()
