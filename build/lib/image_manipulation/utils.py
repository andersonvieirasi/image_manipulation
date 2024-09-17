# image_manipulation/utils.py

from PIL import Image, ImageFilter

def resize_image(image_path, output_path, size):
    """
    Redimensiona a imagem para o tamanho especificado.

    :param image_path: Caminho para a imagem original.
    :param output_path: Caminho para salvar a imagem redimensionada.
    :param size: Tupla (largura, altura) para o novo tamanho.
    """
    with Image.open(image_path) as img:
        resized_img = img.resize(size)
        resized_img.save(output_path)
        print(f"Imagem redimensionada e salva em {output_path}")

def apply_blur(image_path, output_path, radius=2):
    """
    Aplica um filtro de desfoque na imagem.

    :param image_path: Caminho para a imagem original.
    :param output_path: Caminho para salvar a imagem com o filtro aplicado.
    :param radius: Raio do desfoque.
    """
    with Image.open(image_path) as img:
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius))
        blurred_img.save(output_path)
        print(f"Filtro de desfoque aplicado e imagem salva em {output_path}")
