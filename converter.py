import os
import pathlib

from PIL import Image

"""
path_file = 'C:/Users/ismas/OneDrive/Documentos/ismael/SBTech_docs'
image_name = ['imagem.jpg', 'image1.jpg', 'imagem2.jpg']
pdf_name = 'nome'

print(pdf_name[-4:])
print('.pdf' == pdf_name[-4:])

pdf_name = pdf_name + '.pdf'
print(pdf_name)

path_file = path_file.replace("/", "\\")
print(repr(path_file))
"""


def converter_images(dir_path, images_name, pdf_name):

    dir_path = dir_path[2:]
    file_ext = pdf_name[-3:]

    if not 'pdf' == file_ext:
        pdf_name = pdf_name + '.pdf'

    file = pathlib.Path(dir_path + '\\' + pdf_name)

    if not file.exists():

        dir_path = dir_path.replace("/", "\\")

        image_list = []
        for i, image in enumerate(images_name):

            img = Image.open(
                dir_path + '\\' + images_name[i])

            image = img.convert('RGB')
            image_list.append(image)

        first_image = image_list[0]

        first_image.save(dir_path + '\\' + pdf_name,
                         save_all=True, append_images=image_list)
