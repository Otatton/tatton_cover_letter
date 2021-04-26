#!/usr/bin/python

#This is an interactive cover letter script written in python
#Just so you know, I wrote this old school in vi
#No fancy new fangled tools like notepad++
#Thanks again for the look, your company looks great from the website and I would love to work there
#Wrtten by ORyan Tatton 3/22/21

import time, sys, argparse

parser = argparse.ArgumentParser(description="This is an interactive cover letter script written by ORyan Tatton")
parser.parse_args()

company = "ABC Company"
jobtype = "Internship"
jobtitle = "Software Engineer Intern"
jobdesc = """
         - Assisted with the design and creation of software applications as a member of an agile team of software developers
	 - Performed triage and resolution of software defects
	 - Assisted with the creation of enhancements to software in accordance with feature specifications
	 - Conducted software tests in adherence with quality standards
	 - Participated in the design and planning of new features
   """

def main():
   greeting(timenow())
   menu()

#using system time to tailor the script greeting
def greeting(hour):
   if hour > 5 and hour < 11 :
      print "Good Morning"
   elif hour > 10 and hour < 16 :
      print "Good Afternoon"
   elif hour > 15 and hour < 22 :
      print "Good Evening"
   else:
      print "Wow, when do you sleep? Well, nice to meet you"
   print("""
My name is ORyan Tatton and I would love to set up an interview
Call me at 801-809-9876 or shoot me an email at otatton@gmail.com
""")

def timenow():
   currentime = time.localtime(time.time())
   var = currentime[3]
   return var

#main menu function
#Why use sleep? This thing is so lightweight I wanted to slow it down to make if "feel" like it is doing more work than it is
def menu():
   print("")
   print("Welcome to my interactive cover letter script")
   option = 1
   while option != 0:
      time.sleep(1)
      print("")
      print("")
      option = input("""
      1- Professional Coding Experience
      2- Other Experience
      3- Education
      4- Why did I write this in python?
      0- Exit
      ----------------------------------
      
      Please enter your option: """)

      if option == 1:
         coding()
      elif option == 2:
         other()
      elif option == 3:
         edu()
      elif option == 4:
         why()
      elif option == 0:
         sys.exit
      else:
         print("      That is not a valid option, please try again")

def coding():
   print("""
      You have a fine sense of humor, if I had profesional coding expererience I wouldnt be applying for this %s.

      But if you hire me then this section can get the love and attention it deserves.

      Just imagine how great this would look if you came here and it said:

         Coding Experience:

         %s at %s %s
      """ %(jobtype, jobtitle, company, jobdesc))
   print("      Wouldnt that just look amazing?")

def other():
   print(""" 
            Senior Analyst, VxRail at DellEMC March 2018 to March 2021

	       Performed soul crushing technical support for datacenter infrastructure:
	          - Linux and esxi command line troubleshooting
	          - Log analysis and review
	          - Hardware, network, and application level troubleshooting
		  - PostgreSQL queries and table manipulation for vCenter and VxRail databases

            Information Technology Intern at Moog Industries, March 2017 to March 2018

	       General help desk internship:
	          - Active directory administration
		  - System imaging
		  - Line terminations
		  - Computer hardware support
   
            I also spent 4 years in law enforcement and owned a Taekwondo studio for several years
   
        """)

#sub menu function for education section
def edu():
   option = 1
   while option != 0:
      time.sleep(1)
      option = input("""
          
          Education

	  Weber State University - Currently attending as a senior for a BIS in Computer Science, Network Management, and Criminal Justice

	  Pick an option for course details and grades:

	  1- Computer Science
	  2- Network Management
	  3- Criminal Justice
	  4- GPA
	  0- Go back to main menu
	  q- Exit program
	  
	  """)

      if option == 1:
         print(""" 
	        Computer Science Emphasis
		
	        Courses Completed:
		   
		   Course	Title				Grade	Credits
		   CS 1400	Fundamentals of Programming	A	4
		   CS 1410	Object Oriented Programming	A	4
		   CS 2350	Web Development			B	4
		   CS 2420	Intro Data Structures and Algo	B+	4
		   CS 2550	Database Design & Application	A	3
		   CS 3230	Obj Orient User Interface Java	A-	4
		   CS 3270	Mobile Develop for Android	A	4

		   Note: Some CS courses taken are part of the NTM emphasis and are not listed here, such as scripting languages

		   """)
	 
      elif option == 2:
	 print("""
	        Network Management Emphasis
		
		Courses Completed:

		Course		Title				Grade	Credits
		NTM 2200	Microcomputer Operating System	A	3
		CS 2705		Network Fundamentals/Design	A	3
		CS 3030		Scripting Languages		B	4
		NTM 3200	Linux Systems Administration	B+	3
		NET 3710	Switching & Transmission	A	3
		NET 3715	Transmission Network Apps	A	2
		NET 4700	Data & Voice Network Design	A	4
		NET 4760	Network/Telecommunicatn Intern	C	3

		""")
	     
	 
      elif option == 3:
	 print("""
	        Criminal Justice Emphasis
		
		Courses Completed:
		
		Course		Title				Grade	Credits
		CJ 1010		SS Intro to Criminal Justice	A	3
		CJ 1330		Criminal Law			A	3
		CJ 1340		Criminal Investigation		B	3
		CJ 1350		Introduction Forensic Science	A	3
		CJ 2350		Laws of Evidence		A-	3
		Cj 3270		Theories - Crime & Delinquency	A	3

		Note: You may be asking yourself "Why Criminal Justice? That is so random."

		And you would be right. We all make mistakes in our youth, this one just took years of my life and thousands of dollars in tuition.

		The only good thing a CJ degree is good for is making it harder to sleep at night and causing you to lose all faith in humanity.
	
		""")
         
      elif option == 4:
	 print(""" 
	        Computer Science Emphasis GPA:   3.70
		Network Management Emphasis GPA: 3.52
		Criminal Justice Emphasis GPA:   3.78

		Overall GPA:                     3.27

		""")
	 
      elif option == 0:
         time.sleep(2)
      elif options == "q" or "Q":
	 sys.exit
      else:
         print("      That is not a valid option, please try again")
	                            
      
#cover letters suck
def why():
   print("""
       Ah, the eternal question: Why?""")
   time.sleep(1)
   print("       well...")
   time.sleep(2)
   print("       ...")
   time.sleep(3)
   print("       uhh...")
   time.sleep(4)
   print("""
       honestly? It seemed like fun.
       
       I haven't written anything in python since my linux admin class so it seemed like a good oportunity to pick it back up.
       I also hate writing standard cover letters, they are just the worst.
       
       """)
   

try:
   main()
except:
   print("      Thanks for taking a look, I look forward to your call")



