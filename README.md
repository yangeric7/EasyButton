# EasyButton
Easy Button is a one push solution to pay all of your bills!

### Description
Easy Button is a button that pays all possible bills within 2 days of the payment date. If a customer has a savings account and multiple bills that are due within 2 days, one push of the button will pay all possible bills. If bills exist that are not payable in that there is not enough money in the savings account, the bills will not be paid. 

####Dependencies
1. Arduino 
2. Python 2.7.11
* [pySerial](https://github.com/pyserial/pyserial)
* [requests](https://github.com/kennethreitz/requests)

#####How to run
1. Load the Arduino with the `payButtonBill.ino` file.
2. Open `index.html` in Chrome to track the accounts and bills 
3. Run `python communication.py`  to connect Python with the Arduino
4.  Press the button on the board attached to the Arduino to pay your bills!


#####Notes
* If encountering error with loading files into Arduino or using Python to communicate with the Arduino, check the COM port and make sure they are synced together. Before loading a file into Arduino, press the reset button. 
* A savings account must exist for the customer in order to pay the bills. To create a savings account and locate any detail about the customer, account, or bills, go to the [Nessie API page](api.reimaginebanking.com) and enter in the `API_KEY`.
