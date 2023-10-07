from .models import Category

def menu_links(reques):
    links = Category.objects.all()
    return dict(links=links)