import flet as ft


def route_controller(page: ft.Page, views: list):
    def route_change(route):
        page.views.clear()
        page.views.append(views[0])

        for v in views:
            if v.route == route:
                page.views.append(v)
                break

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
