# QCAA Year 12 OP Prediction in Python (Scott Howie)

Well, in an attempt to find out my OP before it's calculated I've made the building blocks to an OP estimation program. 

# DISCLAIMER

This program is very experimental and I made because I was bored. The actual OP calculation process is MUCH MUCH more complicated as it involves different procedures for small groups of students, intermediate groups of students, large groups of students, VISA students, and a mixture of all of those. These conditions are all ignored. There is also verification of student SAIs which make sure there are no anomalies. It doesn't even account for non OP students. This python program is in no way accurate and is kinda as good as guessing. If you really wanna know your OP, ask your deputy at your school and she will probably give you a good idea. As I don't have access to other student's grades, the achievements are estimated and obtained from public sources on the QCAA website. This introduces massive reliably issues and therefore should not be used as a definite result. If you were a school and had access to student grades and information, it's theoretically possible to use this program by inserting that information but I doubt anybody reading this is a teacher. If you are interested in using this program for your school, feel free to contact me because I would totally be down to program that. Field positions are also NOT calculated because those are boring and no student wants to know their field positions.

# Rundown of how OPs are calculated in terms of this program

At the end of the year, your teachers will compare your work against everybody else in your cohort who is OP eligible. Although you might have grades like VHA or HA, they actually mean very little. You are instead given a Subject Achievement Indicator (SAI). The person whos work is the worst will get an SAI of 200. The person whos work is the best gets an SAI of 400. Everybody else is inbetween 200 - 400. It doesn't matter if the worst person got a SA3, they would still get an SAI of 200. This is done for every one of your OP subjects, so you get an SAI for each one of your subjects. YOU WILL NEED THIS SAI TO USE THE PROGRAM!

The QCS test is split into 4 different tests. The result you get in your short response and written response are both out of 100, and the  multipul choice tests add to 100 questions. This gives you a max QCS score of 300. For each subject, an average SAI is calculated but also the standard deviation. The average and standard deviation of your subject's QCS results is also calculated. Then using Z scores, the SAIs are scaled onto the QCS results and the resulting values are referred to as scaled SAIs. It should be made clear that each subject is scaled to those students who are in that subject only. So my SAI for English will not be scaled with somebody elses from another subject or who is not OP eligible.

So each student now has a scaled SAI for each OP subject. If a student is doing 6 OP subjects, the worst scaled SAI is dropped as only the best 5 are used. If a student is doing 5 OP subjects, those scaled SAIs are used. Those scaled SAIs are then averaged to produce an Overall Achievement Indicator (OAI).

Every single OP eligible student's OAI is then averaged and standard deviation is produced. This happens to every single student in the school regardless of subjects. Then, everybody's QCS results are also averaged and a standard deviation is also produced. Using Z scores again, the OAIs are scaled onto the QCS results to produce scaled OAIs.

This scaled OAI is what determines your OP. Each OP band (eg OP 1 or OP 3) is given a specific range of values of which it sits in. Anything between this range gets that OP. For example (assuming from 2016 results), if the scaled OAI I got was between 200.5054 and 206.6367 then I would have gotten an OP of 4. However, if I got a scaled OAI between 206.6367 and 214.3284 then my OP would be 3.

And Field positions? Nobody cares about those so don't worry about them.

# How my program works

First of all, there is no way to know students results as I don't have access to that information. However, the QCAA publishes how many students get between an OP 1-5, 6-10, 11-15, 16-20 and 20-25. My program uses that information to produce "fake" QCS test results, so that schools where lots of people get good OPs get good QCS results. This isn't very accurate at all but it's the only information I have access to. {This part of my program needs calibrating as of Jan 2017}. The QCAA also publishes (for public schols) how many students are in each cohort in each school. This is helpful because my program gives each student in each subject in each school an SAI. Depending on how many people are in the subject, these SAIs are perfectly linear and all have an average of 300. This is a major flaw in my program, but theres not much I can do as I don't have any other information to go by.

Using the fake QCS results, those SAIs are then scaled for each subject. However, the person using the program would enter their school and SAIs as well as their subjects. These would be inserted into the corrasponding subject groups and will be scaled with other fake SAI information. So for those subjects only, the average would be slightly different to 300.

Then, the person's scaled SAIs are retrieved and all averaged together to produce an OAI. For now, my program uses that OAI instead of a scaled OAI to produce an OP score. This is also wrong, but I haven't finished the program and haven't added that step yet. That OAI is then checked against all the OPs and the one it falls into is printed to the screen.
