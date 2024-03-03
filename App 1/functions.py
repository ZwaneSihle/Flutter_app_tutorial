from flet import *

## Function to shrink the container ##
def shrink(e, page):
    page.controls[0].width= 120
    page.controls[0].scale= transform.Scale(
        0.8, alignment=alignment.center_right
    )
    page.controls[0].border_radius=border_radius.only(
        top_left=35,
        top_right=0,
        bottom_left=35,
        bottom_right=0
    )
    page.update()

## Function to restore the container ##
def restore(e, page):
    page.controls[0].width= 400
    page.controls[0].scale= transform.Scale(
        1, alignment=alignment.center_right
    )
    page.update()