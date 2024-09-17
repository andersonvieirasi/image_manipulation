# image_manipulation/main.py

from utils import resize_image, apply_blur

def main():
    # Exemplo de uso das funções
    input_image = 'input_image.jpg'
    resized_image = 'resized_image.jpg'
    blurred_image = 'blurred_image.jpg'
    
    # Redimensionar imagem
    resize_image(input_image, resized_image, (800, 600))
    
    # Aplicar desfoque
    apply_blur(resized_image, blurred_image, radius=5)

if __name__ == "__main__":
    main()