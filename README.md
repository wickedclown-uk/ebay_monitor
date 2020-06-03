 
This is a tool to monior an Ebay page for updates.
Have you ever been wait for something to appear on ebay,
but they only appear a few times a week or month, 
so you do not need to check it every day this will check it every 6hrs.
You of cause need to have this on a machine, that is on 24 / 7 .. like a media server?!?

This script will email you, so you will need to have an email server you control, 
I tried email but could not get it working.. well, I kept getting messages of unauthorised access. LOL.

So I set it up on my personal email system, and it works. :)
So I created a new email called ebay@ and got it to email myself.


Save this script to you system, 

make sure is it is executable 'chmod +x em.py'

Configure crontab: crontab -e
at the bottom of the file add the following:

0 */6 * * * /opt/em/em.py

55 23 * * * /opt/em/em.py

Save the file, now the cronjob will run every 6 hrs, and 2355hrs.
REMEBER: change the folder location where you saved the script.
