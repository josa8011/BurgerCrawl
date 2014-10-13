# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
    burgerCrawler = BurgerCrawler()

    matches = burgerCrawler.getMatches()
    restaurants = burgerCrawler.getRestaurants()
    
    return dict(
                matches=matches,
                restaurants=restaurants)

def add():
	burgerCrawler = BurgerCrawler()

	url = request.vars.url if request.vars.url != 'None' else None
	restaurant = request.vars.namn if request.vars.namn != 'None' else None

	if restaurant is not None and url is not None:
		burgerCrawler.addRestaurant(url, restaurant)

	redirect(request.env.http_referer)
	return dict()

def error():
    return dict()

