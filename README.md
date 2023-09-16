# OTT-subscription-system

Goal: As a smart OTT company, we want to offer customized OTT plans for our customers so that the customers should be able to choose to build their plan by choosing different streaming platforms and how many viewing hours they want for each of them. 
We do support the following streaming services and below is their tariff plan. 

Netflix 10 hrs - 10 rs
Amazon 5 hrs - 2 rs
HotStar 5 hrs - 1 rs



Viewing hours can be subscribed based on the multiples of the above mentioned units only. 
Based on the user’s choice, the system should show the total amount which should be paid by the customer.

* Sample Input 1 Viewing hours for Netflix: 20 Viewing hours for Amazon Prime: 10 Viewing hours for Hotstar: 50 Sample Output Total amount should be paid: Rs.34 (10 * 2 + 2 * 2 + 1 * 10)

* Sample Input 2 Viewing hours for Netflix: 10 Viewing hours for Amazon Prime: 0 Viewing hours for Hotstar: 100 Sample Output Total amount should be paid: Rs.30 (10 * 1 + 2 * 0 + 1 * 20)

* Sample Input 3 Viewing hours for Netflix: 10 Viewing hours for Amazon Prime: 2 Sample Output Amazon Prime allows viewing hours in multiples of 5 only 


* Used factory pattern for calling subscription classess
* Inheritance relationship