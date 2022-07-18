#This is a simple code for creating a instabot that can follow unfollow upload and do may tasks few of them are mentioned below

#importing the instabot
#if not installed install it by pip install instabot

from instabot import Bot

#calling the function

bot=Bot()

#Login into your account using username/gmail/phone no , password

bot.login(username="#give username /gmail /phone no ", password="Give your account password ")

#After login in the account you can follow a particular account by giving his username

bot.follow("#username of the account you want to follow") #passing username as a string

#you can unfollow the particular account by giving the particular username

bot.unfollow("#username of the account you want to unfollow")  #passing username as a string

#you can upload any of the photo you want from your device storage by just giving the path to the image

bot.upload_photo("#path of the photo in your storage",cation="#any caption as you wish")

#approves the pending follow requests of the account

bot.approve_pending_follow_requests()

#blocks the acoount specifying the username

bot.block( self,#username)

#delets any media by giving the media link
bot.delete_media()

#you can send messages to single / multiple accounts specifying their username

bot.send_message("#any Message eg-hello",["#username1","username2","username3"])

#below code show the followers list to the mentioned username and prints all the followers present on that account one by one

followers=bot.get_user_followers("username")
for follower in followers:
    print(bot.get_user_info(followers))

#below code show the following list to the mentioned username and prints all the following present on that account one by one

following=bot.get_user_following("#username")
for Following in following:
    print(bot.get_user_info(Following))
