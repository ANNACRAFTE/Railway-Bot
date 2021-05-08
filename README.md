# Railway-Bot
Discord bot for railway fans

Very simple bot that allows users to add, request to remove, view trains in the uk. It will also have the abilty to show live trains from all stations in the UK

# Planned Features
- Live travel updates from national rail.
Using the National Rail public api this bot will provide you with live travel updates. 

- Train database (add and remove features)
In this i am thinking of building a mysql based database with a very very simple json api and allowing people to `!requestadd` to the request to add a train of any sort. Once requested it will be sent to a webhook in my main dev server (soon to be public) and then i will approve the request and send it to the database(api). The `!requestremove`  will work in the same way however i will only allow remove requests if they are 1. not a loco in the uk 2. not even a loco (spam filters will be added). 
I will also add a command that allows users to `!requestedit`. This command will allow them to request to change loco info. 
**All Requests will be sent to me(bean) until they are approved unless they are from in house/in my server**

- Live departure boards (web feature)
For this feature i was thinking of having some form of web system that would display (using the national rail api) a live departure board from the top 100 stations and then make people be able to request this in a image state into discord. 


# Planned Bot Release Date. 
I plan to have the first two points out by 12/05/2021. 
**However i cant promise anything**

# Planned API Release Date
I plan to have the **api** out by 14/05/2021. Note: It will be online upon the bot coming out but not for public use. 

# Website Planned Release Date
I plan to have a website before the end of May.

# Suggest a feature. 
To suggest a feature let me in my discord dms. `bean!!!!!!!#0041`

Thanks, Bean
Lead Dev @ Alle Group

**Alle Group are hiring join today @ Our discord https://discord.gg/F9cpRS7gX8 Or Via TMP https://truckersmp.com/vtc/allegroup**

**The Discord Bot will be written in:**
- python
- Json
- TS 
- React



# The code will be open source but only partly.
- Simple Bot Code (no api info, bot tokens)
- No webiste code
- No web server info. 



# Update 08/05/2021
Here is a sample image of what the `!requestadd` command looks like. 
![yhjkjkl](https://user-images.githubusercontent.com/67719111/117544252-801cb200-b018-11eb-8c6c-24d1e5e1e1c5.png)
