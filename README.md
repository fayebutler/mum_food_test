
# Mum Food Test


## Setup

Pull the docker image and run:

`https://cloud.docker.com/repository/docker/fayebutler/mum_food_test`

This will start the django server and the database.
Access at: 

`localhost:8000/admin`

`localhost:8000/api`


## Admin

To login, there is a user set up:

`username: test`

`password: changeme11`



## API

Example of how to achieve the user stories using Httpie

#### User stories
1. As an anonymous user I want to see a list of recipes, ordered by popularity (amount of likes).

`http GET http://localhost:8000/api/recipes/`

2. As an anonymous user I want to be able to see if a recipe is good for vegans. Is understood that a recipe is good for vegans if all the ingredients are compatible for vegan people.

`http GET http://localhost:8000/api/recipes/`

3. As an anonymous user I want to be able to filter the recipes by ingredients and if they are vegan or not.

`http GET http://localhost:8000/api/recipes/ vegan==true ingredients==Basil,Tomato`

4. As an anonymous user I want to be able to like a recipe.

`http POST http://localhost:8000/api/recipes/Marinara\ Pizza/like/`

5. As an anonymous user I can check a recipe to see the ingredients for it.

`http GET http://localhost:8000/api/recipes/Marinara\ Pizza/`

6. As a registered user I want to be able to create a ingredient.

`http POST http://localhost:8000/api/ingredients/ name="Ham" vegan=False Authorization:"Token 839c4f9e7a45411036285d4175a3208dbf4cc7a9"`

7. As a registered user I want to be able to create a recipe.

`http POST http://localhost:8000/api/recipes/ name="Tomato&Mushrooms" ingredients="Mushroom,Tomato" Authorization:"Token 839c4f9e7a45411036285d4175a3208dbf4cc7a9"`

