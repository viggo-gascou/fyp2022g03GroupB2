import regex as re


# multiple signs(?,!,...), 
# emojis /: 👨‍🦼  😎🤓 
# Undtagelser: 
# Capital letters between dots (U.S.A) [A-Z.A-Z]*
# evt behold gåseøjne?? (ejjj hvor "sjovt")
# [-6] == sation, er det samme som zation & [-3] == ise == ize 
# Tænke over om ord der ligner hinanden skal være de samme run=running, five = 5 osv, color = colour. 
# 


# Her er en lille regex string der fanger det meste
# w/
# w/o
# @ eller # foran
# ord i anførselstegn
# ord med bindestreger i
# to ord med store startbogstaver efterfulgt af hindanden (fx New York eller Los Angeles)
# \b\d{1}\b|(?<!#)\b[A-Z]\w+\s[A-Z]\w+\b|w\/|w\/o|['"]\b\p{L}+\b(?:'\b\w+\b)?(?:-\b\w+\b)?['"]|w\/o|@?#?\b\p{L}+\d*\b(?:'\b\w+\b)?(?:-(?!http)\b\w+\b)?

# Emojis: [\U0000263a-\U000e007f]
 

# Fanger links -> (http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)

line = 'A cat #sat on the 0% mat. #HeIsNOTFunny!!!😒 His name was Måns... 0/10 he is a "fun" cat. can\'t 100% 10/10 @user 😎 Ucan MAKE MONEY #TWEETING this info w/ new app||http://t.co/Q2WB7riAvK <-News ||https://t.co/cpJZkEgNe7 som\' '

line = """All I can say is I'm lucky. 
#notcies #eu Liverpool workers "miscarriage of justice" victims 
@user yesss! What makes it worse is when they look gorgeous and say "I just got my face beat!" Wtf?  #Contradiction 
Xmas on the blog feat @user and @user * Read our story and share the LOVE ❤️ Click the link... 
Watching the move 'Begin Again' and the verisimilitude is overpowering, it's like I'm back in the 90s music business again.   
This is not the moon. Pictures like the moon is made of light bulbs.  #the #moon :) 
I got ready and then got to school and parked in less than 12 minutes! #miracle 
@user yeah. So as you can see, I have great success with the ladies! And I'm totally excited for having sex some more!  
I don't like clowns but I'm going to be one.  
MLS Transactions 2015 #MLS making waves again   2 b fair it will take more than 2 players to fix this 
@user I'll be a bit sweaty by the time I get to you! 
 a bad game last night. Way to go Packers! 
I hope I could recover from fever today. I need to start with strama.. 
somebody wake me up early tomorrow ive been facing weird aches in my back since early december .,. and why do u think that relates madaka 
The Champions League is overrated anyway!  
Porygon2 are  found in the www.monstermmorpg. com wild. #firemen follow @user #paint 
@user are you looking at the wrong profile picture? 
@user One day I want to travel with my bestfriend 🌏✈️ DONE DID TRAVELED DA WORLD!! @user ❤️ 
@user u simply cant win with @user if it is twitter fight!!! :-P 
Fully charged my #Anker portable charger...it lasted 1/2 an hour.  Awesome #Fail 
#Italy -- #Cabinet #approves #first #planks of #Renzi's #labour #reform. via @user 
ruling party in power#central#state#misusing their power#PM speaking only in foreign parliment#pm to visit out side india during session 
Gareth's polar opposite is a chicken-loving vegetarian 😂🐣  #Bones @user 
Watching creepy shit before bed when alone = bad idea. Is there a spell to turn a French bulldog into a big ass bulldog? #bewareofdog  
i do occupy rent free space in his cranial cavity LOL @user 
Had to take a #PatioPics - snow falling still. This was totally clear when I went to sleep. #WCCO 
August has the most birthdays, February has the least and most of the serial killers are born in November!||-so dont mess up with me|#nov26 
Lol RT @user Wouldn't surprise me if Soldado bangs in a hatrick and we win 0-3 against Chelsea tonight .. The legend is back 
My husband thinks I'm crazy because I taped my tape dispenser. Hehe. I'm handy like that. .... 
My secret name is lizard squad. I like to ruin people's fun time. Follow and rt to a billion and you'll have fun. #psn  #giveitup 
Tomorrow's afternoon #NFL sked in #PanamaCity area: WECP 12p #KCvsPIT, 3:25p #INDvsDAL; WPGX 12p #ATLvsNO. 
@user @user I sure hope ev1 vaccinations are up to date! #GoBolts @user @user @user 
Pulis turned down #NUFC cos he wants to spend a load of money on 30 year old journeymen. Parish wouldn't let him & neither would MA. #cpfc 
Sending best wishes to all my coworkers at the 9AM this morning  
@user try having no internet for a month. Now I know how Ethiopians feel.  
so, sane peoples would talk to themselves in twitter because they can't find other sane humans to talk to. that  #retweet#ifagree 
Thanks @user for connecting. Always look forward to exchange thoughts n ideas with #entrepreneur working on #green n #sustainability 
Seems as if @user wants to endorse me on LinkedIn for  - any thoughts on this from the #OMCchat crowd? 
Love being made fun of  
@user @user @user Oh wow your talking Skype! Cool!  
he was half of what she deserved, yet he was all that she ever wanted ,,,,  
5:30AM 00:00 12PM
#Christmas  #been #the #best @ West Monkseaton 
Parking meter obviously forgot to get its own parking ticket.  
About to fuck up this Media exam  #actuallyihopeso 
well today is gonna be a great day 👌  
Heaven help the fool who did her wrong 
Just bartered for a bottle of rum in best one, and got it down from £18 to £14. Happy Fucking New Year to me!! 
find ONE local PD that reported an 80% drop @user @user @user @user @user @user 
@user @user Money 4 Church|http://t.co/Q2WB7riAvK|SmartPhone APP PAYS you!|See-http://t.co/RDlRuGN0iE |Go 2: 
Well it's always a good time losing at the Bay... @user @user @user 
Welsh devolution? How's this for starters... 
I love when folks call Brady a system QB but are THE BIGGEST Peyton Manning fans. . 
@user Instead of playing the pompous "do you know who I am card?" , how about you actually make an educated rebuttal? 
Kind of love how I got a voicemail from my seat neighbor wondering where I was yet they constantly sell their ticket & I never ask  
I feel a nap in my near future. #NapTime 
#AnalScreen #Exotic Exotic brunette gets her little tight butt nailed right on the office desk 
#sundayfunday #mylove #mermaidlove #newyear2015 @ Rockefeller Center 
The ever so caring @user gets to see the siege ending first. Great journalism.  
www.google.com
@user You truly are my son. 
hmmm. I do wonder why Astec has one fewer employee? #lol  
#Germany -- #ECB's #Weidmann #says #German #2015 #growth #may #be #better #than #expected. via @user 
Kevin Durant with 23pts on 8-13 shooting, has this nigga been inefficient since he came.  
This chap seems to be a bit of an over sexed out going extrovert ... Must be his overly masculine voice and demeanor.   
Damit, this fatima bhutto has an instagram account but not pics of her. Some random shit...and then ppl i follow keep posting pics.  
@user so funny lolololol  
@user @user what the hell ever. 
On my lunch break so sleepy😴 
@user @user More clean OR cleaner, never more cleaner  
Amen, that's due to them  having respect for themselves. """

