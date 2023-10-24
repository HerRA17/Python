from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

engine = create_engine("mysql://cf-python:Hermannr17@localhost/my_database")
Base = declarative_base()

class Recipe(Base):
    __tablename__ = "practice_recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
            return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

tea = Recipe(
        name = "Tea",
        cooking_time = 5,
        ingredients = "Tea Leaves, Water, Sugar"
)
session.add(tea)

coffee = Recipe(
      name = "Coffee",
      cooking_time = 5,
      ingredients = "Coffee Powder, Sugar, Water"
) 

session.add(coffee)

cake = Recipe(
      name = "Cake",
      cooking_time = 50,
      ingredients = "Sugar, Butter, Eggs, Vanilla Essence, Flour, Baking Powder, Milk"      
)

session.add(cake)

banana_smoothie = Recipe(
      name = "Banana Smoothie",
      cooking_time = 5,
      ingredients = "Bananas, Milk, Peanut Butter, Sugar, Ice Cubes"      
)

session.add(banana_smoothie)
session.commit()