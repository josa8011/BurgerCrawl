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

        return restaurants

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
	
