# Railway-Bot
Discord bot for railway fans

Very simple bot that allows users to add, request to remove, view trains in the uk. It will also have the abilty to show live trains from all stations in the UK

# Planned Features
- Live travel updates from national rail.
Using the National Rail public api this bot will provide you with live travel updates. 

- Train database (add and remove features)
In this i am thinking of building a mysql based database with a very very simple json api and allowing people to `!requestadd` to the request to add a train of any sort. Once requested it will be sent to a webhook in my main dev server (soon to be public) and then i will approve the request and send it to the database(api). 

The `!requestremove`  will work in the same way however i will only allow remove requests if they are 1. not a loco in the uk 2. not even a loco (spam filters will be added). 

I will also add a command that allows users 
