# **Unique Beauty**

![Main image]()

Unique Beauty Website is an imaginary website designed for selling cosmetics. I have worked on it as a student of [Code Institute](https://codeinstitute.net/) for my fifth portofolio project. This webpage is created using [Code Institute Full Template](https://github.com/Code-Institute-Org/ci-full-template).

[View the live project here!]()

[View the Github repository]()

# **Table of Contents**


- [**Unique Beauty**](#unique-beauty)
- [Project Goals](#project-goals)
- [User Stories](#user-stories)\
- [Features](#features)
- [Navbar](#navbar)
- [Home](#home)
- [Menu](#menu)
- [Gallery](#gallery)
- [Footer](#footer)
- [Booking](#booking)
- [Managebooking](#managebooking)
- [Messages](#messages)
- [Frameworks, Libraries \& Tools](#frameworks-libraries--tools)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Github Deployment](#github-deployment)
  - [Deploying with heroku](#deploying-with-heroku)
- [Languages](#languages)
- [Code](#code)
- [Text](#text)
- [Media](#media)
- [Acknowledgements](#acknowledgements)

## Unique Beauty
    
    Unique Beauty is an online shopping app that is created for cosmetics. Some people do not have enough time for shopping. This is the best way to save time and buy and order beauty products such as lipstick, suncream, eyeshadow... from anywhere and anytime.

## Project Goals

    The main purpose is to create an eccommerce application for Unique Beauty to sell their products using it.
    When the shopper opens this website can easily click on the SHOP NOW button to view the products or search for a spcific product that they are looking for.

## User Stories

  - ### Administrator
    - As a website admin, I can log in to admin panel using the super user.
    - As a website admin, I can view the products and categories so that I can make changes to them.
    - As an Admin, I want each product to have the Shop Now and View buttons so that they can be added to the bag or the product detail is viewed.

  - ### First Time User
    - As a first time user, I want to view the website homepage and find information about Unique Beauty.
    - As a first time user, I want to see different categories of products to see what kind of products are available.
    - As a first time user, I want to see a search input field to find easily something that I am looking for.
    - As a first time user, I want to see a button that can be clicked to see all the products.
    - As a first time user, I want to see product name, image and price.
    - As a first time user, I want to be able to select the quantity of an item that I want to buy.
    - As a first time user, I want to see all the details and informations of a specific product by clicking on it.
    - As a first time user, I want the website to have a navbar with the links of different pages and categories so that I can navigate between the pages easily.
    - As a first time user, I want to the webpage to have the signup form so that I can register for an account.
    - As a site user, I want to receive a confirmation email after registering so that I can verify that my account registration was successful.
  
- ### Frequent User
  - As a returning user, I want to be able to login using my username and password to see my account information.
  - As a returning user, I want to have a personalized user profile so that I can view my personal order history and order confirmations, and save my payment information.
  - As a site user, I want to easily log in or log out so that I can easily access my personal account information..
  - As a shopper, I want to have a shopping bag to add the products to it so I can see all the products and the total price I want to buy.
  - As a shopper, when I view a product I want to see the add to bag button so that I can click on it and add the product to the bag.
  - As a shopper, I want the site to havve the input field for the quantity of a product to specify how many of it I want to buy.
  - As a shopper, I want each product to have the Shop Now and View buttons so that they can be added to the bag or the product detail is viewed.

## Frameworks, Libraries & Tools

- [**Heroku**](https://dashboard.heroku.com/apps) is used for deploying this project
- [**Github**](https://github.com/) is used to store the project.
- [**Codeanywhere**](https://codeanywhere.com/) is used as a development environment.
- [**Django**](https://docs.djangoproject.com/) that is a python framework.
- [**Cloudinary**](https://cloudinary.com/)is used for media and static files.
- [**Database-URL**](https://pypi.org/project/dj-database-url/0.5.0/)is used to represent database settings
- [**Gunicorn**](https://pypi.org/project/gunicorn/20.1.0/) is used to run Django on heroku.
- [**Psycopg2**](https://pypi.org/project/psycopg2/2.9.3/) to connect Postgre SQL
- [**Bootstrap**](https://getbootstrap.com/) used for the frontend
- [**allauth**](https://docs.allauth.org/en/latest/release-notes/recent.html)
- [**Am I responsive**](https://ui.dev/amiresponsive) is used to check if the website is responsive to different devices.
- [**Github issues & Kennan Board**](https://github.com/users/Saleha-m14/projects/3/views/1) is used to track the progress of the project.

## Testing

- ### Bugs
  - #### Fixed Bugs


- #### Remaining Bugs

  There is not any known bugs in my project.

- ### Testing User Stories

- ### First Time User
      
- ### Frequent User

- ### Returning User

## Deployment

### Github Deployment

    -  Login to your github account and navigate to your repositories and click on New.
    -  Select a template(the Code Institute full template is used for this project).[Code-Institute-Org/python-essentials-template](https://github.com/Code-Institute-Org/p3-template)
    -  Write a name for your repository
    -  Select public
    -  Click on create to create your repository.
    -  Copy the link of your repository
    -  log in to your cloudinary using github
    -  click on crete new workspace and paste the github url.
    -  Run the commands first "git add .", then "git commit -m "commit message" and finally "git push" to push the files to github.

### Deploying with heroku

This project is deployed using [Heroku](https://id.heroku.com/) and following the instruction of deployment video of Course Institue. These are the deployment steps:

    1. Open Heroku and click on "Create New App".
    2. Write your app name and select region. You should give your app a unique name.
    3. On the new page click on "settings" and select Config Var and add the below keys:
        -  key: PORT & value 8000
        -  Add key: DATABASE_URL, this should have been created automatically by Heroku.
        -  Add key: CLOUDINARY_URL and the value as your cloudinary API Environment variable e.g.
        -  Add key: SECRET_KEY and the value as a complex string which will be used to provide    cryptographic signing.

    4. Click on "Deploy" tab.
    5. Select "Github" as deployment method.
    6. Search for your repository name and click connect.
    7. Make sure that "main" branch is selected and click on "Enable Automatic Deploys" then, click on "Deploy Branch".
    8.  When your project is deployed you can open it simply by clicking "View".

## Languages

    -  Python
    -  JavaScript
    -  HTML5
    -  CSS3

## Code

    - [Django Documenation](https://docs.djangoproject.com/en/4.2/) was used to provide examples of code solutions and Django functionality.
    - [Bootstrap Documenation](https://getbootstrap.com/docs/4.1/getting-started/introduction/) was used to provide examples of Bootstrap functionality and building blocks.
    - Code Institute walkthrough as inspiration and code examples, the code institute walkthrough "Boutique Ado" is used.The overall idea of this project is comming from "Boutique Ado" project.

## Text

   The texts are written by author.

## Media

    The images comes from [Pixels](https://www.pexels.com/)

## Acknowledgements

    I am thankful of tutor support team at Code Institute for their help and guidance with issues that I faced during working on this project.
    My Code Institute Mentor for feedback and suggestions.
