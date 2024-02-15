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

### Header Page

*Navigation Bar*

- The navigation bar is visible at the top of every page along with links to other pages.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/e6913daf-001f-4685-909f-5264ad16a14c)

*Logo*

- The logo was created using the website [Logo](https://logo.com/).
- The logo is placed on the top left side of the navigation bar.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/7f4fbd54-ce63-4145-b0f6-3c76f2076ac3)

*Search Bar*

- The search bar icon is included in the navigation bar. When a user clicks on the icon, the search bar will open.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/47de5769-48e8-4397-adfa-da276bda1983)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/8361ef98-05f3-4f0e-8319-04cad24c1e9c)

*Other Features*

- Other icons present are the shopping cart, heart icon (acts as the wishlist icon which if clicked will take the user to their wishlist page), profile icon, number and phone icon present, and 'Login' (if user is not logged in), or 'Logout' (if user is logged in).
- Cart Icon: if user clicks on the icon, it will show them what is in their shopping cart (includes name, price, quantity, and image of the products they added. It also includes the 'Total' amount of the products added along with a 'View Cart' (takes user to shopping cart page) and 'Checkout' (takes user to checkout page) button.
- Profile Icon: if user is logged in then if they click on the icon, they will see the following options; 'Profile' (will take them to their profile page) and 'Logout' (will log them out of their account. If user is not logged in, they will see an option to 'Login'

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/6c7ff870-9a1a-417b-b8d0-157e49135b42)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/14104249-fadf-47c6-9ec7-56a34bb36309)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/2c6c725a-aeef-4857-9a62-806863768540)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/1ad6bb9f-dc41-40dd-8e8e-28bb0029ba68)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/7843a5e8-e793-4dbf-b712-61d8b896125f)

### Footer Page

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/9b2e7627-d882-428b-84bc-ef1816f5899c)

- Includes: message from the 'Essence' company along with the logo. If logo is clicked, will take the user to the home page.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/66a5c180-f13c-4f37-9431-a5b33be05c62)

- Includes the following 'Useful Links': 'About Essence', FAQ', and 'Contact Us'.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/b5d89943-8fcf-489a-ae2b-ce4bad11ea3e)

- Includes 'My Account' links: 'View Cart', 'My Wishlist', and 'Help'.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/8256fb41-2e9c-442e-8279-4ff5d1ae429c)

- There are also 'Social Media' icons on the right side that takes the user to their respective pages.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/839aa2a7-54c4-47e7-bd7f-db0d0395c13c)

- There's also a copyright sentence displayed at the bottom and on the right side, there are card payment icons which are just there for beauty purposes, nothing will happen if they are selected.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/51b59e98-35a8-4502-a4df-329bc4a8afbb)

### Home Page

- This page consists of a slideshow that introduces the categories that are present on the website. There are also two images on the right side of the slideshow.
- 'Shop Now' and 'Discover Now' buttons are included on the images. These buttons if clicked will take the users to their respective pages. For example, if the 'Shop Now' button which is on the 'Hair Care' image is clicked by the user, it will take them to the Hair Care products page.
- The 'Gift Sets' image has a 'Discover Now' button. It has not been implemented yet, this is just for visual purposes. For future implementation, the gift sets are products that will be 'Available From 5th March 2024' (visible on the page), if the user selects the button, it will take them to the products page for 'Gifts Sets'. But for now, this feature has not been implemented.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/b5e06da3-45d8-4a07-97cf-2425820aca5c)

*Featured Products*

- Includes images, names, and prices of products that are featured.
- The products are displayed as a 'slider' so they basically slide to the left on their own. If user hovers on each product, there will be an 'Add to Cart' that is displayed underneath each product.
- If hovered on the products, user can also see the heart icon which if clicked (by a registered user), it will add the product to their wishlist.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/8a9a1e4b-e2b1-449d-bd65-5d4493fb56ad)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/aeb951c3-c97f-4b43-bbac-c20b6aee6e78)

