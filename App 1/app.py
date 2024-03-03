from flet import *
from custom_checkbox import CustomCheckBox


def main(page: Page):

    ## Concept colors ##
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    ## User details placeholder ##
    u_name = 'Sihle'

    ## Function to shrink the container ##
    def shrink(e):
        page_2.controls[0].width= 120
        page_2.controls[0].scale= transform.Scale(
            0.8, alignment=alignment.center_right
        )
        page_2.controls[0].border_radius=border_radius.only(
            top_left=35,
            top_right=0,
            bottom_left=35,
            bottom_right=0
        )
        page_2.update()

    ## Function to restore the container ##
    def restore(e):
        page_2.controls[0].width= 400
        page_2.controls[0].scale= transform.Scale(
            1, alignment=alignment.center_right
        )
        page_2.update()

    
    ## Create task view ##
    ctv = Container(
        content=Container(
            on_click=lambda _: page.go('/'),
            height=40, width=40,
            content=Text('x')
        )
    )

    ## Task list ##
    tasks = Column(
        height=300,
        scroll='auto',
        controls=[]
    )

    ## Append tasks ##
    for i in range(10):
        tasks.controls.append(
            Container(
                height=50,
                width=400,
                bgcolor=BG,
                border_radius=15,
                animate=animation.Animation(600,AnimationCurve.DECELERATE),
                animate_scale=animation.Animation(400,AnimationCurve.DECELERATE),
                padding=padding.only(
                    left=15, top=13
                ),
                content=CustomCheckBox(PINK,
                    font_size=14,
                    label='Get to the money all day.')
                )
        )

    ## Catergories widget ##
    ## Create empty Row, and append 'dump/placeholder' content to the widget ##
    categories_card = Row(
        scroll='auto'
    )

    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categories_card.controls.append(
            Container(
                border_radius=20,
                bgcolor=BG,
                width=170,
                height=110,
                padding=15,
                content=Column(
                    controls=[
                        Text('40 Tasks', color='#FFFFFF'),
                        Text(category, color='#FFFFFF'),
                        Container(
                            width=160,
                            height=5,
                            bgcolor='white12',
                            border_radius=20,
                            padding=padding.only(right=i*30),
                            content=Container(
                                bgcolor=PINK,
                            )
                        )
                    ]
                )
            )
        )

    ## Content/Widgets ##
    first_page_content = Container(
        content=Column(
            controls=[
                Row( alignment='spaceBetween',
                    controls=[
                        Container(on_click=lambda e: shrink(e),
                            content=Icon(
                                icons.MENU, color='#FFFFFF'
                            )
                        ),
                        Row(
                            controls=[
                                Icon(icons.SEARCH, color='#FFFFFF'),
                                Icon(icons.NOTIFICATIONS_OUTLINED, color='#FFFFFF')
                            ]
                        )
                    ]
                ),
                Text(
                    value= f'\nWhat\'s up, {u_name}!', color='#FFFFFF', size=28
                ),
                Text(
                    value='CATEGORIES', color='#FFFFF3'
                ),
                Container(
                    padding=padding.only( top=10, bottom=20),
                    content=categories_card
                ),
                Container(height=20),
                Text("TODAY'S TASKS"),
                Stack(
                    controls=[
                        tasks,
                        FloatingActionButton( bottom=0, right=5,
                            icon= icons.ADD,
                            on_click=lambda _: page.go('/create_task')
                        )
                    ]
                )
            ]
        )
    )

    ## Pages ##
    page_1 = Container(
        width=400,
        height=850,
        bgcolor=BG,
        border_radius=35,
        padding=padding.only(left=50, top=60, right=200),
        content=Column(
            controls=[
                Row(alignment='end' ,
                    controls=[
                        Container(
                            border_radius=25, padding=padding.only(top=13,left=18),
                            height=50, width=50, border=border.all(color='white', width=1),
                            on_click=lambda e: restore(e),
                            content=Text('<')
                        )
                    ]
                ),
                Container(height=20),
                Text(f'{u_name}', size=32, weight='bold'),
                Text(f'The only ninja with a vission'),
                Container(height=20),
                Row(controls=[
                    Icon(icons.FAVORITE_BORDER_SHARP, color='white'),
                    Text('Templates')
                ]
                ),
                Row(controls=[
                    Icon(icons.CARD_TRAVEL_OUTLINED, color='white'),
                    Text('Templates')
                ]
                ),
                Row(controls=[
                    Icon(icons.CALCULATE_OUTLINED, color='white'),
                    Text('Templates')
                ]
                )
            ]
        )
    )

    page_2 = Row(alignment='end',
        controls=[
            Container(
                width=400,
                height=850,
                bgcolor=FG,
                border_radius=35,
                padding=padding.only(
                    top=50, left=20,
                    right=20, bottom=5
                ),
                content=Column(
                    controls=[
                        first_page_content
                    ]
                )
            )
        ]
    )

    ## Main container ##
    container = Container(
        width=500,
        height=780,
        bgcolor=BG,
        border_radius=35,
        content=Stack(
            controls=[
                page_1,
                page_2
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
                ctv
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