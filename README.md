# **Unique Beauty**

![Main image]()

Unique Beauty Website is an imaginary website designed for selling cosmetics. I have worked on it as a student of [Code Institute](https://codeinstitute.net/) for my fifth portofolio project. This webpage is created using [Code Institute Full Template](https://github.com/Code-Institute-Org/ci-full-template).

[View the live project here!]()

[View the Github repository]()

# **Table of Contents**
- [**Unique Beauty**](#unique-beauty)
- [**Table of Contents**](#table-of-contents)
  - [Unique Beauty](#unique-beauty-1)
  - [Project Goals](#project-goals)
  - [User Stories](#user-stories)
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
  - As a shopper, I want to select the quantity of the product when purchasing it to ensure that I do not select the wrong quantity of the product I want to buy.
  - As a shopper, I want to view the items that I have already added to my shopping bag so that I can identify all the items that I have added and the total cost of them.
  - As a shopper, I want to be able to update the quantity of an item in the bag so that I can have the ability to make changes to the product before checkout.
  - As a shopper, I want to have the ability to remove an item that is added to the shopping bag so that I can remove something that is unintentionally added to the bag before checkout.
  - As a shopper, I want to have the ability to easily enter my payment information so that I can check out the items that are in the shopping bag.
  - As a shopper, I want to feel safe when entering my personal and payment information so that I can provide the needed information to check out an item.


- ### Features

  - #### Navbar

    The navbar is fixed on the top of the page. It contains several links. 
    -  It has a Unique Beauty logo. O the desktop view it is on the left side and is linked to the home page. 
    -  In the middle of the page the search input filed is added to search for products. 
    -  On the right side of the page the account dropdown exists and when it is clicked it opens dropdowns menu according to user authentication. If the user is authentiacated and superuser it opens the product management link, my profile, and logout. If the user is only authenticated and not a superuser the my profile and logout will open otherweise it will open link to register and login forms.
    -  On the right side of the page and next to the account the shopping bag is positioned. It is linked to the shopping_bag.html file that all the bag items are added to it. It also displays the total cost of all the bag items.

  - #### Home Page
  
    The homepage has a background image that is in the center of the page and on the page a short text(If you want to look unique use Unique Beauty products.) is written. On the bottom of the text the shop now button exists that is linked to the products page. Once it is clicked it will open the list of all available products.

  - #### Products Page

    When the shop now button is clicked it will open the list of all available products. 
    -  On the top of the products page the page header with the text of Unique Beauty Products is added.
    - In this page all the products are listed that each product is in a seperate card.
    - The product image is added on the top and the product name is written as the card title. The product rating, price and also the shop now and view buttons are in the card footer.
    - The quantity input is not displayed because it takes too much of the space.
    - If the shoper wants to buy a product can easily click on the shop now button. Since the quantity value is one as default so one item will be added to the bag.
    - If the shopper needs more details of the product can easily click on the view or the product image to open the product details page.

  - #### Product Details Page
  
    - When the user clicks on a product image or view button the product details page will open.
    - The page title is on the top
    - The product details contains all the details of a such as product image, name, price, rating, description, quantity input, keep shopping and add to bug buttons.
    - The user can open the image on a new page by clicking on it.
    - The user can select the number of item to be purchased.
    - The keep shopping button will bring the shopper back to the all products page if the user wantedd to buy more products and the add to bag button will add the product with its quantity to the shopping back.
  
  - #### Shopping Bag
    
    - If any item doesn't exist in the shopping bag a text is inserted that tells you that there is not any product in the bag and a shop now button will be there to take you to the prodcuts page.
    - If item in the shopping bag exists it will display each item details in a single row.
    - Each row will have five columns. In the first column will be the product image and in the second on the product name and sku. In the third column will be product price, the product quantity input will be in the fourth column and in the last column will be the subtotal.
    - In the bottom of the page and on the desktop view on the right corner of the page the total cost of all products, delivery cost, grand total and keep shopping and checkout buttons are added.
  


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
- [*Free Logo Maker Looka**](https://looka.com/editor/163700118) is used to create the Unique Beauty logo
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
  -  Select a template(the Code Institute full template is used for this project).[Code-Institute-Org/     python-essentials-template](https://github.com/Code-Institute-Org/p3-template)
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
