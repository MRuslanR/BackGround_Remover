import gradio as gr
from rembg import remove
from PIL import Image
import numpy as np


def remove_background(input_image):
    # Конвертируем изображение из Gradio в PIL
    image = Image.fromarray(input_image.astype('uint8'), 'RGB')

    # Удаляем фон с помощью U²-Net
    output_image = remove(image)

    # Конвертируем результат обратно в numpy array для Gradio
    return np.array(output_image)


# Создаем интерфейс с примерами изображений для теста
demo = gr.Interface(
    fn=remove_background,
    inputs=gr.Image(label="Загрузите фото"),
    outputs=gr.Image(label="Результат без фона"),
    title="Background Remover",
    description="Загрузите фото → получите PNG без фона!"
)


if __name__ == "__main__":
    demo.launch(share=False)