*Shop by Categories*

- This section consists of four images that include the names of each category.
- If the image is clicked, the user will be taken to the specific categor page that they selected.
- If user hovers on the images, there's a 'Shop Now' button present on each image.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/e047ec79-853d-4ae8-8d80-9280cb328c91)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/e6370efb-383d-428a-8cd3-d1bde034dbee)

*Remaining Features For Home Page*

- Payment & Delivery, Returns & Refund, and Quality Support.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/f1618b8f-dfae-4d96-8ab0-f37122cc75fb)

- Newsletter Subscription Sign Up: user can input their email address and they'll be sent a confirmation email.

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/e0e1a3f5-4b88-49a9-8fa0-7df8b8493a6b)

### About Us Page

| PAGE      | FEATURE                                                                                                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------|
| ABOUT US  | - Includes information about the company: company’s vision, mission, and who they are.                               |
| ABOUT US  | - This page includes testimonies from customers in a slideshow format. User can click on 'next' and 'previous' symbols. |

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/2356e505-a039-4266-b310-3af9a0413252)

### Contact Us Page

| PAGE        | FEATURE                                                                                                               |
|-------------|-----------------------------------------------------------------------------------------------------------------------|
| CONTACT US  | - User can view the company’s contact information such as their address, phone number, email address, and office opening days and hours. |
| CONTACT US  | - User can view and have access to a contact us form which includes fields for name, email address, phone number, subject of email, and message. |
| CONTACT US  | - There is a ‘Submit’ button for users to send their message to the company. |
| CONTACT US  | - Users receive a confirmation message after submitting, assuring their message has been sent and the company will get back to them. |

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/8c22b393-6e79-4163-ab40-8980cd8db03d)

### FAQ Page

| PAGE  | FEATURE                                                                                         |
|-------|-------------------------------------------------------------------------------------------------|
| F.A.Q. | - Questions and answers regarding shipping information, orders & returns, and payments are visible here. |

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/a86f079c-ce31-49b0-8ae8-c38d84d9a8e1)

### Register Page

| PAGE      | FEATURE                                                                                         |
|-----------|-------------------------------------------------------------------------------------------------|
| REGISTER  | - Includes a Register form which consists of the following fields: email address, password, confirm password. |
| REGISTER  | - If all fields are not filled in, there’ll be an alert stating 'Please fill out this field'. |
| REGISTER  | - There is a ‘SIGN UP’ button present and functional. |
| REGISTER  | - There is also a box that MUST be clicked saying that ‘I agree to the privacy policy’. If the box is not selected, the user won’t be able to click on the ‘SIGN UP’ button. |
| REGISTER  | - If a user has already registered with an email address, they’ll be told ‘An account with this email already exists. Please use a different email address’. |
| REGISTER  | - For password security, if a password a user uses is too common, they’ll be notified – ‘This password is too common’. They will need to choose another password before they can move forward. |
| REGISTER  | - Once user can register, they’ll receive an email notification providing them with a link to activate their account. |
| REGISTER  | - Once the account is activated, they’ll be able to access their account and will receive a welcome notification - ‘You’re Welcome (email address), Account activated successfully’. |

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/85665f68-88a7-4fcb-91eb-6403d10bc723)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/4ed2c4f6-a66f-4d8c-bd16-8fa6bcace80c)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/ae33f2d3-927b-4dfe-9b3b-6e14754ae77e)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/dcc0ed5f-e10c-4550-8de4-f3b3234ccab9)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/6d0e3191-ce3f-48f3-8249-80de2eaad74f)

### Sign In Page

