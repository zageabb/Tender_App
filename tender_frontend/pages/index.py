import reflex as rx

class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Reflex Tendering Assistant"),
        rx.text("Welcome to the Reflex Tendering Assistant App"),
    )

app = rx.App()
app.add_page(index)
app.compile()
