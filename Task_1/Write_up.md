# Booking Hotel
## _Key Scenarios to be Tested:_

- Profile Verification 
   - In the profile verification face complete login process will be verified,login will be tried out different combinations of username and passwords, different logout/login scenarios will be tested.
   - Profile details will be verified, details are displayed properly of the userhas to be verified.
   - History/Recent operations has to be verified, proper detailing of recent booking or transactions are captured or not.
   - Contact details has to be verified, users contact info details are proper or not has to be tested.
   - Account balance details has to be verified and account related transactions are properly listed or not.
- Booking Scenario 
    - Searching of hotel,In this case we will try with different locations, different inputs(dates,number of persons, etc) both negative and postive scenarios, corner cases will be tested.
    -  Post search case selecting the required hotel, navigating through different options they provides for booking, review details etc has to be tested.
    -  Post selection filling up the required details, with different combinations both negative and postive scenarios, corner cases will be tested.
    -  Payment, verifying whether payments are happening through secure way, payment options, trying multiple combinations of payments.
    -  confirmation mail/sms, post payment confirmation mail and sms are received or not will be verified. Mail/sms has all the details or not will be verified.
- Cancelation Scenario
    - Cancelling of the existing bookings, will verify whether cancelation is allowed for the existing booking.
    - Partial cancelation, partial cancellation or modification of existing booking will be verified.
    - Cancel confirmation, post cancellation confirmation mail/sms is received or not has to be verifed.
    - Refund process post cancellation refund details are available in the website as well as in the cancelation confirmation has to be tested.
    
# Testing Details:
- Exploration target: what scenario are you exploring? What’s the functionality?
    - Booking scenarios
    - Booking Functionality

- Does the site behave as you would expect? Did you discover anything that looks like a bug? Did you see anything you think could be improved?
    
    -Issue - It should display hotel which are available for the day
    -Issue - Suggestion hotel are getting into 404 error
    -Issue - Hotelcount is not getting updated after filtering
    -Issue - Page count is also not getting updated after filtering 
    -Isuue - Most of buttons are not clickable
    -Enhancement - star grades : count of hotels can be displayed
    -Enhancement - Instead of showing oops not match found , it can show the next availabilities
## _Unable to proceed with booking scenario as all hotels are showing No Rooms available._  

- Prioritisation of those use cases - which area of the website or testing would you explore first and why?
    - Profile Verification
    - Booking Scenarios

- What kind of risks do you need to mitigate for this type of application?
    -Traffic testing scenarios
    - Secure payments scenarios
    - Privacy of customer details
    - Items added in the website should be genuine
    - Booking details should be in sync with hotels where booking has been done.
