import urllib

class BurgerCrawler(object):
	
	def _matchSite(self, url, word):
		f = urllib.urlopen(url)
		for line in f:
			if word in line.lower():
				return line

	def getRestaurants(self):
		restaurants = list()
		with open("sites.txt", "r") as sites:
			for line in sites:
				if line.strip().len() > 0:
					url, restaurant = line.split(" ")
					restaurants.append((url.strip(), restaurant.strip()))

	def addRestaurant(self, url, restaurant):
		with open("sites.txt", "a") as sites:
			sites.writeline(url + " " + restaurant)
		
	def crawl(self, word):
		matches = list()
		with open("sites.txt", "r") as sites:
			for line in sites:
				if line.strip().len() > 0:
					url, restaurant = line.split(" ")
	
					url = url.strip()
					restaurant = restaurant.strip()

					l = self._matchSite(url, word)
			
					if l is not None:
						match = "Match at %s - %s" % (restaurant, url)
						matches.append(match)

		return matches

#			 SITES = [("http://hamnpaviljongen.com/lunchmeny/", "Hamnpaviljongen"),
#					  ("http://www.kadbano.se/index.php/lunch", "Kadbano"),
#					  ("http://www.rmagnussons.se/index.php/lunch", "Magnussons"),
#					  ("http://www.villaromana.se/index.php/se/lunchmeny", "Villa Romana"),
#					  ("http://www.kvartersmenyn.se/start/rest/13682", "Sherlocks"),
#					  ("http://www.xn--vrdshusetliljan-0kb.se/index.php/lunch", "Värdshuset Liljan"),
#					  ("http://www.kvartersmenyn.se/start/rest/10511", "Börjes"),
#					  ("http://fagelsangen.kvartersmenyn.se/", "Fågelsången"),
#					  ("http://borgenuppsala.se/dagens-lunch-i-uppsala/", "Borgen"),
#					  ("http://domtrappkallaren.se/dagens-lunch-i-uppsala/", "Domtrappkällaren"),
#					  ("http://www.unt.se/Page.aspx?url=lunchguiden%2f&ShowInfo=1&RestID=1947851", "Lucillus"),
#					  ("http://www.unt.se/Page.aspx?url=lunchguiden%2f&ShowInfo=1&RestID=1947819", "Picnic"),
#					  ("http://www.unt.se/Page.aspx?url=lunchguiden%2f&ShowInfo=1&RestID=1947650", "Stationen"),
#					  ("http://www.ukk.se/Restaurang-cafe/Veckans-luncher/", "UKK"),
#					  ("http://www.unt.se/Page.aspx?url=lunchguiden%2f&ShowInfo=1&RestID=1947780", "Åkanten")]
	