| PAGE    | FEATURE                                                                                              |
|---------|------------------------------------------------------------------------------------------------------|
| SIGN IN | - There’s a ‘Sign In’ form visible.                                                                 |
| SIGN IN | - Sign In form consists of the following fields: email address and password.                         |
| SIGN IN | - The form also includes a ‘LOG IN’ button.                                                          |
| SIGN IN | - When the ‘LOG IN’ button is clicked, user will be able to access their account.                    |
| SIGN IN | - They’ll receive a welcome message when logged in – “You’re welcome (email address)’.               |
| SIGN IN | - If user inputs incorrect details, they’ll be notified: ‘ERROR! Invalid Credentials’.               |
| SIGN IN | - If user inputs their email address without the ‘@’, they’ll be notified: “Please include an ‘@’ in the email address, ‘…..’ is missing an ‘@’. Even if they input the ‘@’ but they didn’t complete their email address, they’ll be notified that their email address is ‘incomplete’. |
| SIGN IN | - There’s a ‘Remember Me’ feature which contains a box that user can click if they want to opt-in for their login details to be remembered – for easier access. |
| SIGN IN | - There’s a ‘Forgot Your Password?’ option included in the form. If user selects this option, they’ll be taken to a page where they’ll input their email address. When they input their email address, they’ll receive an email notification which contains a link for them to reset their password. |

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/6602a2c2-48c5-4a28-b1cd-1d422ca35049)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/14e06076-aa0e-4c96-959d-483ea6abba29)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/d9b62fdd-5d68-4e8c-ae43-2ac6c0e80707)

