Problem statement:
	Due to the onset of the Covid-19 pandemic, we have been encouraged to stay home to minimize the spread of the virus.  
  Weekly trips to the grocery store became dangerous for anyone who was immunocompromised and at risk of infection. 
  Even though shopping in public presents challenges, people still require access to food for themselves and their families. 
  The need for organized food delivery services has never been greater. 
  While multiple services exist for ordering food, they do not have the same offers and it can be difficult to decide which one to use. 
  This problem is especially evident among the elderly who may not be accustomed to purchasing their food remotely. 
  The elderly population is also at the greatest risk of developing a serious infection as a result of Covid-19. 
  That is why this project is focused on developing a simple yet effective method for ordering food online from all your favorite restaurants. 

Solution statement:
	Our project serves as a way for people to get the food they need without ever leaving their homes. 
  While the actual food delivery system would be up to the restaurant, we created an organized database of potential restaurants for the user to choose from. 
  This way the user simply needs to call one of our many operating centers and place their order. 
  They may choose a specific restaurant or just describe what they are looking for and we can pair them with one of the restaurants in our database. 
  We also include relevant identifying information for each restaurant to ensure the user knows exactly which location they are selecting. 
  This will allow people to confidently and safely order food without putting themselves and others at risk. 

User:
	Anyone who is interested in reducing the spread of Covid-19 is a potential target for our project. 
  Since it also alleviates the stress of finding a restaurant's phone number and placing an order, anyone who wants to save time getting dinner can use our project as well. 
  All a person needs to do is call one of our operating centers and sign up for an account, either standard or premium, and then they are all set to begin using our service. 
  Then after they placed their order we will send them a venmo request to pay for their meal. 

Domain objects:
	One domain object that has been implemented in this project is instructions and it belongs to the orders domain. 
  In this domain object the user describes any special instructions for their order that we can relay to the restaurant that is preparing the food.  
  Another domain object that we created is food request and it also belongs to the orders domain.
  This domain object allows a user to request the food they want as well as the option to request a specific restaurant to order from.
  Then if the user specified a restaurant the food request is ordered from that location,if not the order is given to the closest restaurant that serves the food they want. 

1. The name of the project is DumbDash.
2. The name of our team is The DumbDashers.
3. The DumbDashers include Daniel Draymore (section 3), John Drohan (section 3), and Vasu Zalawadia (section 4).
4. The need for organized food delivery services has never been greater due to the COVID-19 pandemic, especially for the elderly community. 
  Our project is focused on developing a simple yet effective method for ordering food online from all your favorite restaurants, mitigating risk of exposure to the virus. 
  We created an organized database of potential restaurants for the user to choose from. 
  The user simply needs to call one of our many operating centers and place their order. 
  They may choose a specific restaurant or just describe what they are looking for and we can pair them with one of the restaurants in our database. 
  This will allow people to confidently and safely order food without putting themselves and others at risk.
5. Updated UML Diagram (viewable [here](https://github.com/jdrohan356/DB_Project/blob/main/db_design_final_project_UML.pdf)) ![UML](/UML.png)
6. The user data model includes information on each user’s name, username, password, address, zip, Venmo username, phone number, email, and the time of account creation. 
  This data is important because it allows us to easily find at which address to deliver the food to any given customer, contact any customer by email and/or phone with updates on their order or if there is a problem, and have them pay us the correct amount through Venmo.
7. Our two domain objects are orders, and restaurants. 
  The orders data model includes the desired food and associated prices. 
  The restaurants data model includes the names of the restaurants and the corresponding phone numbers. 
  This information allows us to find a nearby restaurant that will satisfy the customer’s food request, place the order at the restaurant we found, and verify the Venmo amount we should have received.
8. The relationship between the user and the order data models is one to many. 
  Any given order was placed by only one account and each user can place many orders. 
  For example, any given user could order dinner every night using our service.
9. The relationship between the order and the restaurant data models is many to one. 
  One restaurant can receive many orders from our customers and each order can only be for one restaurant. 
  If more than one restaurant is required to get the customer all requested items, separate orders must be placed.
10. The portable enumeration describes which type of account each user has. 
  The two types of accounts are standard and premium. 
  The premium account has everything the standard account has and more, except it comes at a cost of $25 per month. 
  The benefits of the premium account include a 10% service fee charge (compared to 30% for standard accounts) and guaranteed 24 hour response time from our customer service.
11. The user interface of our database has been designed so that those working in our call centers can efficiently record a user's order and place it at the appropriate restaurant.
  It first presents a list of previous orders along with an option to create a new order.
  When this option is selected the operator will then fill in the appropriate information corresponding to a specific order. 
  This new order will then be added to the list of previously completed orders. 
  The UI also provides the ability to create, edit, and delete users from the database. 
  This way new, current, and previous users can alter their accounts with a simple phone call to one of our operators. 
  To create a new user, click the ID of any existing user, change the ID to a number that does not yet exist, fill in the information for the new user, and click the "Insert User" button.
  To update a user, click the ID of the user that needs updating, replace the old information with the new information, and click the "Save User" button.
  We decided to CRUD in this fasion as it increases modularity and reduces the risk of human errors.
  Finally to keep the data stored in the database up to date, the UI also allows the operators to create, update, and delete any of the orders or restaurants currently being stored.
