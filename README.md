# TTC-heardlediscordbot
A bot to track heardle scores for discord members

Track our scores after a headle past
Stats would be numbers of heardles reported divided by points

TODO:
 - [ ] Break out each apps post logic into sperate files as classes that follow template
   - [ ] Heardle
   - [ ] Wordle
   - [ ] CineNerdle 
   - [ ] namethatride 
   - [ ] Moviedle 
 - [x] Dynamodb mvp
   - [x] Create Dynamodb table 
   - [x] save/overwrite entire jsob blop to table
   - [ ] ~~Pull down all results and save into dictionary at start~~
 - [x] Dynamodb 2.0
   - [x] Create id based on username+dis
   - [ ] ~~In username create unqid that is the app~~
   - [x] Update dynamodb table with new score post
   - [ ] Query dynamodb table and to pull user's average score for app
   - [ ] Query dynamodb table and get all user's score per app
 - [ ] Dynamodb Bleed
   - [ ] Save meta data about user
   - [ ] Compare bewteen Guilds (servers) on averages
   - [ ] Create table for app specific data 
     - [ ] Query actual site and insert data about post here for later stats
 - [ ] DESIGN 
   - [ ] Figure out skip logic
     - [ ] <put answer here>
   - [x] When a user posts twice in the same day CALL THEM AND IDIOT
   - [ ] Come up with stats to show players
     - [ ] Leaderboard?
     - [ ] par?
   - [x] Make MVP commands for bot
     - [x] Just copy from what surf does for rank and stats
     - [ ] ~~!dleStats~~
     - [ ] ~~!dleRank~~

## DEV NOTES:
Heardle emjois
- 🔊 1st try success
- 🔉 2-5th success
- 🔈 6th try success
- 🔇 failure
- ⬛️ skip #This isn't Ascii
- ⬜️ didn't reach #This isn't Ascii
- 🟩 success 
- 🟥 wrong
- 🟨 correct artist wrong song

## Helpful links
- https://google.github.io/styleguide/pyguide.html
- https://discordpy.readthedocs.io
- https://discord.com/developers/applications/979565962883899462/bot
- https://www.heardle.app/
- https://discord.com/developers/docs/intro

### Old TODOs:
 - [x] Core logic
   - [x] Get user name (Fake user name)
     - [x] Crate an Dictionary of username to value
 - [x] Parse Heardle pastes
   - [x] Count emjois
 - [x] Get discord stuff
   - [x] Get user name