![image](https://github.com/Rafz9Abz9/Essence/assets/126483536/55b645e5-1cd7-49d8-9dd2-8262de74bee6)

### Forgot Password Page


### Products Page


### Shopping Cart Page


### Checkout Page


### Account Information/Profile Page


### Error Page


## Authentication
- **Register**: easily sign up for an account using the ‘Register’ option in the account navbar. Once registered, user will receive a confirmation email. User can register with their email address and password. 

- **Login**: if user already has an account, they can select the ‘Login’ option in the account navbar. User can login with their email address and password. 

- **Log out**: if user wants to log out, they can click on the ‘Log out’ option in the account navbar. 

- **Forgot Password**: if a user forgets their password, they can click on the ‘Forgot Password’ on the Login page. Provide the email address used when registering an account, and an email with a password reset link.

- **Change Password**: if a user wants to change their password, they can go to their profile page and select the ‘Change Password’. User will have to put in their ‘Old Password’ then enter in their ‘New Password’ and select ‘Save Changes’ to save the details. 


## Future Features

- **Live Chat Functionality:** in my upcoming developments, I’d like to introduce a live chat feature that will allow users to receive immediate assistance while navigating our website, ensuring a smoother shopping experience.

- **Create an order tracking system:** I’d also like to craft an order tracking system that empowers customers to effortlessly track the real-time status and location of their orders, providing transparency and peace of mind.

- **Discount vouchers capability:** I’d also like my platform to boast the capability to apply discount vouchers during checkout, giving our users the advantage of unlocking potential savings on their purchases.

- **Ability to add reviews exclusively for purchased products:** I’d also like to work on a feature that allows customers to share their experiences by adding reviews exclusively for products that they’ve purchased, fostering a more genuine and reliable feedback system.

# Technology Used 

## Language
- HTML & CSS (Bootstrap template): **HTML** structures the web pages, while **CSS** styles them. **Bootstrap** provides ready-made templates and components for faster website development. 
- JavaScript: for the interactivity and dynamic features to web pages.
- Python: used for creation of the back-end function of the website.

## Tools
1. Version Control
      - GitHub: hosting the site and managing version control.
2. Development Tools
      - Visual Studio Code: utilized as the primary integrated development environment (IDE).
      - Django: python web framework used for building web applications.
3. Deployment
      - Heroku: deployment platform for the site.
4. Design & Planning
      - Balsamiq: creating the wireframes for the website.
      - Lucidchart: generating the flowchart for the website's structure.
      - DrawSQL: designing the database schema.
5. Graphics & Styling
      - Logo: creating the website's logo and typography.
      - Bootstrap: used template for front-end development.
6. Code Validation & Testing
      - W3C HTML Validator: validating HTML.
      - W3C CSS Validator: validating CSS.
      - JSHint: validating JavaScript code.
      - CI Python Linter: validating Python code.
      - Chrome DevTools: debugging and testing with Lighthouse.
7. Data Management
      - AWS: storing media and static data.
      - PostgreSQL (Postgres): used for storing and managing structured data.
8. Payment Processing
      - Stripe: handling online payments and managing transactions.
9. Content Generation
      - [ChatGPT](https://chat.openai.com/): used for creating descriptions for website's introductions.
10. Testing & Performance
      - Lighthouse: testing performance of website.


# Testing


# Deployment
This project was developed using **Visual Studio Code** as the IDE, [**GitHub**](http://github.com/) as the remote repository, [**AWS**](https://aws.amazon.com/) to store static and media files, [**Heroku**](https://www.heroku.com/) as the deployment site, and [**Stripe**](https://stripe.com/en-se) for processing online payments.

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

**Connecting AWS to Django**
- Sign Up for AWS: Create an AWS account if you haven't already.
- Install Boto3: Use pip to install the Boto3 library, the official AWS SDK for Python.
- Set Up AWS IAM User: Create an IAM user in the AWS Management Console with appropriate permissions and note down the Access Key ID and Secret Access Key.
- Configure AWS Credentials: Add your AWS credentials to your Django project's settings using environment variables or a configuration file.
- Install Django Storages: Use pip to install Django Storages, a library that provides custom storage backends for Django applications.
- Configure Django Settings: Set up Django to use AWS S3 for static and media file storage by specifying the bucket name and AWS credentials in your settings.py file.
- Upload Files to S3: Use the AWS Management Console or Boto3 to upload your static and media files to your S3 bucket.
- Test Integration: Start your Django server and verify that static and media files are being served from AWS S3.
- By following these steps, you'll be able to connect AWS to your Django project and use S3 for storing static and media files.

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


**Stripe Payment**
1.	Sign Up and Get Keys: Log in to your Stripe account, go to the "Developers" tab, and copy your API keys. Then, in your Heroku dashboard, add these keys as config variables:

•	STRIPE_PUBLIC_KEY: Copy your Stripe publishable key here.

•	STRIPE_SECRET_KEY: Paste your Stripe secret key here.

2.	Set Up Webhook: In Stripe, create a new webhook for your live site. Navigate to the "Webhooks" section, click "Add Endpoint," and paste your live site's URL followed by /checkout/wh/. Make sure it's set to listen for all events.
   
3.	Get Webhook Secret: After setting up the webhook, click on it, and at the top, you'll see "Signing Secret." Click to reveal the secret value. Copy this secret and set it as a new config variable in Heroku:

•	STRIPE_WH_SECRET: Paste the signing secret from your new webhook here.

By following these steps, you'll have successfully set up Stripe payments for the website.


# Credits

## Content
- Bootstrap template was used for the front-end development and customised.
- Boutique Ado Walkthrough from [Code Institute](https://codeinstitute.net/) was used as an inspiration. It allowed me to have an idea of how to go about my website. It was very helpful and made it less stressful.
- [Django Documentation](https://www.djangoproject.com/) was used for examples of code solutions and Django functionality.
- [Stripe](https://stripe.com/en-se) used for processing online payments and managing transactions for businesses, allowing them to accept payments securely over the internet.

## Media
- [Logo](https://logo.com/) was used for the website's logo.
- [Unsplash](https://unsplash.com/) was used for some of the images used on the website.
- [Freepik](https://www.freepik.com/) was used for some of the images used on the website.
- [Google](https://www.google.com/): some images were also taken from Google.
- [Boots](https://www.boots.ie/) was used for some of the product images  used on the website. The details of the products were also taken from this website.
- [iStock](https://www.istockphoto.com/): some images were taken from here.
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
