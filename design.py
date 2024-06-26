import streamlit as st


class PageDetails:
    page_title = "Онлайн зчитувач тексту із зображення"
    file_headline = "### Підтримувані типи файлів:"
    lang_headline = "### Підтримувані мови:"

    def __init__(self, file_types: list, lang_types: list):
        self.file_types = file_types
        self.lang_types = lang_types
    
    @staticmethod
    def points(bullet_points):
        for point in bullet_points:
            st.markdown(point)

    def show_details(self):
        st.title(self.page_title)
        st.write(self.file_headline)
        self.points(self.file_types)
        st.write(self.lang_headline)
        self.points(self.lang_types)
        st.write("")

    