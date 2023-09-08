This is the v1 protocol spec.
"Packets" are all sent in a json format. An example message is below.
```json
{
	"packet": "init",
	"info": {
		"version": 1,
		"id": "test",
		"receiveFromOthers": true,
		"receiveFromDiscord": true
	}
}
```


# Packets :
## init :
This is used for a client to "register" with the server. This should be *ignored* if the server is already registered, to account for servers building a new squirrel vm upon map change.
- "version", int, marks the version of the spec
- "id", string, marks the id of a client
- "receiveFromOthers", boolean, whether the client should receive chat from other clients
- "receiveFromDiscord", boolean, whether the client should receive chat from discord

## heartbeat :
Clients must send this to the server at least every 10 seconds. Server must drop the connection entirely if there is no heartbeat for 40 seconds or more - there is *one* exception, the map change. Servers should implement this exception as simply a higher timeout limitation.
- "id", string, marks the id of a client.

## map :
Sent from client to server when a map loads. 
- "id", string, marks the id of the client.
- "map", string, map name.
- "mode", string, mode name.

## playerJoin : 
Clients send this when a player successfully connects.
- "id", string, marks the id of the client.
- "uid", int, marks the user id of the player joining.
- "username", string, marks the name of the player joining.

## playerLeave : 
Clients send this when a player disconnects.
- "id", string, marks the id of the client.
- "uid", int, marks the user id of the player that left.
- "username", string, marks the name of the player that left.

## chatMessage : 
Clients send it when a player chats, and servers send it when either a discord user chats, or when another server chats.
- "id", string, marks the id of the client the player chatted on, or "Discord" if sent on discord.
- "text", string, marks the message content.

## exec :
Only ever sent from server to client. Makes the client run a command on the respective Northstar server.
- "command", string, the complete command including arguments.
