import flet as ft
import controllers.ctrl_route_controller as rotas
import views.view_inicio as vi
import views.view_conta as vc
import views.view_agendamento as va
import views.view_cartao_convenio as vcc


# Ponto de entrada do aplicativo. A execução começa com a chamada dessa função main
def main(page: ft.Page):
    # Criar as instâncias de cada view aqui
    view_inicio = vi.ViewInicio()
    view_conta = vc.ViewConta()
    view_agendamento = va.ViewAgendamento()
    view_cartao_convenio = vcc.ViewCartaoConvenio()

    # Definir a cor básica para gerar outras cores
    page.theme = ft.theme.Theme(color_scheme_seed=ft.colors.TEAL_800)

    # Definindo plataforma android e altura e largura para mobile
    page.platform = ft.PagePlatform.ANDROID
    page.window_width = 720
    page.window_height = 1280

    # Conforme cada view for criada, ela deve ser inserida nessa lista, para ser enviada para a função que
    # controla a navegação entre cada tela (view) do aplicativo.
    lista_de_views = [
        view_inicio.view, view_conta.view, view_agendamento.view, view_cartao_convenio.view
    ]

    # Chamando a função que controlola a navegação entre as telas (views) e passando a lista com todas as views
    # como parâmetro.
    rotas.route_controller(page=page, views=lista_de_views)


ft.app(main, view=ft.AppView.FLET_APP)
