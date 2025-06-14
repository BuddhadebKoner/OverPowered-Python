print("example 1")

class Manager:
    @staticmethod
    def final_review():
        print("Final Review")


class Reviewer(Manager):
    @staticmethod
    def review():
        print("Reviewing...")


class Writer(Reviewer):
    @staticmethod
    def writes():
        print("Writes the code\n")

o = Writer()
o.final_review()
o.review()
o.writes()
