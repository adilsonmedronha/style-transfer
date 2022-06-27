
import streamlit as st
import os
from PIL import Image


import style

st.title('Transferência de Estilo')
prev_path = os.path.abspath(os.path.join(".."))

imgs_to_infer_path = os.path.join(prev_path, "images", "in")
img_file_names = os.listdir(imgs_to_infer_path)
img = st.sidebar.selectbox(
    'Selecione a imagem', img_file_names
)

model_path = os.path.join(prev_path, "models", "coco2017")
model_file_names = os.listdir(model_path)
model_file_names = [file[:-6] for file in model_file_names]
style_name = st.sidebar.selectbox(
    'Selecione o tipo', model_file_names
)

model_path = os.path.join(prev_path, model_path, style_name + ".model")
model = model_path


input_image = os.path.join(imgs_to_infer_path, img)
output_image = os.path.join(prev_path, "images", "out", style_name + "-" + img)

st.write('### Imagem:')
image = Image.open(input_image)
st.image(image, width=400)

clicked = st.button('Estilizar')
if clicked:
    model = style.load_model(model)
    style.stylize(model, input_image, output_image)

    st.write('### Imagem Estilizada:')
    image = Image.open(output_image)
    st.image(image, width=400)
