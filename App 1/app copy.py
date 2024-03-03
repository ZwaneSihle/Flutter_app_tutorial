from flet import *
from pages import pages as pgs
from custom_checkbox import CustomCheckBox


def main(page: Page):

    ## Concept colors ##
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    ## User details placeholder ##
    u_name = 'Sihle'


    ## Main container ##
    container = Container(
        width=500,
        height=780,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[ 
                pgs(page, CustomCheckBox, u_name, BG, FG, PINK )[0], pgs(page, CustomCheckBox, u_name, BG, FG, PINK )[1]
            ]
        )
    )

    ## Pages container (dictionary) ##
    pages = {
        '/':View(
            "/",
            [
                container
            ]
        ),
        '/create_task': View(
            "/create_task",
            [
                pgs(page, CustomCheckBox, u_name, BG, FG, PINK )[-1]
            ]
        )
    }

    ## Routing and Navigation ##
    def route_change(route):
        ## Clear page ##
        page.views.clear()
        ## Append views into the main container ##
        page.views.append(
            pages[page.route]
        )

    page.add(container)

    page.on_route_change = route_change

app(target=main)