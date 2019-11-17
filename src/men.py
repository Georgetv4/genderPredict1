class Men:
    def __init__(self, weight, height, gender):
        self.weight = float(weight)
        self.height = float(height)
        self.gender = 1 if gender.lower() == '"male"' else 0

