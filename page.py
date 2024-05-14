import streamlit as st
# from reader import read_image
from reader import Image
from design import PageDetails

# st.title("Онлайн зчитувач тексту із зображення")
# st.write("### Підтримувані типи файлів:")
# st.markdown("- JPG")
# st.markdown("- PNG")
# st.markdown("- TIFF")

# st.write("### Підтримувані мови:")
# st.markdown("- українська")
# st.markdown("- англійська")
# st.write("")

page = PageDetails(["- JPG", "- PNG", "- TIFF"], ["- українська", "- англійська"])
page.show_details()


upload_file = st.file_uploader("Оберіть файл зображення")

uploaded_file = Image(upload_file)
uploaded_file.try_read_image()
