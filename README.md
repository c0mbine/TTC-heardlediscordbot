# TTC-heardlediscordbot
A bot to track heardle scores for discord members

Track our scores after a headle past
Stats would be numbers of heardles reported divided by points

TODO:
 - [x] Core logic
   - [x] Get user name (Fake user name)
     - [x] Crate an Dictionary of username to value
 - [x] Parse Heardle pastes
   - [x] Count emjois
 - [x] Get discord stuff
   - [x] Get user name
 - [ ] Store results
   - [ ] Store results in flat text file for now (on whoever)
   - [ ] OR go through all of chat and re-parse
 - [ ] Count skips if someone didn't post for a day
 - [ ] When a user posts twice in the same day CALL THEM AND IDIOT
 - [ ] Account for skips

STRETCH:
 - [ ] Gather meta data from heardle for each day 
 - [ ] Par per genre
 - [ ] Par per decade

DEV NOTES:
# 🔉 sounds start
# ⬛️ skip
# ⬜️ didn't reach
# 🟩 success
# 🟥 wrong
# 🟨 correct artist wrong song