languages = set()

languages = {"english", "mandarin", "spanish", "english", "spanish", "portugese"}
print(languages)


showroom = set()

showroom = {"jeep-wrangler", "jeep-cherokee", "jeep-waggoneer", "jeep-honcho"}
print(showroom)
print(len(showroom))

showroom.add("jeep-honcho")
print(showroom)

new_cars = set()
new_cars = {"corvett", "camaro"}

showroom.update(new_cars)
print(showroom)

showroom.discard('camaro')
print(showroom)

junkyard = set()
junkyard = {"jeep-wrangler", "jeep-cherokee", "stinger", "model-T", "BMW"}
print(junkyard)

newjunk = showroom.intersection(junkyard)
print(newjunk)

junkyard.discard("jeep-wrangler")
junkyard.discard("jeep-cherokee")
print(junkyard)