# Initialise lists
tokens = []
unmatchable = []

# Compile patterns for speedup
# token_pat = re.compile(r"""[\U0000263a-\U000e007f]|\b\d{1,3}%|(?:1)?0\/10|http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|\b\d{1}\b|(?<!#)\b[A-Z]\w+\s[A-Z]\p{Ll}\w*\b|w\/|w\/o|['"]\b\p{L}+\b(?:'\b\w+\b)?(?:-\b\w+\b)?['"]|@?#?\b\p{L}+\d*\b(?:'\b\w+\b)?(?:-\b\w+\b)?""")
token_pat = re.compile(r"""http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+|www\.\w+\.\w{3}|[012]?[0-9](?:(?::[0-6]{2})|(?:[AP]M))+|#?\b[12]\d{3}\b|[6-9]0'?s|[\U0000263a-\U000e007f]|\b\d{1,3}%|(?:1)?0\/10|(?<![!\-:/])\b\d{1}\b(?![!\-:/])|(?<!#)\b[A-Z]\w+\s[A-Z]\p{L}\w*\b|w\/|w\/o|['"]\b\p{L}+\b(?:'\b\w+\b)?(?:-\b\w+\b)?['"]|@?#?\b\p{L}+\d*\b(?:'\b\w+\b)?(?:-(?!http)\b\w+\b)?""")

# skippable_pat = re.compile(r'[\.!?]+')  # typically spaces
skippable_pat = re.compile(r'\s+')

# As long as there's any material left...
while line:
    # Try finding a skippable token delimiter first.
    skippable_match = re.search(skippable_pat, line)
    if skippable_match and skippable_match.start() == 0:
        # If there is one at the beginning of the line, just skip it.
        line = line[skippable_match.end():]
    else:
        # Else try finding a real token.
        token_match = re.search(token_pat, line)
        if token_match and token_match.start() == 0:
            # If there is one at the beginning of the line, tokenise it.
            tokens.append(line[:token_match.end()])
            line = line[token_match.end():]
        else:
            # Else there is unmatchable material here.
            # It ends where a skippable or token match starts, or at the end of the line.
            unmatchable_end = len(line)
            if skippable_match:
                unmatchable_end = skippable_match.start()
            if token_match:
                unmatchable_end = min(unmatchable_end, token_match.start())
            # Add it to unmatchable and discard from line.
            unmatchable.append(line[:unmatchable_end])
            line = line[unmatchable_end:]
# tokens = re.findall(token_pat, line)
# unmatchable = re.findall(skippable_pat, line)

print(tokens)
print(unmatchable)