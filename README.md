# Essence

# Project Overview
Essence is your go-to destination for top-quality self-care essentials. From women’s care and hair care to baby-care, skin care, and men’s care products, Essence has got you covered. The site’s mission is to simplify your self-care routine by offering a curated selection of products tailored to your needs. Whether you’re a woman, a parent, or a man focused on grooming, find what you need for a healthier, more confident lifestyle on Essence. Shop on the site for a convenient, reliable, and satisfying self-care experience. 

# Table Content
1. [Project Overview](#project-overview)
2. [UX & Website Design](#UX-&-website-design)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits)

# UX & Website Design

## Strategy

### User Stories

1.	As a first-time user, I want to:
- Understand the main purpose of the website immediately.
- Easily navigate through the pages.
- Effortlessly search for products available.
- Purchase for products without creating an account.
- View the reviews submitted by other users.
- Access the pages on any devices or screen sizes. 
- Have the option to login or create a user account.
- Contact the company regarding any questions I may have.

2.	As a registered user, I want to:
- Access my account information/profile page.
- View my order history.
- View my product reviews.
- View my wish list.
- Have the option to opt-in and opt-out of newsletter subscription. 
- Update and save my personal information.
- Make purchases with my delivery information pre-filled. 
- Leave reviews for products.

3.	As an admin, I want to:
- Easily create, read, update, and delete products.
- Manage customer reviews efficiently.
- Delete any inappropriate customer reviews.
- Ensure efficient access and security measures for admin controls and functions.

## Structure
The website is set up with different pages, and each page is made for a specific type of user. The flow diagram below shows how these pages are organized and gives details about what you can find on each of them. This was created using [Lucidchart](https://lucid.co/)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/02b5919b-9c5d-4a17-a37c-5a6493320dce)

## Skeleton

1. Database Schema
- I created a clear and organized layout for the database in order to make building the website easier for me.
- I used [DrawSQL](https://drawsql.app/) to draw the database which uses a database called Postgres.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/c548cd5d-9028-43f1-87a5-c6d3462c95ce)


2. Wireframes: the wireframes were created using Balsamiq.


## Surface

### Colour & Typography
- I used [Logo](https://logo.com/) for the website logo and font.
- Typography: Alex Brush Regular
- The colours used are: Hex #101010 (Primary), Hex #000000 (Secondary), Hex #cc9966 (Accent), and Hex #fdfefe (Background).

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/f9aa1e3b-de6f-4bee-9fa7-76fa643703ad)
  
![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/7f9d154b-cf95-4bff-9528-fcdd6ef7b78e)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/a14e38c8-a5ed-4d00-8570-fc05de2c8e19)


### Images and Icons

# Features

## Existing Features

### Home Page


### Products Page


### Shopping Cart Page


### Checkout Page


### Account Information/Profile Page


### Contact Form Page


### Register Page


### Login Page


### Forgot Password Page


### Error Page


## Authentication


## Future Features

- **Live Chat Functionality:** in my upcoming developments, I’d like to introduce a live chat feature that will allow users to receive immediate assistance while navigating our website, ensuring a smoother shopping experience.

- **Create an order tracking system:** I’d also like to craft an order tracking system that empowers customers to effortlessly track the real-time status and location of their orders, providing transparency and peace of mind.

- **Discount vouchers capability:** I’d also like my platform to boast the capability to apply discount vouchers during checkout, giving our users the advantage of unlocking potential savings on their purchases.

- **Ability to add reviews exclusively for purchased products:** I’d also like to work on a feature that allows customers to share their experiences by adding reviews exclusively for products that they’ve purchased, fostering a more genuine and reliable feedback system.

# Technology Used 

## Language


## Tools

# Testing


# Deployment
This project was developed using **Visual Studio Code** as the IDE, **GitHub** as the remote repository, **AWS** to store static and media files, and **Heroku** as the deployment site.

**Set Up AWS to Store Static & Media Files**
- Create an account on [AWS](https://aws.amazon.com/).
- Login and go to All Services > Storage > S3
- Create a new bucket by clicking the orange ‘Create Bucket’ button on the S3 page.
- Name the bucket and choose the nearest region.
- Under ‘Object Ownership’, select ‘ACLs enabled’, keeping Object Ownership as ‘Bucket owner preferred’.
- Uncheck ‘Block all public assess’, acknowledge the warning to make the bucket public, and click ‘create bucket’.
- Click the created bucket’s name, go to the properties tab, and under ‘Static website hosting’, click ‘edit’.
- Enable Static website hosting, copy default index and error document values, and click ‘save changes’.
- Go to the permissions tab, find the Cross-origin resource sharing (CORS) section, click edit, and paste in the following code:

[
    {
        "AllowedHeaders": [
        "Authorization"
        ],
        "AllowedMethods": [
        "GET"
        ],
        "AllowedOrigins": [
        "*"
        ],
        "ExposeHeaders": []
    }
]

- Go to the ‘Bucket Policy’ section, click ‘edit’, and then choose ‘Policy generator’ to open the AWS policy generator page.
- In the ‘Select type of policy’ dropdown, pick ‘S3 Bucket Policy’, and in the ‘Principle’, allow all by typing ‘*’.
- Choose ‘Get object’ from the ‘Actions’ dropdown.
- Go back to the previous tab, find the Bucket ARN number and copy it.
- Return to the policy generator, paste the ARN in the ‘Amazon Resource Name (ARN)’ field, click ‘Add statement’, then ‘Generate Policy’.
- Copy the generated policy and paste it into the bucket policy editor.
- Before saving, add ‘/*’ at the end of your resource key to allow access to all resources in the bucket.
- Save the changes and scroll down to the ‘Access control list (ACL)’ section, then click ‘edit’.
- Check the ‘list’ checkbox next to ‘Everyone (public access)’, acknowledge the warning, and click ‘save’.

**IAM**
- Open the window and search for IAM, then select it.
- On the IAM page, go to the sidebar and click ‘User Groups’ followed by ‘Create group’.
- Name the group ‘manage-your-project-name’ and click ‘Create group’.
- From the sidebar, click ‘Policies’, then ‘Create policy’.
- Go to the JSON tab, click ‘import policy’, search for ‘S3’, and select ‘AmazonS3FullAccess’. Click import.
- After importing, update the Resource key in the policy by copying your bucket’s ARN. Add two lines with your ARN and your ARN followed by a ‘/*’.

Example:

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "YOUR-ARN-NO-HERE",
                "YOUR-ARN-NO-HERE/*"
            ]
        }
    ]
}

-  Click ‘Next’ > Tags, ‘Next’ > ‘Review’.
- Provide a name and description, then click on ‘Create policy’.
- Return to the policy page, find your newly created policy, and attach it to the group.
    - Click ‘User groups’, select your group, go to the permissions tab, click ‘Add permission’, and choose ‘Attach policies’.
    - Find and select the policy, then click ‘Add permissions’.
- Create a user by selecting ‘Users’ from the sidebar, clicking ‘Add user’, giving a username, checking ‘Programmatic Access’, and clicking ‘Next’ > Permissions.
- Select the group with the attached policy, click ‘Next’ > Tags, ‘Next’ > ‘Review’, and ‘Create user’.
- On the next page, download the CSV file containing the user’s access key and secret access key for future use.

**Heroku**
- Go to the Heroku website.
- Register or login.
- Click on the 'New' button and 'Create New App'.
- Name your app and select your region.
- Go to the 'Settings' and click on 'Reveal Config Vars' then add the following keys and their respective values:

| Key                    | Value                                               |
|------------------------|-----------------------------------------------------|
| AWS_ACCESS_KEY_ID      | your AWS bucket ID                                  |
| AWS_SECRET_ACCESS_KEY  | your AWS secret key                                 |
| DATABASE_URL           | add ElephantSQL database URL here                   |
| SECRET_KEY             | used for the Django project                         |
| USE_AWS                | True                                                |
| STRIPE_SECRET_KEY      | Stripe account                                      |
| STRIPE_PUBLIC_KEY      | from Stripe account                                 |
| STRIPE_WH_SECRET       | from Stripe account                                 |



# Credits


## Content
- Bootstrap template was used for the front-end development and customised.
- Boutique Ado Walkthrough from [Code Institute](https://codeinstitute.net/) was used as an inspiration. It allowed me to have an idea of how to go about my website. It was very helpful and made it less stressful.
- [Django Documentation](https://www.djangoproject.com/) was used for examples of code solutions and Django functionality.

## Media
- [Logo](https://logo.com/) was used for the website's logo.
- [Unsplash](https://unsplash.com/) was used for some of the images used on the website.
- [Freepik](https://www.freepik.com/) was used for some of the images used on the website.
- [Google](https://www.google.com/): some images were also taken from Google.
- [Boots](https://www.boots.ie/) was used for some of the product images  used on the website. The details of the products were also taken from this website.
- [Lucidchart](https://lucid.co/) was used to create the structure of the website.
- [DrawSQL](https://drawsql.app/) was used to create the database schema of the website.
- Slack: watched videos and notes of plans and guides on how to start and complete the project.
- Code Institute README template was used as an inspiration for my README.md file. 
- Bootstrap was used as a template for the front-end development of the website.
- [Bootstrap](https://getbootstrap.com/): this documentation was used for examples of Bootstrap functionality.

## Acknowledgements
- Slack Community for the helpful materials.
- Code Institute for their helpful materials.
- My mentor Antonio Rodriguez for his advice and support.
