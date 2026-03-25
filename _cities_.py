# Write code below 💖
class city():
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

london = city('London', 'UK', 1000, ["London Bridge", "Suya spot"])
leeds = city('Leeds', 'UK', 800, ["London waters", "Suya niger"])

print(vars(london))
print(vars(leeds))