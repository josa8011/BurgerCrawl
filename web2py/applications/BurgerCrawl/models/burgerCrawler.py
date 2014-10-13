import urllib

class BurgerCrawler(object):
	
	def _matchSite(self, url, word):
		try:
			f = urllib.urlopen(url)
		except:
			return None

		for line in f:
			if word in line.lower():
				return line

	def getRestaurants(self):
		restaurants = list()
		with open("sites.txt", "r") as sites:
			for line in sites:
				if len(line.strip()) > 0:
					url, restaurant = line.strip().split(" ", 1)
					restaurants.append((url.strip(), restaurant.strip()))

		return restaurants

	def getMatches(self):
		matches = list()
		with open("matches.txt", "r") as mFile:
			for line in mFile:
				url, restaurant = line.strip().split(" ", 1)

				match = (url.strip(), restaurant.strip())

				matches.append(match)

		return matches

	def addRestaurant(self, url, restaurant):
		with open("sites.txt", "a") as sites:
			sites.write(url + " " + restaurant + "\n")
		
	def crawl(self, word):
		matches = list()
		with open("sites.txt", "r") as sites:
			with open("matches.txt", "w") as mFile:
				for line in sites:
					if len(line.strip()) > 0:
						url, restaurant = line.strip().split(" ", 1)
		
						url = url.strip()
						restaurant = restaurant.strip()
	
						l = self._matchSite(url, word)
				
						if l is not None:
							mFile.write(url + " " + restaurant + "\n")
	
