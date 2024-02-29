import flet as ft


class ViewAgendamento:
    def __init__(self):

        self.view = self._get_view()

    def _get_view(self):
        return ft.View(
            route='/agendamento',
            controls=[

            ]
        )
