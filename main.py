import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = 0
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()
    def save(e):
        my_file = open("Save", "a+")
        my_file.write(txt_number.value)
        my_file.close()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.CLEAR, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADS_CLICK, on_click=plus_click),
                ft.IconButton(ft.icons.SAVE, on_click=save),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)