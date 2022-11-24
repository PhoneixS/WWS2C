<style>
  @media print { 
    .phb { 
      height: 279.4mm;
      width: 215.9mm;
    }
    /*.phb {
        width: 8.75in;
        height: 11.25in;
        padding: .518in .794in .715in .794in;
        }
    .phb::after {
        margin-bottom:0.125in;
    }
    .pageNumber.auto {
        right: 0.145in;
        bottom:0.355in;
    }
    .phb:nth-child(even) .pageNumber {
        left: 0.145in;
    }
    .phb .footnote {
        bottom:0.515in;
    }*/
   } 
.cover-footer, .cover-header { text-shadow:3px 3px 3px #000, -3px 3px 3px #000, 3px -3px 3px #000, -3px -3px 3px #000, 0px 3px 3px #000, 0px -3px 3px #000, 3px 0px 3px #000, -3px 0px 3px #000 !important }
.cover-initial{ font-family: NodestoCaps,nodesto,sans-serif; font-size:200%; position:relative; text-shadow:1px 3px 3px #000, -3px 3px 3px #000, 1px -3px 3px #000, -3px -3px 3px #000, 0px 3px 3px #000, 0px -3px 3px #000, 1px 0px 3px #000, -3px 0px 3px #000 !important}
.phb#p1{ text-align:center; } .phb#p1:after{ display:none; }
.toc a {color: inherit !important;	/*toc specifically wants black text. Th ftft sees resets the headers*/}
.toc li span:nth-child(2){ /*Allow dot leaders to fill remaining space but not overlap*/
 width: auto; overflow: hidden; white-space: nowrap; display: block;}
.toc li span:nth-child(2):after{
 font-family: BookSanity; /*Remove any header styles from dot leaders*/
 font-size: 0.317cm; font-weight: normal; color: black; content:" ........................................" "........................................." ".........................................";}
.toc li span:first-child{ /*Remove any header styles from page numbers*/
 float: right; font-family: BookSanity; font-size: 0.317cm; font-weight: normal; color: black; margin-left: 1px; /*Leaves a small space between page numbers and dot leaders*/}
/*Special cases for headings*/ 
.toc li h3 span:nth-child(2):after{content: " ";/*Remove dot leaders on h3*/}
.toc li h3 {margin-bottom: 4px !important;	/*Special spacing for h3*/
 margin-top: 10px !important; line-height: initial !important; /*For some reason Multi-line h3 line spacing changed*/}
.toc li h3 span:first-child{line-height: 1.8em !important; 	/*Line page numbers up with Multi-line h3 better*/}
.toc li h5 span:first-child{font-size:14px; font-weight:bold; line-height: 1.3em !important; 	/*Line page numbers up with h5 better*/}
.toc ul ul {margin-left: 10px !important; /*Original lists intented too much*/}
.toc>ul>li {margin-bottom: initial !important; /*margin for list items needs to be removed or 0*/}
ul a.custom-internal-link {color:#000; text-decoration: none;}
ul a.custom-internal-link:hover, h4 a.custom-internal-link:hover {text-decoration: underline;}
h4 a.custom-internal-link {color: #58180D; text-decoration: none;}

/* Print Friendly
  .phb, .phb hr+section blockquote { background-image:none !important; background-color:#fff !important; }
  .phb table tbody tr:nth-child(odd), .phb blockquote { background-image:none !important; background-color:#ecefe3;}
  .phb .bgwatercolor {filter:brightness(2000%) !important; }*/</style>

<img src='https://www.gmbinder.com/images/y5YSKWi.jpg' class='cover-image' style='width:inherit; height:105%; top:-50px; left:-170px;' />
<div class='cover-header' style='text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 0px 2px 2px #000, 0px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000 !important; font-size:18px;'>Wands & Wizards</div>
<div class='cover-header' style='text-shadow:3px 3px 3px #000, -3px 3px 3px #000, 3px -3px 3px #000, -3px -3px 3px #000, 0px 3px 3px #000, 0px -3px 3px #000, 3px 0px 3px #000, -3px 0px 3px #000 !important; margin-top:40px;'>W.A.N.D.S. Rulebook</div>
<div class='cover-diamond' style='margin-top:40px;'></div>
<div class='cover-footer' style='top: 175px;font-weight: 600;text-shadow:3px 3px 3px #000, -3px 3px 3px #000, 3px -3px 3px #000, -3px -3px 3px #000, 0px 3px 3px #000, 0px -3px 3px #000, 3px 0px 3px #000, -3px 0px 3px #000 !important;'>A Harry Potter 5e Adaptation</div>
<div class='cover-splotch' style='bottom: 750px !important;'></div>
<div class='wide' style='position: absolute; top: 945px; left: 60px; right: 60px; color:white; text-shadow:2px 2px 4px #000, -2px 2px 4px #000, 2px -2px 4px #000, -2px -2px 4px #000, 0px 2px 4px #000, 0px -2px 4px #000, 2px 0px 4px #000, -2px 0px 4px #000 !important;'>

Wands & Wizards is unofficial Fan Content permitted under the Fan Content Policy. Not approved/endorsed by Wizards. Portions of the materials used are property of Wizards of the Coast. ©Wizards of the Coast LLC. Not approved/endorsed by J.K. Rowling or Warner Bros. Entertainment Inc. Portions of the materials used are property of J.K. Rowling or Warner Bros. Entertainment Inc. 
___
This document was created solely for private use. All rights are retained by the owners of trademarks and copyrights of the content within this document. This document, in part or whole, cannot be reproduced for the intent of retail sale or personal gain except by those said interested parties or by others with legal, written consent by said parties.</div>

\pagebreak

<div class='wide' style="text-align: center">

### 
# Contents
###
</div>

<div class='toc' style="margin-top:30px;">

- ### [<span>3</span><span>Introduction</span>](#p3)
  - - [<span>3</span><span>Differences from 5e</span>](#p3)
  - - [<span>3</span><span>Levels and Hogwarts Years</span>](#p3)
- ### [<span>4</span><span>Part 1</span>](#p4)
- - ##### [<span>4</span><span>Chapter 1: Houses</span>](#p4)
  - - [<span>4</span><span>Hogwarts Houses</span>](#p4)
  - - [<span>6</span><span>Beauxbatons and Durmstrang</span>](#p6)
  - - [<span>7</span><span>Ilvermorny Houses</span>](#p7)
- - ##### [<span>9</span><span>Chapter 2: Casting Styles</span>](#p9)
  - - [<span>10</span><span>Base Sorcerer Features</span>](#p10)
  - - [<span>11</span><span>The Willpower Caster</span>](#p11)
  - - [<span>13</span><span>The Technique Caster</span>](#p13)
  - - [<span>15</span><span>The Intellect Caster</span>](#p15)
- - ##### [<span>17</span><span>Chapter 3: Schools of Magic</span>](#p17)
  - - [<span>17</span><span>Charms</span>](#p17)
  - - [<span>18</span><span>Jinxes, Hexes, and Curses</span>](#p18)
  - - [<span>19</span><span>Transfiguration</span>](#p19)
  - - [<span>22</span><span>Healing</span>](#p22)
  - - [<span>23</span><span>Divination</span>](#p23)
  - - [<span>25</span><span>Magizoology</span>](#p25)
- - ##### [<span>27</span><span>Chapter 4: Wands</span>](#p27)
  - - [<span>27</span><span>Wand Components</span>](#p27)
  - - [<span>28</span><span>Backgrounds</span>](#p28)
- - ##### [<span>39</span><span>Chapter 5: Wizarding Equipment</span>](#p39)
  - - [<span>39</span><span>Starting Equipment</span>](#p39)
  - - [<span>39</span><span>Tools</span>](#p39)
  - - [<span>40</span><span>Wealth</span>](#p40)
  - - [<span>40</span><span>Cloaks</span>](#p40)
  - - [<span>40</span><span>Wizarding Gear</span>](#p40)
  - - [<span>41</span><span>Potions</span>](#p41)
  - - [<span>49</span><span>Magical Pets</span>](#p49)
- - ##### [<span>53</span><span>Chapter 6: Wizarding Feats</span>](#p53)
  - - [<span>53</span><span>Innate Feats</span>](#p53)
  - - [<span>54</span><span>Standard Feats</span>](#p54)
- - ##### [<span>56</span><span>Chapter 7: Wizarding Skills</span>](#p56)
- - ##### [<span>57</span><span>Chapter 8: Dark Magic Corruption</span>](#p57)
- ### [<span>59</span><span>Part 2</span>](#p59)
- - ##### [<span>59</span><span>Chapter 9: Spells</span>](#p59)
  - - [<span>59</span><span>Spellcasting</span>](#p59)
  - - [<span>61</span><span>Unique Spells</span>](#p61)
  - - [<span>63</span><span>Spell Conversions</span>](#p63)
  - - [<span>65</span><span>Spell List</span>](#p65)
  - - [<span>66</span><span>Spell Descriptions</span>](#p66)
</div>

\columnbreak

<div class='toc' style="margin-top:35px;">

- - ##### [<span>89</span><span>Appendices</span>](#p89)
  - - [<span>89</span><span>Appendix A: Potion Brewing</span>](#p89)
  - - [<span>93</span><span>Appendix B: Patronus Rolling Tables</span>](#p93)
  - - [<span>99</span><span>Appendix C: Chocolate Frog Cards</span>](#p99)
- - ##### [<span>116</span><span>Glossary</span>](#p116)
</div>

<div style='padding-top:15px;'></div>

> ##### Credits - Created by u/Murphen44
> Version 1.4, published on 7/11/2022
>
> <a href="https://www.reddit.com/r/WandsAndWizards/" target="_blank">r/WandsAndWizards</a> - <a href="https://discord.gg/zcmbyMt" target="_blank">Discord Server</a>
> ___
> ##### Excerpts from 
> * <a href="https://www.wizardingworld.com/writing-by-jk-rowling" target="_blank">Writings by J.K. Rowling</a>
> * <a href="https://sortinghatchats.tumblr.com/" target="_blank">Sorting Hat Chats</a>
> * <a href="https://harrypotter.fandom.com/wiki/Main_Page" target="_blank">Harry Potter Fandom Wiki</a>
> * <a href="https://harrypotter.bloomsbury.com/uk/fun-stuff/glossary/" target="_blank">Bloomsbury Harry Potter Glossary</a>
> ___
> ##### Artwork by 
> * <a href="https://atomhawk.com/" target="_blank">Atomhawk</a>/<a href="https://www.wizardingworld.com/" target="_blank">Pottermore</a>
> * Even Amundsen - <a href="https://www.instagram.com/evenmehlamundsen/" target="_blank">IG</a> - <a href="https://twitter.com/evenmamundsen" target="_blank">Twitter</a> - <a href="https://www.artstation.com/mischeviouslittleelf" target="_blank">ArtStation</a>
> * Frida Lundqvist - <a href="https://www.instagram.com/fridouw/" target="_blank">IG</a> - <a href="https://twitter.com/fridouw" target="_blank">Twitter</a>
> * Gergely Gizella - <a href="https://www.instagram.com/gergelygizella/" target="_blank">IG</a> - <a href="https://twitter.com/logartis" target="_blank">Twitter</a> - <a href="https://www.logartis.info/" target="_blank">Behance</a>
> * Jeff Brown - <a href="https://www.deviantart.com/jbrown67" target="_blank">DeviantArt</a> - <a href="http://jeffbrowngraphics.com/" target="_blank">Website</a>
> * Raph Lomotan - <a href="https://www.deviantart.com/raphtor" target="_blank">DeviantArt</a> - <a href="https://www.artstation.com/raphlomotan" target="_blank">ArtStation</a>
> * UptheHill Art - <a href="https://www.instagram.com/upthehillart/" target="_blank">IG</a> - <a href="https://upthehillart.tumblr.com/" target="_blank">Tumblr</a> - <a href="https://www.deviantart.com/upthehillart" target="_blank">DeviantArt</a>
> ___
> ##### Special Thanks to
> * Everyone who's encouraged me and joined the Wands & Wizards subreddit and Discord
> * Everyone at the Discord of Many Things
> * Aughts / u/aughts for wand backgrounds
> * Blake / u/Rain-Junkie for dragon stat blocks
> * CaelReader / u/CaelReader for Houses as Races
> * Carric#4730 for animagus forms
> * DCixen / u/tharian83 for Ilvermorny Houses
> * Entrench / u/devikyn for Adaptive Ranger's beast companion rules
> * Izzy for feedback and class guidance
> * Jay / u/CKSalamander for chocolate frog cards
> * Jared Ondricek / u/flamableconcrete for image watercolor stains
> * Jeff Venancio / u/Hageshii01 for apparition, *expecto patronum* and more spells
> * MadManNBlueBox for starting equipment and background equipment
> * Matt Mercer for Corruption Rules (Dark Magic), and Dezidério for telling me about them
>
> Made using <a href="https://www.gmbinder.com/" target="_blank">GMBinder</a>.

\pagebreak
# Introduction
If you are a fan of both Dungeons & Dragons and Harry Potter, I present to you Wands & Wizards, a Harry Potter 5e Adaptation. Joining the magic of the Wizarding World with the gameplay of D&D 5e, this comprehensive Wizarding Alternative for Novelty Dungeoneering Stories (or W.A.N.D.S.) Rulebook substitutes 5e races, classes, subclasses, backgrounds, feats, skills, equipment, and spells. Like the 5e PHB, Part 1 of the W.A.N.D.S. Rulebook contains new character creation options. Part 2 focuses on the changes made to spellcasting and all of the new spells from the Harry Potter series. If you are unfamiliar with any of the Harry Potter references, please review the Glossary at the end of the W.A.N.D.S. Rulebook.

## Differences from 5e
While all the core mechanics and rules of D&D still apply, all the character creation options have been replaced. None of 5e's default character options are available in W&W: no races, classes, backgrounds, feats, or equipment are compatible (unless specifically noted, like a handful of feats). The process of character creation remains unchanged, so you need only progress through the W.A.N.D.S. Rulebook sequentially, just like you would with the PHB. Below is a table that converts the 5e terminology into W&W terminology.

<div class='classTable' style="margin-top:50px;">

##### Character Creation Conversion Table
| 5e                 | W&W             |
|:------------------:|:---------------:|
| Race               | House           |
| Class              | Casting Style   |
| Subclass or Archetype | School of Magic |
| Background         | Wand or Background |
</div>

Aside from character creation, there have been a few other changes to the system. Firstly, some skills have been added, removed, or replaced to better represent the skills used in the wizarding word. The skill conversion table can be found on page 40, which outlines how old 5e skills correspond with W&W skills. These are not simply renamings; new W&W skills can have different definitions and applications. 

Most importantly, you will not be using the normal 5e spell lists. You will only use the spells in this rulebook, but quite a few 5e spells have been renamed or slightly modified. If a 5e spell has been included in W&W, it will be shown in the spell conversion tables on pages 45 and 46.

\columnbreak
### A Harry Potter Spellcaster
For character classes, you'll see three different casting styles. Although these represent three different classes, all three are built on the chassis of the 5e Sorcerer. Additionally, because they're all the same class at their core, they all have the same spell list. In W&W, everyone has access to the same spells (with some clear exceptions).
### The Role of the HM
HM stands for Headmaster or Headmistress, which is used specifically to represent the Game Master running the game of W&W. That abbreviation is used throughout the document to refer to this person, whereas the term "headmaster" will mean the head professor of Hogwarts.
## Levels and Hogwarts Years
A character’s early levels can be associated with the magical abilities acquired through different years of school. Levels 1-2 correspond to average first-year students, just being introduced to schools of magic. Level 3 is second year and level 4 is third year, and at this point, they have learned to exercise some control over their magic. The threats they face are relatively minor, usually only posing a danger to other children or small villages. 

Level 5 will typically be covered in the fourth year. Fifth-year students are levels 6-7, while sixth-year students are levels 8-9. This is when young witches and wizards really come into their own, learning powerful spells and abilities from their school of magic and becoming capable of facing dangers that threaten adult wizards. 

Seventh year students are level 10 while Hogwarts graduates and the majority of adult wizards are levels 11-12. Only well-practiced wizards reach levels 13-16, like Aurors, Hogwarts teachers and members of the Order of the Phoenix (back in the Second Wizarding War). These characters have reached a level of power that makes them special even among wizards, confronting threats to whole regions or wizard academies. 

At levels 17-20, characters achieve the pinnacle of their school of magic’s features, becoming heroic (or villainous) archetypes in their own right. The fate of magical governments or even the entire muggle world might hang in the balance during their adventures.
<div class='footnote'>Introduction</div>

\pagebreakNum
# Chapter 1: Houses (Races)
Hogwarts students are divided up into four houses by the Sorting Hat when they first arrive at Hogwarts. Houses at Hogwarts are both the living and learning communities for its students. Each year's group of students in the same house shares their dormitory and many classes, acting as a sort of family. The houses compete by earning points for the House Cup and playing for the Inter-House Quidditch Cup.

Each house has stereotypical traits that are grounded in reality, but students are quite diverse. Some young witches and wizards share traits with another house, like Hermione Granger's Ravenclaw-like brilliance. Others might appear the exact opposite of their house, like Neville Longbottom's lack of confidence (needing time to grow into bravery) or Luna Lovegood's ostensible disconnection from facts (keeping a creative, open mind and being perceptive). The Sorting Hat places students in the house that will benefit them the most.

The way you decide your character's house is not always by what they do, but what would make them proudest if they were strong enough to do it. Your sorting is what you want to be and what you believe in.

<img src="https://vignette.wikia.nocookie.net/harrypotter/images/b/b1/Gryffindor_ClearBG.png/revision/latest?cb=20190222162949" style="width:200px; margin: -12px -20px -30px 0; float:right;" />

## Gryffindor
With a lion as its crest, Gryffindor is the house which most values the virtues of determination, courage, and chivalry. Some call these traits recklessness or "pointless heroics," but a Gryffindor is sure to take action. Gryffindor's house colors are red and gold.
### Champions of Justice
Gryffindors trust their moral intuitions and have a need and a drive to live by them. They feel what’s right in their gut, and that matters and guides them. It feels immoral to ignore that.

However, just because they operate on what “feels right,” that doesn’t mean Gryffindors are all impetuous, emotional hellions. Gryffindors can still be intelligent and deliberate, weighing their decisions and moralities carefully.
### Fighting Spirit
Gryffindors charge. They meet the world head-on and challenge it to do its worst. Gryffindors are honest, brash, and bold in pursuit of things they care about. Known for their bravery, it is almost a moral matter to stay true to themselves in any situation.
### Gryffindor Traits
Through their camaraderie, Gryffindors bolster each other's confidence and endeavors.

**Ability Score Increase.** Your Constitution score, Charisma score, and one other ability score of choice increase by 1.

**Bravehearted.** You have advantage on saving throws against being frightened from any source other than a Dementor.

**True Gryffindor.** In times of dire need, the Sword of Gryffindor may present itself to you.

**Feat.** You gain one feat of your choice.

<img src="https://vignette.wikia.nocookie.net/harrypotter/images/0/06/Hufflepuff_ClearBG.png/revision/latest?cb=20161020182518" style="width:200px; margin: -10px -50px 0px 10px; float:right;" />

## Hufflepuff
Hufflepuffs value hard work, patience, loyalty, and fair play, represented by the sturdy badger. Although often disparaged by others for their lack of competitiveness, the house has produced great wizards – not least Newt Scamander, notable magizoologist and author. Hufflepuff's house colors are yellow and black.
### Compassion and Empathy
Hufflepuffs value people and community. They base their decisions on who is in need and who they can help. They value fairness because everyone is a person. Even directly wronged, Hufflepuffs will often give a second (or fifth) chance.

But Hufflepuffs aren't inherently tolerant, like Gryffindors aren't inherently moral. They believe that all people deserve some type of kindness or decency, but they can redefine "person" to exclude anyone who doesn't meet their standards.
### Hard Workers
Hufflepuffs toil. Their strength comes from consistency and the integrity of their method. They have a certain steadiness, naturally becoming the lynchpin of a community. While stereotyped as being social, a Hufflepuff might also be an introverted misanthrope who runs on hard work alone.
### Hufflepuff Traits
You can rely on them to have certain attributes in common.

**Ability Score Increase.** Your Constitution score, Wisdom score, and one other ability score of choice increase by 1.

**Steadfast Loyalty.** You have advantage on saving throws against any effect that would make you attack or work against a creature you would normally consider an ally.


**Kitchen Trips.** Your experience with the Hogwarts house elves has taught you how to politely address and interact with magical beings. Oh, and you can get tons of snacks.

**Feat.** You gain one feat of your choice.
<div class='footnote'>Part 1 | Houses (Races)</div>

\pagebreakNum

<img src="https://static.wikia.nocookie.net/harrypotter/images/7/71/Ravenclaw_ClearBG.png" style="width:200px; margin: 0px -20px 0px -35px; float:left;" />

##     Ravenclaw
           Ravenclaws prize wit,                learning, and wisdom.              It's an ethos etched into           founder Rowena         Ravenclaw's diadem: 'wit       beyond measure is man's            greatest treasure.' Despite          the house's reputation for      eccentricity and reclusiveness,    Ravenclaws tend to make their  mark on the world. Ravenclaw's house colors are blue and bronze.
### A Systematic Mind
Ravenclaws construct systems to test their decisions against before they feel comfortable calling something right. Their systems give them a way to frame the world and a confidence in their ability to interact with it.

Ravenclaws do not lack intuition, but often distrust gut instinct. Although they go about it differently, a Ravenclaw can be just as morally motivated as a Gryffindor.
### Contingency Planners
Ravenclaws plan. They collect information, they strategize. They have tools. They run hypotheticals and try to plan ahead for things that might come up. They build things (of varying degrees of actual usefulness) that they can use later, whether that’s an emergency supply pack or vast knowledge in a niche topic. They feel less at home in improvisation and more comfortable taking the time to be prepared.

### Ravenclaw Traits
With a library in their common room, Ravenclaws will always share studious habits.

**Ability Score Increase.** Your Intelligence score, Wisdom score, and one other ability score of choice increase by 1.

**In-Depth Knowledge.** Whenever you make an Intelligence or Wisdom ability check that lets you add your proficiency bonus, you can treat a d20 roll of 5 or lower as a 6.

**Rowena's Library.** You can easily research a desired topic through enlisting your housemates' help and browsing books exclusively found in the Ravenclaw common room.

**Feat.** You gain one feat of your choice.

<!--<img src="https://www.gmbinder.com/images/5PSCQzJ.png" class="cover-image bgwatercolor" style="width:107%;top:-10px;filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/oF4JQBz.png" class="cover-image bgwatercolor" style="width:120%;top:430px;left:-20px; transform:scaleX(-1) scaleY(-1) rotate(10deg); filter:brightness(94%) sepia(15%)">-->

\columnbreak


## Slytherin
Slytherin produces more than its share of Dark wizards, but also turns out leaders who are proud, ambitious, resourceful, and cunning. Merlin is one particularly famous Slytherin. What others may call cheating or manipulation, a Slytherin calls "playing the game." Slytherin's house colors are green and silver.
### Inner Circle
Slytherins are fiercely loyal to the people they care for most. Slytherin is the place where "you’ll make your real friends"; they prioritize individual loyalties and find their moral core in protecting and caring for the people they are closest to.

Slytherin’s reputation for ambition comes from prioritizing themselves and the select people they deem important. Ambition is something you can find in all four houses, but Slytherin’s looks most obviously selfish.
### Machiavellian Maneuvers

<img src="https://vignette.wikia.nocookie.net/harrypotter/images/0/00/Slytherin_ClearBG.png/revision/latest?cb=20161020182557" style="width:200px; margin: 10px -45px 0 -30px; float:left;" />

Slytherins improvise. They are the        most adaptive, finding their            strength in responding quickly                  to whatever a situation                        throws at them. They                      improvise differently                    than Gryffindors, trying                  new angles instead of                  strong-arming the situation.                  They might have different                    "faces" for different                  situations, only truly being                themselves when they’re            finally alone or feeling safe.

</br>

### Slytherin Traits
Although Slytherins like to keep their secrets, there are some obvious traits they all have.

**Ability Score Increase.** Your Dexterity score, Charisma score, and one other ability score of choice increase by 1.

**Compromising Information.** Whenever you make a Charisma check related to using a person's secrets, you are considered proficient in the appropriate skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus.

**A Noble Quality.** You're able to adopt a persona of importance to blend in among high-ranking officials and prestigious witches and wizards.

**Feat.** You gain one feat of your choice.
<div class='footnote'>Part 1 | Houses (Races)</div>

\pagebreakNum


<img src="https://vignette.wikia.nocookie.net/harrypotter/images/e/ea/BeauxbatonsCrestClearBg.png/revision/latest?cb=20160630041801" style="width:240px; margin: -35px -20px 0 -95px; float:left;" />

## Beauxbatons
Located in the mountains of France, the Académie de Magie Beauxbâtons or Beauxbatons Academy of Magic is       the choice of magical education             for young witches and wizards            living in Western, Southern,         and sometimes even Central       Europe. For wizards in the UK,     Beauxbatons is most notable for its   friendly rivalry to Hogwarts, and the       two schools have often supported        each other throughout history.       Beauxbatons is widely recognized    for the elegance of its castle, its majestic gardens and its well-prepared cuisine.
### Tradition and Discipline
Etiquette and respect are at the forefront of Beauxbatons customs. The students stand at attention whenever their headmaster or headmistress enters a room and continue doing so until they take a seat or order everyone to return to their tasks.

There is a strong atmosphere of school pride, and the Academy's traditions are treasured by staff and students alike. While taught to be polite, that pride often shows through when students of Beauxbatons travel abroad.
### A Delicate Approach to Magic
Beauxbatons Academy of Magic teaches its students to approach magic with control and finesse, instead of clumsiness or brute force. The studies revolve around proper dueling forms, taxonomies and knowledge deeply grounded in magical theory.

To an untrained eye, the deliberate movements of Beauxbatons duelists might resemble a choreographed dance, but it's closer to the precision, quickness and lethality of Muggle fencing.
### Beauxbatons Student Traits
The traits of Beauxbatons students originate from their school's dueling style and from their travels abroad.

**Ability Score Increase.** Your Dexterity score, Wisdom score, and one other ability score of choice increase by 1.

**Nimble Evasion.** Whenever you take the dodge action, add half your proficiency bonus to your AC and your Dexterity saving throws.

**Exchange Student.** You're familiar with the workings of the International Confederation of Wizards and other international associations.

**Feat.** You gain one feat of your choice.

\columnbreak

## Durmstrang
Even among the magical community, the Durmstang Institute's location is a closely guarded secret, a symptom of the magical school's distrust of outsiders. Some believe it to be somewhere in the Nordic countries or Russia, but the only thing that's certain is that it accepts students from Northern, Central and Eastern European countries. Historically, Durmstrang has also refused to accept Muggleborn students, although that might be attributed to a previous headmaster's association with Britain's Death Eaters. Its modern policies are unknown.
### Unorthodox Curriculum
Durmstrang is notorious for its acceptance of the Dark Arts, and was known to have educated (and later expelled) Gellert Grindelwald before his ascension as one of history's most dangerous Dark wizards. 

Contrary to its reputation, Durmstrang doesn't specialize in the Dark Arts themselves, but in combative magic. The school is simply open-minded about the use of Dark Arts, and so most topics studied at Durmstrang incorporate Dark elements other schools would forswear.
### Strength Through Hardship
The stern and militaristic culture that has pervaded the Durmstrang Institute is mirrored in its harsh surroundings. Brutal winters, rigorous physical exercise regimens and swimming in ice cold lakes are all part of the character-building school experience.

Although some parents feel the approach is too extreme, everything is designed to produce resilient and resourceful wizards and witches who will survive any combat.
### Durmstrang Student Traits
The Durmstrang coursework and philosophy strongly define its students' attributes.

<img src="https://vignette.wikia.nocookie.net/harrypotter/images/f/f3/DurmstrangCrest.png/revision/latest?cb=20160112161151" style="width:230px; margin: -14px -50px 0 -100px; float:right;" />

**Ability Score Increase.** </br>Your Strength score, </br>Constitution score, and </br>one other ability score of </br>choice increase by 1.

**Cold Efficiency.** You </br>add the *bombarda* spell </br>to your list of known spells. </br>It does not count against </br>your cantrips known, and </br>cannot be forgotten to learn </br>another cantrip.

**Dark Education.** You have </br>advantage on any rolls made to </br>resist gaining Corruption effects </br>from Dark magic. 

**Feat.** You gain one feat of your choice.
<div class='footnote'>Part 1 | Houses (Races)</div>

\pagebreakNum

<div style="margin: -34px 0px 470px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
© Wizarding World Digital
</div>


<img src="https://static.wikia.nocookie.net/harrypotter/images/3/3f/Horned_Serpent_ClearBG_2.png" style="width:220px; margin: -175px -62px 0 -25px;float:right;" />

## Horned Serpent (Ilvermorny)
Horned Serpent is the house of scholars. Isolt Sayre, the founder of Ilvermorny, named her house for her friendship with a horned serpent and her ability to understand Parseltongue. Horned Serpent represents the mind of the wizard, since Isolt's passion for learning has been preserved in Horned Serpent.
### Natural Academics
Because of Horned Serpent's reputation for studiousness, parallels are often drawn with the Ravenclaw house at Hogwarts, but Hogwarts and Ilvermorny houses are not equivalent to each other. 

While it would be common to find a Horned Serpent student at the top of their class, you're just as likely to find them heading out to obtain first-hand practical experience. A certain appreciation of nature is another notable trait of Horned Serpent.
### Horned Serpent Traits
Horned Serpents consistently like to test their well-rounded intellect.

**Ability Score Increase.** Your Intelligence score, Charisma score, and one other ability score of choice increase by 1.

**Scholar's Mind.** You add half your proficiency bonus to any Intelligence or Wisdom ability check you make that doesn't already include your proficiency bonus.

\columnbreak
<div style='margin-top: 460px;'></div>

**Procedural Thinking.** You enjoy testing yourself with riddles and logic puzzles. If you get stuck on one, you might subconsciously connect a few dots. 

**Feat.** You gain one feat </br>of your choice.

<img src="https://static.wikia.nocookie.net/harrypotter/images/e/e6/Wampus_ClearBG_2.png" style="width:220px; margin: -35px -60px 0px -50px;float:right;" />

## Wampus (Ilvermorny)
The house represents the </br>body of the wizard. Wampus</br> was chosen by Webster Boot, </br>one of the first students of </br>Ilvermorny and one of Isolt </br>Sayre's adopted children. </br>Wampus favors warriors, taking after Webster's career in the British colonies as a prominent "Auror for hire."
### Warriors at Heart
Wampus is named after the wampus cat, an extremely dangerous magical creature found in America. The wampus cat is XXXXX classified by the Ministry of Magic: "Known wizard killer / impossible to train or domesticate," which is fitting for the Ilvermorny house's reputation.

Wampuses rarely back down from a fight, whether it's in the form of an argument, fisticuffs or exchanged hexes. They place great value on swift action and self-defense. Fiercely loyal too, a Wampus is a good person to have on your side and terrible to have against you.

<img src="https://www.gmbinder.com/images/oeyDliA.jpg" class="cover-image" style="width:140%; height:400%; top:inherit; bottom:620px; left:-200px;"><img src="https://www.gmbinder.com/images/oeyDliA.jpg" class="cover-image" style=" top:0px; left:-5px;"><img src="https://watercolors.giantsoup.com/phb/phb_top/0011.png" class="cover-image bgwatercolor" style="width:100%; top:-350px; transform:scaleX(1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/WQXIOUB.png" class="cover-image bgwatercolor" style="width:100%; top:10px; filter:brightness(94%) sepia(15%)">

<div class='footnote'>Part 1 | Houses (Races)</div>

\pagebreakNum
### Wampus Traits
Wampuses' traits can be very useful in times of conflict and turmoil.

**Ability Score Increase.** Your Dexterity score, Constitution score, and one other ability score of choice increase by 1.

**Warrior's Endurance.** When you roll a 16 or higher on a death saving throw, you instantly regain 1 hit point. You can't use this feature again until you finish a long rest.

**Contagious Valor.** Your moxie can be inspiring, and those around you feel more inclined to accompany you into battle against your foes.

**Feat.** You gain one feat of your choice.

## Thunderbird (Ilvermorny)
Thunderbird is said to represent the soul of the wizard and is home to adventurers. The house was named and created by Chadwick Boot, Webster Boot's older brother, Isolt Sayre's other adopted son, and one of the first students of Ilvermorny. The Thunderbird house has been associated with Chadwick's later accomplishments as an international traveller and author of magical textbooks.
### Discovery and Creation
The house is named after the awe-inspiring thunderbird, whose natural habitat is in southwestern United States. Thanks to its ability to create storms and its wide-ranging travels around North America, it's the most widely known magical creatures among indigenous No-Maj communities. Thunderbird students similarly feel a yearning to venture beyond the ordinary. 

That desire can be expressed <br/>through literal or conceptual <br/>exploration, as Thunderbirds <br/>are just as likely to <br/>forge new paths in <br/>their chosen field as <br/>forge new paths through <br/>the untamed wilderness. <br/>Wherever they go, they'll <br/>go boldy.

<img src="https://static.wikia.nocookie.net/harrypotter/images/1/1a/Thundebird_ClearBG_2.png" style="width:295px; margin: -167px -95px -5px -67px;float:right;" />

### Thunderbird Traits
One thing that's a constant for all Thunderbirds is change.

**Ability Score Increase.** Your Strength <br/>score, Charisma score, and one other ability score of choice increase by 1.

**Adventurer's Footing.** Moving through nonmagical difficult terrain costs you no extra movement.

**Dependable Bearings.** You have a good sense of direction and can easily use notable landmarks and geography to remember the general layout of areas. 

**Feat.** You gain one feat of your choice.

\columnbreak

<img src="https://static.wikia.nocookie.net/harrypotter/images/a/a5/Pukwudgie_ClearBG_2.png" style="width:230px; margin: -2px -55px 0 -40px;float:right;" />


## Pukwudgie (Ilvermorny)
The Pukwudgie house <br/>represents the heart of the <br/>wizard, and is commonly <br/>associated with healers. <br/>This house was named by <br/>James Steward, famous <br/>for being the co-founder of Ilvermorny, husband of Isolt <br/>Sayre, adoptive father of Chadwick and Webster Boot and the only known no-maj wandmaker.
### Supportive and Self-Sufficient
James chose this house because a pukwudgie named William had accompanied Isolt. A mix between European goblins and house-elves in both appearance and magical capabilities, pukwudgies are traditionally aloof from human-kind. William later saved the lives of Isolt, James, and the Boots, and because of the respect showed by James, William and his descendants became Ilvermorny's guards and caretakers.

Students of the Pukwudgie house are often quite caring and compassionate. They easily empathize, even with an enemy, and enjoy seeing others achieve their goals. However, Pukwudgies are just as capable of taking care of themselves and won't forget to prioritize their own happiness.
### Pukwudgie Traits
Pukwudgies' perspective gives them common attributes.

**Ability Score Increase.** Your Wisdom score, Charisma         score, and one other ability score of choice increase by 1.

                        **Healer's Knack.** Whenever you make a                         Wisdom (Medicine) check to stabilize a                         creature, add half your proficiency bonus to                         your roll.

            **A Diplomatic Touch.** If you assist a hostile being in             a meaningful way, they're more likely to reconsider             their hostility towards you, potentially defusing the             situation.

            **Feat.** You gain one feat of your choice.


<div class='footnote'>Part 1 | Houses (Races)</div>

\pagebreakNum
# Chapter 2: Casting Styles (Classes)
While any wizard can cast a wide variety of spells, a young wizard's approach to magic defines his own unique casting style. Casting styles separate wizards and affect how they learn and use magic. The three available casting styles to choose from are Willpower, Technique, and Intellect. A wizard can only have one casting style and cannot multiclass or gain levels in any other casting styles.

Casting styles are the wizarding equivalent of classes. Casting style determines a character's Hit Dice, spellcasting ability score, saving throw proficiencies, and two skills. Although all wizards and witches are based what a Muggle would call a Sorcerer, each casting style will have slightly different class features, number of spells known, sorcery points, and metamagic progression.
<div class='classTable wide' style='margin:50px 0px 50px;'>

| Casting Style | <span style="color:white;">__</span> | Description | Hit Die | Primary Ability | Saving Throws | Skill Proficiency Options |
|:-------------:|:-| :------------|:-------:|:---------------:|:-------------------------:|:--------------------------|
| Willpower     | | An inspirational survivor, who </br>has a heart of a warrior | d10 | CHA          | CON </br>& CHA                 | Athletics, Deception, </br>Intimidation, Magical Theory, Persuasion, Sleight of Hand, Survival |
| Technique     | | A powerful specialist, with immense control over spells | d6 | WIS           | INT </br>& WIS | Acrobatics, Herbology, Insight, Perception, </br>Potion-Making, Sleight of Hand, Stealth |
| Intellect     | | A versatile academic, with a solution for every problem | d8 | INT           | DEX </br>& INT|                 Acrobatics, Herbology, Insight, Investigation, </br>Magical Creatures, Magical Theory, Medicine, Muggle Studies and Survival |
</div>

Similarly, a witch's interests and background will lead her to specialize in a particular school of magic (Chapter 3). Studying a school of magic grants special abilities and knowledge related to that favored branch of magic, typically connecting to a future wizarding profession. A witch can only have one school of magic and cannot gain levels in any other school of magic. Schools of magic are the wizarding equivalent of subclasses, but schools of magic are not restricted to certain casting styles.

A wizard of any casting style can study any school of magic, but some combinations will synergize particularly well. Each school of magic will have its own subclass features and some schools of magic have a list of spells — its school of magic spells — that you learn once you gain a spell slot of the level noted in the school of magic description. Once you gain a school of magic spell, it's added to your spells known, it doesn’t count against your number of spells known, and it cannot be forgotten to learn another spell.

<div class='classTable wide' style='margin:30px 0px;'>

| School of Magic | Description | Suggested Class |
|:---------------:|:------------|:---------------:|
| Charms          | A non-lethal dueling master casting a spell for</br>every situation and enchanting artifacts | Technique or Intellect |
| Jinxes, Hexes, and Curses | A combatant going toe-to-toe with Dark wizards</br>and nullifying ancient curses and harmful magic | Willpower |
| Transfiguration | An innovator manipulating the elements or</br>shapeshifting into an animal form | Technique |
| Healing         | A skilled professional saving lives through the</br>treatment of magical ailments and injuries | Willpower or Intellect |
| Divination      | A mystic unraveling visions of the future or</br>probing minds for the answers they seek | Willpower or Technique |
| Magizoology     | A researcher bonding with fearsome beasts and</br>facing off with dark creatures | Intellect |
</div>
<div class='footnote'>Part 1 | Casting Styles (Classes)</div>

\pagebreakNum

## Base Sorcerer Features
### Font of Magic
#### Sorcery Points
You can never have more sorcery points than shown on the table for your level. You regain all spent sorcery points when you finish a long rest.
#### Flexible Casting
You can use your sorcery points to gain additional spell slots, or sacrifice spell slots to gain additional sorcery points.

**Creating Spell Slots.** You can transform unexpended sorcery points into one spell slot as a bonus action on your turn. The created spell slots vanish at the end of a long rest.

| Slot Level | SP Cost | | Slot Level | SP Cost |
|:---:|:-:|:-:|:---:|:-:|
| 1st | 2 |   | 4th | 6 |
| 2nd | 3 |   | 5th | 7 |
| 3rd | 5 |

**Converting a Spell Slot to Sorcery Points.** As a bonus action on your turn, you can expend one spell slot and gain a number of sorcery points equal to the slot's level.

### Metamagic
You can use only one Metamagic option on a spell when you cast it, unless otherwise noted.
#### Careful Spell
When you cast a spell that forces other creatures to make a saving throw, you can protect some of those creatures from the spell’s full force. To do so, you spend 1 sorcery point and choose a number of those creatures up to your spellcasting ability modifier (minimum of one creature). A chosen creature automatically succeeds on its saving throw.
#### Distant Spell
When you cast a spell that has a range of 5 feet or greater, you can spend 1 sorcery point to double the spell's range.

When you cast a spell that has a range of touch, you can spend 1 sorcery point to make the range of the spell 30 feet.
#### Empowered Spell
When you roll a spell's damage, you can spend 1 sorcery point to reroll a number of damage dice up to your spellcasting ability modifier (minimum one). You must use the new rolls.

You can use Empowered Spell even if you have already used a different Metamagic option during the spell's casting.
#### Extended Spell
When you cast a spell that has a duration of 1 minute or longer, you can spend 1 sorcery point to double its duration, to a maximum duration of 24 hours.

\columnbreak

#### Heightened Spell
When you cast a spell that forces a creature to make a saving throw to resist its effects, you can spend 3 sorcery points to give one target of the spell disadvantage on its first saving throw made against the spell.
#### Quickened Spell
When you cast a spell that has a casting time of 1 action, you can spend 2 sorcery points to change the casting time to 1 Bonus Action for this casting.
#### Subtle Spell
When you cast a spell, you can spend 1 sorcery point to cast it without any somatic or verbal Components.
#### Twinned Spell
When you cast a spell that targets only one creature and doesn’t have a range of self, you can spend a number of sorcery points equal to the spell’s level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip).

<div class='classTable' style='margin-top:70px;'>

##### Spell Slots per Level
| Level | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th |
|:-----:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1st   | 2   | —   | —   | —   | —   | —   | —   | —   | — |
| 2nd   | 3   | ─   | —   | —   | —   | —   | —   | —   | — |
| 3rd   | 4   | 2   | ─   | ─   | ─   | —   | —   | —   | — |
| 4th   | 4   | 3   | —   | —   | —   | —   | —   | —   | — |
| 5th   | 4   | 3   | 2   | —   | —   | —   | —   | —   | — |
| 6th   | 4   | 3   | 3   | —   | —   | —   | —   | —   | — |
| 7th   | 4   | 3   | 3   | 1   | —   | —   | —   | —   | — |
| 8th   | 4   | 3   | 3   | 2   | —   | —   | —   | —   | — |
| 9th   | 4   | 3   | 3   | 3   | 1   | —   | —   | —   | — |
| 10th  | 4   | 3   | 3   | 3   | 2   | —   | —   | —   | — |
| 11th  | 4   | 3   | 3   | 3   | 2   | 1   | —   | —   | — |
| 12th  | 4   | 3   | 3   | 3   | 2   | 1   | —   | —   | — |
| 13th  | 4   | 3   | 3   | 3   | 2   | 1   | 1   | —   | — |
| 14th  | 4   | 3   | 3   | 3   | 2   | 1   | 1   | —   | — |
| 15th  | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | — |
| 16th  | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | — |
| 17th  | 4   | 3   | 3   | 3   | 2   | 1   | 1   | 1   | 1 |
| 18th  | 4   | 3   | 3   | 3   | 3   | 1   | 1   | 1   | 1 |
| 19th  | 4   | 3   | 3   | 3   | 3   | 2   | 1   | 1   | 1 |
| 20th  | 4   | 3   | 3   | 3   | 3   | 2   | 2   | 1   | 1 |

</div>

<div class='footnote'>Part 1 | Casting Styles (Classes)</div>

\pagebreakNum

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/30314805-0284-4dac-99bc-19935cbc4642/d9bfwu7-0ec67f08-9a90-4042-a4be-453783d49e65.jpg/v1/fill/w_1024,h_1449,q_75,strp/godric_gryffindor_by_raphtor_d9bfwu7-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ0OSIsInBhdGgiOiJcL2ZcLzMwMzE0ODA1LTAyODQtNGRhYy05OWJjLTE5OTM1Y2JjNDY0MlwvZDliZnd1Ny0wZWM2N2YwOC05YTkwLTQwNDItYTRiZS00NTM3ODNkNDllNjUuanBnIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.CK6U4ijtUeA7n6bK5LsFca0N72iIdrcWf6oFLu8EqPk" class="cover-image" style="width:60%; top:-40px; right:-60px; left:inherit;"><img src="https://www.gmbinder.com/images/ShMie2y.png" class="cover-image bgwatercolor" style="width:103%;height:80%;top:-125px; filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/ShMie2y.png" class="cover-image bgwatercolor" style="width:140%; left: inherit; right:0px; top:inherit; bottom:0px; filter:brightness(94%) sepia(15%)">


# The Willpower </br>Caster

When witches and wizards cast with feeling, they put all of their energy into their spells. Their “gut instinct” approach to magic taps into that willpower, but teaches them to take shortcuts. These wizards often have strong personalities and gravitate to the frontlines.
## Class Features
As a Willpower caster, you gain the following class features.
#### Hit Points
___
- **Hit Dice:** 1d10 per Willpower level
- **Hit Points at 1st Level:** 10 + your Constitution modifier
- **Hit Points at Higher Levels:** 1d10 (or 6) + your Constitution modifier per Willpower level after 1st

#### Proficiencies
___
- **Saving Throws:** Constitution, Charisma
- **Skills:** Choose two from Athletics, Deception, Intimidation, Magical Theory, Persuasion, Sleight of Hand and Survival
#### Equipment
You start with the following equipment, in addition to the equipment granted by your background: a wand, a student's pack, a winter cloak, and a magical pet of your choice.
#### Spellcasting
Charisma is your spellcasting ability for your spells. You use your Charisma whenever a spell refers to your spellcasting ability. In addition, you use your Charisma modifier when setting the saving throw DC for a spell you cast and when making an attack roll with one.

You must use a wand as a spellcasting focus for your spells. Your spell slot progression is the standard for full casters.

Additionally, when you gain a level in this class, you can choose two of the cantrips or spells you know and replace them with two new cantrips or spells, which also must be of a level for which you have spell slots.
#### Sorcerous Resilience
The accidental magic in your early childhood never stopped protecting you. Your AC equals 13 + your Dexterity modifier.
#### Font of Magic, Metamagic, and Ability Score Improvement
Unless differences are shown in the Willpower class table, a Willpower caster has all Font of Magic, Sorcery Points, Flexible Casting, Metamagic, and Ability Score Improvement class features from a 5e Sorcerer.
#### Metamagic: Fierce Spell
At 3rd level, when you cast a spell, you can spend 2 sorcery points to cast that spell as if it were cast using a spell slot one level higher than its original level, or 4 sorcery points to cast that spell two levels higher. The spell's higher level cannot 

\columnbreak
<div style="margin: 310px -10px 80px 0px; font-style: italic; color:#ECE6D0; text-align:right; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">Art by Raph Lomotan</div>

exceed your highest available level of spell slots. This does not count against your number of Metamagic options.
#### Metamagic: Resistant Spell
At 3rd level, when you cast a spell, you can spend 1 sorcery point per increased level to make your spell be treated by spell deflection, *finite incantatem*, or *reparifors* as if your spell was cast using a spell slot higher than its original level, making your spell more resistant. The spell's higher level cannot exceed your highest available level of spell slots. This does not count against your number of Metamagic options.
#### Apparition Lessons
When you reach 9th level, you gain the Apparition ability.
#### Signature Spells
When you reach 20th level, you gain mastery over two powerful spells and can cast them with little effort. Choose two of your known 3rd-level spells as your signature spells. You can cast each of them once at 3rd level without expending a spell slot. When you do so, you can’t do so again until you finish a short or long rest.
### Schools of Magic
Choose from the available Schools of Magic found in Chapter 3 to determine your subclass. You have access to the full spell list and can learn spells of any school of magic, except where signified with an asterisk in the Spell List in Chapter 9.

<div class='footnote'>Part 1 | Casting Styles (Classes)</div>

\pagebreakNum
<div class='classTable wide' style='margin-top:30px'>

##### Willpower
| Level | Proficiency</br>Bonus | Sorcery</br>Points | Metamagic | Features | Cantrips</br>Known | Spells</br>Known |
|:-----:|:---------------------:|:------------------:|:---------:|:---------|:------------------:|:----------------:|
| 1st   | +2                    | —                  | —         | Spellcasting, Sorcerous Resilience, School of Magic | 4 | 3 |
| 2nd   | +2                    | 2                  | —         | Font of Magic | 4             | 4                |
| 3rd   | +2                    | 3                  | 2         | Metamagic, Fierce Spell, Resistant Spell | 4 | 5 |
| 4th   | +2                    | 4                  | 2         | Ability Score Improvement | 5 | 6                |
| 5th   | +3                    | 5                  | 2         | ─        | 5                  | 8                |
| 6th   | +3                    | 6                  | 2         | School of Magic Feature | 5   | 8                |
| 7th   | +3                    | 7                  | 2         | ─        | 6                  | 10               |
| 8th   | +3                    | 8                  | 2         | Ability Score Improvement | 6 | 11               |
| 9th   | +4                    | 9                  | 2         | Apparition Lessons | 6        | 13               |
| 10th  | +4                    | 10                 | 3         | School of Magic Feature, Metamagic | 7 | 14      |
| 11th  | +4                    | 11                 | 3         | ─        | 7                  | 15               |
| 12th  | +4                    | 12                 | 3         | Ability Score Improvement | 7 | 15               |
| 13th  | +5                    | 13                 | 3         | ─        | 8                  | 17               |
| 14th  | +5                    | 14                 | 3         | School of Magic Feature | 8   | 17               |
| 15th  | +5                    | 15                 | 3         | ─        | 8                  | 18               |
| 16th  | +5                    | 16                 | 3         | Ability Score Improvement | 8 | 18               |
| 17th  | +6                    | 17                 | 4         | Metamagic | 9                 | 20               |
| 18th  | +6                    | 18                 | 4         | School of Magic Feature | 9   | 20               |
| 19th  | +6                    | 19                 | 4         | Ability Score Improvement | 9 | 20               |
| 20th  | +6                    | 20                 | 4         | Signature Spells          | 9 | 20               |
</div>

<img src="https://www.gmbinder.com/images/lM0nRa5.jpg" class="cover-image" style="width:140%; top:520px; left:-250px;"><img src="https://www.gmbinder.com/images/nuH93ZS.png" class="cover-image bgwatercolor" style="width:125%; top:0px; filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/nuH93ZS.png" class="cover-image bgwatercolor" style="width:100%; top:180px; filter:brightness(94%) sepia(15%)"><div style="text-align:right; margin: 260px -370px 20px 0px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk /

© Pottermore Limited
</div>

<div class='footnote'>Part 1 | Casting Styles (Classes)</div>

\pagebreakNum

<div style=" margin: -34px 0px 190px 40px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">Art by Even Amundsen - @evenmehlamundsen</div><img src="https://cdnb.artstation.com/p/assets/images/images/000/301/473/large/Kari6.jpg?1443927911" class="cover-image" style="width:200%; top:-100px; "><img src="https://cdnb.artstation.com/p/assets/images/images/000/301/473/large/Kari6.jpg?1443927911" class="cover-image" style="width:80%; top:-50px; right:-20px; left:inherit;"><img src="https://www.gmbinder.com/images/60YwJDt.png" class="cover-image bgwatercolor" style="width:120%; height:120%; right:0px; left:inherit; filter:brightness(94%) sepia(15%)">

# The </br>Technique </br>Caster

These spellcasters</br> have practiced countless</br> hours to obtain their level</br> of control of magic. They are</br> specialists: powerful and reactive. </br>Their eye for detail them makes them</br> formidable foes in the dueling world, </br>and often are credited as the best of their field.
## Class Features
As a Technique caster, you gain the following class features.
#### Hit Points
___
- **Hit Dice:** 1d6 per Technique level
- **Hit Points at 1st Level:** 6 + your Constitution modifier
- **Hit Points at Higher Levels:** 1d6 (or 4) + your Constitution modifier per Technique level after 1st
#### Proficiencies
___
- **Saving Throws:** Wisdom, Intelligence
- **Skills:** Choose two from Acrobatics, Herbology, Insight, Perception, Potion-Making, Sleight of Hand and Stealth
#### Equipment
You start with the following equipment, in addition to the equipment granted by your background: a wand, a student's pack, a winter cloak, and a magical pet of your choice.
#### Spellcasting
Wisdom is your spellcasting ability for your spells. You use your Wisdom whenever a spell refers to your spellcasting ability. In addition, you use your Wisdom modifier when setting the saving throw DC for a spell you cast and when making an attack roll with one.

You must use a wand as a spellcasting focus for your spells. Your spell slot progression is the standard for full casters (22 slots at level 20).

Additionally, when you gain a level in this class, you can choose two of the cantrips or spells you know and replace them with two new cantrips or spells, which also must be of a level for which you have spell slots.

#### Spell Deflection
At 3rd level, when you are the target of a spell or included in the area of a spell, you can deflect the spell as a reaction. The spell must be on your list of known spells and you spend a number of sorcery points equal to twice that spell's level.

\columnbreak

<div style='margin-top:290px;'></div>

Upon deflection, you automatically succeed on your </br>saving throw against the spell and you can direct the </br>spell's effect to a creature within 10 feet of you, if desired. </br>If the spell does not have a saving throw, it has no effect on you. If a creature was also targeted by the spell or included in the area of the spell, you cannot redirect the spell to that creature.
#### Font of Magic, Metamagic, and Ability Score Improvement
Unless differences are shown in the Technique class table, a Technique caster has all Font of Magic, Sorcery Points, Flexible Casting, Metamagic, and Ability Score Improvement class features from a 5e Sorcerer.
#### Apparition Lessons
When you reach 9th level, you gain the Apparition ability.
#### Sorcerous Restoration
When you reach 20th level, you regain 4 expended sorcery points whenever you finish a short rest.
### Schools of Magic
Choose from the available Schools of Magic found in Chapter 3 to determine your subclass. You have access to the full spell list and can learn spells of any school of magic, except where signified with an asterisk in the Spell List in Chapter 9.

<div class='footnote'>Part 1 | Casting Styles (Classes)</div>

\pagebreakNum
<div style="margin: -34px 0px 0px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk / © Pottermore Limited
</div>
<div class='classTable wide' style='margin-top:400px'>

##### Technique
| Level | Proficiency</br>Bonus | Sorcery</br>Points | Metamagic | Features | Cantrips</br>Known | Spells</br>Known |
|:-----:|:---------------------:|:------------------:|:---------:|:---------|:------------------:|:----------------:|
| 1st   | +2                    | —                  | —         | Spellcasting, School of Magic | 4 | 4            |
| 2nd   | +2                    | 3                  | —         | Font of Magic| 4              | 5                |
| 3rd   | +2                    | 4                  | 2         | Metamagic, Spell Deflection | 4 | 6              |
| 4th   | +2                    | 5                  | 2         | Ability Score Improvement | 5 | 7                |
| 5th   | +3                    | 7                  | 3         | Metamagic | 5                 | 10               |
| 6th   | +3                    | 8                  | 3         | School of Magic Feature | 5   | 11               |
| 7th   | +3                    | 9                  | 4         | Metamagic | 6                 | 12               |
| 8th   | +3                    | 10                 | 4         | Ability Score Improvement | 6 | 13               |
| 9th   | +4                    | 12                 | 5         | Apparition Lessons, Metamagic | 6 | 16           |
| 10th  | +4                    | 13                 | 5         | School of Magic Feature | 7   | 17               |
| 11th  | +4                    | 14                 | 5         | ─        | 7                  | 18               |
| 12th  | +4                    | 15                 | 6         | Ability Score Improvement, Metamagic | 7 | 18    |
| 13th  | +5                    | 17                 | 6         | ─        | 8                  | 21               |
| 14th  | +5                    | 18                 | 6         | School of Magic Feature | 8   | 21               |
| 15th  | +5                    | 19                 | 7         | Metamagic | 8                 | 22               |
| 16th  | +5                    | 20                 | 7         | Ability Score Improvement | 8 | 22               |
| 17th  | +6                    | 22                 | 7         | ─        | 9                  | 25               |
| 18th  | +6                    | 23                 | 8         | School of Magic Feature, Metamagic | 9 | 25      |
| 19th  | +6                    | 24                 | 8         | Ability Score Improvement | 9 | 25               |
| 20th  | +6                    | 25                 | 8         | Sorcerous Restoration | 9     | 25               |
</div>
<img src="https://www.gmbinder.com/images/Zhqv7Pd.jpg" class="cover-image" style="width:140%; height:400%; top:inherit; bottom:620px; left:-200px;"><img src="https://www.gmbinder.com/images/Zhqv7Pd.jpg" class="cover-image" style="width:140%; top:-100px; left:-200px;"><img src="https://www.gmbinder.com/images/4Q3HUFE.png" class="cover-image bgwatercolor" style="width:100%; filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/4Q3HUFE.png" class="cover-image bgwatercolor" style="width:100%; height:80%; top:-10px; filter:brightness(94%) sepia(15%)">
<div class='footnote'>Part 1 | Casting Styles (Classes)</div>

\pagebreakNum
# The Intellect Caster
Clever wizards delve into the underlying theory of magic. These academics are able to learn a wide variety of spells, although they might struggle in the heat of battle. Their expertise and magical versatility makes them invaluable companions across the wizarding world.
## Class Features
As an Intellect caster, you gain the following class features.
#### Hit Points
___
- **Hit Dice:** 1d8 per Intellect level
- **Hit Points at 1st Level:** 8 + your Constitution modifier
- **Hit Points at Higher Levels:** 1d8 (or 5) + your Constitution modifier per Intellect level after 1st

#### Proficiencies
___
- **Saving Throws:** Dexterity, Intelligence
- **Skills:** Choose two from Acrobatics, Herbology, Insight, Investigation, Magical Creatures, Magical Theory, Medicine, Muggle Studies and Survival
#### Equipment
You start with the following equipment, in addition to the equipment granted by your background: a wand, a student's pack, a winter cloak, and a magical pet of your choice.
#### Spellcasting
Intelligence is your spellcasting ability for your spells. You use your Intelligence whenever a spell refers to your spellcasting ability. In addition, you use your Intelligence modifier when setting the saving throw DC for a spell you cast and when making an attack roll with one.

You must use a wand as a spellcasting focus for your spells. Your spell slot progression is the standard for full casters (22 slots at level 20).

Additionally, when you gain a level in this class, you can choose two of the cantrips or spells you know and replace them with two new cantrips or spells, which also must be of a level for which you have spell slots.
#### Ritual Casting
Your ability to recall information allows you to freely cast spells, as long as you have enough time to stop and focus. At 1st level, you can cast a spell as a ritual if that spell has the ritual tag and you know the spell. A ritual version of a spell takes only 1 minute longer to cast than normal. It also doesn't expend a spell slot, which means the ritual version of a spell can't be cast at a higher level.
#### Font of Magic, Metamagic, and Ability Score Improvements
Unless differences are shown in the Intellect Progression table, an Intellect caster has all Font of Magic, Sorcery Points, Flexible Casting, Metamagic, and Ability Score Improvement class features from a 5e Sorcerer.

\columnbreak

#### Diverse Studies
At 3rd level, you gain both level 1 features of your chosen School of Magic.
#### Apparition Lessons
When you reach 9th level, you gain the Apparition ability.
#### Arcane Recovery
When you reach 20th level, you have learned to regain some of your magical energy by studying in your free time. Whenever you finish a short rest, you can choose expended spell slots to recover. The spell slots can have a combined level that is equal to or less than 10, and none of the slots can be 6th level or higher.

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/c1a41765-eb04-4512-951c-b64089908593/d9l5fzv-3151b0a7-4fc8-4486-91a9-c8c7aa2b2080.png/v1/fill/w_600,h_849,strp/hermione_granger_by_fridouw_d9l5fzv-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODQ5IiwicGF0aCI6IlwvZlwvYzFhNDE3NjUtZWIwNC00NTEyLTk1MWMtYjY0MDg5OTA4NTkzXC9kOWw1Znp2LTMxNTFiMGE3LTRmYzgtNDQ4Ni05MWE5LWM4YzdhYTJiMjA4MC5wbmciLCJ3aWR0aCI6Ijw9NjAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.CBRI6GdT5HOR5Ndqi9JiJ8twXmlYSMpDBb49tzASlDo" class="image-location-top-right-bottom-left" height="650" style="position:relative; margin-top:0px;margin-left:-35px;">
<img src="https://www.gmbinder.com/images/5PSCQzJ.png" class="cover-image bgwatercolor" style="width:111%;top:-250px; left:inherit; right:-1px; transform:scaleX(-1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/5PSCQzJ.png" class="cover-image bgwatercolor" style="width:113%;top:268px;left:inherit;right:-1px;transform:scaleX(-1) scaleY(-1); filter:brightness(94%) sepia(15%)">


<div style="margin: -190px -10px 80px 0px; font-style: italic; color:#ECE6D0; text-align:right; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Frida Lundqvist
<p>@fridouw <span style="color:black;">-</span></p>
</div>

### Schools of Magic
Choose from the available Schools of Magic found in Chapter 3 to determine your subclass. You have access to the full spell list and can learn spells of any school of magic, except where signified with an asterisk in the Spell List in Chapter 9.

<div class='footnote'>Part 1 | Casting Styles (Classes)</div>

\pagebreakNum
<div class='classTable wide' style='margin-top:30px'>

##### Intellect
| Level | Proficiency</br>Bonus | Sorcery</br>Points | Metamagic | Features | Cantrips</br>Known | Spells</br>Known |
|:-----:|:---------------------:|:------------------:|:---------:|:---------|:------------------:|:----------------:|
| 1st   | +2                    | —                  | —         | Spellcasting, Ritual Casting, School of Magic | 6 | 6 |
| 2nd   | +2                    | 2                  | —         | Font of Magic | 6             | 8                |
| 3rd   | +2                    | 3                  | 1         | Metamagic, Diverse Studies | 7 | 10              |
| 4th   | +2                    | 4                  | 1         | Ability Score Improvement | 7 | 12               |
| 5th   | +3                    | 4                  | 1         | ─        | 8                  | 16               |
| 6th   | +3                    | 5                  | 1         | School of Magic Feature | 8   | 18               |
| 7th   | +3                    | 6                  | 2         | Metamagic | 9                 | 20               |
| 8th   | +3                    | 7                  | 2         | Ability Score Improvement | 9 | 22               |
| 9th   | +4                    | 7                  | 2         | Apparition Lessons | 10       | 26               |
| 10th  | +4                    | 8                  | 2         | School of Magic Feature | 10  | 28               |
| 11th  | +4                    | 9                  | 2         | ─        | 11                 | 30               |
| 12th  | +4                    | 10                 | 2         | Ability Score Improvement | 11 | 30              |
| 13th  | +5                    | 10                 | 3         | Metamagic | 12                | 34               |
| 14th  | +5                    | 11                 | 3         | School of Magic Feature | 12  | 34               |
| 15th  | +5                    | 12                 | 3         | ─        | 13                 | 36               |
| 16th  | +5                    | 13                 | 3         | Ability Score Improvement | 13 | 36              |
| 17th  | +6                    | 13                 | 3         | ─        | 14                 | 40               |
| 18th  | +6                    | 14                 | 3         | School of Magic Feature | 14  | 40               |
| 19th  | +6                    | 15                 | 3         | Ability Score Improvement | 15 | 40              |
| 20th  | +6                    | 15                 | 3         | Arcane Recovery | 15          | 40               |
</div><img src="https://www.gmbinder.com/images/A5jd1h7.png" class="cover-image" style="width:160%; top:470px; left:-350px;"><img src="https://www.gmbinder.com/images/nuH93ZS.png" class="cover-image bgwatercolor" style="width:125%; top:0px; transform:scaleX(-1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/nuH93ZS.png" class="cover-image bgwatercolor" style="width:100%; top:130px; transform:scaleX(-1); filter:brightness(94%) sepia(15%)">

<div style="text-align:right; margin: 230px -370px 20px 0px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk / 
<p>© Pottermore Limited</p>
</div>
<div class='footnote'>Part 1 | Casting Styles (Classes)</div>

\pagebreakNum

# Chapter 3: Schools of Magic (Subclasses)
## Charms
Charms, a type of spell that alters properties of a thing, can be some of the most powerful spells in existence. The Fidelius Charm, for example, can completely hide a person or a place in such a way that no one can find them unless given the Secret. Memory Charms can be so strong as to remove a person's memory or damage their mind permanently.
### Duelists
Many charms have been weaponized for magical combat. A wizard's duel is a formal practice in wizarding culture in which wizards or witches faced each other and, at the count of three, attempted to disarm, stun, injure, defeat, or kill each other in order to force submission. A duelist is a master of this art, competing in organized, refereed, and non-lethal duels to test and hone their skills.
### Enchanters
Other wizards try their hand at enchantments, a nearly permanent charm placed on an inanimate object. These bewitched objects can range from handy (like a self-stirring coffee mug), to complex (like a top-tier racing broom), to bizarre (like a book acting like a rabid version of its subject matter). An enchanted or bewitched object can be powerful in the hands of the right wizard.
##### School of Magic Spells
| Spell Level  | Spell |
|:------------:|:------|
|  2nd         | *muffliato* |
|  4th         | *capacious extremis* |
|  5th         | *obliviate*, *piertotum locomotor* |
___
### Subclass Features
#### Bewitching Studies
At 1st level, you gain one of the following features.

**Called Shot.** You've honed your aim to be able to strike very specifically with your dueling Charms. When casting a Charm, you can target specific items or body parts, as well as restrict the effects of the charm to only that specific item or body part.

**Protective Enchantments.** Any charm spell you cast that affects an area (cube, line, sphere, or cone) has its area's size doubled.
___
#### Advanced Charmswork
At 6th level, you gain one of the following features.

**Target Practice.** Your steady hand and hours of practice have given you an edge. Whenever you add your spellcasting ability modifier to a spell attack roll, add half your Dexterity modifier (rounded up) as a bonus as well.

**Professional Charmer.** You've learned to weave your enchantments throughout objects. If you cast a single target Charm with a duration longer than Instantaneous on an individual object, the effects have a permanent duration, if desired, until dispelled by you. This feature does not remove Concentration or Dedication requirements.
___
#### Unique Talents
At 10th level, you gain one of the following features.

**Muggle Dueling.** You've trained in non-magical dueling as a last-ditch effort. Add your proficiency bonus to your damage rolls for unarmed strikes and to any Strength checks involved with grappling or disarming a wizard.

**Obliviator.** Instead of simply erasing memories, when you cast *oblivate*, you can choose to implant very detailed false memories. These memories are undetectable by the target of the spell, but if others examine the target's memories (through Legilimency or a Penseive), they might be able to detect that they're false.
___
#### Refined Techniques
At 14th level, you gain one of the following features.

**Wand and Shield.** You've uncovered an ancient dueling style, allowing both offense and defense at the same time. When you cast *protego* or *protego maxima*, you can transition the spell's casting to your off-hand, freeing up your wand to cast other spells. The spell's dedication now expends a bonus action instead of an action, and you are able to cast and maintain another concentration or dedication spell with your wand. Any factor that affects maintaining concentration is applied individually to each effect (e.g. upon taking damage make a Constitution saving throw for each spell).

**A Duty to Protect.** When you cast *piertotum locomotor*, concentration is no longer required, twice as many objects can be animated, and the duration is extended to 1 hour.
___
#### Pinnacle of Casting
At 18th level, you gain one of the following features.

**Lightning-Fast Wand.** You've honed your skills in the dueling ring to be able to cast spells twice as fast as the average wizard. If you don't already have it, Quickened Spell is added to your metamagic options and does not count towards your metamagic count. When you use the Quickened Spell metamagic to cast a spell as a bonus action, you are able to cast any spell as your action and the normal bonus action spellcasting rules do not apply.

**Secret-Keeper.** You add the *fidelius mysteria celare* spell to your list of known spells. It does not count against your number of spells known, and cannot be forgotten to learn another spell.

<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum

<div style="margin: -34px 0px 280px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk / © Pottermore Limited
</div>

<img src="https://www.gmbinder.com/images/OCj9Jyt.jpg" class="cover-image" style="width:104%; top:-45px; left:-315px;"><img src="https://www.gmbinder.com/images/PxOX2zF.png" class="cover-image bgwatercolor" style="width:93%; height:55%; left:-30px; filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/PxOX2zF.png" class="cover-image bgwatercolor" style="width:100%; filter:brightness(94%) sepia(15%)">

## Jinxes, Hexes, and Curses
Formally referred to as Dark charms, jinxes, hexes and curses are often associated with the Dark Arts because they inflict malicious effects on the target. While jinxes are mostly irritating and hexes are a little worse or more painful, curses are the worst kind of Dark magic. All three Unforgivables are classified as curses, and the average civilian wizard could go their whole life without casting a serious curse.
### Aurors
Curses are mainstays in the arsenals of Aurors, highly-trained specialist officers tasked with upholding the law and protecting their magical communities from large-scale threats. To be successful, an Auror must be capable across a variety of skills, like curses, counter-spells, transfiguration, poisons, antidotes, concealment, disguise, and tracking.
### Curse-Breakers
On the other end of the spectrum, a curse-breaker removes, counters or breaks curses placed on objects or places for a living. Whilst curse-breakers could work for the Ministry of Magic, the term is also used to denote a number of adventurous bankers employed by Gringotts Wizarding Bank, tasked with disabling and countering curses in ancient tombs or historical sites to bring back gold and treasure.
##### School of Magic Spells
| Spell Level  | Spell |
|:------------:|:------|
|  3rd         | *langlock* |
|  4th         | *sectumsempra* |
|  5th         | *nullum effugium*, *omnifracto* |
___
### Subclass Features
#### Practical Studies
At 1st level, you gain one of the following features.

**Auror Training.** You've already started practicing the required skills to become an Auror. You learn one common potion recipe and gain proficiency in two of the following: Investigation, Potion-Making, Stealth, Survival.

\columnbreak

**Curse-Breaking.** Your curiosity in taking apart spells and enchantments has found an outlet. Gain a set of Curse-breakers' Tools and gain proficiency in Curse-breakers' Tools.
___
#### Combat-Ready
At 6th level, you gain one of the following features.

**Forceful Magic.** You cast every spell as if it were life-or-death. When you cast a spell that deals damage, add 1d6 to one damage roll.

**Magical Adrenaline.** Your magic invigorates you in times of dire need. As a bonus action, you can spend one hit die to recover hit points as you normally would after a short rest, equal to hit die + Constitution modifier. You have a number of uses equal to your proficiency bonus, and all uses are restored after a long rest.
___
#### Specialized Skills
At 10th level, you gain one of the following features.

**Dark Traces.** You've learned the patterns and styles of Dark magic. You have advantage on any Investigation, Insight, or Perception roll that is involved with detecting Dark magic or a Dark wizard. 

**Ward-Breaker.** *Curse-Breaking required.* It is impossible for anyone to magically detect the act of you successfully breaking a curse, removing an enchantment, or taking down a ward. If someone sees you curse-breaking or is actively looking for the removed magic, they will notice the magic's absence. If a spell is designed to notify the caster in some way, it no longer works and the caster will not be notified.
___
#### Cursemaster
At 14th level, you gain one of the following features.

**Dark Duelist.** Your experience fighting Dark wizards has taught you how to use their own techniques against them. You have advantage on any saving throws made against Dark spells, and any Dark spells you cast are automatically cast one level higher than the consumed spell slot, not exceeding the highest available level of spell slots you have.

**Defensive Arts.** You've learned how to block the most dangerous of spells. Defensive spells are automatically cast two levels higher than the consumed spell slot, not exceeding the highest available level of spell slots you have.
___
#### Legendary
At 18th level, you gain one of the following features.

**Auror Alert.** As a prominent combatant of Dark magic, you have connections in the Department of Magical Law Enforcement. You can call in a two-man auror team to apparate in on your location. You can’t use this feature again until you finish a long rest.

**Unravelling Magic.** Automatically succeed whenever casting *finite incantatem*.

**Fractured Soul.** Your pursuit of Dark magic has uncovered the writings of Herpo the Foul. You can create a Horcrux by performing the Horcrux Ritual, committing murder, and selecting a target to become the Horcrux. Only one Horcux may exist at one time.
<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum
## Transfiguration
Transfiguration is a branch of magic that focuses on the alteration of the form or appearance of an object, via the manipulation of the object's molecular structure. Transfiguration is regarded as “very hard work” and is “more scientific” than any other form of magic, i.e. the practicing witch or wizard has to get it exactly right for the transfiguration to be successful.
### Animagi
The most legendary practitioner of transfiguration is an Animagus, a witch or wizard who can self-transfigure into an animal at will. It takes skill, practice, and patience for wizards and witches to become Animagi. The process is long and arduous, and has the potential to backfire and cause the transformation to go horribly wrong. As a result, there are very few Animagi, and the power they possess requires registration with the Ministry of Magic.
### Alchemists

<img src='https://www.gmbinder.com/images/xsse1yI.png' style='margin: 10px -40px 0px 0; transform:rotate(-10deg); float:right;'>

A far less known application of transfiguration is Alchemy, the branch of magic and an ancient science concerned with the study of the structure, composition, and magical properties of the four basic elements (earth, air, fire, and water), as well as the transmutation of substances. Intimately connected with potion-making, chemistry and transfiguration, there are many who hold it to be the most difficult magic.

<div style="margin-bottom: 10px;"></div>

<div style="text-align:right; margin: -25px -10px 15px 0; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

##### School of Magic Spells
| Spell Level  | Spell |
|:------------:|:------|
|  2nd         | *orbis*, *reparifarge* |
|  3rd         | *ignis laqueis* |
|  4th         | *lapifors* |
___
### Subclass Features
#### Scientific Studies
At 1st level, you gain one of the following features.

**Anatomy Textbook.** Your knowledge of the inner workings of a creature make your transfigurations easier. If a Transfiguration spell must be cast at a higher level to involve a living creature, you can involve a living creature and consume a spell slot one level lower than what's required.

**Intuitive Conversion.** Conceptualizing a transfiguration just comes easily to you. When you cast *vera verto*, it automatically affects targets one size larger than specified by the spell slot level.

\columnbreak
#### Transfiguration Prodigy
At 6th level, you gain one of the following features.

**Animagus Transformation.** You can use your action to magically assume the shape of your animagus form (see *Your Animagus Form* below). You can use this feature twice. You regain expended uses when you finish a short or long rest. 

**Elementalist.** Your study of Alchemy has given you insights in the nature of elements. Any spell that involves only fire, water, earth, or air is automatically cast one level higher than the consumed spell slot, not exceeding the highest available level of spell slots you have.
___
#### Precise Control
At 10th level, you gain one of the following features.

**Partial Transfiguration.** Your understanding of magical theory has enabled you to compartmentalize your magic. Any transfiguration spell can be intentionally cast as a partial transfiguration, converting only the desired portion of the target. All the same capabilities and restrictions of casting those spells at higher levels apply.

**Molding the Elements.** You've learned to bend the elements to your will. Any spell that involves only fire, water, earth, or air can be cast in a different shape than the original spell intended. The new shape cannot exceed the approximate area or volume of the original spell.
___
#### Magically Reinforced
At 14th level, you gain one of the following features.

**Durable Constructs.** You imbue your constructs of creatures with a more potent magic. Your transfigured or conjured living constructs gain additional hit points equal to your level and deal an additional 1d6 of damage.

**Fortified Structures.** You've learned to make magical objects stronger than the real thing. Your transfigured or conjured objects have twice as many hit points before breaking, and can support three times as much weight as their mundane equivalents.
___
#### Molecular Manipulator
At 18th level, you gain one of the following features.

**Apex Predator.** *Animagus Transformation required.* You've achieved complete mastery over the mystical art of animagus transformations. You can transform on your turn as a bonus action, instead of an action Additionally, you can select two additional creatures as your animagus shapes, and you can choose to keep these shapes hidden from the Ministry of Magic. You may also choose to use any of these animals as your corporeal patronus.

**True Alchemist.** Your lifelong study of Flamel's and Dumbledore's writings has finally come to fruition. You can create a Philosopher’s Stone, turning any metal into gold and producing the Elixir of Life. You cannot die of natural causes, and you age at a slower rate. For every 10 years that pass, your body ages only 1 year. Only one Philosopher’s Stone may exist at one time.
<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum
### Your Animagus Form
You can stay in animagus form for a number of hours equal to half your transfiguration level (rounded down). You then revert to your normal form unless you expend another use of this feature. You can revert to your normal form earlier by using a bonus action on your turn. You automatically revert if you fall unconscious, drop to 0 hit points, or die.

While you are transformed, the following rules apply:
* Your game statistics are replaced by the statistics of the beast, but you retain your alignment, personality, and intelligence, wisdom, and charisma scores. You also retain all of your skill and saving throw proficiencies, in addition to gaining those of the creature. If the creature has the same proficiency as you, use the higher bonus.
* When you transform, you assume the beast's hit points and hit dice. When you revert, you return to the hit points you had before you transformed. If you revert as a result of dropping to 0 hit points, any excess damage carries over to your normal form. For example, if you take 10 damage in animagus form and have only 1 hit point left, you revert and take 9 damage.
* You can't cast spells, and the actions you can take are dependent on your beast form's physical capabilities. Transforming doesn't break your concentration or prevent actions that are part of an already-cast spell, but Dedication spells end upon transforming.

<div style="margin: 410px 0px 20px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk / 
<p>© Pottermore Limited</p>
</div>
<img src="https://www.gmbinder.com/images/QTiAQtl.jpg" class="cover-image" style="width:200%; top:490px; left:-450px;"><img src="https://www.gmbinder.com/images/nuH93ZS.png" class="cover-image bgwatercolor" style="width:100%; top:160px; filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/nuH93ZS.png" class="cover-image bgwatercolor" style="width:100%; height:130%; filter:brightness(94%) sepia(15%)">

\columnbreak
* You retain the benefit of any features from your class, race, or other source and can use them if the new form is physically capable of doing so.
* Your equipment merges into your new form and has no effect until you leave the form.

When you gain the *Animagus Transformation* feature, you must decide between the two types of forms: Combat form or Evasion form. This is a permanent, one-time choice and will determine the stats and abilities of your animagus form.
#### Combat Form
A Combat animagus form is a large or powerful predator that can hold its own against dangerous creatures. It is both sturdy and capable of fighting back with lethal force.

Your form must be classified into one of two categories: Land or Water. If your chosen animal breathes and lives underwater, it must be Water. Otherwise, it will be Land, an air-breathing animal that lives on land and is incapable of flight. This classification will determine certain statistics and traits of your animagus form's stat block.

Combat forms can be one of two sizes: Medium or Large. Your form's size should be determined by the creature's actual size; for instance, all dogs would be Medium, not Large. You need your HM's approval to choose a Large-sized animagus form, and transforming into a Large animal may mean you'll be unable to transform in cramped spaces.

<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum
#### Evasion Form
An Evasion animagus form is a small and discreet animal that would not typically attract a lot of attention. It is likely prey in the natural word, surviving by being quiet, mobile and alert. Evasion forms are largely useless in combat, but can hide, escape and get to hard-to-reach places.

Your form must be classified into one of two categories: Land, Water or Air. If your chosen animal breathes and lives underwater, it must be Water. If it is an air-breathing animal that lives on land and is incapable of flight, it must be Land. If it is capable of sustained flight, it must be Air. This classification will determine certain statistics and traits of your animagus form's stat block.

Evasion forms can be one of three sizes: Tiny, Small or Medium. Your form's size should be determined by the creature's actual size; for instance, a cat would be Tiny and a hawk would be Small.
<div style="margin-bottom: 50px;"></div>

___
> ## Combat Animagus
>*Medium or Large*
> ___
> - **Armor Class** 12 + [PB]
> - **Hit Points** 15 + [15 times PB]
> - **Speed** 30 ft. (Land), swim 30 ft. (Water)
>___
>| STR | DEX | CON | INT | WIS | CHA |
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|18 (+4)|14 (+2)|16 (+3)|–|–|–|
>___
> - **Skills** Intimidation, Perception
> - **Senses** darkvision 60 ft. (Land Only), </br>blindsight 60 ft. (Water Only)
> - **Languages** understands languages of its human form but can't speak
> ___
> ***Blood Frenzy (Water Only).*** The animagus has advantage on melee attack rolls against any creature that doesn't have all its hit points.
>
> ***Keen Smell (Land Only).*** The animagus has advantage on Wisdom (Perception) checks that rely on smell.
>
> ***Pack Tactics (Land Only).*** The animagus has advantage on an attack roll against a creature if at least one of the animagus's allies is within 5 ft. of the creature and the ally isn't incapacitated.
>
> ***Water Breathing (Water Only).*** The animagus can breathe only underwater.
> ### Actions
> ***Maul.*** *Melee Weapon Attack:* +[2 + PB] to hit, reach 5 ft., one target. *Hit:* [half PB]d10 + [2 times PB] piercing damage.
>
> ****PB: Your Proficiency Bonus***

\columnbreak
#### Choosing an Animal
Your animagus form is the same animal as your corporeal patronus. Choose your animagus form from the animals listed in Appendix B: Patronus Rolling Tables. You should choose a patronus based on your desired animagus attributes (Combat vs. Evasion, Land vs. Water vs. Air). Your animagus form cannot be a magical beast. If you roll a magical beast (91-00 or 0) while determining your corporeal patronus, you must re-roll your patronus animal.

___
> ## Evasion Animagus
>*Tiny, Small or Medium*
> ___
> - **Armor Class** [10 + PB]
> - **Hit Points** [10 times PB] - 20 (Air Only), </br>[15 times PB] - 30 (Land and Water Only) 
> - **Speed** 5 ft., fly 60 ft. (Air Only), 40 ft. (Land Only), </br>0 ft., swim 30 ft. (Water Only)
>___
>| STR | DEX | CON | INT | WIS | CHA |
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|10 (+0)|16 (+3)|8 (-1)|–|–|–|
>___
> - **Skills** Investigation, Perception, Sleight of Hand, Stealth
> - **Senses** darkvision 60 ft. (Air and Land Only), </br>blindsight 60 ft. (Water Only)
> - **Languages** understands languages of its human form but can't speak
> ___
> ***Cunning Action.*** The animagus can take the Dash, Disengage, or Hide action as a bonus action on each of its turns.
>
> ***Keen Senses (Air and Land Only).*** The animagus has advantage on Wisdom (Perception) checks that rely on sight, hearing or smell.
>
> ***Water Breathing (Water Only).*** The animagus can breathe only underwater.
> ### Actions
> ***Rake.*** *Melee Weapon Attack:* +[PB - 3] to hit, reach 5 ft., one target. *Hit:* [1 + PB] slashing damage.
>
> ****PB: Your Proficiency Bonus***
<div style="margin-bottom: 30px;"></div>

> ##### Different Mobilities
> It may make sense for a land animal to have different speeds. Work with your HM to customize your animagus form, like giving an otter swim speed, a monkey climb speed or a mole burrow speed. To compensate, the usual speed of 40 ft. should then be reduced to 30 ft.

<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum

<img src="https://www.gmbinder.com/images/3hN3dhz.jpg" class="cover-image" style="width:170%; top:-95px; left:-200px;"><img src="https://www.gmbinder.com/images/RbZHChh.png" class="cover-image bgwatercolor" style="width:125%; left:-200px; filter:brightness(94%) sepia(15%)">

<div style="text-align:right; margin: -43px -267px 24px 0px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk / © Pottermore Limited
</div>

## Healing
Healing magic is devoted to improving the physical and mental condition. With many different spells and potions, healing magic requires a wizard to be well-versed in magical conditions and their different remedies.
### Healers
A healer is the wizarding world equivalent of a Muggle doctor. They tend to the sick and injured, often finding employment in St Mungo's Hospital for Magical Maladies and Injuries, England's primary wizarding hospital. Healers may find themselves facing artifact accidents, Dark creature bites, magical diseases, potion poisoning, or spell damage.
### Mediwizards
A mediwizard takes a much more active role in preserving life; if a healer is a doctor, then a mediwizard is a first responder. Mediwitches travel with research expeditions, watch over professional Quidditch, accompany monster hunters, and dive into war to save lives.
##### School of Magic Spells
| Spell Level  | Spell |
|:------------:|:------|
|  Cantrip     | *anapneo* |
|  3rd         | *intus sunt* |
|  6th         | *protego totalum*, *vulnera sanentur* |

### Subclass Features
#### Medical Studies
At 1st level, you gain one of the following features.

**Natural Remedies.** Your interest in healing has led you to study potions and poultices. You learn the recipe for star grass salve and gain proficiency in one of the following skills: Herbology, Medicine, Potion-Making.

**Unshakable Nerves.** Your study of injuries and magical diseases have given you a strong stomach and iron will. You have advantage on saving throws against being frightened.
___
#### Dedicated Protector
At 6th level, you gain one of the following features.

**Accelerated Recovery.** Your healing spells are more effective. Whenever you use a spell of 1st level or higher to restore hit points to a creature, the creature regains additional hit points equal to 2 + the spell’s level.

**Durable Shielding.** Your shield spells are more effective. Whenever you use a defensive spell of 1st level or higher that improves a creature’s AC or grants temporary hit points, the creature gains additional temporary hit points equal to 2 + the spell’s level, which last the duration of the spell's effect.
___
#### Moral Support
At 10th level, you gain one of the following features.

**Phoenix Song.** You have a soothing presence. You gain proficiency in Persuasion and advantage on Charisma checks to ease someone's pain or help them maintain composure.

\columnbreak
<div style='margin-top:340px;'></div>

**Empathic Bond.** You feel others' pain deeply, which gives insight into their suffering. When you cast a Healing spell on another creature, they gain additional hit points and you lose hit points equal to your proficiency bonus, unless their hit points are fully restored by the Healing spell or unless this effect would reduce your hit points to 0.
___
#### Combat Medic
At 14th level, you gain one of the following features.

**Extended Assistance.** You've pushed the limits of your healing magic to saves lives on the front lines. All of your Healing spells' ranges are doubled. If a Healing spell has a range of touch, its new range is 60 feet.

**A Saving-People Thing.** You will throw yourself in the line of fire to protect others. If a creature you can see within 10 feet of you is targeted by a spell or attack, you can use your reaction to cast *protego* and leap in front of that creature, becoming the new target of the attack. If the spell or attack affects both of you and you step in front of that creature, you will be subject to the effects of that spell or attack twice.
___
#### Savior
At 18th level, you gain one of the following features.

**Phoenix Tears.** Your saint-like devotion to others and bravery in the face of danger has earned the respect of phoenixes. If you spend 8 hours reaching out with your magic, a phoenix will appear in a flash of fire and shed tears into a vial for you. Phoenix tears remove all curses, diseases, and poisons affecting a creature. Also, the creature regains all its hit points. A phoenix will only appear and fill a vial with tears when you do not have any other tears, and the phoenix tears will lose their healing properties if anyone other than you possesses the tears or tries to administer them.

**Healing Pulse.** Your healing and defensive magic have intertwined, energizing nearby allies. Whenever you cast a defensive spell, each non-hostile creature within 30 feet of you (including you) is healed a number of hit points equal to half its level.
<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum

<img src='https://www.gmbinder.com/images/jH7TqqD.jpg' class='cover-image' style="width:140%; top:0px; left:-155px;">
<div style='margin: -34px 0px 350px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;'>
Art by Atomhawk / © Pottermore Limited
</div><img src='https://www.gmbinder.com/images/XzbbBU4.png' class='cover-image bgwatercolor' style="top:190px; filter:brightness(94%) sepia(15%)">

## Divination
Divination is an unusual branch of magic involving gathering insights into past, present and future events. It is an inexact science, requiring interpretation of tea leaves and omens. Some believe true divination involves meditation and a belief of non-self to access the Inner Eye, while Centaurs have a unique way of practicing divination by observing the movement of planets, moons, and stars.
### Seers
Naturally gifted in divination, a seer is a wizard or witch who can see into the future with their Inner Eye. While some seers unknowingly utter prophecies about strangers, other seers will glimpse their own futures. Albus Dumbledore believed that seeing into the future is incredibly difficult, because the complexity of every action and its consequences.
### Legilimens
Legilimency is a far more tangible ability, navigating through the many layers of a person's mind and interpreting one's findings. Muggles call this “mind-reading,” but practitioners disdain the term as naive. They often practice occlumency, shielding your mind from the invasion of another legilimens. Although rare natural legilimens exist, it is a field of study that requires great dedication and care.
___
##### School of Magic Abilities
| Required Level | Ability |
|:--------------:|:----------|
|  2nd           | Cleromancy  |
|  3rd           | Tasseomancy |
|  7th           | Cartomancy  |
|  9th           | Crystal-gazing |

\columnbreak
<div style='margin: 0px 0px 365px 0px;'></div>

### Subclass Features
#### Clairvoyant Studies
At 1st level, you gain one of the following features.

**Fortune Teller.** You've particularly taken to astronomy, tasseography, and crystal gazing. You gain a Diviner's Kit and proficiency in using a Diviner's Kit.

**Sensing Danger.** You add half your proficiency bonus to your Initiative and cannot be surprised while conscious.
___
#### Farseeing
At 6th level, you gain one of the following features.

**Foresight.** You start to see omens everywhere you look. After a long rest, roll two d20s and record those rolls as your two foresight rolls. 

When you or a creature you can see is about to make an attack roll, saving throw, or ability check, you can expend one of your foresight rolls to use that number, once per turn. After a long rest, you lose and reroll your foresight rolls. At level 10, you gain another foresight roll, for a total of 3.

**Legilimency.** You add the *legilimens* spell to your list of known spells. It does not count against your number of spells known, and cannot be forgotten to learn another spell.
___
#### The Unseeable
At 10th level, you gain one of the following features.

**Palmistry.** You've mastered reading life lines. After observing a creature for 30 seconds, as an action, you can sense its current hit points.

**Skilled Occlumens.** *Legilimens* and veritaserum will not work on you, unless you allow it. You can choose to let *legilimens* continue and reveal false information, false emotions, or false memories of your choosing.

<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum

___
#### Revealed Intentions
At 14th level, you gain one of the following features.

**Aura Reading.** Your connection with your Inner Eye allows you to see colorful auras around intelligent beings. You can immediately sense if a being is hostile, friendly or neutral.

**Darting Eyes.** *Legilimency required.* As a bonus action, you can cast *legilimens* in combat to see the next spell or action a creature is planning, as long as their eyes are visible.
___
#### Mystical Knowledge
At 18th level, you gain one of the following features.

**Vivid Visions.** Your connection to your Inner Eye gives you a lucid visions of the immediate future. As a bonus action, you can see a vision of your next action and its immediate consequences, rolling any required rolls and hearing a description of the results. If you choose that action, your vision becomes reality, using all the same rolls. The vision is instantaneous, and takes up no time. After you use this ability, you can’t use it again until you finish a long rest.

**Master of Minds.** *Legilimency required.* Your skill in navigating thoughts is unparalleled. You can now cast *legilimens* at-will, verbally or non-verbally. Any attempt to resist your *legilimens* spell is made at disadvantage.
### Divination Abilities
All of the following abilities can only be performed by using a Diviner's Kit. If you are not proficient in using the Diviner's Kit, there's a 33 percent chance your ability fails and you receive a random reading. You will not know your ability has failed. The HM makes this roll in secret.
#### Cartomancy
You gain insight into the past, present, and future of a being other than yourself by performing a tarot card reading. Your subject asks a single question concerning a specific goal, event, or activity to occur within 7 days. By spending 6 sorcery points and 10 minutes, the cards tell you a story (a truthful reply from the HM). The cards' meaning might be a short phrase, a cryptic rhyme, or an omen.

This ability doesn't take into account any possible circumstances that might change the outcome, such as a different use of magic or the loss or gain of a companion.

If you perform a reading two or more times before finishing your next long rest, there is a cumulative 25 percent chance for each reading after the first that you get a random reading. The HM makes this roll in secret.
#### Cleromancy
You focus your inner eye upon rune-inscribed sticks or Grindylow bones as you cast them on the ground. As an action, you can spend 2 sorcery points to interpret their meaning and advise one being of your choice within 30 feet of you. The next time the being makes an ability check, attack roll or saving throw within the next 10 minutes, the target can roll a d4 and add the number rolled to the attack roll or saving throw. This effect can only be active on one target at a time. If you are concentrating on a spell at the time of interpreting the sticks or bones, you lose concentration.

\columnbreak
#### Crystal-gazing
By gazing into the cloudy depths of the crystal ball, you can spend 7 sorcery points to see a particular creature you choose for 10 minutes. The target must make a Wisdom saving throw, which is modified by how well you know the target and the sort of physical connection you have to it. If a target knows you're using this ability, it can fail the saving throw voluntarily if it wants to be observed.

| Knowledge                     | Save Modifier  |
|:------------------------------------------|:--:|
| Secondhand (you have heard of the target) | 0 |
| Firsthand (you have met the target)       | -5 |
| Familiar (you know the target well)       | -10 |

On a successful save, the target isn't affected, and you can't use this ability against it again for 24 hours.

On a failed save, this ability lets you see as if you were there, within 10 feet of the target. Your view moves with the target, remaining within 10 feet of it for the duration.

Instead of targeting a creature, you can choose a location you have seen before as the target of this ability. When you do, your view shows that location and doesn't move.

<img src='https://www.gmbinder.com/images/iznjxIr.png' style='margin: -10px -40px 0 0; width:65%; transform:rotate(0deg);'>

<img src='https://www.gmbinder.com/images/GJAbDv6.png' style='margin: -220px -20px 0 0; transform:rotate(5deg); float:right;'>

<div style="text-align:right; margin: -30px -30px 25px 0; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

#### Tasseomancy
The future is revealed through a uniquely complex reading of symbols and patterns within residual tea leaves a cup recently consumed by a being other than yourself. After ten minutes of preparation, you can spend 3 sorcery points to interpret the cup's omens and predict the results of a specific course of action that your subject plans to take within the next 30 minutes. The HM chooses from the following possible omens:

* **Weal**, for good results
* **Woe**, for bad results
* **Weal and woe**, for both good and bad results
* **Nothing**, for results that aren't especially good or bad

This ability doesn't take into account any possible circumstances that might change the outcome, such as a different use of magic or the loss or gain of a companion.

If you cast the spell two or more times before completing your next long rest, there is a cumulative 25 percent chance for each casting after the first that you get a random reading. The HM makes this roll in secret.
<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum
## Magizoology
Magizoologists study magical creatures. As they work with many different creatures, the Department for the Regulation and Control of Magical Creatures at the Ministry of Magic created a classification of every known beast, being and spirit, ranging from X to XXXXX. Whether harmless or an untameable wizard-killer, magizoologists record the unique traits of beasts for wizardkind’s safety.
### Dragon-Keepers
Dragon-keepers call the dragon reserve home, caring for the most famous XXXXX classified creature among wizards and Muggles alike. Spending day after day with them, dragon-keepers often learn to see through the eyes of their ward and empathize with the plight of many magical beasts. They seek to understand dragons for the benefit of all.
### Monster Hunters
Alternatively, some take a confrontational style of protection. When a wizarding village is plagued by a growing community of trolls, or they suspect a vampire is the cause of their dead livestock, they turn to a monster hunter. Dark creatures blur into the magical being category, so a monster hunter must deal with intelligent demi-humans just as well as corral a stray beast. It is up to the monster hunter to approach a situation wand blazing or seeking a peaceful resolution.
### Subclass Features
#### Biological Studies
At 1st level, you gain one of the following features.

**Caretaker.** Your study of magical creatures has taught you about their injuries and physiologies. You can cast any known Healing spells on beasts.

**Folio Bruti.** You have your own personal notebook of beasts where you record your findings. Whenever you add Magical Creatures proficiency to an Ability check, add your Intelligence modifier as a bonus as well.
___
#### Way of the Wild
At 6th level, you gain one of the following features.

**Wizard's Best Friend.** Your care and compassion towards creatures earns you their trust and respect. You can have a beast companion (see *Your Beast Companion* below).

**Prepared Ambush.** In learning to combat dangerous targets, you know how to place a magical trap, waiting to be sprung. When you cast a spell that targets a single creature or area using a spell slot of 1st level or higher, you can weave that spell into your surroundings, having no immediate effect. The spell is cast when it is triggered by something, which you decide at the time of setting the trap, such as entering an area, getting within a certain distance, or manipulating an object. You can also set conditions for creatures that don't trigger the spell, such as specific people or those who say a certain password.

Using this ability expends a spell slot two levels higher than the intended spell. For example, to set a 1st level spell as a magical trap, you must expend a 3rd level spell slot.

\columnbreak

If the spell requires a target, the spell can only target one triggering creature, or if it affects an area, the spell's area of effect is centered on the triggering creature. If the spell conjures hostile creatures, they appear as close as possible to the triggering creature and attack. If the spell requires concentration, it lasts its full duration. A trap can be detected by a successful Intelligence (Investigation) check against your spell save DC, or by casting *specialis revelio*.

#### Outdoorswizard
At 10th level, you gain one of the following features.

**Survivalist.** You are particularly adept at traveling through and surviving in natural environments. 

You gain proficiency in either Herbology or Survival. Between Herbology and Survival, choose one that you're proficient in; your proficiency bonus is doubled when you make any check using that chosen skill. Also, you and your group gain the following benefits:
<div style='margin-top:-10px;'></div>

* Difficult terrain doesn’t slow your group’s travel.
* Your group can't be surprised while resting, as long as you are keeping watch.
* If a hit die roll is lower than their proficiency bonus, your group can reroll it once and take the higher result.

**Monster Hunting.** You have vast experience studying, tracking, and hunting creatures, allowing you to quickly adapt to threats. If you spend 10 minutes studying a beast or dark being's tracks, you automatically learn what the creature is, its size, and its speed. If you choose, that creature becomes and remains Hunted until you use this feature again.

You have advantage on Wisdom checks to track a Hunted creature and on Intelligence checks to recall information about them. While you're within 30 feet of a Hunted creature that you're actively tracking, you can sense its direction relative to you and distance in feet away from you.
#### Genus Genius
At 14th level, you gain one of the following features.

**Beast Whisperer.** You've learned the body language and social rituals of many beasts. As an action, you can use a Wisdom (Magical Creatures) check to attempt to soothe and calm a hostile beast. On success, the beast believes you mean it no harm and is neutral to the party. The effect is canceled if you or a party member inflicts any damage or condition on that beast or any identical beasts. You cannot use this feature again until you complete a short or long rest.

**Exploited Vulnerabilities.** You know exactly how to hit where it hurts. As a bonus action, you can call out an enemy's weaknesses to your allies. The target takes an additional 2d8 damage from your allies' damaging spells until the start of your next turn. You have a number of uses equal to your Intelligence modifier, and uses are restored after a long rest.

___
#### Sixth Sense
At 18th level, you gain one of the following features.

**Draconic Empathy.** *Wizard's Best Friend required.* Your dedication as a dragon-keeper allows you to deeply understand dragons. If you've ever raised a dragon from an egg, it will view you as an ally and can serve as your beast companion. Tamed dragons have their own hit points, hit dice, and ability scores, and use natural attack actions.
<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum

<img src='https://www.gmbinder.com/images/BL4sO75.jpg' class='cover-image' style="width:160%; top:-110px; left:-90px;">
<div style='margin: -34px -360px 280px 0; text-align:right; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;'>
Art by Atomhawk / © Pottermore Limited
</div>
<img src='https://watercolors.giantsoup.com/phb/phb_top/0011.png' class='cover-image bgwatercolor' style="top:-540px; transform:scaleX(-1); filter:brightness(94%) sepia(15%)"><img src='https://www.gmbinder.com/images/XzbbBU4.png' class='cover-image bgwatercolor' style="top:250px; transform:scaleX(-1); filter:brightness94%) sepia(15%)">


**Hunter's Reflexes.** You've precisely honed your instincts in combat. As a reaction to a creature you can see casting a spell or attacking, you can cast a spell with a casting time of one action, bonus action, or reaction, targeting only that creature. Conditions and damage are applied before the target completes their action. Damage dealt to the target imposes disadvantage on its attack roll. You cannot use this feature again until you complete a short or long rest.
### Your Beast Companion
___
#### Bonding with Your Beast
With 8 hours of uninterrupted communication and bonding, you can call upon a non-hostile beast to serve as your faithful companion. When you gain this feature, select your companion from any Medium or larger single beast of challenge rating 1/4 or lower. You can have only one beast companion at a time.

Your beast companion obeys your commands as best it can. The beast moves and acts during your turn, but you determine its actions, decisions, attitudes, and so on. You and your companion can move and act in any order you choose. If you are incapacitated or absent, your companion acts on its own.

Your companion will fight in unison with you. The following rules apply while it is bonded to you by this feature:
* It can't use its natural attack actions, but it can make unarmed
strikes. Its damage die for unarmed strikes becomes a d4.
* It is proficient in two saving throws and two skills of your choice, in addition to its normal proficiencies.
* It uses your proficiency bonus for attacks, as well as for saving throws and skills in which it is proficient.
* It adds your proficiency bonus to its armor class.

To find your companion's maximum hit points, take the stat block's hit points and add 5 times your caster level. Whenever you gain an Ability Score Improvement, you can also allocate two points among your companion's ability scores. If your beast companion is ever slain or dismissed, a bond may be formed with another beast and that beast will progress according to your current level.

\columnbreak
<div style='margin: 0px 0px 235px 0px;'></div>

#### Commanding Your Beast
You train your companion to follow certain commands. You have a number of Command Dice equal to half your level (rounded down) + your Wisdom modifier. A command die is a d6, and it is used to issue specifically trained commands to beasts, including your beast companion.

You can issue one command at a time to a beast within 120 feet of you that can hear you; the beast must be able to hear you to follow the command, and the command is wasted if the beast doesn't fulfill it before the end of its next turn. When a command die is rolled, its use is expended. Your command die becomes a d8 when you reach 14th level.

You regain all command dice when you finish a long rest.

##### Beast Commands
Your companion knows two beast commands of your choice. It learns an additional command when you reach 14th level. You can also teach any friendly beast other than your companion only one beast command by spending at least 1 hour per day for 7 days training the creature.

**Attack.** You can use your bonus action and roll a command die to issue this command. Your companion can use its action to take one of its natural attack actions. However, it can't use its Multiattack action, if it has one. If the attack hits, add the result of the command die to the damage roll.

**Down.** You can use your bonus action and roll a command die to issue this command. Your companion uses its reaction to fall prone and attempt to Hide, adding the result of the command die to its Dexterity (Stealth) check. The first attack it makes while hidden in this way also adds the result of the command die to its attack roll.

**Find.** You can use your bonus action and roll a command die to issue this command. Your companion uses its reaction to attempt to Search for hidden creatures or objects, adding the result of the command die to the Search's skill check.

**Grab.** When your companion makes an opportunity attack, you can use your reaction and roll a command die to issue this command. If the attack hits, your companion can attempt to grapple the target as part of the attack, adding the result of the command die to the skill check it makes for the attempt.

**Rush.** You can use your bonus action and roll a command die to issue this command. Your companion uses its reaction to take the Help action, aiding the next attack against a creature within its reach that it can see. If this attack hits, add the result of the command die to the attack's damage.

<div class='footnote'>Part 1 | Schools of Magic (Subclasses)</div>

\pagebreakNum

<!--<img src="https://www.gmbinder.com/images/9bhT1xA.png" class="cover-image bgwatercolor" style="width:110%; top:inherit; left:300px; bottom:550px; transform: rotate(-20deg) scalex(-1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/9VkhTcw.png" class="cover-image bgwatercolor" style="width:74%; top:inherit; left:inherit; bottom:510px; right:290px; transform: scaleX(-1) rotate(-40deg); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/uvX1qOq.png" class="cover-image bgwatercolor" style="width:80%; top:600px; left: 150px; transform: scalex(-1) rotate(13deg); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images//PxOX2zF.png" class="cover-image bgwatercolor" style="width:100%; top:-80px; left:260px; transform: rotate(-60deg); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/9VkhTcw.png" class="cover-image bgwatercolor" style="width:100%; top:640px; left:-35px; transform: scaleY(-1) rotate(-23deg); filter:brightness(94%) sepia(15%)">-->

# Chapter 4: Wands (Backgrounds)
Every witch and wizard purchases a wand before their first year at Hogwarts, and spends their entire life using that wand, unless they break it or win another wand in combat. The conduit through which their magic flows, a wand is a deeply personal and valuable possession to wizards. Those knowledgable in wandlore will often describe a wand as if it can think and feel. Every single wand is unique and its character will depend on the particular tree and magical creature from which it derives its materials. Moreover, each wand, from the moment it finds its ideal owner, will begin to learn from and teach its human partner.

\columnbreak
## Wand Components
### Wood
Only a minority of trees produce wand quality wood (just as a minority of humans can produce magic), so it takes years of experience to tell which trees have the gift. A wand’s wood determines the core personality of the wand. As Garrick Ollivander said, the wand chooses the wizard, and so the wood of a wand tells you about the wizard who wields it.
<div style='margin: 0 0 0 140px;'>

### Cores
#### Unicorn Hair
Unicorn hair generally produces the most consistent magic, and is least subject to fluctuations and blockages. Wands with unicorn cores are generally the most difficult to turn to the Dark Arts. 

They are the most faithful of all wands, and usually remain strongly attached to their first owner, irrespective of whether he or she was an accomplished witch or wizard. Minor disadvantages of unicorn hair are that they do not make the most powerful wands (although the wand wood may compensate) and that they are prone to melancholy if seriously mishandled, meaning that the hair may ‘die’ and need replacing.</div>
####                                 Dragon Heartstring
                                As a rule, dragon heartstrings produce                             wands with the most power, and which are                         capable of the most flamboyant spells. Dragon                     wands tend to learn more quickly than other                 types. While they can change allegiance if won from             their original master, they always bond strongly with         the current owner. The dragon wand tends to be easiest     to turn to the Dark Arts, though it will not incline that way of its own accord. It is also the most prone of the three cores to accidents, being somewhat temperamental.
#### Phoenix Feather
Phoenix feather is the rarest core type. Phoenix feathers are capable of the greatest range of magic, though they may take longer than either unicorn or dragon cores to reveal this. They show the most initiative, sometimes acting of their own accord, a quality that many witches and wizards dislike. 

Phoenix feather wands are always the pickiest when it comes to potential owners, for the creature from which they are taken is one of the most independent and detached in the world. These wands are the hardest to tame and to personalize, and their allegiance is usually hard won.
<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum

#### Uncommon Wand Cores
Those three wand cores are the only kinds of wands crafted by Garrick Ollivander, but many other wand cores exist. Around the world and in the shops of other wand makers, you might find wands with cores of Kelpie hair, Dittany stalk, Kneazle whisker, Veela hair, coral, or even troll whisker. These unusual cores have a reputation for being less reliable, but sometimes an uncommon core produces a wand that's the perfect match for a one-of-a-kind wizard.
### Length
Many wandmakers simply match the wand length to the size of the witch or wizard who will use it, but this is a crude measure, and fails to take into account many other, important considerations. Longer wands might suit taller wizards, but they tend to be drawn to bigger personalities, and those of a more spacious and dramatic style of magic. Neater wands favour more elegant and refined spell-casting. However, no single aspect of wand composition should be considered in isolation of all the others, and the type of wood, the core and the flexibility may either counterbalance or enhance the attributes of the wand’s length.

Most wands will be in the range of nine and fourteen inches. Extremely short wands (eight inches and under) and very long wands (over fifteen inches) are exceptionally rare. In the latter case, a physical peculiarity demanded the excessive wand length. However, abnormally short wands usually select those in whose character something is lacking, rather than because they are physically undersized.
### Flexibility
Wand flexibility or rigidity denotes the degree of adaptability and willingness to change possessed by the wand-and-owner pair. Although, again, this factor ought not to be considered separately from the wand wood, core and length, nor of the owner’s life experience and style of magic, all of which will combine to make the wand in question unique.
## Backgrounds
Wand woods are grouped into backgrounds based on their general traits, which help define your character and determine your background skill proficiencies and background feature. Once you've selected your background, choose a wood. Then select your remaining wand components: core, length, and flexibility. You are free to create any combination of Ideals, Bonds, and Flaws to match the personality of your witch or wizard.

 
> ##### Mix-and-Match Wandmaking
> Like 5e, character backgrounds are entirely customizable. Even wand woods are mere suggestions, and any wood can be paired with any background. Feel free to work with your HM to modify an existing background or create a brand new one to bring your character concept to life.

\columnbreak

If you want the experience of the wand choosing the wizard, all wand attributes have rolling tables for random selection.
| d100  | Wand Wood     |
|:-----:|:--------------|
| 1-2   | Acacia        |
| 3-6   | Alder         |
| 7-9   | Ash           |
| 10-11 | Apple         |
| 12-13 | Aspen         |
| 14-16 | Beech         |
| 17    | Blackthorn    |
| 18-19 | Black Walnut  |
| 20-22 | Cedar         |
| 23    | Cherry        |
| 24-25 | Chestnut      |
| 26-28 | Cypress       |
| 29-32 | Dogwood       |
| 33-34 | Ebony         |
| 35    | Elder         |
| 36-37 | Elm           |
| 38-40 | English Oak   |
| 41-44 | Fir           |
| 45-47 | Hawthorn      |
| 48-50 | Hazel         |
| 51    | Holly         |
| 52-54 | Hornbeam      |
| 55-57 | Larch         |
| 58-60 | Laurel        |
| 61-63 | Mahogany      |
| 64-66 | Maple         |
| 67-69 | Pear          |
| 70-72 | Pine          |
| 73-75 | Poplar        |
| 76-77 | Red Oak       |
| 78-79 | Redwood       |
| 80-83 | Rowan         |
| 84-85 | Silver Lime   |
| 86-88 | Spruce        |
| 89-91 | Sycamore      |
| 92-93 | Vine          |
| 94-97 | Walnut        |
| 98-99 | Willow        |
| 00    | Yew           |

<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum
<div style='margin: -34px 0px 145px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;'>© Pottermore Limited</div><img src='https://www.gmbinder.com/images/4daS5xo.jpg' class='cover-image' style="width:100%; top:25px;"><img src='https://www.gmbinder.com/images/4daS5xo.jpg' class='cover-image' style="width:120%; top:-245px; left:-75px; transform: scaleX(-1);"><img src='https://www.gmbinder.com/images/WQXIOUB.png' class='cover-image bgwatercolor' style="top:-380px; width:100%; filter:brightness(94%) sepia(15%)"><img src='https://www.gmbinder.com/images/WQXIOUB.png' class='cover-image bgwatercolor' style="transform: scaleX(-1); filter:brightness(94%) sepia(15%)">

### Artist
You see yourself as an observer of the world around you, capturing little glimpses of that world. You express yourself through those glimpses, satisfying your need to create and communicating your own unique perspective. Your chosen medium might be magically developed moving photographs, a painted portrait with a personality, a bewitched sculpture or even enchanted cartography.

**Skill Proficiencies:** Insight, Performance

**Equipment:** The tools of the art medium of your choice (e.g. painter's supplies, musical instrument, costume, etc.), and a sketch pad with charcoal sticks
#### Background Feature: Apprentice
Although you're not yet able to create original works, you have enough knowledge and rudimentary skills to begin an apprenticeship under a mentor, should you find one willing to teach you. Additionally, you've become practiced in hand-eye coordination and precise work.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 10px;'>d6</span> | Wood (Personality Traits) |
|:---:|:--------------|
| 1-2 | Pine          |
| 3-4 | Red Oak       |
| 5-6 | Sycamore      |
#### Pine
Pine wands always choose an independent, individual master who may be perceived as a loner, intriguing and perhaps mysterious. Pine wands enjoy being used creatively, and unlike some others, will adapt unprotestingly to new methods and spells. Many wandmakers insist that pine wands are able to detect, and perform best for, owners who are destined for long lives. The pine wand is one of those that are sensitive to non-verbal magic.
#### Red Oak
You will often hear the ignorant say that red oak is an infallible sign of its owner’s hot temper. In fact, the true match for a red oak wand is possessed of unusually fast reactions, making it a perfect duelling wand. Less common than English oak, its ideal master is light of touch, quick-witted and adaptable, often the creator of distinctive, trademark spells, and a good man or woman in a fight.
#### Sycamore
The sycamore makes a questing wand, eager for experience and losing brilliance in mundane activities. These may combust if allowed to become ‘bored,’ and many aging witches and wizards are disconcerted to find their wand bursting into flame as they ask it, one more time, to fetch their slippers. The sycamore’s ideal owner is curious,

\columnbreak
<div style='margin-top: 150px;'></div>

 vital and adventurous, and with such an owner, it demonstrates a highly-prized capacity to learn and adapt.

<div style='margin-top: 20px;'></div>


| <span style='padding:0px 15px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* Beauty. When I create, I make the world better than it was.  |
| 3-4 | *Dragon Heartstring:* People. I want to make an impact on everyone who experiences my work. |
| 5-6 | *Phoenix Feather:* Honesty. Art should reflect the soul; it should come from within and reveal who we really are. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *10":* I owe my mentors a great debt for shaping me into the person I am today. |
| 3-4 | *11.5":* I have a family, but I have no idea where they are. One day, I hope to see them again. |
| 5-6 | *13":* My camera/easel/instrument is my most treasured possession, and it reminds me of someone I love. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Reasonably Firm:* In fact, the world does revolve around me. |
| 3-4 | *Slightly Swishy:* There's no room for caution in a life lived to the fullest. |
| 5-6 | *Quite Yielding:* I'll do anything to win fame and renown.  |
<div style='margin-top: 20px;'></div>

#### Variant Artist: Performer
Even moreso than visual artists, you're compelled to express yourself, your experiences and your emotions. While you aren't immune to bouts of uncertainty and performance anxiety, you generally seem to be quite extraverted. You've found your calling in at least one of the performing arts: singing, dancing, playing an instrument or magical theater.
<div style='margin-top: 30px;'></div>

> ##### Variant Feature: Dramatic Entrance
> Your flair for the dramatic means you can always do things in the most attention-grabbing way as possible. This often makes for an excellent distraction or starts to build a crowd.

<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum
<div style='margin: -34px -365px 20px 0px; text-align:right;font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;'>© Pottermore Limited</div>

### Bookworm
You've always been known to have your nose in a book, whether obsessing over homework or escaping reality into a world of fiction. You often solve your problems through research and study. Because you absorb so much from others, you've learned things, traveled places, felt emotions, and seen wonders far beyond your own experiences.

**Skill Proficiencies:** Magical Theory, Investigation

**Equipment:** Your favorite book, a book you're </br>currently reading, and a small back-up quill
#### Background Feature: Teacher's Pet
Because you are a bright individual, teachers and those in positions of authority are more likely to interpret your actions and intentions favorably. You might be in a better position to enlist their help, or have plausible deniability based on your academic reputation.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 10px;'>d4</span> | Wood (Personality Traits) |
|:-:|:------------|
| 1 | Beech       |
| 2 | Hornbeam    |
| 3 | Vine        |
| 4 | Walnut      |
#### Beech
The true match for a beech wand will be, if young, wise beyond his or her years, and if full-grown, rich in understanding and experience. Beech wands perform very weakly for the narrow-minded and intolerant. When properly matched, the beech wand is capable of a subtlety and artistry not seen in any other wood, hence its lustrous reputation.
#### Hornbeam
Hornbeam, a fine-tuned and sentient wand, selects for its life mate the talented witch or wizard with a single, pure passion. Hornbeam wands adapt more quickly to their owner’s style of magic and become so personalized, so quickly, that others will find them extremely difficult to use. They likewise absorb their owner’s code of honor and will refuse to perform acts - good or ill - conflicting with their master’s principles. 
#### Vine
Vine wands are among the less common types, and their ideal owners are nearly always those witches or wizards who seek a greater purpose, have a vision beyond the ordinary and frequently astound those who think they know them best. Vine wands seem strongly attracted by personalities with hidden depths, and often instantly detect a match.
#### Walnut
Walnut wands are often found in the hands of highly intelligent magical innovators and inventors; this is a handsome wood possessed of unusual versatility and adaptability. Walnut wands will, once subjugated, perform any task its owner desires, provided that the user is of sufficient brilliance. This makes for a truly lethal weapon in the hands of a witch or wizard of no conscience, for the wand and the wizard may feed on each other in an unhealthy manner.

\columnbreak

<div style='margin-top: 350px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* Creativity. The world is in need of new ideas and bold action.|
| 3-4 | *Dragon Heartstring:* Knowledge. The path to power and self-improvement is through knowledge. |
| 5-6 | *Phoenix Feather:* Self-improvement. The goal of a life of study is the betterment of oneself. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *10":* I want my life's work to be magical textbooks related to a specific field. |
| 3-4 | *12.5":* I've been searching my whole life for the answer to a certain question. |
| 5-6 | *13":* My family has an ancient text of terrible secrets that must not fall into the wrong hands. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Unyielding:* Uncovering knowledge is worth any price, even a piece of my own humanity. |
| 3-4 | *Reasonably Supple:* I let my need to win arguments overshadow friendships and harmony. |
| 5-6 | *Pliant:* I overlook obvious solutions in favor of complicated ones. |
<div style='margin-top: 20px;'></div>

#### Variant Bookworm: Prodigy
You've always exhibited unusual control over your magical abilities. Where others struggle, things come naturally to you. The ease with which you gain knowledge or skills sometimes results in arrogance or naivete. You've also been burdened with greater expectations and if you entered wizarding school early or skipped a year, you're accustomed to being younger than your peers.

<img src='https://www.gmbinder.com/images/PhVhz6w.jpg' class='cover-image' style="width:95%;top:-220px;left:310px;"><img src='https://www.gmbinder.com/images/PhVhz6w.jpg' class='cover-image' style="width:95%;top:-290px;left:310px;"><img src='https://watercolors.giantsoup.com/phb/phb_top-right/0012.png' class='cover-image bgwatercolor' style="width:110%;height:100%;top:0px;left:0px;transform: scaleX(1); filter:brightness(94%) sepia(15%)">

<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum

### Dreamer
Your dreams fill your thoughts, distracted by all of life's possibilities. Introspection comes easily to you and frankly, you don't understand how a person can live without looking for meaning, thinking deeply about society's values, or being overcome with wonder. You might even feel out of place in a world of people focused on material success and just getting through the day.

**Skill Proficiencies:** Insight, Perception

**Tool Proficiencies:** Astronomer's tools

**Equipment:** Astronomer's tools, and a mystical trinket you believe gives you protection (but doesn't)
#### Background Feature: Stargazer
Many of your nights are spent staring up at space, contemplating existence. You're a natural at Astronomy and share the Centaurs' views on the importance of the heavens. Your affinity for the ethereal also leads ghosts to be more trusting of you and more forthcoming with information.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 10px;'>d10</span> | Wood (Personality Traits) |
|:---:|:--------------|
| 1-2 | Black Walnut  |
| 3-4 | Cedar         |
| 5-6 | Hazel         |
| 7-8 | Redwood       |
| 9-10| Silver Lime   |
#### Black Walnut
Less common than the standard walnut wand, black walnut wands seek a master of good instincts and powerful insight. Black walnut is a very handsome wood, but is not the easiest to master. If the wand is paired with a sincere, self-aware owner, however, it becomes one of the most loyal and impressive wands of all, with a particular flair in all kinds of charmwork.
#### Cedar
Never matched to the easily-fooled, the cedar wand finds its perfect home where there is perspicacity and perception. Some wandmakers would go further than that, saying one should never cross the owner of a cedar wand, especially if harm is done to their allies or kin. The witch or wizard who is well-matched with cedar carries the potential to be a frightening adversary, which often comes as a shock to those who have thoughtlessly challenged them.
#### Hazel
A sensitive wand, hazel often reflect its owner’s emotional state and works best for a master who understands and can manage their own feelings. Others should be careful handling a hazel wand if its owner has been angered or disappointed, because the wand will absorb such energy and discharge it unpredictably. It is capable of outstanding magic in the hands of the skilful and is so devoted to its owner that it often ‘wilts’ at the end of their master's life.

\columnbreak
#### Redwood
Wand-quality redwood is in short supply due to its reputation for bringing good fortune. As usual with wandlore, the populace has it backwards: redwood wands are not themselves lucky, but are strongly attracted to witches and wizards who already possess the admirable ability to fall on their feet, to make the right choice, to snatch advantage from catastrophe. One can expect to hear of exciting exploits when such a witch or wizard wields a redwood wand.
#### Silver Lime
This unusual and highly attractive wand wood was greatly in vogue in the nineteenth century, and demand consistently outstripped supply. The reasons for these wands’ desirability lay not only in their unusually handsome appearance, but also because they had a reputation for performing best for Seers and those skilled in Legilimency, mysterious arts both, which consequently gave the possessor of a silver lime wand considerable status.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* Honesty. Lies, hypocrisy and inauthenticity cause the most spiritual harm to a person's soul. |
| 3-4 | *Dragon Heartstring:* Change. All good and bad things must come to an end. Change is the nature of existence. |
| 5-6 | *Phoenix Feather:* Independence. My spirit is free, and no one else has authority over my life. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *9.5":* I'm seeking enlightenment, but it always eludes me. |
| 3-4 | *11.5":* I see what others are blind to, and I need to open their eyes. |
| 5-6 | *14":* I suffer recurring dreams of a terrible event in the future and will do anything to prevent it. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Rigid:* I can't keep a secret to save my life, or anyone else's. |
| 3-4 | *Slightly Yielding:* I am dogmatic in my thoughts and philosophy. |
| 5-6 | *Surprisingly Swishy:* I am easily distracted and if there's a plan, I'll forget it. If I don't forget it, I'll ignore it. |
<div style='margin-top: 20px;'></div>

<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum
### Groundskeeper
Your childhood has always been spent outdoors, climbing trees or capturing insects. You've always felt an intense connection to all forms of life around you, and that drives you to be considerate towards other beings. Going without fresh air leaves you feeling trapped, but some greenery and a ray of sunshine is all it takes to put you in a great mood.

**Skill Proficiencies:** Survival, Magical Creatures

**Tool Proficiencies:** Herbologist's tools

**Equipment:** Herbologist's tools, and a compass
#### Background Feature: Value All Life
You've earned a reputation for your compassionate demeanor. Magical beings and intelligent beasts are more likely to treat you favorably or grant you an audience. If they have any prejudices against wizardkind, you'll have the chance to prove yourself and become exempt from those prejudices.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 10px;'>d4</span> | Wood (Personality Traits) |
|:-:|:--------------|
| 1 | Chestnut      |
| 2 | English Oak   |
| 3 | Maple         |
| 4 | Poplar        |
#### Chestnut
This is a most curious, multi-faceted wood, which takes a great deal of colour from the personality that possesses it. The wand of chestnut is attracted to witches and wizards who are skilled tamers of magical beasts and those who are natural fliers. However, three successive heads of the Wizengamot have possessed chestnut and unicorn wands, for this combination shows a predilection for those concerned with all manner of justice.
<div style="margin: 130px 0px 20px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">Art by Gergely Gizella

www.logartis.info</div><img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/97ccfcaf-cad6-4cc1-9780-ee2507cebffa/d9on02y-20d4a6d1-34d5-47c1-8b6b-3c10244d8369.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzk3Y2NmY2FmLWNhZDYtNGNjMS05NzgwLWVlMjUwN2NlYmZmYVwvZDlvbjAyeS0yMGQ0YTZkMS0zNGQ1LTQ3YzEtOGI2Yi0zYzEwMjQ0ZDgzNjkuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.5oC5uold5XOOfMlEQxFH80u3iAuhC3efG7kpC9KOmI8" class="cover-image" style="width:104%; top:590px; left:-13px;"><img src="https://watercolors.giantsoup.com/phb/phb_left/0020.png" class="cover-image bgwatercolor" style="width:60%; height:60%; top:inherit; left:inherit; bottom:-40px; right:-20px; transform: rotate(90deg) scaleX(-1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/nuH93ZS.png" class="cover-image bgwatercolor" style="width:100%; height:75%; top:395px; transform: scaleX(1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/nuH93ZS.png" class="cover-image bgwatercolor" style="width:100%; height:130%; filter:brightness(94%) sepia(15%)">

\columnbreak
#### English Oak
A wand for good times and bad, this is a friend as loyal as the wizard who deserves it. Wands of English oak demand partners of strength, courage and fidelity. Less well-known is the propensity for owners of English oak wands to have powerful intuition, and, often, an affinity with the magic of the natural world, with the creatures and plants that are necessary to wizardkind.
#### Maple
Garrick Ollivander found that witches and wizards chosen by maple wands, a beautiful and desirable wood, are by nature travelers and explorers. They are not stay-at-home wands, and prefer ambition in their owner, otherwise their magic grows lackluster. Fresh challenges and regular changes of scene cause this wand to literally shine, burnishing itself as it grows with its partner in ability and status, earning its reputation as the wand of high achievers.
#### Poplar
Poplar wands can be relied upon, wands of consistency, strength and uniform power. Always happiest when working with a witch or wizard of clear moral vision, some wizards joke that a poplar wand has never chosen a politician. However, two of the Ministry’s most accomplished Ministers for Magic, Eldritch Diggory and Evangeline Orpington, were possessors of fine, Ollivander-made poplar wands.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* Redemption. There’s a spark of good in everyone. |
| 3-4 | *Dragon Heartstring:* Community. We have to take care of each other, because no one else will. |
| 5-6 | *Phoenix Feather:* Nature. The natural world is more precious than all of so-called civilization. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *10.5":* An injury to unspoiled wilderness is an injury to me. |
| 3-4 | *11":* I owe my life to the wizard who took me in when my parents died. |
| 5-6 | *13.5":*  It is my duty to preserve and sustain endangered creatures. |
<div style='margin-top: 20px;'></div>

<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum

<img src="https://www.gmbinder.com/images/Pv0sOrL.png" class="cover-image" style="width:200%; top:-310px; left:-1050px; transform:scaleX(-1);"><img src="https://www.gmbinder.com/images/Pv0sOrL.png" class="cover-image" style="width:80%; top:-25px; left:-240px; transform:scaleX(-1);"><img src="https://www.gmbinder.com/images/RbZHChh.png" class="cover-image bgwatercolor" style="width:115%;height:96%; left:-10px; transform:scaleX(-1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/RbZHChh.png" class="cover-image bgwatercolor" style="width:155%; left:-10px; transform:scaleX(-1); filter:brightness(94%) sepia(15%)"><div style="margin: 170px 0px 80px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">© Pottermore Limited</div>

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Brittle:* I am suspicious of strangers and suspect the worst of them. |
| 3-4 | *Slightly Springy:* I speak quite tactlessly, without really thinking through my words. |
| 5-6 | *Quite Bendy:* Don't expect me to save those who can't save themselves. It is nature's way that the strong thrive and the weak perish. |
### Klutz
Maybe you're an incredibly uncoordinated person, or perhaps you inherited a particularly petty curse. Whatever the cause, you continually find yourself in the middle of mishaps and blunders. Since being accident-prone is a very dangerous thing to be in the wizarding world, you tend to be hypervigilant and wary of your surroundings.

**Skill Proficiencies:** Medicine, Perception

**Equipment:** A lucky charm, and a package of plasters
#### Background Feature: Walking Disaster
You've seen so many situations go completely awry that you've started being able to predict all the ways things can go wrong. If you're looking to hinder something or bring about a dangerous accident, you'll have no shortage of ideas.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 10px;'>d6</span> | Wood (Personality Traits) |
|:---:|:--------------|
| 1-2 | Ash           |
| 3-4 | Cypress       |
| 5-6 | Willow        |
<div style='margin-top: 20px;'></div>

#### Ash
The ash wand clings to its one true master and ought not to be passed on or gifted from the original owner, because it will lose power and skill. Witches and wizards best suited to ash wands are not lightly swayed from their beliefs or purposes. However, a brash or over-confident witch or wizard will be disappointed by its effects. The ideal owner may be stubborn, and will certainly be courageous, but never crass or arrogant.

\columnbreak
#### Cypress
Cypress wands are associated with nobility and dying a heroic death, historically. Fortunately, the possessors of cypress wands are rarely called upon to lay down their lives, but doubtless many of them would do so if required. Wands of cypress find their soulmates among the brave, the bold and the self-sacrificing: those who are unafraid to confront the shadows in their own and others’ natures.
#### Willow
Willow is an uncommon wand wood with healing power, and their ideal owner often has some (usually unwarranted) insecurity, however well they may try and hide it. With a handsome appearance and well-founded reputation for enabling advanced, non-verbal magic, the willow wands have consistently selected those of greatest potential, rather than those who feel they have little to learn.

| <span style='padding:0px 15px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* Greater Good. The most noble cause is to lay down our lives to defend others. |
| 3-4 | *Dragon Heartstring:* Respect. All people—rich or poor, powerful or weak, magical or muggle—deserve respect. |
| 5-6 | *Phoenix Feather:* Sincerity. There's no good pretending to be something I'm not.  |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *9":* Someone is depending on me, and I'll never forgive myself if I let them down.  |
| 3-4 | *12.5":* I have to prove to that I'm not a disappointment to my family, mentors or peers.  |
| 5-6 | *14":* I will be fiercely loyal to anyone who doesn't see me for my faults, but for who I am. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Inflexible:* I am slow to trust that others' words are sincere, because of some bad experiences. |
| 3-4 | *Slightly Pliant:* I follow the rules, even if they aren't what's best.  |
| 5-6 | *Very Supple:* I'm always putting my foot in my mouth, invariably insulting or embarrassing others. |
<div style='margin-top: 30px;'></div>

> ##### Variant Feature: Punching Bag
> You may not be coordinated, but at least you've learned how to take a punch. You have resistance to damage dealt by falling, traps or inanimate objects. You also have disadvantage on saving throws made to avoid or resist traps, any rolls made to detect traps and Dexterity (Acrobatics) checks.
<div style='margin-top: 40px;'></div>

<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum
<div style='margin: -34px 0px 260px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;'>Art by Atomhawk / © Pottermore Limited</div><img src='https://www.gmbinder.com/images/fuBoBAT.jpg' class='cover-image' style="width:111%;height:36%; top:-30px; left:-50px"><img src='https://www.gmbinder.com/images/fuBoBAT.jpg' class='cover-image' style="width:111%; top:-50px; left:-50px"><img src='https://www.gmbinder.com/images/Iu6blc4.png' class='cover-image bgwatercolor' style="top:105px; height:110%; transform: scaleX(-1) scaleY(-1); filter:brightness(94%) sepia(15%)">

### Potioneer
More than once, you've been accused of perfectionism, but your attention to detail allows you to succeed where others fail. This trait shines when you turn your focus to brewing potions. You approach situations with drive and vigor, and live with strong conviction in your values and principles.

**Skill Proficiencies:** Herbology, Potion-making

**Tool Proficiencies:** Potioneer's kit

**Equipment:** A potioneer's kit, and a muggle notebook with a ballpoint pen
#### Background Feature: Regular Customer
You're a familiar face to any prominent wizarding apothecary, and as a frequent customer, you get access to new and unusual inventory that potion supplies stores may not want to open up to the public. You've also picked up one common and one uncommon potion recipe of your choice.

<div style='margin-top: 20px;'></div>

| <span style='padding:0px 10px;'>d4</span> | Wood (Personality Traits) |
|:-:|:------------|
| 1 | Acacia      |
| 2 | Elm         |
| 3 | Larch       |
| 4 | Laurel      |
#### Acacia
This very unusual wand wood creates tricky wands that often refuse to produce magic for any but their owner, and also withholds their best effects from all but those most gifted. This makes them difficult to place, and wandmakers often keep only a small stock for those witches or wizards of sufficient subtlety, for acacia is not suited to what is commonly known as ‘bangs-and-smells’ magic. When well-matched, an acacia wand matches any for power, though it is often underrated due to the peculiarity of its temperament.
#### Elm
Elm wands prefer owners with presence, magical dexterity and a certain native dignity. Although some wizards have spread rumors that elm wands’ magic requires blood purity, there have been perfect matches of elm wands who 


\columnbreak
<div style='margin-top: 270px;'></div>

are Muggle-borns. Of all wand woods, elm produces the fewest accidents, the least foolish errors, and the most elegant charms and spells; these are sophisticated wands, capable of highly advanced magic in the right hands.
#### Larch
Larch wands have a reputation for instilling confidence and courage in the user. The celebrated wandmaker Garrick Ollivander found that larch always created wands of hidden talents and unexpected effects, which likewise describes the master who deserves it. It is often the case that the witch or wizard who belongs to the larch wand may never realize the full extent of their considerable talents until paired with it, but that they will then make an exceptional match.
#### Laurel
It is said a laurel wand cannot perform a dishonourable act, although in the owner’s quest for glory, laurel wands can perform powerful and sometimes lethal magic. The laurel wand seems unable to tolerate laziness in a possessor, and in that case, can be won away from their owner most easily. Otherwise, it will cleave happily to its first match and issue a spontaneous zap if another attempts to steal it.

| <span style='padding:0px 15px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* Tradition. The ways of the past must never be forgotten, for they teach us who we are. |
| 3-4 | *Dragon Heartstring:* Aspiration. I work hard to be recognized as the best there is at my craft. |
| 5-6 | *Phoenix Feather:* Live and Let Live. Meddling in the affairs of others only causes trouble. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *9":* I will face any challenge to win the approval of my family. |
| 3-4 | *10.5":* I idolize legendary wizards and measure my deeds against theirs.  |
| 5-6 | *12":* I am the only one carrying on my name, and it is up to me to immortalize it in history. |
<div style='margin-top: 20px;'></div>


<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Hard:* I'm convinced of my work's significance, and blind to my shortcomings and the risk of failure.  |
| 3-4 | *Barely Yielding:* Once I pick a goal, I become obsessed with it to the detriment of everything else in my life. |
| 5-6 | *Quite Flexible:* I'm horribly jealous of anyone who outshines my work. Everywhere I go, I'm surrounded by rivals.  |
<div style='margin-top: 20px;'></div>


### Protector
You have a strong sense of justice and do everything you can to stand up for victims, likely because of an instinctive empathy or your own history of being victimized. Seeing a narcissist take advantage of someone else makes you feel sick. You've made sure you're physically capable of stopping the people you care about from being hurt, so you make an excellent ally to the downtrodden.

**Skill Proficiencies:** Athletics, Intimidation

**Equipment:** A Beater's bat, and a picture of a loved one
#### Background Feature: People's Champ
The way you carry yourself makes people comfortable and confident that you can help them when they're feeling harrassed or imperiled. As long as you live up to your reputation, your noble deeds can make you a shoo-in for prefect, team captain or other small positions of authority.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 10px;'>d10</span> | Wood (Personality Traits) |
|:---:|:--------------|
| 1-2 | Blackthorn    |
| 3-4 | Hawthorn      |
| 5-6 | Mahogany      |
| 7-8 | Rowan         |
| 9-10| Yew           |
<div style='margin-top: 20px;'></div>

#### Blackthorn
A very unusual wand wood, blackthorn wands have the reputation of being best suited to a warrior. One finds blackthorn wands among the Aurors as well as among the denizens of Azkaban. These wands appear to need to pass through danger or hardship with their owners to become truly bonded. Given this condition, the blackthorn wand will become a loyal and faithful servant.
#### Hawthorn
Hawthorn wands may be particularly suited to healing magic, but they are also adept at curses, and it has been generally observed that the hawthorn wand seems most at home with a conflicted nature or a period of turmoil. Hawthorn wands are not easy to master, however, and one should only ever be placed in the hands of a witch or wizard of proven talent. Hawthorn wands have a notable peculiarity: their spells can, when badly handled, backfire.

\columnbreak
#### Mahogany
The mahogany tree symbolizes strength, safety, protectiveness, and practicality, and these traits are mirrored in a mahogany wand’s suitable match. With plenty of power and a knack for transfiguration, the owners of mahogany wands are often reliable and serve as cornerstones for their local wizard community.
#### Rowan
Rowan wood has always been much-favored for wands, because it is reputed to be more protective than any other and renders all manner of defensive charms especially strong and difficult to break. It is also commonly stated that no dark witch or wizard ever owned a rowan wand. Rowan is most happily placed with the clear-headed and the pure-hearted, but this reputation for virtue ought not to fool anyone – these wands frequently outperform others in duels.
#### Yew
Yew wands are among the rarer kinds, and their ideal matches are likewise unusual and occasionally notorious. The wand of yew is reputed to endow the power of life and death, retaining a fearsome reputation in the spheres of duelling and curses. However, a witch or wizard might equally prove a fierce protector. Where wizards have been buried with wands of yew, the wand generally sprouts into a tree guarding the owner’s grave. A yew wand never chooses either a mediocre or a timid owner.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* Charity. I always try to help those in need, no matter what the personal cost. |
| 3-4 | *Dragon Heartstring:* Fairness. No one should get preferential treatment, and no one is above justice.  |
| 5-6 | *Phoenix Feather:* Might. History is written by the victors, and the strong will always win. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *9.5":* I owe a debt I can never repay to someone who once defended me. |
| 3-4 | *10.5":* Nothing is more important than honoring a pledge I make. |
| 5-6 | *13.5":* I protect those who cannot protect themselves. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Very Solid:*  I have little respect for anyone who is not willing to stand up for what is right. |
| 3-4 | *Mildly Flexible:* Secretly, I believe that things would be better if I were a tyrant, ruling over everyone else. |
| 5-6 | *Whippy:* Too often, violence is my answer to almost any situation. |
<div style='margin-top: 20px;'></div>


<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum
<div style='margin: -34px 0px 145px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;'>© Pottermore Limited</div><img src='https://www.gmbinder.com/images/4daS5xo.jpg' class='cover-image' style="width:120%; left:-75px"><img src='https://www.gmbinder.com/images/WQXIOUB.png' class='cover-image bgwatercolor' style="top:-395px; width:100%; transform: scaleX(-1); filter:brightness(94%) sepia(15%)"><img src='https://www.gmbinder.com/images/WQXIOUB.png' class='cover-image bgwatercolor' style="transform: scaleX(-1); filter:brightness(94%) sepia(15%)">

#### Variant Protector: Bully
When you feel powerless, you hurt those weaker than you to regain some semblance of control. It might be a necessary coping mechanism, an assertive demeanor or an innately sadistic nature. You might even be very selective about your victims or only lash out in relatively harmless ways. Regardless, you're a bully and you thrive off of feeling superior.
<div style='margin-top: 20px;'></div>

> ##### Variant Feature: Common Thug
> Everyone who's heard of you has heard of your misdeeds, and they will know to come to you when they need someone to take care of their dirty work. The faint of heart will immediately fear you and try to escape your ire by letting you boss them around.
<div style='margin-top: 40px;'></div>

### Quidditch Fan
Whether your fondest childhood memories were at your local team's matches or you just discovered the sport upon arriving at Hogwarts, you **love** quidditch. It makes complete sense, given your competitive streak and affinity for rough-housing. You use your common sense and ability to take initiative to get by.

**Skill Proficiencies:** Acrobatics, Athletics

**Tool Proficiencies:** Vehicle (Broomstick)

**Equipment:** A quaffle, and a chocolate frog card of your favorite quidditch player
#### Background Feature: Superfan
It seems like you can only think about broomsticks and quaffles. You're always on top of recent matches, the latest brooms, and quidditch tactics. Also, you can easily strike up conversation and build rapport with a fellow enthusiast.

| <span style='padding:0px 10px;'>d6</span> | Wood (Personality Traits) |
|:---:|:----------|
| 1-2 | Cherry    |
| 3-4 | Fir       |
| 5-6 | Spruce    |
<div style='margin-top: 20px;'></div>

#### Cherry
This very rare wand wood creates a wand of strange power, most highly prized by the wizarding students of the school of Mahoutokoro in Japan, where those who own cherry wands have special prestige. The Western wand-purchaser should dispel from their minds any notion that the pink blossom

\columnbreak
<div style='margin-top: 130px;'></div>

of the living tree makes for a frivolous or merely ornamental wand, for cherry wood often makes a wand that possesses truly lethal power, whatever the core.
#### Fir
One wandmaker called wands of fir wood ‘the survivor’s wand’, because he had sold it to three wizards who subsequently passed through mortal peril unscathed. There is no doubt that this wood, coming as it does from the most resilient of trees, produces wands that demand staying power and strength of purpose in their true owners. Fir wands are particularly suited to Transfiguration, and favour owners of focused, strong-minded and, occasionally, intimidating demeanor.
#### Spruce
Spruce wands are ill-matched with cautious or nervous natures, becoming positively dangerous in fumbling fingers. They require a firm hand, because they seem to have their own ideas about what magic it ought to produce. However, when a spruce wand meets its match in a bold spell-caster with a good sense of humor, it becomes a superb helper. Intensely loyal to owners, the wands are capable of producing particularly flamboyant and dramatic effects.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* Friends. I’m loyal to my friends, and anyone else can go soak their head. |
| 3-4 | *Dragon Heartstring:* Retribution. Wrongdoers should suffer the same misery they've inflicted. |
| 5-6 | *Phoenix Feather:* Competition. The struggle to win and survive drives greatness. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *9.5":* I will be incredible at my chosen pursuits, the greatest that ever lived |
| 3-4 | *11":* I'll never forget a crushing defeat or the opponent who dealt it.  |
| 5-6 | *14":* Those who fight beside me are those worth dying for. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Unbending:* My hatred of my enemies is blind and unreasoning. |
| 3-4 | *Fairly Supple:* Despite my best efforts, I am unreliable to my friends. |
| 5-6 | *Very Pliant:* I too often hear veiled insults and threats in innocent words, and I'm quick to anger. |


<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum
### Socialite
You seem to make friends wherever you go. It might be your forceful personality or the delicious gossip, but no matter what it is, people are drawn to you. You enjoy being the center of attention and feel invigorated by lively crowds, but you might get carried away with impressing your admirers.

**Skill Proficiencies:** Deception, Persuasion

**Equipment:** A ring with a family crest or another type of heirloom jewelry, and a peacock feather quill
#### Background Feature: Rumor-Monger
Your skill at making connections has earned you inroads with people in the know. When you attempt to uncover a particularly juicy secret or a dangerous rumor, your sources may be able to help you or point you in the right direction.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 10px;'>d4</span> | Wood (Personality Traits) |
|:---:|:------------|
| 1 | Alder       |
| 2 | Apple       |
| 3 | Aspen       |
| 4 | Pear        |
#### Alder
While the wood itself is unyielding, the ideal owner of an alder wand is not stubborn or obstinate, but often helpful, considerate and most likeable. When an alder wand is happily placed, it becomes a magnificent, loyal helpmate. Of all wand types, alder is best suited to non-verbal spell work, whence comes its reputation for being suitable only for the most advanced witches and wizards.
#### Apple
Applewood wands are not made in great numbers. They are powerful and best suited to an owner of high aims and ideals, as this wood mixes poorly with Dark magic. It is said that the possessor of an apple wand will be well-loved and long-lived, and wizards of great personal charm often find their perfect match in an applewood wand.
#### Aspen
Wand-quality aspen wood is prized for its stylish resemblance to ivory and usually outstanding charmwork. The proper owner of the aspen wand is often an accomplished duellist, for the aspen wand is particularly suited to martial magic. An infamous and secretive eighteenth-century duelling club, the Silver Spears, only admitted owners of aspen wands. Owners are generally strong-minded and determined, likely to be attracted by quests; this is a wand for revolutionaries.
#### Pear
The golden-toned wood of pear produces wands of splendid magical powers. Possessors of pear wands are usually popular and well-respected, and no one knows of a single instance where a pear wand was in the possession of a Dark witch or wizard. Pear wands are among the most resilient, and they commonly keep a remarkable appearance of newness, even after many years of hard use.
<div style='margin-top: 20px;'></div>

\columnbreak

<!--<img src="https://www.gmbinder.com/images/W7kvPfG.png" class="cover-image bgwatercolor" style="width:100%; top:-350px; transform: scaleX(-1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/ShMie2y.png" class="cover-image bgwatercolor" style="width:110%; top:-100px; left: inherit; right:0px; filter:brightness(94%) sepia(15%)">-->

| <span style='padding:0px 15px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* People. I like seeing smiles on people’s faces. That’s all that matters. |
| 3-4 | *Dragon Heartstring:* Might. The strong are meant to lead and the weak will follow.  |
| 5-6 | *Phoenix Feather:* Destiny. Nothing and no one can steer me away from my higher calling. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *10":* I want to be famous, whatever it takes. |
| 3-4 | *12":* Family and institutions are most important--friends and sycophants come and go. |
| 5-6 | *13":* It is my duty to lead and inspire others. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Solid:* I'm never satisfied with what I have--I always want more. |
| 3-4 | *Reasonably Springy:* I secretly believe that everyone is beneath me. |
| 5-6 | *Swishy:* I'm a (misguided) romantic and a sucker for a pretty face. |
<div style='margin-top: 40px;'></div>


#### Variant Socialite: Follower
Instead of building social status through the force of your own personality, you've found success by following someone who is more influential or popular than you are. You know how to stay useful to them and use their reputation to influence others. Whether you see yourself as a hero's sidekick or a bully's sycophant, you're happy to watch from the sidelines and be second best.
<div style='margin-top: 20px;'></div>

> ##### Variant Feature: Forgettable Face
> If a person were to take you at face value, you'd come across as inconsequential and they would assume your unimportance. It's also unusually difficult to pick your face out from a crowd, making it easier for you to blend in and harder for someone to blame you in particular.
<div style='margin-top: 50px;'></div>

<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum

### Troublemaker
Whether you consider yourself a purveyor of pranks or simply a curious soul, trouble tends to follow you wherever you go. As a result, you've learned to be a little more careful and avoid the obvious pitfalls of rule-breaking. That's very useful, as there's no shortage of messes you get yourself into.

**Skill Proficiencies:** Sleight of Hand, Stealth

**Equipment:** A fake hall pass, and a small pack of Exploding Whizz Poppers
#### Background Feature: Creative Thinker
Having found yourself in some predicaments, you're quick to look for a way out; "work smart, not hard" is your motto. Your invented alibis always sound half-reasonable to others, and you're good at finding figurative and literal shortcuts. Also, rule-breakers are more willing to share their secrets with you.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 10px;'>d4</span> | Wood (Personality Traits) |
|:-:|:----------|
| 1 | Dogwood   |
| 2 | Ebony     |
| 3 | Elder     |
| 4 | Holly     |
#### Dogwood
Dogwood wands are quirky, noisy, and mischievous; they have playful natures and insist upon partners who provide excitement and fun. It would be quite wrong to think dogwood wands aren’t capable of serious magic; they perform outstanding spells in difficult conditions, and with a suitably clever owner, can produce dazzling enchantments.
#### Ebony
Ebony wands are impressive in appearance and reputation, being highly suited to Transfiguration and combative magic. Ebony is happiest in the hand of those with the courage to be themselves. Frequently non-conformist or comfortable with being an outsider, the ebony wand’s perfect match will not be swayed lightly from their beliefs and purpose.
#### Elder
The rarest wand wood of all, and reputed to be unlucky (a baseless superstition), elder wands are trickiest to master. They contain powerful magic, but scorn any owner who is not a superior caster; it takes a remarkable wizard to keep an elder wand. The truth is that only a highly unusual person will find their perfect match in elder, but that witch or wizard in question is certainly marked out for a special destiny.

\columnbreak
#### Holly
Holly is one of the rarer kinds of wand woods; traditionally considered protective, it works most happily for those who may need help overcoming a tendency to anger and impetuosity. At the same time, holly wands often choose owners engaged in some dangerous and often spiritual quest. Holly is a notoriously difficult wood to team with phoenix feather, but should such a pairing find its match, nothing and nobody should stand in their way.
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 20px;'>d6</span>  | Core (Ideal) |
|:---:|:----------------------------------------------------|
| 1-2 | *Unicorn Hair:* Aspiration. I'm going to prove that I'm worthy of a better life. |
| 3-4 | *Dragon Heartstring:* Cynicism. I only help the people who help me; that’s how you survive. |
| 5-6 | *Phoenix Feather:* Freedom. When people follow rules blindly, they imprison themselves. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Length (Bond) |
|:---:|:-----------------------------------------------------|
| 1-2 | *9":* An impudent joke once earned me a horrible beating, and I will take my revenge on any bully I encounter. |
| 3-4 | *11.5":* I will do anything to prove myself superior to my hated rival. |
| 5-6 | *13.5":* No one else is going to have to endure the hardships I've been through. |
<div style='margin-top: 20px;'></div>

| <span style='padding:0px 15px;'>d6</span>  | Flexibility (Flaw) |
|:---:|:----------------------------------------------------------|
| 1-2 | *Stiff:* Once someone questions my courage, I never back down no matter how dangerous the situation. |
| 3-4 | *Slightly Bendy:* I remember every insult I've received and nurse a silent resentment toward anyone who's ever wronged me. |
| 5-6 | *Flexible:* I'll say anything to avoid having to do extra work. |


<div class='footnote'>Part 1 | Wands (Backgrounds)</div>

\pagebreakNum
# Chapter 5: Wizarding Equipment
Every witch and wizard remembers their first visit to Diagon Alley: a bustling street lined with vendors hawking their extraordinary wares. The vibrant energy reaches its peak during school shopping in the summer. From broomsticks to boomslang skin to Bertie Bott's Every Flavour Beans, you can find it in those wondrous stores. Being properly equipped is essential in the wizarding world, whether you're buying school supplies for your first year at Hogwarts or stocking up for cursebreaking an ancient tomb.
## Starting Equipment
Wizards and witches start their journey at a very young age and most of their expenses are covered by their parents or Hogwarts. Because of this, a typical student will be given a Student's Pack and a small amount of spending money.

</br>

> ##### Equipment Packs and Family Finances
> Because a first-year student at Hogwarts is typically 11 years old, a character starting at level 1 will depend on their family to buy their school supplies. Their financial situation decides how much spending money they start with and what quality of equipment they receive. Choose from the options below, and use this starting wealth instead of the starting wealth granted by your background.
>
> **Hand-Me-Down Student's Pack.** Includes a patched-up schoolbag, 3 sets of darned and worn work robes (black) with name tags sewn in, a crumpled pointed hat (black), a 10-foot roll of parchment, a quill, and a bottle of black ink. When receiving this pack for the first time, it also includes a pouch containing 5 sickles.
>
> **Standard Student's Pack.** Includes a standard schoolbag, 3 sets of plain work robes (black) with name tags sewn in, a plain pointed hat (black), 2 10-foot rolls of parchment, 3 quills, and 2 bottles of black ink. When receiving this pack for the first time, it also includes a pouch containing 15 sickles.
>
> **Wealthy Student's Pack.** Includes a rip-proof schoolbag, 3 sets of luxurious work robes (black) with name tags sewn in, a fancy pointed hat (black), 3 10-foot rolls of parchment, 5 quills, 2 bottles of black ink, a bottle of emerald green ink, and a bottle of scarlet ink. When receiving this pack for the first time, it also includes a pouch containing 2 galleons.

\columnbreak

Hogwarts also requires some fundamental supplies from a potioneer's kit, like a full-size cauldron and measuring scales, and herbologist's tools, like dragon-hide gloves. Despite them being on the official shopping list, these items won't be carried around by your average Hogwarts student and require the appropriate toolset to keep them handy.
## Tools
A tool helps you to do a number of things, usually associated with a Hogwarts subject or wizarding profession. A defining factor of all of these tools is that they come in a compact and convenient container. These cases will either fit within or alongside a standard schoolbag.

**Astronomer's Tools.** This tubular case contains a featherlight-charmed travel telescope, a sextant, an astro-compass, several star charts, spare parchment, ink and a quill.

**Curse-breakers' Tools.** The Curse-breakers' tools include a curse sneakoscope, a compact secrecy sensor, an eye loupe set, a collapsible retriever tool with a hook on the end, a small mirror and a very large pair of tweezers. Proficiency with these tools lets you add your proficiency bonus to any ability check you make using finite incantatem or to remove a curse from an object or an area.

**Diviner's Kit.** The Diviner's kit is a small carpet bag containing a wide range of divination equipment, including tea leaves, a tea cup and saucer, a travel tea pot, grindylow bones, rune inscribed sticks, a deck of tarot cards and a small crystal ball. Proficiency with this kit allows you to make more accurate predictions with your Divination Abilities. Divination Abilities cannot be performed without this kit.

**Herbologist's Tools.** This set of tools includes a trowel, hand cultivator, pruning shears, dragon-hide gloves, twine, small burlap sacks, a few small pots and a pair of earmuffs.

**Potioneer's Kit.** The Potioneer's Kit includes a set of brass scales, silver knife, cutting board, mortar and pestle, measuring cups, eye dropper and vials, jars and flasks, as well as some staple ingredients that aren't included in recipes.

<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
## Wealth
### Optional Coinage
Wizard money can often seem strange and incomprehensible to Muggles, so they may be more comfortable using terms they're familiar with, like gold pieces. However, it's actually not too hard to keep straight the values of the copper, silver, and gold coins issued by Gringott’s, when you convert it to Muggle value (United States Dollars are used in the following examples). 

The copper Knut is the smallest denomination. 29 Knuts make one silver Sickle. 17 Sickles (or 493 Knuts) make one Galleon, the large gold coin. Approximately speaking, one Knut is worth one nickel ($0.05), which means a Sickle is $1.45 and a Galleon is $24.65. A Gringott’s Standard ruby is worth 20 galleons (or $493).

#####  Exchange Rates (Rounded)
| Name    | Conversion  | USD    | GBP    | D&D    |
|:--------|------------:|-------:|-------:|-------:|
| Knut    | --          | $0.05  | £0.04  | 1/5 cp |
| Sickle  | 29 Knuts    | $1.50  | £1.20  | 6 cp   |
| Galleon | 17 Sickles  | $25.00 | £20.00 | 1 gp   |
| Ruby    | 20 Galleons | $500.00 | £400.00 | 2 pp |

## Cloaks (Armor)
In the wizarding world, mundane armor is useless against spells. The best way to survive a duel is to avoid being hit.

**Winter Cloak.** One of the required supplies for attendance at Hogwarts, this heavy winter cloak keeps its wearer quite warm in cold, snowy winters. A winter cloak helps conceal a duelist's intended movements from their opponents, but the weight and bulk can be a hindrance.

**Silk Cloak.** All of the concealing benefits of a cloak with none of the unwieldy bulk, a silk cloak is the preferred travel wear of experienced duelists. The smooth and lightweight material allows for a full range of movement and nimbleness.

**Shield Cloak.** Popular in times of war and always in high demand among Aurors, a shield cloak is a standard silk cloak that's been enchanted with the *protego* charm. While nowhere near as effective as the actual Shield Charm, the enchantment provides minor spell resistance that can make the difference between life and death.

**Demiguise Cloak.** A demiguise cloak is a rough cloak woven with a thick silvery-white fiber. The outer layer is made from the hair of a Demiguise, a rare and elusive magical creature from Asia with the ability to turn invisible at will. The cloak functions as perfect camouflage from all angles, but when the wearer moves, there is a perceptible delay before the cloak matches its new surroundings. In combat, this often gives its wearer a visible but blurred appearance.

**Disillusionment Cloak.** Created by weaving *pellucidi pellis* and a few other enchantments into a silk cloak, the disillusionment cloak has no delay, functioning as an effective invisibility cloak. However, in a certain light, an onlooker may be able to see a slightly distorted outline of the cloak's shape. In combat, it's quite effective, but as with any invisibility cloak, the wearer becomes partially visible if they open it to cast a spell.
### Donning and Doffing Cloaks
The time it takes to don (put on) a cloak is one action, and the time it takes to doff (take off) a cloak is also one action.
## Wizarding Gear
Coming soon!

<div class='classTable wide' style='margin: 80px 0px 0px 0px;'>

##### Armor
| Cloak | Cost | Armor Class (AC) | Stealth | Weight |
|:------|:----:|:-----------------|:--------|-------:|
| Winter Cloak | 9 g | 11 + Dex modifier (max 2) | Disadvantage | 20 lb. |
| Silk Cloak | 25 g | 11 + Dex modifier | — | 12 lb. |
| Shield Cloak | 75 g  | 12 + Dex modifier | ─ | 12 lb. |
| Demiguise Cloak | 400 g | 13 + Dex modifier (max 2) | Advantage | 18 lb. |
| Disillusionment Cloak | 750 g | 14 + Dex Modifier | Advantage | 10 lb. |
</div>

<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum

<!--<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum-->
## Potions
Potions fulfill a variety of purposes that spells alone cannot accomplish, and the more adventuresome wizards know that having the right potions at hand can be the difference between life and death. Almost every potion must be drunk to receive its effects, but if not, it will be clearly stated.

The below tables connect new potion names to equivalent 5e potion or spell names. Players shouldn't assume that just because there's an equivalent 5e potion or spell, the Harry Potter potion will operate in exactly the same way or have the exact same description.
<div class='classTable' style='margin:40px 0px 60px;'>
<span style="text-align:center">

##### Potion Conversions</span>
| New Potion                | Equivalent 5e Potion/Spell|
|:-------------------------:|:-------------------------:|
| Antidote of Common Poisons| Antitoxin                 |
| Baruffio's Brain Elixir   | Enhance Ability           |
| Confusing Concoction      | Confusion                 |
| Draught of Peace          | Calm Emotions             |
| Essence of Dittany        | Potion of Supreme Healing, Regenerate |
| Felix Felicis             | Foresight                 |
| Fire Protection Potion    | Potion of Fire Resistance |
| Fungiface Potion          | Vicious Mockery           |
| Gillyweed                 | Alter Self                |
| Girding Potion            | False Life                |
| Invigoration Draught      | Potion of Superior Healing    |
| Murtlap Essence           | Potion of Greater Healing |
| Shrinking Solution        | Potion of Diminution      |
| Sleeping Draught          | Sleep                     |
| Star Grass Salve          | Potion of Healing         |
| Strengthening Solution    | Potion of Hill Giant Strength  |
| Swelling Solution         | Potion of Growth          |
| Veritaserum               | Zone of Truth             |
| Vitamix Potion            | Enhance Ability           |
| Volubilis Potion          | Actor (Feat)                |
| Wideye Potion             | Potion of Vitality        |
| Wound-cleaning Potion     | Healer's Kit              |
</div>

\columnbreak
### Antidotes
If a potion is listed as an antidote to another potion or spell, the effects of that potion or spell immediately end. If the antidote has a duration, you are immune to the effects of the countered potions or spells for the duration.

<div class='classTable' style='margin:40px 0px 50px;'>
<span style="text-align:center">

##### Poison Conversions</span>
| New Potion                | Equivalent 5e Potion/Spell|
|:-------------------------:|:-------------------------:|
| Bloodroot Poison          | Pale Tincture             |
| Death-Cap Draught         | Purple Worm Poison        |
| Draught of Living Death   | Imprisonment              |
| Essence of Insanity       | Eyebite                   |
| Garrotting Gas            | Drow Poison               |
| Herbicide Potion          | Blight                    |
| Moonseed Poison           | Serpent's Venom           |
| Noxious Potion            | Burnt Othur Fumes         |
| Weedosoros                | Wyvern Poison             |
</div>

> ##### Looking at Love Potions
> The morality of love potions is questionable at best. While love potions are often handled humorously in the original series, we must recognize the importance of consent. Love potions do not allow for consent and should not be used to cross any character's boundaries. If you are going to play W&W with love potions, please have a conversation with your table to ensure everyone is comfortable and will behave respectfully. Otherwise, do not include them in your game.

___
<div class='classTable' style='margin:30px 0px 60px;'>
<span style="text-align:center">

##### Love Potion Conversions</span>
| New Potion                | Equivalent 5e Potion/Spell|
|:-------------------------:|:-------------------------:|
| Amortentia                | Dominate Person           |
| Beguiling Bubbles         | Philter of Love           |
| Gregory's Unctuous Unction| Charm Person              |
| Heartbreak Teardrops      | Suggestion                |
| Kissing Concoction        | Compulsion                |
| Twilight Moonbeams        | Enthrall                  |
</div>


<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
<div class='spellList' style='margin-top:15px'>

### Potion List
##### Common Potions
- Antidote of Common Poisons
- Babbling Beverage
- Baneberry Poison
- Blemish Blitzer
- Confusing Concoction
- Cupid Crystals
- Doxycide
- Dr. Ubbly's Oblivious Unction
- Dreamless Sleep Potion
- Elixir to Induce Euphoria
- Forgetfulness Potion
- Fungiface Potion
- Garrotting Gas
- Heartbreak Teardrops
- Herbicide Potion
- Hiccoughing Solution
- Moonseed Poison
- Oculus Potion
- Pepperup Potion
- Pet Tonic
- Regerminating Potion
- Shrinking Solution
- Star Grass Salve
- Swelling Solution
- Wound-Cleaning Potion
##### Uncommon Potions
- Aging Potion
- Antidote of Uncommon Poisons
- Baruffio's Brain Elixir
- Beautification Potion
- Befuddlement Draught
- Beguiling Bubbles
- Blood-Replenishing Potion
- Bloodroot Poison
- Draught of Peace
- Exstimulo Potion
- Fatiguing Fusion
- Fire Protection Potion
- Gillyweed
- Girding Potion
- Gregory's Unctuous Unction
- Memory Potion
- Murtlap Essence
- Noxious Potion
- Sleeping Draught
- Strengthening Solution
- Twilight Moonbeams
- Vitamix Potion
- Volubilis Potion
- Wideye Potion
- Wiggenweld Potion
##### Rare Potions
- Erumpent Potion
- Essence of Insanity
- Hate Potion
- Invigoration Draught
- Invisibility Potion
- Kissing Concoction
- Mandrake Restorative Draught
- Skele-Gro
- Weedosoros
- Wit-Sharpening Potion
##### Very Rare Potions
- Amortentia
- Death-Cap Draught
- Draught of Living Death
- Essence of Dittany
- Polyjuice Potion
- Wolfsbane Potion
##### Legendary Potions
- Drink of Despair
- Felix Felicis
- Veritaserum
</div>

\columnbreak

<div style="text-align:right; margin: 475px -370px 20px 0px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk / © Pottermore Limited
</div>

<img src='https://www.gmbinder.com/images/d3uBeC2.jpg' class='cover-image' style="width:141%; height:60%; top:inherit; bottom:10px; left:-180px"><img src='https://www.gmbinder.com/images/d3uBeC2.jpg' class='cover-image' style="width:141%;  top:inherit; bottom:110px; left:-150px">
<img src='https://www.gmbinder.com/images/aL7n0dS.png' class='cover-image bgwatercolor' style="top:375px; height:90%; transform: scaleX(-1); filter:brightness(94%) sepia(15%)"><img src='https://www.gmbinder.com/images/Iu6blc4.png' class='cover-image bgwatercolor' style="top:-435px; height:100%; transform: scaleX(-1); filter:brightness(94%) sepia(15%)">

<img src="https://www.gmbinder.com/images/gezbRSW.png" class="cover-image bgwatercolor" style="width:102%; height:85%; top:inherit;bottom:-458px; transform: scaleX(-1) scaleY(-1) rotate(-5deg); filter:brightness(94%) sepia(15%)">

<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
#### Aging Potion 
*Potion, uncommon*
___
When you drink this potion, your age is increased by 4d10 years for 1 hour. This effect authentically changes your age, but doesn't reduce your lifespan or introduce maladies due to aging. One quarter, one half, or three quarters of this potion may be drunk, modifying the effect to 1d10, 2d10, or 3d10.
___
#### Amortentia 
*Love potion, very rare* 
___
When a being drinks this potion, they are overwhelmingly charmed by the brewer of this potion for 1 week. The charmed subject believes the brewer to be their one true love and will perform any request the brewer asks, to the best of their ability. All thoughts will be colored by a powerful obsession with the brewer, but their personality will otherwise be unchanged. This charmed effect can only be removed by an antidote to this potion.
___
#### Antidote of Common Poisons 
*Potion, common* 
___
When you drink this potion, simple poisons in your system are neutralized and you gain advantage on saving throws against poison for 1 hour. If you took poison damage in the previous minute, you regain half of your hit points lost to poison damage, up to a maximum of 15 hit points. 

**Antidote to:** Baneberry Poison, Doxycide, Garrotting Gas, Moonseed Poison
___


<div style="text-align: right; margin: -20px 50px 0px 0; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

#### Antidote of Uncommon Poisons 
*Potion, uncommon* 
___

<img src='https://www.gmbinder.com/images/flSGCdA.png' style='width:120px; margin: -75px -35px -10px -40px; float:right;transform:rotate(5deg);'>

When you drink this potion, this more </br>potent antidote counteracts poisons and </br>you gain advantage on saving throws against </br>poison for 1 hour. If you took poison damage </br>in the previous minute, you regain all of your </br>hit points lost to poison damage, up to a </br>maximum of 30 hit points. 

**Antidote to:** Baneberry Poison, Bloodroot Poison, Doxycide, Garrotting Gas, Moonseed Poison, Noxious Potion
___
#### Babbling Beverage
*Potion, common*
___
When you drink this potion, every word you try to say comes out as gibberish or complete nonsense for the next 1 minute. 
___
#### Baneberry Poison 
*Poison, common* 
___
While this poison doesn't actually cause any harm in the body, its toxins interfere with blood clotting and produce an overall sickly feeling. A creature that ingests this poison must succeed on a DC 13 Constitution saving throw or become poisoned. The poisoned creature must repeat the saving throw every 24 hours. 

Until this poison ends, the creature can’t be healed by any means. After seven successful saving throws, the effect ends and the creature can heal normally.
___

<div style="margin: 90px 0 -110px -110px; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Niantic, Inc.
</div>
<img src='https://vignette.wikia.nocookie.net/harrypotterwizardsunite/images/7/73/Baruffio%27s_Brain_Elixir.png/revision/latest?cb=20190624230320' style='width:80px; margin: 0 -10px -10px -20px; float:left;'>

#### Baruffio's Brain Elixir
*Potion, uncommon* 
___
  When you drink this potion, you have advantage     on Intelligence checks for 1 hour. Your thoughts       become louder and faster, making it easy to       focus.

      **Antidote to:** Befuddlement Draught,       *confundo*, Confusing Concoction, *infirma       cerebra*
___
#### Beautification Potion 
*Potion, uncommon*
___

<img src='https://www.gmbinder.com/images/NX5R8RK.png' style='width:120px; margin: -80px -35px 0px -5px; float:right;'>

When you drink this potion, your appearance is transformed to be more attractive for 10 minutes. For the duration, when you make a Charisma (Deception), Charisma (Performance) or Charisma (Persuasion) check, you roll a d4 and add the number rolled to the check.
___

<div style="text-align:right; margin: 10px -28px -30px 0; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

___
#### Befuddlement Draught
*Potion, uncommon* 
___
When you drink this potion, you become belligerent and reckless for 1 hour. For the duration, you have disadvantage on Intelligence checks and Wisdom checks, and you have advantage on saving throws against being frightened from any source other than a Dementor.
___
#### Beguiling Bubbles
*Love potion, uncommon* 
___
When a being drinks this potion, they become charmed by a chosen being for 1 hour. The chosen being is selected by the brewer speaking their name into the potion during brewing. If the chosen being is someone the charmed subject would normally be attracted to, they regard that being as their true love while they are charmed.
___
#### Blemish Blitzer 
*Potion, common* 
___
This specially formulated potion will magically remove any acne or blemishes from your face when applied. 

**Antidote to:** Fungiface Potion, *furnunculus*
___
#### Blood-Replenishing Potion 
*Potion, uncommon* 
___
Typically administered in an emergency, this healing potion helps replenish blood lost from injuries. If the next rest you take is a short rest, the amount of hit points gained from rolling hit dice is doubled during that short rest. If the next rest you take is a long rest, you regain all spent hit dice.

**Antidote to:** Baneberry Poison, Bloodroot Poison
___

<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
#### Bloodroot Poison 
*Poison, uncommon*
___
The Bloodroot Poison gets into the bloodstream and causes a very gradual internal necrosis. A creature that ingests this poison must succeed on a DC 16 Constitution saving throw or take 7 (2d6) poison damage and become poisoned. The poisoned creature must repeat the saving throw every 24 hours, taking 7 (2d6) poison damage on a failed save. 

Until this poison ends, the damage the poison deals can’t be healed by any means. After seven successful saving throws, the effect ends and the creature can heal normally.
___
#### Confusing Concoction 
*Potion, common* 
___
When you drink this potion, you become utterly discombobulated for 6 seconds. You can’t take actions or reactions and you roll a d10. If you roll 1-8, you must use all of your movement to move in a random direction. To determine the direction, assign a direction to each number 1-8. If you roll a 9-10, you don't move.
___
#### Cupid Crystals 
*Love potion, common* 
___
When a being drinks this potion, they will become infatuated with the next being they see within 10 minutes. They become charmed by that being for 1 hour.
___
#### Death-Cap Draught
*Poison, very rare* 
___
Death cap mushrooms are the key ingredient to one of the most deadly poisons. A creature that ingests this poison must make a DC 19 Constitution saving throw, taking 84 (24d6) poison damage and becoming poisoned for 1 day on a failed save, or half as much damage and poisoned for 1 minute on a successful one.
___
#### Doxycide 
*Poison, common* 

<div style="text-align:right; margin: -45px 105px 15px 0; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore</br>Limited
</div>

<img src='https://www.gmbinder.com/images/yQdM3fw.png' style='width:100px; margin: -65px -10px 0px 0px; float:right; transform: scaleX(1) rotate(-4deg);'>

___
Delivered as a mist via a spray bottle, this mild poison is a household staple to deal with pests. A creature that inhales this poison must succeed on a DC 13 Constitution saving throw, taking 2 (1d4) poison damage on a failed save, or half as much damage on a successful one. 

If the victim of this poison is a tiny Beast, it is paralyzed for 1 hour on a failed save.
___
#### Dr. Ubbly's Oblivious Unction 
*Potion, common* 
___
When you drink this potion, your brain's perception is softened for 1 hour to protect it from harmful thoughts. For the duration, you have disadvantage on Wisdom checks. 

\columnbreak

If you are targeted by *legilimens*, you can make a Wisdom saving throw to resist its initial effects, and if you are targeted by *imperio*, you have advantage on the first Charisma saving throw.
___
#### Draught of Living Death 
*Poison, very rare* 
___
The drinker of this infamous and challenging poison falls into a deep sleep and can't be awoken by any means, aside from administering an antidote. The creature will breathe normally, but cannot be suffocated in this state. It also doesn't need to eat or drink. The creature will age normally, and it can die of old age while under the effects of this poison.
___

<div style="margin: -20px 0 -20px -90px; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore </br>Limited
</div>
<img src='https://www.gmbinder.com/images/HcRL3wM.png' style='width:90px; margin: -5px -10px -10px -45px; float:left;'>

#### Draught of Peace 
*Potion, uncommon* 
___
When you drink this potion, all strong emotions are suppressed for 1 hour, putting you into a neutral and relaxed disposition. Any charmed or frightened   condition is removed and you have advantage on     saving throws against being charmed or frightened.      Unfortunately, the feeling of this potion wearing off      has been described as experiencing all of the     suppressed emotions at once, and some suppressed   conditions may resume. 

Additionally, if you are hostile, you will become indifferent to the targets of your hostility. This indifference ends if you are attacked or harmed by a spell or if you witnesses any of your friends being harmed.

**Antidote to:** Beguiling Bubbles, Cupid Crystals, Elixir to Induce Euphoria, *exhilaro*, Gregory's Unctuous Unction, Heartbreak Teardrops, Twilight Moonbeams
___
#### Dreamless Sleep Potion 
*Potion, common* 
___
When you drink this potion, you immediately fall asleep and gain the benefits of a long rest after 4 hours of uninterrupted sleep. However, your sleep is far deeper than usual, and someone using their action to shake you or taking damage is the only way for you to wake before 4 hours have passed.
___
#### Drink of Despair 
*Poison, legendary* 
___
When a creature drinks this fabled poison, it hallucinates all of its worst fears and memories, vividly reexperiencing its deepest regrets and darkest traumas. It is incapacitated for 30 seconds, it is reduced to 1 hit point and its gains 4 levels of exhaustion.
___

#### Elixir to Induce Euphoria 
*Potion, common* 
___
When you drink this potion, your emotions are overpowered by a sudden inexplicable happiness, with the side effects of spontaneous singing and nose-tweaking. You gain resistance to psychic damage for 1 hour. For the duration, you have disadvantage on Dexterity (Stealth), Charisma (Intimidation), and Charisma (Deception) checks.
___

<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
#### Erumpent Potion 
*Potion, rare* 
___
As an action, you can throw a bottle of Erumpent Potion at a point up to 60 feet away, releasing a violent explosion and shockwave. Each creature within 10 feet of that point must make a DC 14 Dexterity saving throw, taking 10d6 bludgeoning damage on a failed save, or half as much damage on a successful one. Each creature within 30 feet of that point takes 4d8 thunder damage. This potion is highly volatile and will explode if it is poured out of its container.
___
#### Essence of Dittany 
*Potion, very rare* 
___
This highly concentrated liquid rapidly heals and regenerates open wounds, helping you regain 10d4 + 20 hit points when applied. If the target has lost body members (fingers, legs, and so on) and the severed part is held to its place, applying this potion causes the limb to heal back on immediately.
___
#### Essence of Insanity 
*Poison, rare* 
___
Instead of attacking the body, this oil attacks the mind. A creature that makes contact with this poison is overwhelmed with paranoia and becomes poisoned for 1 hour. It is frightened of the nearest creature for the duration. On its next turn, the victim must take the dash action and move away from that creature by the safest and shortest available route, unless there is nowhere to move.
___
#### Exstimulo Potion 
*Potion, uncommon* 
___
<img src='https://vignette.wikia.nocookie.net/harrypotter/images/e/e5/Exstimulo_Potion.png/revision/latest?cb=20201115005039' style='width:110px; margin: -65px -20px 0px 10px; float:right;'>

When you drink this potion, the next spell you cast within the next 8 hours will be as if it were cast using a spell slot one level higher than its original level.

<div style="text-align:right; margin: 40px 0 -45px 0; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Niantic, Inc.
</div>

#### Fatiguing Fusion 
*Poison, uncommon* 
___
A creature that ingests or inhales this </br>tiresome poison must succeed on a DC 13 Constitution saving throw or gain 3 levels of exhaustion. This poison cannot cause you to reach more than 5 levels of exhaustion.
___
#### Felix Felicis 
*Potion, legendary* 
___
Also known as "liquid luck," this potion makes you exceptionally lucky for 1d4 hours, to the point of succeeding at everything you attempt. For the duration, your Charisma score is raised to 21, you can’t be surprised and have advantage on attack rolls, ability checks, and saving throws. Additionally, other creatures have disadvantage on attack rolls against you for the duration. 

\columnbreak

This potion has been stated to greatly resemble molten gold. It is meant to be used sparingly, however, as it causes giddiness, recklessness, and dangerous overconfidence if taken in excess. Felix Felicis is highly toxic in large quantities.
___
#### Fire Protection Potion 
*Potion, uncommon* 
___
When you drink this potion, you gain </br>resistance to fire damage for 1 hour.
___

<div style="text-align: right; margin: -95px -10px 50px 220px; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore </br>Limited
</div>
<img src='https://www.gmbinder.com/images/s8fRwJp.png' style='width:90px; margin: -60px 0px 10px 0px; float:right; transform: scaleX(-1) rotate(2deg);'>

#### Forgetfulness Potion 
*Potion, common* 
___
When you drink this potion, you forget everything you perceived in the last minute and you won't be able to remember anything you perceive in the next 10 minutes.
___
#### Fungiface Potion 
*Potion, common* 
___
When you drink this potion, you gain the effects of the *furnunculus* spell, sprouting dense and itchy mushrooms on your face instead of pimples. This effect lasts 1 hour.
___
#### Garrotting Gas 
*Poison, common* 
___
This gas produces a choking or suffocating sensation, which, given the fact it's colorless, can be quite dangerous. A creature that inhales this poison must succeed on a DC 13 Constitution saving throw or be poisoned for 1 hour. If the saving throw fails by 5 or more, the creature is unconscious while poisoned in this way. The creature wakes up if it takes damage or a creature shakes it awake as an action. 

As an action, you can throw a bottle of Garrotting Gas at a point up to 60 feet away, releasing the gas and exposing creatures within 5 feet of that point.
___
#### Gillyweed 
*Potion, uncommon* 
___
When you eat this plant, your body adapts to an aquatic environment, sprouting gills and growing webbing between your fingers for 1 hour. You can breathe underwater and gain a swimming speed equal to your walking speed. However, you                 lose the ability to breathe air, following the rules for                     suffocating if you emerge from water.
___

<img src='https://www.gmbinder.com/images/BZsURYw.png' style='width:90px; margin: -35px 10px 0px -25px; float:left; transform:rotate(-4deg);'>

#### Girding Potion
*Potion, uncommon*
___
When you drink this potion, you gain 6d4 + 6 temporary hit points for 1 hour. This feels like an abnormal amount of physical stamina and pain tolerance.

<div style="margin: 20px 0 15px 0px; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

___
<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
#### Gregory's Unctuous Unction
*Love potion, uncommon* 
___
When you drink this potion, you are charmed by the giver of the potion for 1 hour. The charmed subject believes the giver is their very best friend.
___

<div style="text-align: right; margin: -15px -10px -20px 220px; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore </br>Limited
</div>
<img src='https://www.gmbinder.com/images/T0ZBRAg.png' style='width:140px; margin: 15px -15px 10px -10px; float:right;transform:scaleX(-1);'>

#### Hate Potion 
*Love potion, rare* 
___
When a being drinks this potion, they view a chosen being as their most hated enemy for 10 minutes. If the brewer does not select a chosen being by speaking their name into the potion during brewing, the drinker will be hostile towards the next being they see within the potion's duration. If this potion is used as an antidote, it has no effect beyond acting as an antidote for the same duration. 

**Antidote to:** Amortentia, Beguiling Bubbles, Cupid Crystals, Gregory's Unctuous Unction, Heartbreak Teardrops, Kissing Concoction, Twilight Moonbeams
___
#### Heartbreak Teardrops 
*Love potion, common* 
___
When a being drinks this potion, they are overcome with the fear of being rejected by the object of their desire for 1 hour. If no relationship or attraction exists, a new one will be magically created. The being is susceptible to the next suggested course of action to try to avoid rejection. The suggestion does not need to logically prevent rejection, but it must be reasonable and not be obviously harmful. It pursues the course of action you described to the best of its ability, until the course of action is complete or until the potion's effect wears off.
___

<img src='https://www.gmbinder.com/images/DOfHvPr.png' style='width:100px; margin: 0 -10px -10px -25px; float:left; transform:rotate(2deg);'>

#### Herbicide Potion 
*Poison, common* 
___
When this poison is poured directly on a magical plant, the plant immediately withers and dies.  There is only enough poison to affect a plant     that fits within a 5 foot cube. If the magical       plant is larger than a 5 foot cube, the affected       area will wither, but the plant will not die       until the entire plant is withered.

<div style="margin: 10px 0 10px 70px; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

___
#### Hiccoughing Solution 
*Potion, common* 
___
When you drink this potion, you come down with a bad case of the hiccups for 1 hour. For the duration, you have disadvantage on Charisma checks. If you try to cast a spell verbally, roll a d10. On a 1, the casting fails and the spell is wasted.
___
\columnbreak
#### Invigoration Draught
*Potion, rare* 
___
You regain 8d4 + 8 hit points when you drink this shimmering orange potion.
___
#### Invisibility Potion 
*Potion, rare*
___
When you drink this silvery potion, you gain the effects of *pellucidi pellis* for 10 minutes (no concentration required). The potion's effect ends if you attack or cast a spell. This potion can also be poured over an object for a similar effect.
___
#### Kissing Concoction 
*Love potion, rare* 
___
When a being drinks this potion, they become charmed by a chosen being and powerfully compelled to kiss them for 1 hour. The chosen being is selected by the brewer speaking their name into the potion during brewing. If the charmed subject sees the chosen being, they must use as much of their movement as possible to move to the chosen being and kiss them, ending the potion's effect. 

If the brewer uses a bonus action to tell the charmed subject where the chosen being might be, the charmed subject must use as much of their movement as possible to move in that direction on their next turn. They can take their action before they move. They won't be compelled to move into an obviously deadly hazard, but they will provoke opportunity attacks.
___
#### Mandrake Restorative Draught 
*Potion, rare* 
___
When this healing potion is administered, it ends one of the following effects on the target: 
* One effect that charmed, paralyzed or petrified the target. 
* One Transfiguration spell that's changed the target's form.

<img src='https://www.gamingtierlist.com/wp-content/uploads/2019/06/ui_item_potion_MemoryPotion-206x300.png.webp' style='width:110px; margin: 10px -15px 3px -25px; float:left; transform: rotate(-19deg);'>

#### Memory Potion 
*Potion, uncommon* 
___
        When you drink this potion, lost memories          are restored to you and you're able to recall           more details than usual. You have            advantage on Intelligence (Herbology),            Intelligence (Magical Theory) and            Intelligence (Muggle Studies) checks for            10 minutes.

           **Antidote to:** Forgetfulness Potion,            *obliviate*

<div style="margin: -12px 0 -10px 0; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Niantic, Inc.
</div>


<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
#### Moonseed Poison 
*Poison, common* 
___
The moonseed vine, its leaves and its berries give their toxicity to this basic poison. A creature that ingests this poison must succeed on a DC 11 Constitution saving throw, taking 21 (6d6) poison damage on a failed save, or half as much damage on a successful one.
___
#### Murtlap Essence 
*Potion, uncommon* 
___
This solution of strained and pickled tentacles of Murtlaps soothes painful cuts and abrasions, helping you regain 4d4 + 4 hit points when applied.
___
#### Noxious Potion 
*Poison, uncommon* 
___
The liquid and fumes of this potion are equally dangerous, allowing for creatively nefarious uses. A creature that ingests or inhales this poison must succeed on a DC 13 Constitution saving throw or take 21 (6d6) poison damage, and must repeat the saving throw at the start of each of its turns. On each successive failed save, the character takes 7 (2d6) poison damage. After three successful saves, the poison ends.

As an action, you can throw a bottle of Noxious Potion at a point up to 60 feet away, releasing the gas and exposing creatures within 5 feet of that point.
___
#### Oculus Potion 
*Potion, common* 
___
Drinking this deep orange potion removes the blind condition, restoring your eyesight to its normal state. 

**Antidote to:** *conjunctivia*
___
#### Pepperup Potion 
*Potion, common* 
___
When you drink this deep red potion, jets of steam shoot out of your ears, you're cured of the common cold and you feel quite warm throughout your body, rendering you immune to gaining exhaustion from cold environments for 1 hour. One level of exhaustion is removed for the duration, but it is regained at the end of the potion's effects.
___
#### Pet Tonic 
*Potion, common* 
___

<img src='https://www.gmbinder.com/images/BXA8up8.png' style='width:140px; margin: -50px -10px 0px -15px; float:right; transform: scaleX(1) rotate(-4deg);'>

When this potion is given to a magical pet, all of its hit points are restored, any diseases and conditions are removed and it gains 1d4 temporary hit points for 1 hour.

<div style="text-align:right; margin: 20px 0px -25px 0; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

\columnbreak
#### Polyjuice Potion 
*Potion, very rare* 
___
After adding the hair, nail clipping, or other part of a human, drinking this potion perfectly transforms you into that human for 1 hour, changing your height, weight, facial features, sound of your voice, hair length and coloration. None of your statistics change, but your size may change to match the targeted human. 

The potion works for part-humans, but not half-humans. The consistency of the potion is always like a thick mud, but the color and flavor change based on the targeted human, typically tasting very unpleasant.
___
#### Regerminating Potion 
*Potion, common* 
___
When this potion is poured on the roots of a dying plant, it is revitalized. It also accelerates the growth of healthy seedlings. 

**Antidote to:** Herbicide Potion
___
#### Shrinking Solution 
*Potion, common* 
___
When you drink this potion, you gain the effects of the *diminuendo* spell for 1d4 hours (no concentration required). This potion can also be poured over an object for the effects of *reducio*. 

**Antidote to:** *engorgio*, Swelling Solution
___
#### Skele-Gro 
*Potion, rare* 
___
Used to rapidly regrow and repair bones, this healing potion is a staple in a mediwizard's potion case. If the next rest you take is a short rest, you regain hit points equal to half your hit point maximum. If the next rest you take is a long rest, you regain all spent hit dice and gain temporary hit points equal to twice your caster level.
___

<img src='https://www.gmbinder.com/images/MKauHSe.png' style='width:80px; margin: -15px 0px 0px 10px; float:left;'>

#### Sleeping Draught 
*Potion, uncommon* 
___
When you drink this potion, you fall unconscious into a deep sleep. You can't be awoken by any means for 1 hour, aside from administering an antidote. After that, the sleep is natural, so you would sleep only as   long as you normally would or until woken     by taking damage or someone shaking or     slapping you awake.

<div style="margin: 15px -10px 10px 0; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

___
#### Star Grass Salve 
*Potion, common* 
___
You regain 2d4 + 2 hit points when you apply this medicinal balm to your injuries.
___
<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
#### Strengthening Solution 
*Potion, uncommon* 
___
When you drink this potion, your Strength score is raised to 21 for 1 hour. The potion has no effect on you if your Strength is equal to or greater than that score.
___
#### Swelling Solution 
*Potion, common*
___

<img src='https://www.gmbinder.com/images/VegQC0i.png' style='width:100px; margin: -50px -30px -20px 5px; float:right; transform:rotate(5deg);'>

When you drink this potion, you gain the effects of the *engorgio* spell for 1d4 hours (no concentration required). This potion can also be poured over an object for a similar effect. 

**Antidote to:** *diminuendo*, *reducio*, </br>Shrinking Solution

#### Twilight Moonbeams 
*Love potion, uncommon* 
___
When a being drinks this potion, they become charmed by a chosen being for 1 hour. The chosen being is selected by the brewer speaking their name into the potion during brewing. The charmed subject's mind is clouded with daydreams and has disadvantage on Wisdom (Perception) checks to notice anything other than the chosen being. 
___
#### Veritaserum 
*Potion, legendary*
___
A creature subjected to this potion must succeed on a DC 21 Charisma saving throw. On a failed save, the creature is compelled to tell the whole truth to any questions asked of it within the next 10 minutes. You know whether the creature succeeds or fails on its saving throw, based on the dull and dazed look in its eyes. 

On a successful save, the creature is aware of the potion's effect for the next 10 minutes, and can avoid answering questions to which it would normally respond with a lie. Such creatures can be evasive in their answers as long as they remain within the boundaries of the truth.
___

<img src='https://www.gmbinder.com/images/jIA8VpW.png' style='width:170px; margin: -5px -40px -10px -65px; float:left; transform:rotate(-4deg);'>

#### Vitamix Potion 
*Potion, uncommon*
___
When you drink this potion, you have advantage on Dexterity checks for 1 hour. Drinking it feels like 'a burst of energy', greatly sharpening one's reflexes. 

**Antidote to:** *digitus wibbly*, *locomotor wibbly*

<div style="margin: 10px 0 5px 70px; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

___
#### Volubilis Potion 
*Potion, uncommon* 
___
When you drink this potion, you have an advantage on Charisma (Deception) and Charisma (Performance) checks when trying to pass yourself off as a different person for 10 minutes. It magically alters your voice to sound like someone else's, or if your voice is lost, it will restore it. 

**Antidote to:** *silencio*
___
#### Weedosoros 
*Poison, rare* 
___
Named after the mysterious magical plant, weed of sorrows, this poison is reputed to fill the victim with deep regret in their final moments. A creature that ingests this poison must make a DC 15 Constitution saving throw, taking 49 (14d6) poison damage and being poisoned for 1 day on a failed save, or half as much damage and poisoned for 1 minute on a successful one.
___
<div style="margin: 90px 0 -110px -130px; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>
<img src='https://www.gmbinder.com/images/bagv7fh.png' style='width:110px; margin: 5px 10px 0px -10px; float:left;'>

 
#### Wideye Potion 
*Potion, uncommon* 
___
Also known as the Awakening Potion, drinking this potion removes up to two levels of exhaustion. Other uses are awakening someone from non-magical drugging or concussion, and side effects include restlessness and insomnia.
___
#### Wiggenweld Potion 
*Potion, uncommon* 
___
This healing potion is the antidote for magically induced sleep, immediately waking the victim. 

**Antidote to:** Draught of Living Death, Sleeping Draught, *stupefy*
___
#### Wit-Sharpening Potion 
*Potion, rare* 
___
When you drink this potion, your brain's neurological functioning is maximized, raising your Intelligence and Wisdom scores to 20 for 1 hour. The potion has no effect if your ability scores are equal to or greater than that score. 

**Antidote to:** Befuddlement Draught, Common and Uncommon Love Potions, *confundo*, Confusing Concoction, *infirma cerebra*
___
#### Wolfsbane Potion 
*Potion, very rare* 
___
When a lycanthrope drinks this potion once a day for the entire week before the full moon, their alignment does not change and they are not placed under HM control during their transformation. If the drinker misses a single dose in the preceding week, the potion has no effect.
___
#### Wound-Cleaning Potion 
*Potion, common* 
___
When you apply this potion to open wounds, it stings, smokes and perfectly sterilizes the area. A bottle contains ten doses, and one dose stabilizes a creature that has 0 Hit Points, without needing to make a Wisdom (Medicine) check.
___

<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum

<img src='https://www.gmbinder.com/images/R1kJnvR.png' class='cover-image' style="width:122%; top:0px; left:inherit; right:-40px;"><img src="https://www.gmbinder.com/images/PxOX2zF.png" class="cover-image bgwatercolor" style="width:82%; height:75%; left:-30px; top:-70px; transform: scaleX(-1); filter:brightness(94%) sepia(15%)">

<img src="https://www.gmbinder.com/images/PxOX2zF.png" class="cover-image bgwatercolor" style="width:85%; height:100%; transform: scaleX(-1); filter:brightness(94%) sepia(15%)">

<img src="https://www.gmbinder.com/images/g6l5tBv.png" class="cover-image bgwatercolor" style="top:120px; left:inherit; right:-250px; transform: scaleX(1) rotate(20deg); filter:brightness(94%) sepia(15%)">

<div style="text-align:center; margin: -43px -327px 24px 55px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk / 

© Pottermore Limited
</div>

## Magical Pets
From owls and rats to toads and cats, </br>Hogwarts students have been helped and </br>hindered by various creature companions. </br>Animals of all shapes and sizes have long </br>been associated with magic. Muggles often </br>called them familiars, and thought them to </br>have supernatural abilities assisting with </br>the practice of magic. The animals owned </br>by Hogwarts students aren’t familiars in </br>this sense; they are largely pets, rather than </br>supernatural creatures.

When you select a magical pet, it forms a special connection with you and understands one language you speak. Your magical pet acts independently of you, but it always obeys your verbal commands to the best of its ability. In combat, it rolls its own initiative and acts on its own turn. A magical pet can attack and take other actions as normal. Hogwarts only allows one magical pet per student.
### Owls
The old British superstition that it is unlucky to see owls flying by daylight is readily explained, for when wizards break cover to send messages by day, something dramatic must be afoot in the magical world. As a (mostly) nocturnal bird of prey, the owl is inevitably seen as sinister by Muggles, but they are faithful servants and the most common method used by wizardkind across the world for magical communication.

The advantages of owls as messengers are those very qualities that make them suspicious to Muggles: they operate in the darkness; they have exceptionally well-developed night vision; and are agile and stealthy. Whether because they possess an innate magic or their ancestors have been trained for it, owls learn very quickly and thrive on tracing the witch or wizard for whom their letters are intended.

Trained owls are expensive, and it is quite usual for a wizarding family to share a single owl, or else only use Postal owls. However, when a witch or wizard has their own personal owl, they can enjoy the convenience of sending anyone a letter or package for free.

<div style=margin-top:30px;></div>

| <span style='padding:0px 10px;'>d8</span> | Owl Breeds |
|:-:|:------------------|
| 1 | Tawny Owl         |
| 2 | Screech Owl       |
| 3 | Snowy Owl         |
| 4 | Barn Owl          |
| 5 | Great Grey Owl    |
| 6 | Scops Owl         |
| 7 | Eagle Owl         |
| 8 | Barred Owl        |

\columnbreak
<div style='margin-top:375px;'></div>

___
> ## Pet Owl
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 11
> - **Hit Points** 1 (1d4-1)
> - **Speed** 5 ft., fly 60 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|3 (-4)|13 (+1)|8 (-1)|4 (-3)|12 (+1)|7 (-2)|
>___
> - **Skills** Perception +3, Stealth +3
> - **Senses** Darkvision 120 Ft., passive Perception 13
> ___
> ***Flyby.*** The owl doesn't provoke opportunity attacks when it flies out of an enemy's reach.
>
> ***Keen Hearing and Sight.*** The owl has advantage on Wisdom (Perception) checks that rely on hearing or sight.
> 
> ***Magical Post.*** When given a note, letter, or package, the owl will magically know the location of the recipient and fly to deliver the letter.


<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
### Cats
Cats are the creatures most commonly associated with magic. We’ve all seen images of a witch sat on her broomstick accompanied by her black cat. It’s an association that goes back centuries. In the Salem Witch Trials of 1692, Tituba, one of the first to be accused of witchcraft, was said to have both a black and a red cat. Malleus Maleficarum, the best-known treatise against witchcraft, mentions cats and their untrustworthy nature. As clever and  independent creatures, maybe it’s not surprising that cats have been linked with witches and maligned by ignorant Muggles.

Cats are believed to be the most intelligent companions for witches and wizards, and, depending on the breed (and amount of Kneazle heritage), can often be trained to perform complex tasks, as long as the owner has earned their loyalty.
___
> ## Pet Cat
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 12
> - **Hit Points** 2 (1d4)
> - **Speed** 40 ft., climb 30 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|3 (-4)|15 (+2)|10 (+0)|6 (-2)|12 (+1)|7 (-2)|
>___
> - **Skills** Perception +3, Stealth +4
> - **Senses** passive Perception 13
> ___
> ***Hunting Instincts.*** The cat can follow or patrol for a specific target. When doing so, it has advantage on Dexterity (Stealth) checks.
>
> ***Keen Smell.*** The cat has advantage on Wisdom (Perception) checks that rely on smell.
> ***.***
> ### Actions
> ***Claws.*** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* (1d1) slashing damage.

<div style=margin-top:15px;></div>

| <span style='padding:0px 10px;'>d10</span> | Cat Breeds |
|:-:|:------------------|
| 1 | Black Cat         |
| 2 | Calico Cat        |
| 3 | Ginger Cat        |
| 4 | Manx Cat          |
| 5 | Nebelung Cat      |
| 6 | Ocicat            |
| 7 | Tabby Cat         |
| 8 | Tonkinese Cat     |
| 9 | Tortoiseshell Cat |
| 10| White Cat         |

\columnbreak
### Toads
Of the approved animals permitted to students as pets at Hogwarts, the toad is by far the least popular. As a species, toads have as long an association with witchcraft as owls and cats do, but they have gradually appeared less and less frequently as pets at Hogwarts.

History tells us that toads were particularly useful as ingredients in the folk cures practiced in the Dark Ages, and as magical pets, they seem to have a particular link with what were known in 16th century Europe as ‘cunning folk’. These were so-called white witches and healers who practised folk medicine using natural ingredients. Ursula Kemp, an English cunning woman and midwife (tried for witchcraft in 1582), was said to have had a black toad called Pygine.

While toads are looked down upon, their usefulness is found in their role as magical guinea pigs. Whether practicing harmless charms or tweaking the effects of minor potions, toads will unprotestingly play the subject of an experiment, easily absorbing liquids through their skin. As long as the magical effect doesn’t cause pain, the toad won’t think any less of its owner.

___
> ## Pet Toad
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 11
> - **Hit Points** 2 (1d4)
> - **Speed** 20 ft., swim 20 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|1 (-5)|13 (+1)|10 (+0)|2 (-4)|8 (-1)|3 (-4)|
>___
> - **Skills** Perception +1, Stealth +3
> - **Senses** Darkvision 30 ft., passive Perception 11
> ___
> ***Amphibious.*** The frog can breathe air and water
> 
> ***Standing Leap.*** The frog's long jump is up to 10 ft. and its high jump is up to 5 ft., with or without a running start.

<div style=margin-top:30px;></div>

| <span style='padding:0px 10px;'>d8</span> | Toad Species |
|:-:|:----------------------|
| 1 | Common Toad           |
| 2 | Crested Toad          |
| 3 | Dragon Toad           |
| 4 | Giant Purple Toad     |
| 5 | Harlequin Toad        |
| 6 | Horned Toad           |
| 7 | Three-Toed Tree Toad  |
| 8 | Western Green Toad    |

<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
### Alternative Pets
In modern times, Hogwarts is not nearly as strict on students’ pets as it has been. Students are allowed a variety of magical pets, with permission obtained prior to the start of the school year. Pets are required to fit within a standard owl cage and have an XX rating or lower by the Department for the Regulation and Control of Magical Creatures.

Pets found in the wizarding world are almost always smarter than their mundane counterparts, thus earning the title of magical pets. No matter what the species, a magical pet will form a bond with its owner and can often serve as an extra set of eyes, alerting their owner when they spot something amiss or locate a familiar person.

| <span style='padding:0px 10px;'>d10</span> | Alternative Pets |
|:-:|:----------------------|
| 1 | Fruit Bat             |
| 2 | Pipistrelle Bat       |
| 3 | Goliath Tarantula     |
| 4 | Miniature Firecrab    |
| 5 | Adder                 |
| 6 | Grass Snake           |
| 7 | Puffskein             |
| 8 | Pygmy Puff            |
| 9 | Black Rat             |
| 10| Dumbo Rat             |

___
> ## Pet Bat
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 13
> - **Hit Points** 1 (1d4-1)
> - **Speed** 10 ft., fly 60 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|1 (-5)|16 (+3)|9 (-1)|3 (-4)|12 (+1)|4 (-3)|
>___
> - **Skills** Stealth +5
> - **Senses** Blindsight 60 Ft., passive Perception 11
> ___
> ***Echolocation.*** The bat can't use its blindsight while deafened.
>
> ***Flyby.*** The bat doesn't provoke opportunity attacks when it flies out of an enemy's reach.
>
> ***Keen Hearing.*** The bat has advantage on Wisdom (Perception) checks that rely on hearing.
> 
> ### Actions
> ***Bite.*** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* (1d1) piercing damage.

\columnbreak
___
> ## Pet Goliath Tarantula
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 12
> - **Hit Points** 3 (1d4+1)
> - **Speed** 20 ft., climb 20 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|3 (-4)|14 (+2)|12 (+1)|2 (-4)|10 (+0)|2 (-4)|
>___
> - **Skills** Stealth +4
> - **Senses** Darkvision 30 ft., passive Perception 12
> ___
> ***Spider Climb.*** The goliath tarantula can climb difficult surfaces, including upside down on ceilings, without needing to make an ability check.
> 
> ***Web Sense.*** While in contact with a web, the goliath tarantula knows the exact location of any other creature in contact with the same web.
> 
> ***Web Walker.*** The goliath tarantula ignores movement restrictions caused by webbing.
> 
> ### Actions
> ***Bite.*** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* (1d1) piercing damage.
<div style=margin-top:30px;></div>

___
> ## Pet Miniature Firecrab
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 14 (Natural Armor)
> - **Hit Points** 4 (1d4+2)
> - **Speed** 15 ft., swim 15 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|4 (-3)|10 (+0)|14 (+2)|3 (-4)|8 (-1)|3 (-4)|
>___
> - **Senses** passive Perception 9
> ___
> ***Blast-Ended.*** A very small burst of fire may come out of the firecrab's rear end, which ignites flammable objects that aren’t being worn or carried.
>
> ***Hold Breath.*** The firecrab can hold its breath for 1 hour.
> ### Actions
> ***Claw.*** *Melee Weapon Attack:* +2 to hit, reach 5 ft., one target. *Hit:* (1d1) bludgeoning damage.

<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum


___
> ## Pet Adder
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 12
> - **Hit Points** 2 (1d4)
> - **Speed** 20 ft., swim 20 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|2 (-4)|14 (+2)|11 (+0)|5 (-3)|10 (+0)|3 (-4)|
>___
> - **Senses** Blindsight 10 ft., passive Perception 10
>___
> ### Actions
> ***Bite.*** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* (1d1) piercing damage plus (1d4) poison damage. The target must succeed on a DC 10 Constitution saving throw or take the poison damage.
___
> ## Pet Snake
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 13
> - **Hit Points** 2 (1d4)
> - **Speed** 20 ft., swim 20 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|2 (-4)|16 (+3)|11 (+0)|5 (-3)|10 (+0)|3 (-4)|
>___
> - **Senses** Blindsight 10 ft., passive Perception 10
>___
> ### Actions
> ***Bite.*** *Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* (1d1) piercing damage.

<img src='https://images.ctfassets.net/usf1vwtuqyxm/10iq4MOpMuAkkGyGo0qkCO/b9846edd372fa666ed2d0eee3152c917/B3C4M2.jpg' class='cover-image' style="width:150%; height:2000%; top:405px; left:-155px;"><img src='https://images.ctfassets.net/usf1vwtuqyxm/10iq4MOpMuAkkGyGo0qkCO/b9846edd372fa666ed2d0eee3152c917/B3C4M2.jpg' class='cover-image' style="width:150%; height:45%; top:inherit; bottom:50px; left:-155px;"><img src='https://images.ctfassets.net/usf1vwtuqyxm/10iq4MOpMuAkkGyGo0qkCO/b9846edd372fa666ed2d0eee3152c917/B3C4M2.jpg' class='cover-image' style="width:150%; top:inherit; bottom:80px; left:-155px;">
<div style='margin: 10px 0px 0px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;'>
Art by Atomhawk / 

© Pottermore Limited
</div><img src='https://www.gmbinder.com/images/g6l5tBv.png' class='cover-image bgwatercolor' style="top:130px; left:114px; height: 100%; transform:scaleX(1) scaleY(1) rotate(-89deg);filter:brightness(94%) sepia(15%)"><img src='https://www.gmbinder.com/images/XEVwU5k.png' class='cover-image bgwatercolor' style="top:inherit; bottom:-680px; transform:scaleX(1) scaleY(-.9);filter:brightness(94%) sepia(15%)"><img src='https://www.gmbinder.com/images/zdcYLtP.png' class='cover-image bgwatercolor' style="top:-20px; transform:scaleX(-1) scaleY(1);filter:brightness(94%) sepia(15%)">


\columnbreak

___
> ## Pet Puffskein
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 11
> - **Hit Points** 1 (1d4-1)
> - **Speed** 20 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|1 (-5)|12 (+1)|8 (-1)|5 (-3)|12 (+1)|14 (+2)|
>___
> - **Skills** Stealth +3
> - **Senses** passive Perception 10
> ___
> ***Fluffy.*** The puffskein appears to be a living ball of fluff; its cuteness might be distracting to some, much like carrying around an adorable kitten.
>
> ***Prehensile Tongue.*** The puffskein has a disproportionately long tongue that it can use to grab or manipulate small objects.
<div style=margin-top:30px;></div>

___
> ## Pet Rat
>*Tiny beast, unaligned*
> ___
> - **Armor Class** 12
> - **Hit Points** 1 (1d4-1)
> - **Speed** 30 ft.
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|2 (-4)|15 (+2)|9 (-1)|5 (-3)|10 (+0)|4 (-3)|
>___
> - **Senses** Darkvision 30 ft., passive Perception 10
> ___
> ***Keen Smell.*** The rat has advantage on Wisdom (Perception) checks that rely on smell.
> ### Actions
> ***Bite.*** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* (1d1) piercing damage.



<div class='footnote'>Part 1 | Wizarding Equipment</div>

\pagebreakNum
# Chapter 6: Wizarding Feats
Some wizards will show a natural aptitude or predilection for certain abilities. Others will dedicate their free time to self-improvement. A small percentage will have rare powers or traits inherited from their ancestors. Regardless of the reason, feats represent a witch or wizard's additional abilities, and all the standard 5e rules apply to obtaining feats.
## Innate Feats
The following feats are defining traits that certain wizards have at birth. These feats must be taken at level 1, through house traits at character creation, and cannot be gained at any other time.
### Giant's Blood
Even though they are few and far between, it's hard for half-giants and part-giants to hide their genealogy; they tend to turn heads wherever they go. With a broad build, impressive strength and a genetic resistance to magic, wizards with giant blood are powerful allies.
* Increase your Strength score by 1, to a maximum of 20.
* Adult part-giants are between 7 and 9 feet tall and weigh between 300 and 420 pounds. Your size is Medium.
* You are considered one size larger when determining carrying capacity and weight you can push, drag, or lift.
* When a spell or other magical effect inflicts a condition on you, you can use your reaction to resist one condition of your choice. You can’t use this ability again until you finish a long rest.

### Goblin Cunning
The rarest racial combination of all, part-goblins can have goblin ancestry anywhere in their family tree, and it will still make a very noticeable difference. At an average of 4 feet tall, part-goblins may feel out of place in a larger world. However, these small wizards have inherited goblins’ cleverness and often come with big hearts and big personalities.
* Adult part-goblins are between 3 and 5 feet tall and weigh around 110 pounds. Your size is Small.
* You can move through the space of any creature that is of a size larger than yours.
* You have advantage on all Intelligence and Wisdom saving throws against magic.
* You can speak, read, and write Gobbledegook.

\columnbreak
<div style="margin-top:50px;"></div>

> ##### Wizarding Heritage
> Every wizard is human, but wizards are often distinguished by how much magical heritage is in their family tree. Very rarely, wizards will be part-human, inheriting blood and traits from a magical being in their ancestry. Slight prejudices remain around part-human or Muggleborn wizards, but the myths around blood purity have been dispelled.
> ___
> ##### A Witch's Childhood
> Think about how your character's heritage influenced their childhood experiences, and consider how those experiences have shaped your character's personality and worldview.
> 
> **Muggle-borns.** Muggle-borns are wizards and witches born to Muggle parents, non-magical folk. Muggle-borns enter an entirely new world when they receive their letter from Hogwarts. Although they’ll have to adapt to wizarding culture, the lessons they’ve learned from the Muggle world will serve them well and help them see things from a different perspective. Additionally, living in a world without magic means they know how to do things the hard way. 
>
> **Half-bloods.** The vast majority of human wizards are considered half-bloods, wizards that have some combination of magical and Muggle ancestry. Originally used to describe a child of a magical wizard and a non-magical Muggle, half-blood has become an encompassing term. While many half-bloods are raised in the wizarding world, it’s not uncommon for a half-blood to be unaware of their magical side of their family, having a very similar experience to Muggle-borns.
> 
> **Purebloods.** Purebloods come from a long line of wizards and witches, without a drop of Muggle blood in their veins. Raised in wizarding culture, purebloods have grown up riding broomsticks, playing Quidditch in the yard, and hearing the nursery rhymes of Beedle the Bard. Well acquainted with this world, they enter Hogwarts with a little extra confidence.
<div style='margin-top:40px;'></div>


<div class='footnote'>Part 1 | Wizarding Feats</div>

\pagebreakNum

<!--### Muggle-born
Muggle-borns are wizards and witches born to Muggle parents, non-magical folk. Muggle-borns enter an entirely new world when they receive their letter from Hogwarts. Although they’ll have to adapt to wizarding culture, the lessons they’ve learned from the Muggle world will serve them well and help them see things from a different perspective. Additionally, living in a world without magic means they know how to do things the hard way. 
* Increase your Intelligence score by 1, to a maximum of 20.
* You gain proficiency in Muggle Studies.
* Whenever you make an Intelligence (Muggle Studies) check related to blending in with Muggles or interacting with Muggle technology, add double your proficiency bonus to the check, instead of your normal bonus.
### Pureblood
Purebloods come from a long line of wizards and witches, without a drop of Muggle blood in their veins. Raised in wizarding culture, purebloods have grown up riding broomsticks, playing Quidditch in the yard, and hearing the nursery rhymes of Beedle the Bard. Well acquainted with this world, they enter Hogwarts with a little extra confidence.
* Increase your Charisma score by 1, to a maximum of 20.
* You gain proficiency in Magical Theory.
* Whenever you make an Intelligence (Magical Theory) check related to wizarding culture or mythology, add double your proficiency bonus to the check, instead of your normal proficiency bonus.-->
### Metamorph Magic
Once in a great many years, a metamorphmagus is born to a wizarding family with their very particular talent: morphing every aspect of their human appearance. Before becoming an adult, a metamorphmagus will not have complete control over this ability, often letting their emotions or stress get the better of them and losing control.
* At will, you can transform your appearance. As an action, you decide what you look like, including your height, weight, facial features, sound of your voice, hair length, coloration, and distinguishing characteristics, if any. None of your statistics change, you don't appear as a creature of a different size than you, and your basic shape stays the same. If you're bipedal, you can't use this spell to become quadrupedal, for instance. At any time, you can use your action to change your appearance in this way again.
* You can also adapt your body to an aquatic environment, growing webbing between your fingers. As an action, you gain a swimming speed equal to your walking speed.

### Parseltongue
Almost exclusively hereditary, to speak Parseltongue is to magically comprehend and verbally communicate with all snakes and snake-like beasts, like the Runespoor and Basilisk. This oral language has been associated with Dark wizards, owing to Salazar Slytherin's status as a Parselmouth which was passed on to the Gaunt family and Tom Riddle. However, outside of Wizarding Britain, no such association exists.
* You can speak Parseltongue.

### Veela Charm
Just like part-giants, it’s very rare to find a part-veela. A wizard or witch who inherited veela blood will almost always be the center of attention, a picture of grace and beauty. Unlike half-veela or quarter-veela, part-veela are just as likely to be male as female.
* You gain proficiency in one Charisma skill of your choice.
* As an action, you can attempt to charm a humanoid you can see within 30 ft, who would be attracted to you. It must make a Wisdom saving throw, (if hostile, with advantage). If it fails, it is charmed by you for one hour or until you or your companions harm it. The charmed creature regards you as a friendly acquaintance and feels compelled to impress you or receive your attention. After, the creature knows it was charmed by you. You can’t use this ability again until you finish a long rest. 

\columnbreak
## Standard Feats
These feats might come from latent natural talent, but are often manifested through hard work and long hours of study. These feats are not restricted to being gained at level 1.
### Aerial Combatant
You're able to keep yourself oriented and lead your targets while flying a broomstick. You gain the following benefits.
* You gain tool proficiency in Vehicles (Broomstick).
* You no longer suffer disadvantage on attack rolls due to flying.

### Detecting Traces
You've learned to feel magic and recognize styles of spells and curses. Using concentration, you sense the presence of magic within 30 feet of you. If you sense magic in this way, you can use your action to see a faint aura around any visible creature or object in the area that bears magic, and you learn the associated spell's school of magic, if any. This ability can penetrate most barriers, but is blocked by 1 foot of stone, 1 inch of common metal, or 3 feet of wood or dirt.
### Lycanthropy
You've been attacked by a transformed werewolf, infecting you with the blood curse of lycanthropy. You gain the following benefits.
* Increase your Strength and Constitution scores by 1, to a maximum of 20.
* You have advantage on Wisdom (Perception) checks that rely on smell.
___
You also gain the following penalties.
* From sunset to sunrise on the night of the full moon, you undergo your werewolf transformation. During the transformation, your alignment changes to Chaotic Evil and your character is placed under HM control.
* For the day of and three days after your werewolf transformation, you suffer a -3 penalty to your Constitution score, gain two levels of exhaustion that cannot be removed and have disadvantage on Constitution saving throws.
* If your condition becomes known, fellow witches and wizards might fear or discriminate against you.
<div class='footnote'>Part 1 | Wizarding Feats</div>

\pagebreakNum
### Martial Artist
Whether as a childhood extracurricular activity or a supplement to your magical dueling, you're trained in striking and grappling. You gain the following benefits.
* Your unarmed strike uses a d6 for damage.
* When you hit a creature with an unarmed strike on your turn, you can try to grapple the target as a bonus action.
* You have advantage on attack rolls against creatures you are grappling.
* While a creature is grappled by you, you can use your action and make another grapple check to try one of the following maneuvers:
    * **Pin.** If you succeed, you and the creature are both restrained until the grapple ends.
    * **Takedown.** If you succeed, you make an unarmed strike and the creature is knocked prone. 
    * **Disarm.** If you succeed, the creature is forced to drop one item of your choice that it's holding. You can choose to take the item, ending the grapple.

### Occlumency Training
You have developed the presence of mind to resist a mental invasion. When targeted by *legilimens*, you make a Wisdom saving throw to resist its initial effects, and you have advantage on the Intelligence contests. If you fail your initial saving throw, you are immediately aware that the spell is targeting you. If you succeed on a saving throw or contest, you can let the spell continue and reveal false information, false emotions, or false memories of your choosing.

Veritaserum will not work on you, unless you allow it.
### Remarkable Aim
You have unerring accuracy with projectile spells. Your ranged spell attacks ignore half cover and treat three-quarters cover as if it were half cover.
### Steady Caster
You're able to maintain focus, even in stressful situations. You have advantage on Constitution saving throws that you make to maintain concentration on a spell when you take damage.

\columnbreak
### Vampirism
You gain the following benefits:
* You can see in dim light within 120 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray.
* You are stuck at the age and form you were at the time of your undeath. You can't die of old age, you suffer none of the drawbacks of old age, and you can't be aged magically.
* You gain proficiency in Charisma (Persuasion).

You also gain the following penalties:
* You take 1 damage when you start your turn in direct sunlight.
* You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight.
* You can't enter a residence without an invitation from one of the occupants.
* You are repelled by the smell of garlic, and touching or eating it causes intense pain.
* Instead of food and water, you must drink animal, human or magical being blood to sustain yourself.

### Wandless Magic
Through studying ancient tomes or channeling some of the volatile magic of your youth, you're able to perform small magical feats without your wand. If you know any of the following spells, you can cast them without needing a wand or somatic component: *accio*, *alohomora*, *colovaria*, *illegibilus*, *incendio glacia*, *pereo*, *wingardium leviosa*.

You cannot expend a higher level spell slot when casting in this way.

<div style='margin-top:40px;'></div>

> ##### More Feats
> The following 5e Feats are also available.
> * Actor
> * Athlete
> * Dungeon Delver
> * Durable
> * Keen Mind
> * Linguist
> * Observant
> * Skilled

<div class='footnote'>Part 1 | Wizarding Feats</div>

\pagebreakNum

<img src="https://www.gmbinder.com/images/9tcm9JC.jpg" class="cover-image" style="width:140%; top:0px; left:180px;"><img src="https://www.gmbinder.com/images/RbZHChh.png" class="cover-image bgwatercolor" style="width:125%; left:-200px; filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/RbZHChh.png" class="cover-image bgwatercolor" style="width:125%; left:-200px; filter:brightness(94%) sepia(15%)">

<div style="margin: -43px -300px 24px 375px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk /

© Pottermore Limited
</div>


<h1 id="chapter-7-wizarding-skills" style='width:50%;'>Chapter 7: Wizarding Skills</h1>

Due to the nature of the Wizarding World of Harry Potter, unique skills are needed in a wizard's daily life. Some of the traditional 5e skills are not intended for use with this supplement and have been listed below as deprecated. To replace them, new wizarding skills have been added to cover the variety of subjects taught at Hogwarts School of Witchcraft and Wizardry. Even when there's a direct conversion from old to new, applications are distinct from 5e descriptions.

<div class='classTable' style='margin:50px 0px 60px;'>
<span style="text-align:center">

##### Skill Conversions</span>
| Deprecated</br>5e Skill | Equivalent New</br>Wizarding Skill |
|:---------------------:|:-----------------------:|
| INT (Arcana)          | INT (Magical Theory)   |
| INT (History)         | INT (Muggle Studies)    |
| INT (Nature)          | INT (Herbology)         |
| INT (Religion)        | ─                       |
| WIS (Animal Handling) | WIS (Magical Creatures) |
| ─                     | WIS (Potion-Making)     |
</div>

## Deprecated 5e Skills
### Intelligence (Arcana)
Replaced by Intelligence (Magical Theory). Redundant.
### Intelligence (History)
Replaced by Intelligence (Magical Theory) / (Muggle Studies). Redundant.
### Intelligence (Nature)
Replaced by Intelligence (Herbology) / (Magical Creatures) / (Muggle Studies). Redundant.
### Intelligence (Religion)
Replaced by Intelligence (Muggle Studies). Not applicable.
### Wisdom (Animal Handling)
Replaced by Intelligence (Magical Creatures). Redundant.

\columnbreak

<div style='margin-top:150px;'></div>

## New Skills
### Intelligence (Herbology)
Your Intelligence (Herbology) check measures your ability to recall lore about mundane or magical plants.
### Intelligence (Magical Theory)
Your Intelligence (Magical Theory) check measures your comprehension of the workings of magic and spell invention. It also checks whether you can recall lore about the invention of spells, legendary wizards and witches, wizarding mythology, and historical events in the wizarding world.
### Intelligence (Muggle Studies)
An Intelligence (Muggle Studies) check tests your familiarity with Muggle culture, history, arts and sciences, your success when trying to blend in with Muggles, and your ability to understand or interact with Muggle technology.
### Wisdom (Magical Creatures)
When there is any question whether you can calm down a magical creature or intuit a non-magical animal’s intentions, that would call for a Wisdom (Magical Creatures) check. You also make a Wisdom (Magical Creatures) check to keep your head around dangerous creatures and recall their lore.
### Wisdom (Potion-Making)
Your Wisdom (Potion-Making) check is used whenever trying to understand and apply alchemical ingredients' effects, stir a brewing potion in just the right way, or experiment and uncover secret potion-making techniques.
<div style='margin-top:20px;'></div>

> ##### Interacting with Magic
> If a character interacts with a complex piece of magic requiring theoretical knowledge, it might call for an Intelligence (Magical Theory). However, the majority of interactions with magic should use a character's spellcasting ability modifier.

<div class='footnote'>Part 1 | Wizarding Skills</div>

\pagebreakNum

<!-- # Chapter 8: Wizarding Alignment
Besides, the world isn’t split into good people and Death Eaters. We’ve all got both light and dark inside of us. What matters is the part we choose to act on. That’s who we really are.” - Sirius Black, Order of the Phoenix
## Good vs. Dark
Throughout the history of wizardkind, skillful wizards have sought to kill and control their way to power, much like certain muggles. These infamous individuals are labeled Dark wizards and Dark witches, for utilizing malicious forms of magic and using their power to inflict pain and suffering.

Whether from morbid curiosity, academic dedication, or personal ambition, there are countless Dark secrets researched and recorded in the wizarding world. Even at Hogwarts, extremely Dark magic can be found within the restricted section of the library. While the magic itself is dangerous and often ill-intentioned, magic is but a tool. Almost any spell can be used for Dark purposes, if the caster seeks to harm others. The reason the incantations and rituals of extremely Dark magic is viewed differently is partly because of the sadistic design of that magic and because of the horrors that will transpire if it falls into the wrong hands.

<img src='https://drive.google.com/uc?id=0B0TGf4bxO8wBazU4R1daUm9jdTQ' class='cover-image' style='height:540px; width:inherit; top:530px; left:-250px; transform: scaleX(-1);'>
<div style="margin: 445px 0px 0px -52px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk /

© Pottermore Limited <span style="color:black;">-</span>
</div><img src="https://www.gmbinder.com/images/ShMie2y.png" class="cover-image bgwatercolor" style="width:110%;top:278px; left:-25px;filter:brightness(94%) sepia(15%);transform: scaleY(-1) scaleX(-1) rotate(-4deg);"><img src="https://www.gmbinder.com/images/9VkhTcw.png" class="cover-image bgwatercolor" style="width:100%; top:610px; left:-35px; transform: scaleY(-1) rotate(-23deg); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/ShMie2y.png" class="cover-image bgwatercolor" style="width:110%;top:-30px; left:-10px;filter:brightness(94%) sepia(15%);transform: scaleY(-1) scaleX(-1)">

\columnbreak

### Lawful Dark, Neutral Dark, and Chaotic Dark
Alignment itself works in a very similar way to 5e's alignment, with one slight change. The word evil is replaced by the word Dark. This speaks less to the morality of your principles and more to the morality of your actions. For instance, the motto of "For the Greater Good" rings of noble aspirations, but if the means to that end are violent and filled with Dark magic, the appropriate alignment is Dark.

Let's suppose a witch were to study and wield Dark magic for the purpose of good. She might only cast Unforgivable Curses against Dark wizards who do so first, or use her power to protect innocents. Even with those pure intentions, the means by which she attains her power will inevitably cause pain and death, even if it's only those who have used magic for pain and death themselves. The nature of Dark magic draws upon hatred and fear. This witch would be motivated by revenge, and it would be a very narrow path to walk. Her alignment would likely be Chaotic Neutral

<div class='footnote'>Part 1 | Wizarding Alignment</div>

\pagebreakNum-->

# Chapter 8: Dark Magic Corruption
Besides, the world isn’t split into good people and Death Eaters. We’ve all got both light and dark inside of us. What matters is the part we choose to act on. That’s who we really are.” *- Sirius Black, Order of the Phoenix.* 
</br>      As a wizard delves into the foul tomes of Dark magic, changes will begin to take place. Experimenting with Dark magic almost always results from an unquenchable thirst for power, an incredibly intense fear or a deep well of hatred. By using twisted magic and committing unspeakable acts, that inner darkness takes a toll on a Dark witch's physical and mental well-being.
### Gaining Corruption Points
Although a wizard's descent into darkness is gradual, their life is usually marked by definitive moments when the line is finally crossed. Murder, betrayal, and twisted experiments are common in the histories of Dark wizards and witches.

Whenever a character commits an act that represents their growing cruelty, the HM can call for a Wisdom saving throw. The DC of the saving throw is determined by their corruption tier in the table below. If the character fails that saving throw, they gain a single corruption point. Some examples of events that might prompt a corruption roll are:

* Killing a being by reducing it to 0 hit points with a Dark spell, when it could've been spared
* Casting an Unforgivable Curse, whether anyone witnesses it or not
* Betraying an ally that trusted you, for your own gain
* Harming innocents in a foreseeable and preventable way
* Manipulating someone into abandoning their morals
* Acting in a way contrary to alignment

As a character reaches higher corruption tiers, the DC of the saving throw increases. Additionally, the higher tiers grant a corruption boon and inflict a corruption effect on the character. Upon reaching a corruption tier with an effect, the character must roll the appropriate die to determine which effect they receive from the corruption effect tables on the next page. If appropriate, the HM and the character's player can also come to an agreement on which corruption effect a character receives. These effects are cumulative with the effects of lower tiers of corruption. 

These effects are intended to slightly shape a character's personality and action. Roleplaying how the Dark magic is twisting the character is strongly encouraged, and an HM may remind players of their corruption effects.


<div class="wide" style="margin-top:5px;margin-bottom:10px;">

##### Corruption Tiers
| | Pure-Hearted </br>(0 points) | Pragmatic </br>(1-4 points) | Devious </br>(5-7 points) | Vicious </br>(8-11 points) | Vile </br>(12+ points) |
|:-------:|:------------:|:------------:|:------------:|:------------:|:------------:|
| **Save DC** | 10 | 12 | 16 | 22 | - | 
| **Alignment Shift** | - | - | Neutral | - | Dark | 
| **Corruption Boon** | - | Empowered </br>Darkness | - | Heightened </br>Darkness | Inferi </br>Ritual |
| **Corruption Effect** | - | - | One Mild </br>Effect | One Severe </br>Effect | One Severe </br>Effect |
</div>

<img src='https://www.gmbinder.com/images/i11vHyD.jpg' class='cover-image' style='height:500px; width:inherit; top:660px; left:-220px; transform: scaleX(-1);'>
<div style="margin: 0px 0px 0px -10px; padding-top:263px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Atomhawk /

© Pottermore Limited
</div><img src="https://www.gmbinder.com/images/ShMie2y.png" class="cover-image bgwatercolor" style="width:110%;top:403px; left:-25px;filter:brightness(94%) sepia(15%);transform: scaleY(-1) scaleX(-1) rotate(-4deg);"><img src="https://www.gmbinder.com/images/9VkhTcw.png" class="cover-image bgwatercolor" style="width:100%; top:640px; left:-35px; transform: scaleY(-1) rotate(-23deg); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/ShMie2y.png" class="cover-image bgwatercolor" style="width:110%;top:-1px; left:-10px;filter:brightness(94%) sepia(15%);transform: scaleY(-1) scaleX(-1)">

\columnbreak

### Removing Corruption Points
The only way to remove corruption is through true, meaningful remorse. Typically, someone must feel remorse for the specific actions that caused the corruption in the first place, but the remorse can also be more general, based on an entire life of wrongdoing. There must be an amount of suffering that is comparable to the suffering inflicted on others.

Based on the actions and inner thoughts of the character, the HM decides if a character is able to remove a corruption point. The factors required for true remorse might be:
* Acknowledging responsibility for the harm caused
* Feeling a deep sadness and regret over the actions
* Seeking to make amends in whatever way possible

If enough corruption points are removed to reach a lower tier, the boon and effect from the previous higher tier are also removed.

<div class='footnote'>Part 1 | Wizarding Alignment</div>

\pagebreakNum
### Corruption Boons
    ***Empowered Darkness.*** When you have Empowered Spell as one of your metamagic options and use it on a Dark spell, it costs 0 sorcery points.

***Heightened Darkness.*** You can use the Heightened Spell metamagic when casting a Dark spell, whether it's one of your metamagic options or not. When you use Heightened Spell on a Dark spell, it costs 1 sorcery point.

***Inferi Ritual.*** By focusing for 10 minutes and expending a 5th level spell slot, this ritual creates an undead servant. Choose a corpse of a Medium or Small humanoid you can touch. Your spell imbues the target with a foul mimicry of life, raising it as an inferius (the HM has the creature’s stats).

As a bonus action, you can mentally command any of your inferi if one is within 60 feet of you (if you control multiple, you can command any or all with the same command). You decide its action and movement during its next turn, or you can issue a general command, such as to guard a particular corridor. If you issue no commands, the creature only defends itself against hostile creatures. Once given an order, the creature continues to follow it until its task is complete.

The Dark magic that binds the corpse is permanent. The inferius will only deanimate if you die or if it is destroyed.
### Corruption Effects

<div style='column-count:2; margin-top:20px;'>

| <span style="padding:10px;">d6</span> | Mild Effects|
|:-:|:------------|
| 1 | Hoarder |
| 2 | Compulsive |
| 3 | Cough |
| 4 | Reckless |
| 5 | Scent of Decay |
| 6 | Mildly Phobic |

| <span style="padding:10px;">d8</span> | Severe Effects |
|:-:|:---------|
| 1 | Phobic |
| 2 | Jittery |
| 3 | Unnatural Pallor |
| 4 | Paranoid |
| 5 | Crimson Pupils |
| 6 | Distracted |
| 7 | Hallucinations |
| 8 | Sadistic |
</div>

    ***Compulsive.*** You begin to exhibit a mild, compulsive ritual of the HM's choice, likely associated with some fear. This can manifest as quadruple-checking locks and defensive measures, inspecting behind curtains, doors, and bushes for hidden attackers, or refusing to consume anything until you can get a small animal to test it for poison, for example. You take 1.5 times as long to complete a short rest.

***Cough.*** You develop an uncontrollable cough that creeps up every now and then. You have disadvantage on Dexterity (Stealth) checks.

***Crimson Pupils.*** Your eyes are bloodshot and in the right lighting, even the blackest part of your pupils seem to shine red. You have disadvantage on attack rolls when you are facing the sun or a bright light.

***Distracted.*** Your mind has grown scattered and easily clouded. You have disadvantage on Intelligence ability checks, except for Intelligence saving throws. 

***Hallucinations.*** Strange visions and sourceless whispers occasionally tug at your perception. You have disadvantage on Wisdom (Perception) checks.

***Hoarder.*** You are compelled to collect anything that might be remotely useful in protecting you from your greatest fears. Appropriate items stumbled upon must be gathered and carried, if able, until at carrying capacity.

***Jittery.*** You become far too easy to spook or startle. You have disadvantage on initiative rolls.

***Mildly Phobic.*** You begin to obsess over a specific creature or person, believing them to be the cause of your demise. During the first round of combat with a creature of the chosen type, you are frightened.

***Paranoid.*** You no longer trust the people you meet. You do not count as a "friendly" creature to strangers and acquaintances, and they do not count as "friendly" to you, in regards to abilities or spells. You can only target yourself and your closest allies with your beneficial spells and abilities.

***Phobic.*** A specific creature or person invades your dreams, turning them to nightmares. When you enter combat with a creature of the chosen type, you must make a Wisdom saving throw (DC is 10 + your total corruption points). On a failure, you are frightened of them for 1 minute.

***Reckless.*** You've become impulsive in the face of dangerous situations. The first attack made against you in any combat encounter has advantage on the attack roll.

***Sadistic.*** Your bloodlust makes you become entranced by the pain you cause. Whenever you deal damage, the next attack made against you by anything other than the creature you damaged has advantage on the attack roll.

***Scent of Decay.*** Your body emits a faint stench of death. You have disadvantage on Charisma (Persuasion) checks.

***Unnatural Pallor.*** Your skin has become pale and waxy and your features oddly distorted. You have disadvantage on Charisma ability checks, except for Charisma (Intimidation) and Charisma saving throws.
### Restricted Dark Spells
The following spells simply cannot be cast by your average wizard. They require a more intimate understanding of the darker sides of magic. The Cruciatus Curse is specifically fueled by the desire to inflict pain and the Killing Curse requires pure, unadulterated hatred to end a person's life. Neither of these will have a fraction of the effect without the proper feeling behind it.

| Spell Name  | Required Corruption Points |
|:-----------------:|:--:|
| *transmogrify*    | 2  |
| *crucio*          | 4  |
| *azreth*          | 7  |
| *avada kedavra*   | 11 |

Once you've reached the required number of corruption points, you are now able to add that spell to your list of known spells through the usual methods of learning a spell. Once you add a restricted Dark spell to your spell list, you can keep that spell, even if your corruption points return to a number lower than the required amount.

<div class='footnote'>Part 1 | Wizarding Alignment</div>

\pagebreakNum

# Chapter 9: Spells
Magic in the Wizarding World of Harry Potter works in a very fluid and flexible way, limited only by a wizard's knowledge and experience. Some spells are entirely dependent on feeling a specific emotion, while others require mental focus and precise wand movements. Spellcasting is a very personal thing, giving different witches their own signature styles and repertoires.

Because Wands & Wizards focuses exclusively on spellcasters, some extra attention has been given to how spells work. Not every spell can kill, which allows wizards and witches to engage in the non-lethal combat expected by wizarding society. Pay extra attention to the Spell Tags listed in the spell descriptions.
## Spellcasting
### Damaging Spells
Many spells deal some kind of damage to the target. However, because magic is deeply linked to a specific spell’s intent, the effect on the target can vary greatly. Spells can either be lethal or non-lethal. Many dueling spells are designed to be non-lethal, but violent, combative Dark magic will kill.

<div style="margin: 410px 0px 20px -10px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by @upthehillart
</div>
<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5d80281f-995b-4090-a155-1b25e3515e3c/db7af8g-8c93d3c9-d7ce-48c5-9955-9fa7cfecedd8.jpg/v1/fill/w_1023,h_540,q_75,strp/offense_x_defense_by_upthehillart_db7af8g-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTQwIiwicGF0aCI6IlwvZlwvNWQ4MDI4MWYtOTk1Yi00MDkwLWExNTUtMWIyNWUzNTE1ZTNjXC9kYjdhZjhnLThjOTNkM2M5LWQ3Y2UtNDhjNS05OTU1LTlmYTdjZmVjZWRkOC5qcGciLCJ3aWR0aCI6Ijw9MTAyMyJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.Pt0a-fuPkf9TrZP-7cDJteb31oxWjKBvBKnPhau86F0" class="cover-image" style="width:100%; height:46%; top:495px;"><img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5d80281f-995b-4090-a155-1b25e3515e3c/db7af8g-8c93d3c9-d7ce-48c5-9955-9fa7cfecedd8.jpg/v1/fill/w_1023,h_540,q_75,strp/offense_x_defense_by_upthehillart_db7af8g-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTQwIiwicGF0aCI6IlwvZlwvNWQ4MDI4MWYtOTk1Yi00MDkwLWExNTUtMWIyNWUzNTE1ZTNjXC9kYjdhZjhnLThjOTNkM2M5LWQ3Y2UtNDhjNS05OTU1LTlmYTdjZmVjZWRkOC5qcGciLCJ3aWR0aCI6Ijw9MTAyMyJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.Pt0a-fuPkf9TrZP-7cDJteb31oxWjKBvBKnPhau86F0" class="cover-image" style="width:100%; top:520px;"><img src="https://www.gmbinder.com/images/6P52llg.png" class="cover-image bgwatercolor" style="width:100%; height:102%; top:60px; transform: scaleY(-1) scaleX(-1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/nuH93ZS.png" class="cover-image bgwatercolor" style="width:100%; height:130%; filter:brightness(94%) sepia(15%)">


\columnbreak

<div style="margin-top:-10px;"></div>

#### Non-Lethal Magic
A creature cannot be killed by standard spells, no matter the intent of the caster. If a creature is reduced to 0 hit points by a standard spell (and if applicable, fails all of their death saving throws), that creature will be knocked out, non-lethally.
#### Lethal Magic
Dark spells differ from regular spells in one important way: damage dealt by Dark spells is potentially lethal. If a creature is reduced to 0 hit points by a Dark spell (and if applicable, fails all of their death saving throws), that creature dies. It is possible to use damaging Dark spells to injure a creature, and then finish them off with a damaging spell that isn’t Dark, to non-lethally incapacitate it.
### Duration
Wands & Wizards maintains all of the standard 5e rules and conventions regarding spell duration and concentration, but the addition of dedication spells requires more strategic use of a handful of spells. 

<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### Dedication
If a spell is marked as a dedication spell in its Duration entry, you must maintain concentration on that spell and use an action at the start of each of your turns to maintain your dedication. If you lose dedication, the spell ends. 
Like concentration, you can end dedication at any time (no action).

The following factors can break dedication:
- **Casting another spell.** It doesn't matter if the other spell requires dedication or not. Even if you use your bonus action to cast another spell, your dedication is lost.
- **Losing your line of sight to your target.** This only applies if your spell affects a specific target. You cannot lose dedication by losing line of sight to area spells. 
- **Losing concentration.** If your concentration is broken by taking damage or being incapacitated, your dedication is broken.
### Spell Tags
#### Dark
The Dark Arts, also known as Dark magic, refers to any type of magic that is mainly used to cause harm to, exert control over, or even kill the victim. The Dark Arts encompass many spells and actions ranging from the powerful Unforgivable Curses to brewing harmful or poisonous potions and breeding Dark creatures, all of which are often illegal or at least discouraged. Practicing certain Dark magics is rumored to damage the wizard’s very soul, and require some sort of malicious intent in order to cast. However, despite being labelled “dark,” the Dark Arts are not necessarily “evil.” Many prominent wizards and Aurors have been known to rely on Dark spells to carry out their duty, in dire circumstances.

Because of their lethal effects, the use of Dark spells on beings will surely gain your character some attention and may cause people to question that character’s motivations and loyalties. If the Dark tag is accompanied by Unforgivable, this is an Unforgivable Curse, illegal under all circumstances and guaranteed to be punished with a life sentence in Azkaban. Casting Unforgivable Curses or killing a being with a Dark spell should prompt a corruption roll, as outlined in Chapter 8: Dark Magic Corruption.
#### Defensive
Defensive magic is a classification of charms, jinxes, and other types of spells that are specifically focused on nullifying and countering magic. Shield charms, anti-apparition jinxes, and countercurses are just a few examples of defensive magic. Nearly every wizard will rely on Defensive spells at some point in their life, but some wizards will be particularly in tune with this aspect of magic, favoring spells of this type.
#### School of Magic
A school of magic spell is a spell that cannot be learned via the usual methods. These spells cannot be chosen upon leveling up, but instead is granted by a school of magic whenever you gain a spell slot of that spell's level. Once you gain a school of magic spell, it's added to your spells known, it doesn’t count against your number of spells known, and it cannot be forgotten to learn another spell.

\columnbreak
<img src="https://www.gmbinder.com/images/W7kvPfG.png" class="cover-image bgwatercolor" style="width:100%; top:-380px; transform: scaleX(-1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/ShMie2y.png" class="cover-image bgwatercolor" style="width:110%; top:-100px; left: inherit; right:0px; filter:brightness(94%) sepia(15%)"><img src='https://www.gmbinder.com/images/WQXIOUB.png' class='cover-image bgwatercolor' style="top:50px; transform: scaleX(-1); filter:brightness(94%) sepia(15%)">


### Targets
#### Being
A Being is one of the three classifications used by the Ministry of Magic to catalogue the various magical Creatures that inhabit the wizarding world (the others being Beast and Spirit). The definition of a Being is any creature that has sufficient intelligence to understand the laws of the magical community and to bear part of the responsibility in shaping those laws.

All humans are beings, as are goblins, vampires, hags, giants, house-elves, veela, werewolves, merpeople and centaurs. Dementors, boggarts and poltergeists are neither Beings nor Beasts, as they are Non-Beings.
#### Beast
A Beast is any living thing that is does not fit the criteria of a Being. Wild animals and all the creatures students learn about in Care of Magical Creatures are classified as Beasts. Some creatures appear to fit the qualifications that define Being (intelligent speech), such as Acromantulas, Sphinxes, Manticores, and Erklings. These have not been offered Being status due to their extremely violent and even lethal tendencies, which interferes with their role in a lawful society. They are thus classified as Beasts.

<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### Object
An object is quite simply that, an inanimate object. Don’t let movement, imitations of life or even intelligent speech deceive you; there are many enchantments and bewitched objects out there in the magical world that can make an inanimate object quite animate. Never trust something that thinks if you don’t see a place for its brain.
#### Spirit
The Spirit classification was formed when ghosts complained that it was insensitive to classify them as “beings,” when they were so clearly “has-beens.” They’ve often been dissatisfied with governments focusing more on the matters of the living than on the matters of the dead.
## Unique Spells
### Apparition
Apparition is the method by which many adult witches and wizards choose to travel from place to place. When one apparates, they turn on the spot, "feeling [their] way into nothingness," and vanish from their present location to reappear a second later in a new location, accompanied by a loud cracking or popping sound.

Apparition, much like muggle driving, requires the individual take an exam to acquire a license at the age of 17.  To prepare, 16-year-olds can take lessons in apparition, usually by practicing short jumps of only a few feet in the presence of an instructor. This is because the process can be dangerous; if the witch or wizard does not have the proper focus when they apparate, they may leave a part of themselves behind.
#### How to Apparate
In order to apparate, you must have a proficiency bonus of +4 or greater; the process demands a certain level of magical skill that is beyond younger witches and wizards. 

Though apparition is not technically a spell, it taxes the body much like a spell, and requires you to expend a spell slot. Longer distances require more power and higher level spell slots. Apparition also requires a wand.
<div style="margin-top:40px;"></div>

| Slot Level | Apparition Range |
|:---:|:------------|
| 1st | 10 ft |
| 2nd | 50 ft |
| 3rd | 200 ft |
| 4th | 1,000 ft |
| 5th | 1 mile |
| 6th | 5 miles |
| 7th | 20 miles |
| 8th | 100 miles |
| 9th | 500 miles |

As an action, you can attempt to disapparate. Make an ability check using your spellcasting ability. Other modifiers may add to or subtract from your total. The final result determines if you arrive successfully. If you do, you immediately apparate in an unoccupied space within the distance allowed by the spell slot you expended, automatically compensating for any creatures or objects that may be in your intended space. Because apparition is not a spell, it cannot be countered.

**Leisurely Departure.** For most adults, apparition is a straight-forward process to get to work, run errands or even go downstairs, and there are no immediate threats distracting you. Some good reasons for not having a leisurely departure are: being under fire, being in the presence of a particularly terrifying creature, or suffering significant wounds (missing half your hit points). Leisurely departure is decided by the HM and grants advantage on your apparition ability check.
<div style="margin-top:40px;"></div>

| Ability Check | Apparition Result |
|:----:|:-------|
| 15 or higher | You disapparate properly and arrive safely. |
| 11-14 | You disapparate but arrive off-target (d20). |
| 7-10 | The disapparition feels off and you stop yourself. Nothing happens. |
| 5-6 | You suffer a minor splinch and arrive off-target (d20). |
| 4 or lower  | You suffer a major splinch and arrive off-target (d100). |

<div style="margin-top:40px;"></div>

#### Destination, Determination, Deliberation
You must visualize your destination when you attempt to apparate. Typically, this means a wizard can only apparate to a location they've been to before and can clearly remember. Apparating to a new location that is in close proximity to a known location may be possible, but may remove the benefit of leisurely departure or even apply disadvantage to the ability check. How difficult it is to apparate to your desired destination is decided by the HM.

**Off-Target.** If you apparate off-target, you appear a random distance away from the destination in a random direction. Distance off-target is determined by a die roll that gives you the percent of the distance that was to be traveled (i.e. if you meant to travel 120 miles, and rolled a 15, you would be 15% of 120 miles off target, or 18 miles). Depending on the severity of your error, the dice used may be a d20 or d100. To determine the direction, roll a d8 and assign a direction to each die face.

<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum

<div style="margin: 0px 0px 420px 0px"></div><img src="https://vignette.wikia.nocookie.net/harrypotter/images/a/aa/Ron_Splinched_in_Deathly_Hallows_Part_1.jpg/revision/latest?cb=20120812183706" class="cover-image" style="top:-290px; left:-420px;"><img src="https://www.gmbinder.com/images/W7kvPfG.png" class="cover-image bgwatercolor" style="width:100%; top:-480px; transform: scaleX(1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/ShMie2y.png" class="cover-image bgwatercolor" style="width:121%; left: inherit; right:0px; transform: scaleX(-1); filter:brightness(94%) sepia(15%)">

**Wandless Apparition.** Apparating without a wand is far more difficult and dangerous than other wandless magic, which is already rarely practiced. To attempt to apparate without a wand, you must have the Wandless Magic feat, you cannot gain the benefit of a leisurely departure, you have disadvantage on the ability check, and you must expend a spell slot two levels higher than the slot you normally would expend.

#### Side-Along Apparition
When you apparate, you may bring along a number of creatures equal to your spellcasting ability modifier. Every passenger imposes a -2 penalty on your apparition roll. Each creature must be holding on to either you or another creature that is also holding on to you, and you must make a separate apparition ability check for each creature with the same total side-along penalty and the same advantage or disadvantage. This roll only determines whether or not that creature is splinched. Normal splinching rules apply.

**Forced Side-Along Apparition.** If a creature is grappling you when you disapparate, they side-along apparate with you and you have disadvantage on the roll, in addition to the side-along penalty from the additional passenger. If an enemy creature is within 5 feet of you when you disapparate, they can use their reaction to attempt to grapple you before you vanish.

#### Splinching
When you are splinched, you've left a part of yourself behind at your previous location, instead of apparating your entire body. Usually, splinching is a result of not having the proper determination while apparating. How much of you is left behind is determined by whether you had a minor or major splinch.

A minor splinch is when the lost body part is generally non-threatening; perhaps an eyebrow, a part of your finger, or a small section of skin. You determine how much slashing damage you suffer by rolling a single d10. This damage cannot be reduced or prevented in any way.

A major splinch is far more severe and often life threatening. You lose a large body part, such as a leg or arm, or a piece of flesh is ripped from your body. Roll a number of d6 dice equal to your level. You suffer that much slashing damage and a level of exhaustion. This damage cannot be reduced or prevented in any way. At the start of your following turns, you take slashing damage equal to half your level as you bleed out, which ends as soon as you receive hit points from a healing effect.


If you are splinched, the HM will roll on the appropriate table to determine the result. If you lose flesh, the HM can either determine the location arbitrarily, or you can agree on an appropriate spot. For example, if you were being grabbed by an enemy on your right arm, the splinch would likely have occurred there.
<div style="margin-top:40px;"></div>

| d6 | Minor Splinch Result |
|:--:|:-------|
| 1 | You lose a part of a finger. |
| 2 | You lose a toe. |
| 3 | You lose a piece of one of your ears. |
| 4 | You lose a small piece of skin. |
| 5 | You lose one of your eyebrows. |
| 6 | You lose an article of clothing. |
<div style="margin-top:40px;"></div>

| d6 | Major Splinch Result |
|:---:|:---------------|
| 1-2 | You lose part of a leg. |
| 3 | You lose an arm. |
| 4-6 | You lose a large amount of flesh. |
<div style="margin-top:40px;"></div>


### Legilimency and Occlumency
Legilimency is the incredibly rare practice of using magic to pull information from an individual's mind. While this mysterious art often goes unnoticed, there are a select few people who have prepared themselves to resist this magic, called occlumens. The cerebral battle between a legilimens and an occlumens is a direct contest of discipline. An occlumens must keep their mind clear in an almost meditative state, while a legilimens must probe and test to find a weakness in those mental defenses. 

<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum

If a target of the *legilimens* spell has the Occlumency Training feat, their training gives them the chance to make a Wisdom saving throw to immediately resist the intrusion into their mind. Additionally, that occlumens is experienced in the techniques used to throw a person out of their mind and has advantage on the Intelligence contests between them and the legilimens. If the target has the Skilled Occlumens school of magic feature, their mental defenses are flawless. A legilimens cannot even read their surface thoughts and the spell has no effect on them.

Those trained in occlumency have one more trick up their sleeve. If they resist the effects of the *legilimens* spell, they have the choice of immediately ending the spell or fabricating anything of their choosing to show to the legilimens. The legilimens has no way of detecting that the information is any different from the target's true inner thoughts. As a legilimens probes deeper, the occlumens can invent more and more intricate details, constructing false memories and giving misleading information.

### Patronus Casting
The patronus charm is a special bit of magic that requires a wizard to envision one of their happiest memories while casting the spell. If the feeling of happiness is not genuine or not strong enough, the casting attempt will fail. In its most basic form, successfully casting the spell results in a non-corporeal patronus charm, which looks like a beam or ball of bluish-white light being emitted from the caster’s wand. A more advanced form of the charm is the corporeal patronus, which is when that glowing essence forms into the shape of an animal or magical beast. The corporeal shape of a patronus is a reflection of the witch’s soul and is often quite intimate.

A wizard’s corporeal patronus is also the animal that they will transform into during their animagus transformation. The first time you cast *expecto patronum* or complete your animagus transformation, use Appendix B: Patronus Rolling Tables to determine its shape. At your HM's discretion, you can select your desired patronus instead of rolling for it.
## Spell Conversions
Although the spells of Harry Potter have incredible effects, some share similiarities with existing 5e spells. The below tables connect new spell names to equivalent 5e spell names. Because each spell is designed around the effects within the Wizarding World, almost every spell is modified in some way. Players shouldn't assume that just because there's an equivalent 5e spell, the Harry Potter spell will operate in exactly the same way or have the exact same description.

More than one new spell can correspond to a single 5e spell, and the opposite applies if a new spell contains the function of multiple 5e spells. If a spell is not listed in the following tables, it means it is an entirely new spell and does not have a 5e equivalent.

\columnbreak
<div class='classTable' style='margin-top:17px;'>
<span style="text-align:center">

##### Charms Conversions</span>
| W&W Spell                     | Equivalent 5e Spell       |
|:-----------------------------:|:-------------------------:|
| Abscondi                      | Pass without Trace        |
| Accio                         | Mage Hand                 |
| Alohomora, Cistem Aperio      | Knock                     |
| Cave Inimicum                 | Tiny Hut                  |
| Colloportus                   | Arcane Lock               |
| Colovaria                     | Minor Illusion            |
| Confundo                      | Confusion, Suggestion     |
| Defodio                       | Mold Earth                |
| Depulso                       | Arcane Hand               |
| Diminuendo, Reducio           | Reduce                    |
| Dissonus Ululatus, Vigilatus  | Alarm                     |
| Engorgio                      | Enlarge                   |
| Exhilaro, Rictusempra         | Hideous Laughter          |
| Finite Incantatem             | Dispel Magic              |
| Flagrate                      | Illusory Script           |
| Glacius                       | Shape Water               |
| Herbivicus                    | Plant Growth              |
| Immobulus                     | Color Spray               |
| Locomotor, Mobilicorpus       | Floating Disk             |
| Lumos/Nox                     | Light                     |
| Lumos Maxima                  | Daylight                  |
| Novum Spirare                 | Water Breathing           |
| Obliviate                     | Modify Memory             |
| Pellucidi Pellis              | Invisibility              |
| Pereo                         | Control Flames            |
| Piertotum Locomotor           | Animate Objects           |
| Protego                       | Shield                    |
| Protego Maxima                | Mage Armor                |
| Protego Totalum               | Globe of Invulnerability  |
| Reparo                        | Mending                   |
| Repello Inimicum              | Magic Circle              |
| Repello Muggletum             | Suggestion                |
| Scourgify                     | Prestidigitation          |
| Silencio                      | Silence                   |
| Sonorus/Quietus               | Thaumaturgy               |
| Tergeo                        | Shape Water               |
| Wingardium Leviosa            | Levitate                  |
</div>

<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
<div class='classTable' style='margin-top:25px;'>
<span style="text-align:center">

##### Jinxes, Hexes and Curses Conversions</span>
| W&W Spell         | Equivalent 5e Spell   |
|:-----------------:|:---------------------:|
| Avada Kedavra     | Power Word: Kill      |
| Azreth            | Firestorm             |
| Bombarda          | Fire Bolt             |
| Colloshoo         | Entangle              |
| Confringo         | Fireball              |
| Conjunctivia      | Blindness/Deafness    |
| Crucio            | Power Word: Pain      |
| Devicto           | Ray of Frost          |
| Expulso           | Shatter, Thunderwave  |
| Furnunculus, Densaugeo | Vicious Mockery       |
| Impedimenta       | Slow                  |
| Imperio           | Dominate Person       |
| Infirma Cerebra   | Mind Sliver           |
| Langlock          | Counterspell          |
| Oppugno           | Cloud of Daggers      |
| Petrificus Totalus| Hold Person           |
| Relashio          | Knock                 |
| Sectumsempra      | Vitriolic Sphere      |
| Ventus            | Gust                  |
</div>

<div class='classTable' style='margin-top:200px;'>
<span style="text-align:center">

##### Healing Conversions</span>
| W&W Spell | Equivalent 5e Spell |
|:-----------------:|:---------------------:|
| Anapneo           | Spare the Dying       |
| Episkey           | Healing Word          |
| Rennervate        | Lesser Restoration    |
| Reparifors        | Cure Wounds, Lesser Restoration |
| Vulnera Sanentur  | Regenerate            |
</div>



\columnbreak

<div class='classTable' style='margin-top:25px;'>
<span style="text-align:center">

##### Transfiguration Conversions</span>
| W&W Spell         | Equivalent 5e Spell           |
|:-----------------:|:-----------------------------:|
| Aguamenti         | Create or Destroy Water       |
| Avis              | Conjure Animals               |
| Crinus Muto       | Disguise Self                 |
| Draconifors       | Conjure Elemental             |
| Ebublio           | Watery Sphere                 |
| Ignis Furore      | Minute Meteors, Wall of Fire  |
| Ignis Laqueis     | Thorn Whip                    |
| Incendio          | Create Bonfire                |
| Incendio Glacia   | Produce Flame                 |
| Lapifors          | Polymorph                     |
| Nebulus           | Fog Cloud                     |
| Obscuro, Melofors | Blindness/Deafness            |
| Orbis             | Maximilian’s Earthen Grasp    |
| Orchideous        | Druidcraft                    |
| Reparifarge       | Dispel Magic                  |
| Serpensortia      | Conjure Animal                |
| Tarantallegra     | Irresistable Dance            |
| Transmogrify      | Power Word: Pain              |
</div>

<div style="text-align:right; margin: 10px -10px 0px 0px; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;">
Art by Jeff Brown
</div>
<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1a76386f-1d10-401d-a8b8-dbfc10cdd2e9/d813wd8-03ad5f76-0340-40af-bfe9-1f71ae379e8f.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzFhNzYzODZmLTFkMTAtNDAxZC1hOGI4LWRiZmMxMGNkZDJlOVwvZDgxM3dkOC0wM2FkNWY3Ni0wMzQwLTQwYWYtYmZlOS0xZjcxYWUzNzllOGYuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0._QdGweoAvqf8JmGr2j1cbVp3HfUW7wA3Ks7TWLr92ho" class="cover-image" style="width:130%; top:410px; left:-110px; transform:scaleX(-1);"><img src="https://www.gmbinder.com/images/Tkbl4ji.png" class="cover-image bgwatercolor" style="width:100%; top:-140px; transform:scaleY(-1); filter:brightness(94%) sepia(15%)"><img src="https://www.gmbinder.com/images/gezbRSW.png" class="cover-image bgwatercolor" style="width:100%; top:440px; transform:scaleY(-1); filter:brightness(94%) sepia(15%)">

<div class='classTable' style='margin-top:190px;'>
<span style="text-align:center">

##### Divination Conversions</span>
| W&W Spell | Equivalent 5e Spell |
|:-----------------:|:-----------------:|
| Homenum Revelio   | Locate Person     |
| Revelio           | See Invisibility  |
| Specialis Revelio | Identify          |
</div>

<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
<div class='spellList'>

## Spell List
<!--<p style='width:200%;font-family: BookSanity;font-size: .317cm;text-rendering: optimizeLegibility;'></p>

\columnbreak

<div style="margin-top:125px;"></div>
-->

All characters have the same spell list, but spells that can only be learned through a school of magic or feature are indicated with an asterisk.
<span id="spell-list"></span>
### Charms
##### Cantrips (0 Level)
- [Accio](#spell-descr-Accio)
- [Alohomora](#spell-descr-Alohomora)
- [Capto](#spell-descr-Capto)
- [Carpe Retractum](#spell-descr-Carpe-Retractum)
- [Cistem Aperio](#spell-descr-Cistem-Aperio)
- [Colloportus](#spell-descr-Colloportus)
- [Colovaria](#spell-descr-Colovaria)
- [Defodio](#spell-descr-Defodio)
- [Duro](#spell-descr-Duro)
- [Finestra](#spell-descr-Finestra)
- [Flagrate](#spell-descr-Flagrate)
- [Glisseo](#spell-descr-Glisseo)
- [Illegibilus](#spell-descr-Illegibilus)
- [Impervius](#spell-descr-Impervius)
- [Lumos/Nox](#spell-descr-Lumos-Nox)
- [Molliare](#spell-descr-Molliare)
- [Pereo](#spell-descr-Pereo)
- [Periculum/Verdimillious](#spell-descr-Periculum-Verdimillious)
- [Scourgify](#spell-descr-Scourgify)
- [Sonorus/Quietus](#spell-descr-Sonorus-Quietus)
- [Spongify](#spell-descr-Spongify)
- [Tergeo](#spell-descr-Tergeo)
- [Wingardium Leviosa](#spell-descr-Wingardium-Leviosa)
##### 1st Level
- [Arresto Momentum](#spell-descr-Arresto-Momentum)
- [Diffindo](#spell-descr-Diffindo) <sup>**R**</sup>
- [Exhilaro](#spell-descr-Exhilaro) <sup>**R**</sup>
- [Glacius](#spell-descr-Glacius) <sup>**R**</sup>
- [Locomotor](#spell-descr-Locomotor) <sup>**R**</sup>
- [Mobilicorpus](#spell-descr-Mobilicorpus) <sup>**R**</sup>
- [Perfusorius](#spell-descr-Perfusorius) <sup>**R**</sup>
- [Protego](#spell-descr-Protego)
- [Reducio](#spell-descr-Reducio) <sup>**R**</sup>
- [Rictusempra](#spell-descr-Rictusempra)
- [Riddikulus](#spell-descr-Riddikulus)
- [Vigilatus](#spell-descr-Vigilatus) <sup>**R**</sup>
##### 2nd Level
- [Abscondi](#spell-descr-Abscondi) <sup>**R**</sup>
- [Diminuendo](#spell-descr-Diminuendo)
- [Engorgio](#spell-descr-Engorgio) <sup>**R**</sup>
- [Expelliarmus](#spell-descr-Expelliarmus)
- [Finite Incantatem](#spell-descr-Finite-Incantatem)
- [Fumos](#spell-descr-Fumos)
- [Geminio](#spell-descr-Geminio) <sup>**R**</sup>
- [Immobulus](#spell-descr-Immobulus)
- [Muffliato](#spell-descr-Muffliato)*
- [Partis Temporus](#spell-descr-Partis-Temporus)
- [Pellucidi Pellis](#spell-descr-Pellucidi-Pellis)
- [Protego Maxima](#spell-descr-Protego-Maxima)
- [Reparo](#spell-descr-Reparo) <sup>**R**</sup>
- [Silencio](#spell-descr-Silencio) <sup>**R**</sup>
- [Stupefy](#spell-descr-Stupefy)
##### 3rd Level
- [Deprimo](#spell-descr-Deprimo) <sup>**R**</sup>
- [Depulso](#spell-descr-Depulso)
- [Dissonus Ululatus](#spell-descr-Dissonus-Ululatus)
- [Expecto Patronum](#spell-descr-Expecto-Patronum) <sup>**R**</sup>
- [Fianto Duri](#spell-descr-Fianto-Duri)
- [Fortissimum](#spell-descr-Fortissimum)
- [Herbivicus](#spell-descr-Herbivicus)
- [Lumos Maxima](#spell-descr-Lumos-Maxima) <sup>**R**</sup>
- [Novum Spirare](#spell-descr-Novum-Spirare) <sup>**R**</sup>
- [Repello Inimicum](#spell-descr-Repello-Inimicum)
##### 4th Level
- [Capacious Extremis](#spell-descr-Capacious-Extremis)*
- [Confundo](#spell-descr-Confundo) <sup>**R**</sup>
- [Repello Muggletum](#spell-descr-Repello-Muggletum) <sup>**R**</sup>
##### 5th Level
- [Cave Inimicum](#spell-descr-Cave-Inimicum)
- [Ne Ustio](#spell-descr-Ne-Ustio)
- [Obliviate](#spell-descr-Obliviate)*
- [Piertotum Locomotor](#spell-descr-Piertotum-Locomotor)*
- [Salvio Hexia](#spell-descr-Salvio-Hexia)
##### 6th Level
- [Protego Totalum](#spell-descr-Protego-Totalum)*
##### 9th Level
- [Fidelius Mysteria Celare](#spell-descr-Fidelius-Mysteria-Celare)*

### Jinxes, Hexes, and Curses
##### Cantrips (0 Level)
- [Bombarda](#spell-descr-Bombarda)
- [Cantis](#spell-descr-Cantis)
- [Devicto](#spell-descr-Devicto)
- [Furnunculus](#spell-descr-Furnunculus)
- [Genu Recurvatum](#spell-descr-Genu-Recurvatum)
- [Infirma Cerebra](#spell-descr-Infirma-Cerebra)
- [Locomotor Wibbly](#spell-descr-Locomotor-Wibbly)
##### 1st Level
- [Colloshoo](#spell-descr-Colloshoo)
- [Densaugeo](#spell-descr-Densaugeo)
- [Digitus Wibbly](#spell-descr-Digitus-Wibbly)
- [Flipendo](#spell-descr-Flipendo)
- [Locomotor Mortis](#spell-descr-Locomotor-Mortis)
- [Mimblewimble](#spell-descr-Mimblewimble)
- [Petrificus Totalus](#spell-descr-Petrificus-Totalus)
##### 2nd Level
- [Arania Exumai](#spell-descr-Arania-Exumai)
- [Oppugno](#spell-descr-Oppugno)
- [Relashio](#spell-descr-Relashio)
- [Slugulus Eructo](#spell-descr-Slugulus-Eructo)
- [Tarantallegra](#spell-descr-Tarantallegra)
- [Ventus](#spell-descr-Ventus) <sup>**R**</sup>
##### 3rd Level
- [Confringo](#spell-descr-Confringo)
- [Conjunctivia](#spell-descr-Conjunctivia)
- [Expulso](#spell-descr-Expulso)
- [Impedimenta](#spell-descr-Impedimenta)
- [Langlock](#spell-descr-Langlock)*
##### 4th Level
- [Levicorpus/Liberacorpus](#spell-descr-Levicorpus-Liberacorpus)
- [Muco Volatilis](#spell-descr-Muco-Volatilis)
- [Reducto](#spell-descr-Reducto)
- [Sectumsempra](#spell-descr-Sectumsempra)*
##### 5th Level
- [Imperio](#spell-descr-Imperio)
- [Nullum Effugium](#spell-descr-Nullum-Effugium)*
- [Omnifracto](#spell-descr-Omnifracto)*
##### 7th Level
- [Azreth](#spell-descr-Azreth)
- [Crucio](#spell-descr-Crucio)
##### 8th Level
- [Avada Kedavra](#spell-descr-Avada-Kedavra)

### Transfiguration
##### Cantrips (0 Level)
- [Aguamenti](#spell-descr-Aguamenti)
- [Crinus Muto](#spell-descr-Crinus-Muto)
- [Epoximise](#spell-descr-Epoximise)
- [Incendio Glacia](#spell-descr-Incendio-Glacia)
- [Orchideous](#spell-descr-Orchideous)
- [Vera Verto](#spell-descr-Vera-Verto)
##### 1st Level
- [Inanimatus Conjurus](#spell-descr-Inanimatus-Conjurus) <sup>**R**</sup>
- [Incendio](#spell-descr-Incendio) <sup>**R**</sup>
- [Nebulus](#spell-descr-Nebulus)
- [Obscuro](#spell-descr-Obscuro) <sup>**R**</sup>
- [Sagittario](#spell-descr-Sagittario)
##### 2nd Level
- [Incarcerous](#spell-descr-Incarcerous) <sup>**R**</sup>
- [Orbis](#spell-descr-Orbis)*
- [Reparifarge](#spell-descr-Reparifarge)*
- [Serpensortia](#spell-descr-Serpensortia)
##### 3rd Level
- [Avis](#spell-descr-Avis)
- [Evanesco](#spell-descr-Evanesco)
- [Ignis Laqueis](#spell-descr-Ignis-Laqueis)*
- [Melofors](#spell-descr-Melofors)
##### 4th Level
- [Ebublio](#spell-descr-Ebublio) <sup>**R**</sup>
- [Lapifors](#spell-descr-Lapifors)*
##### 5th Level
- [Draconifors](#spell-descr-Draconifors)
- [Transmogrify](#spell-descr-Transmogrify)
##### 6th Level
- [Ignis Furore](#spell-descr-Ignis-Furore)

### Healing
##### Cantrips (0 Level)
- [Anapneo](#spell-descr-Anapneo)*
- [Rennervate](#spell-descr-Rennervate)
##### 1st Level
- [Episkey](#spell-descr-Episkey)
- [Ferula](#spell-descr-Ferula)
- [Reparifors](#spell-descr-Reparifors)
##### 3rd Level
- [Intus Sunt](#spell-descr-Intus-Sunt) <sup>**R**</sup> *
##### 4th Level
- [Brackium Emendo](#spell-descr-Brackium-Emendo)
##### 6th Level
- [Vulnera Sanentur](#spell-descr-Vulnera-Sanentur)*

### Divination
##### Cantrips (0 Level)
- [Point Me](#spell-descr-Point-Me)
- [Prior Incantato](#spell-descr-Prior-Incantato)
##### 1st Level
- [Specialis Revelio](#spell-descr-Specialis-Revelio)
##### 3rd Level
- [Legilimens](#spell-descr-Legilimens)*
- [Revelio](#spell-descr-Revelio)
##### 4th Level
- [Appare Vestigium](#spell-descr-Appare-Vestigium) <sup>**R**</sup>
- [Homenum Revelio](#spell-descr-Homenum-Revelio)
</div>
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum


## Spell Descriptions
The spells are presented in alphabetical order.
#### [Abscondi](#spell-list)
<span id="spell-descr-Abscondi"></span>
*The Track Obliteration Charm - 2nd-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** Self
- **Duration:**  Concentration, up to 1 hour
___
A magical aura makes your impact on your surroundings unseen, masking you and your companions from detection. For the duration, each creature you choose within 30 feet of you (including you) has a +10 bonus to Dexterity (Stealth) checks and can’t be tracked except by magical means. A creature that receives this bonus leaves behind no tracks or other traces of its passage.
#### [Accio](#spell-list)
<span id="spell-descr-Accio"></span>
*The Summoning Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:**  Instantaneous
___
A target object is pulled directly to the caster as if carried by an invisible hand. The object is selected by pointing at it with a wand or by naming it, Accio broom. An object heavier than 20 pounds may not be summoned.

***At Higher Levels.*** When you cast this spell using a spell slot of 1st level or higher, you may select or stack one of the following effects for each slot level above 0.
* Increase spell range by 100 feet.
* Increase weight limit by 20 pounds.
* Increase the number of targetable objects by 5.
#### [Aguamenti](#spell-list)
<span id="spell-descr-Aguamenti"></span>
*The Water-Making Spell - Transfiguration cantrip*
___
- **Casting Time:** 1 action
- **Range:** Self (30 foot cone)
- **Duration:** Dedication, up to 1 minute
___
A cone of clear, pure water shoots from the tip of the caster's wand with the desired force. The water doesn’t go bad and extinguishes exposed flames in the area.
#### [Alohomora](#spell-list)
<span id="spell-descr-Alohomora"></span>
*The Unlocking Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:**  Instantaneous
___
Choose a door or window that you can see within range, that uses mundane or magical means to prevent access.

A target that is held shut by a mundane lock or that is stuck or barred becomes unlocked, unstuck, or unbarred. If the object has multiple locks, only one of them is unlocked.

If you choose a target that is held shut with Colloportus, that spell is removed.

When you cast the spell, the mechanism noisily turns and unlocks. This noise emanates from the target object and is audible from as far away as 100 feet.

\columnbreak
#### [Anapneo](#spell-list)
<span id="spell-descr-Anapneo"></span>
*The Airway Clearing Spell - Healing cantrip*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Instantaneous
- **Tags:** School of Magic - *Healing*
___
A being's airway is cleared and they are assisted in breathing. If used on a living being that has 0 hit points, the being becomes stable.
#### [Appare Vestigium](#spell-list)
<span id="spell-descr-Appare-Vestigium"></span>
*The Tracking Spell - 4th-level Divination (ritual)*
___
- **Casting Time:** 1 minute
- **Range:** Self (30-foot-radius hemisphere)
- **Duration:** Concentration, up to 10 minutes
___
With a spin and a spray of golden mist, recent magical activity is revealed and illuminated through ghostly images hanging in the air, recreating the magical beings, magical creatures, or magical events that have been in the area within the last 10 minutes. Magical footprints and track marks are also highlighted on the ground. Any of the effects can be hidden, highlighted, or expanded for the duration.

***At Higher Levels.*** When you cast this spell using a spell slot of a higher level, the historical window extends to 1 hour (5th level), 24 hours (6th level), or a week (7th level).

#### [Arania Exumai](#spell-list)
<span id="spell-descr-Arania-Exumai"></span>
*The Spider Repelling Spell - 2nd-level Curse*
___
- **Casting Time:** 1 action
- **Range:** Self (30 foot cone)
- **Duration:** Instantaneous
___
This spell blasts away spiders, Acromantulas, or arachnids with a cone of bright scorching light. Each spider-like creature in a 30-foot cone must make a Constitution saving throw. On a failed save, a creature takes 4d6 radiant damage and is knocked back 5 feet plus a number of feet equal to five times your spellcasting ability modifier. On a successful save, it takes half as much damage and isn't knocked back.

Any non-arachnid creatures within the area of the spell are unaffected.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d6 and the shove distance increases by 10 feet for each slot level above 2nd.
#### [Arresto Momentum](#spell-list)
<span id="spell-descr-Arresto-Momentum"></span>
*The Slowing Charm - 1st-level Charm*
___
- **Casting Time:** 1 reaction, which you take when you or a creature within 60 feet of you falls
- **Range:** 60 feet
- **Duration:**  1 minute
___
Choose up to five falling creatures within range. A falling creature's rate of descent slows to 60 feet per round until the spell ends. If the creature lands before the spell ends, it takes no falling damage and can land on its feet, and the spell ends for that creature.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Avada Kedavra](#spell-list)
<span id="spell-descr-Avada-Kedavra"></span>
*The Killing Curse - 8th-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
- **Tags:** Dark - *Unforgivable Curse*
___
The most dangerous of the Unforgivables, Avada Kedavra channels the caster's pure hatred into an unblockable spell that kills whatever it strikes. Make a ranged spell attack against a target within range. On a hit and if the target has 100 hit points or fewer, it dies or is destroyed. Otherwise, the spell has no effect. Defensive spells have no effect against this spell and it can only be blocked by physical objects.

***At Higher Levels.*** When you cast this spell using a spell slot of 9th level, there is no hit point restriction.
#### [Avis](#spell-list)
<span id="spell-descr-Avis"></span>
*The Bird-Conjuring Charm - 3rd-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Concentration, up to 1 hour
___
You conjure either a Swarm of Small Birds or two Swarms of Tiny Birds that are a species of your choice. The swarm disappears when it drops to 0 hit points or when the spell ends.

The conjured birds are friendly to you and your companions. Roll initiative for the summoned swarms as a group, which has its own turns. They obey any verbal commands that you issue to them (no action required by you). If you don't issue any commands to them, they defend themselves from hostile creatures, but otherwise take no actions. 

The HM has the creatures' statistics.

***At Higher Levels.*** When you cast this spell using certain higher-level spell slots, more creatures appear - twice as many with a 5th-level slot, three times as many with a 7th-level slot, and four times as many with a 9th-level slot.
#### [Azreth](#spell-list)
<span id="spell-descr-Azreth"></span>
*Fiendfyre - 7th-level Curse*
___
- **Casting Time:** 1 action
- **Range:** Self (10 foot cube)
- **Duration:** Dedication, up to 42 seconds
- **Tags:** Dark
___
Great plumes of cursed fire pour out from the tip of your wand, rampaging into shapes of beasts and incinerating anything in their path. Upon casting, the area of the fiendfyre is one 10-foot cube, with the number of 10-foot cubes doubling at the beginning of each of your turns. As long as concentration is maintained, you can arrange any newly added cubes as you wish. Each cube must have at least one face adjacent to the face of another cube. Each creature in the area must make a Dexterity saving throw. It takes 7d10 fire damage on a failed save, or half as much damage on a successful one. A creature takes the same damage when it enters the area for the first time on a turn or ends its turn there.

Upon reaching 8 cubes, you must make a DC15 Constitution saving throw to maintain concentration at the beginning of each of your turns. If your concentration is broken after 4 cubes of fiendfyre are active, the spell doesn't end and rages out of control. The fiendfyre will continue to double at the beginning of each round, until the end of its duration. If you decide to end the spell while you still have concentration, the spell ends as normal and all fiendfyre disappears.

The fiendfyre damages objects in the area and ignites flammable objects that aren’t being worn or carried. Even magical objects and defenses are damaged or destroyed by this spell.

***At Higher Levels.*** When you cast this spell using a spell slot of 8th level or higher, the damage increases by 2d10 and the concentration DC increases by 1 for each slot level above 7th.
#### [Bombarda](#spell-list)
<span id="spell-descr-Bombarda"></span>
*The Exploding Charm - Curse cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
- **Tags:** Dark
___
The spell blasts whatever it hits, creating a localized concussive explosion upon impact. Make a ranged spell attack against a target within range. On a hit, the target takes 1d10 bludgeoning damage.

This spell’s damage increases by 1d10 when you reach 5th level (2d10), 11th level (3d10), and 17th level (4d10).
#### [Brackium Emendo](#spell-list)
<span id="spell-descr-Brackium-Emendo"></span>
*The Bone Mending Spell - 4th-level Healing*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Instantaneous
___
This spell heals a being's broken bones immediately, although the process is quite painful. A being you can see that you tap with your wand regains a number of hit points equal to 5d10 + your spellcasting ability modifier, and gains a level of exhaustion.

***At Higher Levels.*** When you cast this spell using a spell slot of 5th level or higher, the healing increases by 1d10 for each slot level above 4th.
#### [Cantis](#spell-list)
<span id="spell-descr-Cantis"></span>
*The Singing Jinx - Curse cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 round
___
When struck by this spell, a being can't help but belt out a couple of lines from the first song that comes to mind. Make a ranged spell attack against a being within range. On a hit, the target must cast all other spells non-verbally until the end of its next turn. If it tries to cast a spell verbally, it must first succeed on an Intelligence saving throw, or the casting fails and the spell is wasted.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Capacious Extremis](#spell-list)
<span id="spell-descr-Capacious-Extremis"></span>
*The Undetectable Extension Charm - 4th-level Charm*
___
- **Casting Time:** 10 minutes
- **Range:** Touch
- **Duration:** Until dispelled
- **Tags:** School of Magic - *Charms*
___
Transform an ordinary small bag/pouch into a Handy Haversack's central pouch, a backpack into a Bag of Holding, or a trunk’s internal capacity into a Bag of Holding with: 3 ft. long and 2 ft. wide opening; internal size of 6 ft. long, 4 ft. wide, and 4 ft. deep; 1000 pounds and 150 cubic ft. limits.
#### [Capto](#spell-list)
<span id="spell-descr-Capto"></span>
*The Gripping Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** 10 minutes
___
One target object becomes quite easily gripped by one hand, almost sticky unless the holder willfully lets go. The holder has advantage against being non-magically disarmed.
#### [Carpe Retractum](#spell-list)
<span id="spell-descr-Carpe-Retractum"></span>
*The Seize and Pull Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 round
___
A bond of light shoots out from the caster and attaches to anything you can see within range, and then retracts, pulling caster and target each 10 feet closer. If the caster or target doesn't move or would easily resist the force of the other being pulled, the other moves 20 feet. If the target is an unwilling creature that is able to be moved, it must make a Strength saving throw to resist being moved. The bond of light keeps the caster and target attached for the duration.

***At Higher Levels.*** When you cast this spell using a spell slot of 1st level or higher, the range and pulling effect both increase by 5 feet for each slot level above 0.
#### [Cave Inimicum](#spell-list)
<span id="spell-descr-Cave-Inimicum"></span>
*The Hiding Charm - 5th-level Charm*
___
- **Casting Time:** 1 minute
- **Range:** Self (10-foot-radius hemisphere)
- **Duration:** 1 hour
- **Tags:** Defensive
___
A forcefield-like dome forms a perimeter around the caster that filters vision of anything or anyone designated by the caster, rendering those objects infallibly invisible. The dome is undetectable from the outside, but slightly visible from the inside, like a wavering glass barrier. Anyone can move through the field freely to see the hidden contents.

***At Higher Levels.*** When you cast this spell using a spell slot of 6th level or higher, you may select or stack one of the following effects for each slot level above 5th.
* Increase the spell radius by 20 feet.
* Increase the duration to 8 hours.
* Add the ability to completely block sounds.
* Add the ability to completely block smells.

\columnbreak
#### [Cistem Aperio](#spell-list)
<span id="spell-descr-Cistem-Aperio"></span>
*The Container Opening Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
___
Choose a box, chest, or another container that you can see within range that uses mundane or magical means to prevent access. 

A target that is held shut by a mundane lock or that is stuck or chained becomes unlocked, unstuck, or unchained. If the object has multiple locks, only one of them is unlocked.

If you choose a target that is held shut with Colloportus, that spell is dispelled.

When you cast the spell, the mechanism noisily turns and unlocks. This noise emanates from the target object and is audible from as far away as 100 feet.
#### [Colloportus](#spell-list)
<span id="spell-descr-Colloportus"></span>
*The Locking Spell - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Until dispelled
___
You touch a closed door, window, gate, chest, or other entryway, and it becomes locked for the duration. It is impassable until it is broken or the spell is dispelled or suppressed.

While affected by this spell, the object is more difficult to break or force open; the DC to break it or pick any locks on it increases by 10.
#### [Colloshoo](#spell-list)
<span id="spell-descr-Colloshoo"></span>
*The Stickfast Hex - 1st-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Concentration, up to 1 minute
___
This creative hex sticks a being's shoes to the ground, rooting them in place. Choose a being you can see within range that is wearing shoes to make a Dexterity saving throw. On a failed save, the target is restrained for the duration. If the saving throw fails by 5 or more, the target is knocked prone as well. The target can use its action to take off its shoes, or make a Strength check against your spell save DC. On a success, it pulls its shoes free.
#### [Colovaria](#spell-list)
<span id="spell-descr-Colovaria"></span>
*The Color Change Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** 1 hour
___
You change the color of any target within range that lasts for the duration, to any desired complexity. The color may only be reverted by dispelling the charm.

Physical interaction with the object reveals that the object has retained its original texture and material, but its color has truly changed.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Confringo](#spell-list)
<span id="spell-descr-Confringo"></span>
*The Blasting Curse - 3rd-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Instantaneous
- **Tags:** Dark
___
A tiny ball of fire flashes from your wand to a point you choose within range and then explodes into a fiery blast on impact. Each creature in a 10-foot-radius sphere centered on that point must make a Dexterity saving throw. A target takes 8d6 fire damage on a failed save, or half as much damage on a successful one. The fire spreads around corners. It ignites flammable objects in the area that aren’t worn or carried.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d6 and the radius increases by 5 feet for each slot level above 3rd.
#### [Confundo](#spell-list)
<span id="spell-descr-Confundo"></span>
*The Confundus Charm - 4th-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Concentration, up to 1 minute
___
The Confundus Charm is a particularly powerful charm that leaves anything confused, forgetful, and impressionable, often causing people to wander off absent-mindedly. If the target is an object you can see within range that operates or functions on its own, it will operate erratically, malfunction, or completely shut down. This spell has no effect on a completely inanimate objects that entirely depend on external manipulation.

If the target is a creature you can see within range, it must succeed on a Wisdom saving throw when you cast this spell or be affected by it. An affected target can’t take reactions and, if not distracted with something, you roll a d10. If you roll 1-8, the creature must use all its movement to move in a random direction. To determine the direction, assign a direction to each number 1-8. If you roll a 9-10, the creature doesn't move. Whether it moves or not, the creature doesn’t take an action this turn.

If desired, you can suggest a course of activity (limited to a sentence or two) at the time of casting and magically influence a creature you can see within range that can hear and understand you. Creatures that can’t be charmed are immune to this effect. The suggestion must be worded in such a manner as to make the course of action sound reasonable. Asking the creature to directly hurt itself or its allies will have no effect. The suggested course of action can continue for the entire duration. You can also specify conditions that will trigger a special activity during the duration. For example, you might suggest that a wizard hug the next blast-ended skrewt he sees. If the condition isn’t met before the spell expires, the activity isn’t performed.

At the end of each of its turns, an affected target can make a Wisdom saving throw. If it succeeds, the spell's effects end for that target.

***At Higher Levels.*** When you cast this spell using a spell slot of 5th level or higher, you can target one additional target for each slot level above 4th. The targets must be within 30 feet of each other when you target them.

\columnbreak
#### [Conjunctivia](#spell-list)
<span id="spell-descr-Conjunctivia"></span>
*The Conjunctivitis Curse - 3rd-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 minute
___
When struck by this curse, a creature's eyes to become irritated and painful, swelling shut. Make a ranged spell attack against a creature within range. On a hit, the target takes 4d8 necrotic damage and is blinded for the duration. At the end of each of its turns, the target can make a Constitution saving throw. On a success, the spell ends. Creatures that are normally magically resistant are vulnerable to this spell.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d8 for each slot level above 3rd.
#### [Crinus Muto](#spell-list)
<span id="spell-descr-Crinus-Muto"></span>
*The Haircut Spell - Transfiguration cantrip*
___
- **Casting Time:** 1 action
- **Range:** Self
- **Duration:** 1 hour
___
Your hair is magically lengthened, shortened, styled, or colored. This may also be applied to eyebrows and facial hair. If your appearance is drastically changed, you may be hard to recognize. To discern that you are disguised, a creature can use its action to inspect your appearance and must succeed on an Intelligence (Investigation) check against your spell save DC.
#### [Crucio](#spell-list)
<span id="spell-descr-Crucio"></span>
*The Cruciatus Curse - 7th-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Dedication, up to 1 minute
- **Tags:** Dark - *Unforgivable Curse*
___
With a single word and a heart full of hatred, waves of intense pain assail one creature you can see within range. If the target has 100 hit points or fewer, it is subject to crippling pain. Otherwise, the spell has no effect on it.

While the target is affected by crippling pain, any speed it has can be no higher than 10 feet. The target also has disadvantage on attack rolls, ability checks, and saving throws, other than Constitution saving throws. Finally, if the target tries to cast a spell, it must first succeed on a Constitution saving throw, or the casting fails and the spell is wasted.

A target suffering this pain must make a Constitution saving throw at the end of each of its turns. On a failed save, the target gains one level of exhaustion.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Defodio](#spell-list)
<span id="spell-descr-Defodio"></span>
*The Gouging Spell - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 30 feet (5 foot cube)
- **Duration:** Instantaneous
___
You choose a portion of dirt or stone that you can see within range and that fits within a 5-foot cube. You manipulate it in one of the following ways:

* If you target an area of stone or earth, you can instantaneously excavate it, move it along the ground, and deposit it up to 5 feet away. This movement doesn’t have enough force to cause damage.
* If the dirt or stone you target is on the ground, you cause it to become difficult terrain. Alternatively, you can cause the ground to become normal terrain if it is already difficult terrain. This change lasts for 1 hour. If cast multiple times, only two of this effect can be active at a time, and you can dismiss such an effect as a bonus action.

***At Higher Levels.*** When you cast this spell using a spell slot of 1st level or higher, the cube's size and distance the earth can be moved are each increased by 5 feet and the number of active normal/difficult terrain effects increase by 1 for each slot level above 0.
#### [Densaugeo](#spell-list)
<span id="spell-descr-Densaugeo"></span>
*The Bucktooth Hex - 1st-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
___
A target's front two teeth grow abnormally long, protruding downwards past its chin. Make a ranged spell attack against a creature within range. On a hit, it takes 2d8 psychic damage and has disadvantage on the next attack roll it makes before the end of its next turn.

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, the damage is increased by 1d8 for each slot level above 1st.
#### [Deprimo](#spell-list)
<span id="spell-descr-Deprimo"></span>
*The Crushing Charm - 3rd-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 120 feet
- **Duration:** Instantaneous
___
You place immense downward pressure on a target you can see within range. If the target is a creature, it must make a Strength saving throw. On a failed save, a creature takes 5d8 bludgeoning damage and is knocked prone. On a successful save, the creature takes half as much damage and isn’t knocked prone. If the target is a flat surface, this will either create a crater or collapse the surface.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the damage is increased by 1d8 for each slot level above 3rd.

\columnbreak
#### [Depulso](#spell-list)
<span id="spell-descr-Depulso"></span>
*The Banishing Charm - 3rd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
___
A target within range is pushed directly away from the caster as if shoved by an invisible hand, being thrown 5 feet away plus a number of feet equal to five times your spellcasting ability modifier. The target is selected by the caster pointing at it with their wand.

If targeting a creature or object that is being worn or carried, make a check with 26 Strength (+8) contested by the Strength (Athletics) check of the target creature. If the target is Medium or smaller, you have advantage on the check. If you succeed, the target is thrown the same distance.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the shove distance is increased by 10 feet for each slot level above 3rd.
#### [Devicto](#spell-list)
<span id="spell-descr-Devicto"></span>
*The Stinging Jinx - Curse cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
___
This weak jinx is a classic training spell between duelists, a startling sting on impact. Make a ranged spell attack against a creature within range. On a hit, it takes 1d6 force damage, and it can't take reactions until the start of its next turn.

The spell's damage increases by 1d6 when you reach 5th level (2d6), 11th level (3d6), and 17th level (4d6).
#### [Diffindo](#spell-list)
<span id="spell-descr-Diffindo"></span>
*The Severing Charm - 1st-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Instantaneous
___
An object is precisely torn or cut, as if a magical blade extended from the tip of your wand. This spell was not designed to be used on creatures and only makes very shallow cuts. Choose a target you can see within range that fits within a 5-foot cube. If the target is a creature, it must make a Dexterity saving throw. It takes 4d4 slashing damage on a failed save or half as much damage on a successful one. This is the counterspell to *incarcerous*, immediately ending that spell's effects.

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, you can target one additional creature or the cube's size increases by 5 feet for each slot level above 1st. If targeting additional creatures, the targets must be within 10 feet of each other when you target them.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Digitus Wibbly](#spell-list)
<span id="spell-descr-Digitus-Wibbly"></span>
*The Jelly-Fingers Jinx - 1st-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 minute
___
This jinx makes fingers numb and relaxed. Make a ranged spell attack against a being within range. On a hit, the target has disadvantage on attack rolls for the duration. At the start of each of its turns, the target can make a Dexterity saving throw. On a success, the spell ends.
#### [Diminuendo](#spell-list)
<span id="spell-descr-Diminuendo"></span>
*The Diminishing Charm - 2nd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Concentration, up to 1 minute
___
Make a ranged spell attack against a creature within range. On a hit, the being or beast's size is halved in all dimensions, and its weight is reduced to one-eighth of normal. This reduction decreases its size by one category - from Medium to Small, for example. 

Until the spell ends, the target also has disadvantage on Strength checks and Strength saving throws. The target's items or equipment also shrink to match its new size, but any item dropped by an affected creature returns to normal size at once. The target deals 1d4 less damage (this can't reduce the damage below 1).
#### [Dissonus Ululatus](#spell-list)
<span id="spell-descr-Dissonus-Ululatus"></span>
*The Caterwauling Charm - 3rd-level Charm*
___
- **Casting Time:** 10 minutes
- **Range:** Self (30-foot-radius hemisphere)
- **Duration:** 8 hours
- **Tags:** Defensive
___
You set an alarm to emit a piercing shriek when an unauthorized person enters the area. Until the spell ends, an alarm sounds whenever a Tiny or larger creature touches or enters the warded area. When you cast the spell, you can designate creatures or areas within the hemisphere that won't set off the alarm. The alarm produces an unpleasant screaming sound for as long as the intruding creature is in the area of the spell, audible from as far away as 300 feet.
#### [Draconifors](#spell-list)
<span id="spell-descr-Draconifors"></span>
*The Dragon-Making Spell - 5th-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Concentration, up to 10 minutes
___
A particularly intimidating display of transfiguration, this spell turns a desk-sized object into a miniature version of an adult dragon. Choose either one or two inanimate, nonmagical objects you can see within range that each fill a 5-foot cube and choose one of the following options: 

* One dragon wyrmling of challenge rating 4 or lower 
* Two dragon wyrmlings of challenge rating 2 or lower 

The object becomes a Medium-sized dragon construct with the chosen wyrmling's statistics, which is untransfigured when it drops to 0 hit points or when the spell ends.

The dragon construct is friendly to you and your companions for the duration. Roll initiative for the dragon construct, which has its own turns. It obeys any verbal commands that you issue to it (no action required by you). If you don't issue any commands to it, it defends itself from hostile creatures, but otherwise takes no actions.

If your concentration is broken, the dragon construct doesn't disappear. Instead, you lose control of the construct, it becomes hostile toward you and your companions, and it might attack. An uncontrolled dragon construct can't be dismissed by you, and it untransfigures 10 minutes after you transfigured it.

The HM has the creature's statistics.

***At Higher Levels.*** When you cast this spell using a spell slot of 7th level, choose one of the following options:

* Two dragon wyrmlings of challenge rating 3 or lower
* Three dragon wyrmlings of challenge rating 2 or lower

When you cast this spell using a spell slot of 9th level, choose one of the following options:

* Two dragon wyrmlings of challenge rating 4 or lower
* Four dragon wyrmlings of challenge rating 2 or lower

#### [Duro](#spell-list)
<span id="spell-descr-Duro"></span>
*The Hardening Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 minute
___
An object you can see within range becomes as hard and tough as stone. It gains resistance to all damage.
#### [Ebublio](#spell-list)
<span id="spell-descr-Ebublio"></span>
*The Bubble Spell - 4th-level Transfiguration (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Concentration, up to 1 minute
___
You conjure up a swirling sphere of water with a 5-foot radius at a point you can see within range. The sphere can hover but no more than 10 feet off the ground. The sphere remains for the spell’s duration.

Any creature in the sphere’s space must make a Strength saving throw. On a successful save, a creature is ejected from that space to the nearest unoccupied space of the creature’s choice outside the sphere. A Huge or larger creature succeeds on the saving throw automatically, and a Large or smaller creature can choose to fail it. On a failed save, a creature is restrained by the sphere and is engulfed by the swirling bubble of water. At the end of each of its turns, a restrained target can repeat the saving throw, ending the effect on itself on a success.

The sphere can restrain as many as four Medium or smaller creatures or one Large creature. If the sphere restrains a creature that causes it to exceed this capacity, a random creature that was already restrained by the sphere falls out of it and lands prone in a space within 5 feet of it.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum

As an action, you can move the sphere up to 30 feet in a straight line. If it moves over a pit, a cliff, or other drop-off, it safely descends until it is hovering 10 feet above the ground. Any creature restrained by the sphere moves with it. You can ram the sphere into creatures, forcing them to make the saving throw.

When the spell ends, the sphere falls to the ground and extinguishes all normal flames within 30 feet of it. Any creature restrained by the sphere is knocked prone in the space where it falls. The water then vanishes.
#### [Engorgio](#spell-list)
<span id="spell-descr-Engorgio"></span>
*The Engorgement Charm - 2nd-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** 1 minute
___
You cause a creature or an object you can see within range to grow larger for the duration. Choose either a creature or an object that isn’t being worn or carried. If the target is unwilling, it can make a Constitution saving throw. On a success, the spell has no effect.

The target's size doubles in all dimensions, and its weight is multiplied by eight. This growth increases its size by one category - from Medium to Large, for example. If there isn't enough room for the target to double its size, the creature or object attains the maximum possible size in the space available. Until the spell ends, the target also has advantage on Strength checks and Strength saving throws. The target's items and equipment also grow to match its new size. While enlarged, the target deals 1d4 extra damage.
#### [Episkey](#spell-list)
<span id="spell-descr-Episkey"></span>
*The Fast-Healing Spell - 1st-level Healing*
___
- **Casting Time:** 1 bonus action
- **Range:** 10 feet
- **Duration:** Instantaneous
___
A being of your choice that you can see within range regains hit points equal to 2d4 + your spellcasting ability modifier. This spell has no effect on undead or constructs.

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d4 for each slot level above 1st.

#### [Epoximise](#spell-list)
<span id="spell-descr-Epoximise"></span>
*The Sticking Spell - Transfiguration Cantrip*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** 1 hour
___
This spell transfigures the surface of an object to become extremely sticky. One object of your choice that you can see within range and that fits within a 1-foot cube adheres to anything it touches for the duration. If a creature wants to overcome the sticking effect, it can use its action to make a Strength check against your spell save DC. On a success, it can pull the target object free or remove one thing from the target object's surface.

***At Higher Levels.*** When you cast this spell using a spell slot of 1st level or higher, the cube's size increases by 1 foot for each slot level above 0.
#### [Evanesco](#spell-list)
<span id="spell-descr-Evanesco"></span>
*The Vanishing Spell - 3rd-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 30 ft
- **Duration:** Instantaneous
___
One non-magical object or magical construct of your choice that you can see within range and that fits within a 1-foot cube is vanished. Vanished objects have been described as being transfigured to go "into non-being, which is to say, everything." Vanishing is often seen as the magical inverse of conjuration.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the cube's size increases by 1 foot for each slot level above 3rd.
#### [Exhilaro](#spell-list)
<span id="spell-descr-Exhilaro"></span>
*The Cheering Charm - 1st-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Concentration, up to 1 minute
___
A creature of your choice that you can see within range becomes quite cheerful. For the next 10 minutes, the target creature has advantage on any saving throw against becoming frightened.

If concentration is maintained for one whole round, the creature perceives everything as hilariously funny and falls into fits of laughter if this spell affects it. The target must succeed on a Wisdom saving throw or fall prone, becoming incapacitated and unable to stand up for the duration. A creature with an Intelligence score of 5 or less isn’t affected.

At the end of each of its turns, and each time it takes damage, the target can make another Wisdom saving throw. The target has advantage on the saving throw if it’s triggered by damage. On a success, the spell ends.
#### [Expecto Patronum](#spell-list)
<span id="spell-descr-Expecto-Patronum"></span>
*The Patronus Charm - 3rd-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 10 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** Defensive
___
A Patronus Charm is a special bit of magic that requires a wizard to envision one of their happiest memories while casting the spell. The feeling of happiness must be genuine or strong enough to produce a radiant, ethereal beast, the embodiment of that wizard's positive emotions that serves as their protector.

When you cast this spell, you can choose to conjure an incorporeal or corporeal patronus. If you attempt to cast this spell while frightened or within 60 feet of a dementor, you must make an ability check using your spellcasting ability. The DC equals 10 + the number of dementors within 60 feet of you. A roll of 19-20 on the die automatically succeeds.

On a success, you cast the spell. On a failure, you can only conjure an incorporeal patronus, but if you fail the check by 5 or more, the spell fails entirely.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum

At the end of your turn, if you are frightened or there are one or more dementors within 60 feet of you while concentrating on this spell, you must repeat the ability check. On a failure, your patronus vanishes and the spell ends.

<div style="margin-top:20px;"></div>

> ##### Highly Advanced Magic
> The Patronus Charm is regarded as a difficult spell partly because the caster must relive a truly joyful memory when casting. This spell's ability check is unusual, but represents the challenge of focusing on suitable memory in a stressful situation. 
>
> Remember that a frightened creature has disadvantage on ability checks, including this one. Your HM can allow you to spend Inspiration to automatically succeed on this check. Your character might bring forth a powerful childhood memory in their time of need.

<div style="margin-top:20px;"></div>

A patronus sheds light in a radius around it. You and friendly creatures can't be frightened while in your patronus's light. A dementor that starts its turn within this light or enters the light for the first time on a turn must succeed on a Wisdom saving throw or become frightened of the patronus until the start of its next turn (this fear ignores any immunity to the frightened condition). While frightened, the dementor must take the Dash action on its turn and move away from the patronus by the safest available route until it leaves the light.

**Incorporeal Patronus.** Your patronus takes the form of a 5-foot burst of glowing mist in an unoccupied space adjacent to you. The patronus doesn't fill its space. It sheds bright light in its space and dim light in a 5-foot radius. On subsequent turns, you can move the patronus to another space adjacent to you as a bonus action. Additionally, you can move it as a reaction to a dementor moving within 10 feet of you.

**Corporeal Patronus.** Your patronus takes the form of a wispy silver animal in an unoccupied space that you can see within range. The patronus doesn't fill its space. It has no hit points and is immune to all damage, but can be targeted by another spell that affects magic, such as *finite incantatem*. The patronus sheds bright light in a 10-foot radius and dim light for an additional 10 feet.

<div style="margin-top:20px;"></div>

> ##### More than Dementors
> The Patronus Charm is most famous against dementors, but it can be a potent protector against other dark creatures in the Wizarding World.
>
> Only dementors and lethifolds have been confirmed to be affected by a patronus. At the HM's discretion, your patronus can interact with or harm creatures like banshees, inferi, or obscuri. If your HM decides a creature can be affected by a patronus, the creature is susceptible to the patronus's fear effect, attacks and damage.
> 
> Even if a patronus is unable to harm a particular kind of creature, its soothing presence can still protect you by preventing fear.

When you cast the spell and as a bonus action on subsequent turns, you can move the patronus. The distance you can move it depends on the size of the patronus. A Medium or smaller patronus can move 60 feet, a Large patronus can move 45 feet, and a Huge patronus can move 30 feet. A patronus ignores objects and terrain. In addition, the Patronus can enter a creature's space and stop there.

At any time during the patronus's movement, you can direct the patronus to charge into a dementor within 5 feet of it. Make a melee spell attack for the patronus using your spell attack modifier. On a hit, the target takes 5d10 radiant damage and the patronus pushes the target up to 5 feet plus a number of feet equal to five times your spellcasting ability modifier. The patronus moves with the target to remain within 5 feet of it and does not use any movement to do so.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d10 and the radius of the dim light increases by 5 feet for each slot level above 3rd.
#### [Expelliarmus](#spell-list)
<span id="spell-descr-Expelliarmus"></span>
*The Disarming Charm - 2nd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
___
Famous for being the spell that finally defeated Voldemort in the Second Wizarding War, this spell can harmlessly end duels by disarming a wizard of his wand. Make a ranged spell attack against a being within range. On a hit, you disarm the target, forcing it to drop one item of your choice that it's holding. The object lands 10 feet away from it in a random direction.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, you can choose the direction the object travels and the object's distance increases by 10 feet for each slot level above 2nd.
#### [Expulso](#spell-list)
<span id="spell-descr-Expulso"></span>
*The Concussive Curse - 3rd-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Instantaneous
___
The spell shoots out from your wand and a wave of thunderous force sweeps out from a point of your choice within range. Each creature in a 10-foot-radius sphere centered on that point must make a Constitution saving throw. On a failed save, a creature takes 4d8 thunder damage and is pushed 10 feet away from that point. On a successful save, the creature takes half as much damage and isn’t pushed. In addition, unsecured objects that are completely within the area of effect are automatically pushed 10 feet away from that point by the spell’s effect, and the spell emits a thunderous boom audible out to 100 feet.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the damage increases by 1d8 for each slot level above 3rd.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Ferula](#spell-list)
<span id="spell-descr-Ferula"></span>
*The Bandaging Charm - 1st-level Healing*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** 10 minutes
___
Bandages and splints are conjured on a being you can see within range, with no more than half of its hit point maximum, and it gains hit points equal to two times your spellcasting ability modifier. Additionally, any Wisdom (Medicine) checks to stabilize that target within the duration are made at advantage, and if the target is successfully stabilized, it regains 1 hit point.
#### [Fianto Duri](#spell-list)
<span id="spell-descr-Fianto-Duri"></span>
*The Reinforcing Charm - 3rd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Instantaneous
- **Tags:** Defensive
___
Whenever you cast this spell on an active defensive spell within range that improves a creature’s AC or grants it temporary hit points, each creature affected by the targeted spell gains temporary hit points equal to twice your caster level + your spellcasting ability modifier. When the targeted spell ends or an affected creature is no longer affected by it, the creature loses any remaining temporary hit points from this spell.

If you are maintaining concentration or dedication on a defensive spell, this spell can uniquely be cast on that active defensive spell without ending that spell or breaking your concentration or dedication.
#### [Fidelius Mysteria Celare](#spell-list)
<span id="spell-descr-Fidelius-Mysteria-Celare"></span>
*The Fidelius Charm - 9th-level Charm*
___
- **Casting Time:** 1 hour
- **Range:** Self (150-foot-radius hemisphere)
- **Duration:** Until dispelled
___
When cast upon a single dwelling that fits within range, it becomes a secret, infallibly invisible and inaccessible by anyone else. This effect reaches to the dwelling's property lines, or if no property lines are defined, the edge of the hemisphere centered on the caster at the time of casting.

You choose yourself or one person within the area of the spell to be the Secret-Keeper. If the Secret-Keeper tells someone the secret (the location of the dwelling) verbally or in writing, that person can see the secret like the Secret-Keeper and step onto the property. It's impossible for anyone other than the Secret-Keeper to share the secret. If the Secret-Keeper dies, everyone who knows the secret becomes Secret-Keepers and can share the secret with others.

Three dimensional space is warped around the secret, as if the space occupied by the secret never existed. If a person walks directly towards the secret, they will magically appear on the other side. Nothing will remain that indicates or gives clues to the existence of the secret. If anyone knew the location of the secret before the spell is cast, they forget the exact address but remember the general area where the secret is located.

This spell is completely undetectable and the area can't be targeted by divination spells. The spell's effects will only end if you dispel it or all Secret-Keepers have died.
#### [Finestra](#spell-list)
<span id="spell-descr-Finestra"></span>
*The Glass-Shattering Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 10 feet
- **Duration:** Instantaneous
___
A pane of glass you can see within range turns to powder, discreetly turning it into an open entryway.
#### [Finite Incantatem](#spell-list)
<span id="spell-descr-Finite-Incantatem"></span>
*The General Counter-spell - 2nd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Instantaneous
- **Tags:** Defensive
___
Choose any creature, object, or magical effect within range. One non-Transfiguration spell of 2nd level or lower on the target ends. If you are aware of at least one spell affecting the target, you can specify that spell in your mind. If you are unaware of what spells are affecting the target, one randomly selected spell ends. For a spell of a higher level on the target, make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a successful check, the spell ends.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, you automatically end the effects of a non-Transfiguration spell on the target if the spell's level is equal to or less than the level of the spell slot you used.
#### [Flagrate](#spell-list)
<span id="spell-descr-Flagrate"></span>
*The Lettering Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Until dispelled
___
You trace your wand in the air or over an object, leaving fiery marks in that position. You may write any letters or depict any shapes, as if you were writing with a quill. Although the glowing letters appear to be made of fire, it is just an illusion and it cannot burn anything.
#### [Flipendo](#spell-list)
<span id="spell-descr-Flipendo"></span>
*The Knockback Jinx - 1st-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
___
The spell feels like a very heavy blow, sharply throwing a creature from its standing position to the ground. Choose a being you can see within range to make a Strength saving throw. On a failed save, a creature takes 1d10 bludgeoning damage, is knocked back a number of feet equal to five times your spellcasting ability modifier, and is knocked prone. On a successful save, the creature takes half as much damage, is knocked back 5 feet, and isn’t knocked prone.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d10 and the knockback on a failed save increases by 5 feet for each slot level above 1st.
#### [Fortissimum](#spell-list)
<span id="spell-descr-Fortissimum"></span>
*The Unbreakable Charm - 3rd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Until dispelled
___
One object of your choice that you can see within range and that fits within a 1-foot cube is made completely invulnerable to physical destruction. This renders it immune to any damage, magical or mundane, but it can still be affected by spells that directly change the object, such as *vera verto* or *evanesco*.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the cube's size increases by 1 foot for each slot level above 3rd.
#### [Fumos](#spell-list)
<span id="spell-descr-Fumos"></span>
*The Smokescreen Spell - 2nd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** Self (15 foot cube)
- **Duration:** Concentration, up to 1 minute
___
A thick spray of smoke billows out from your wand, filling a 15-foot cube originating from you. This smoke spreads around corners. It lasts for the duration or until strong wind disperses the smoke, ending the spell. Its area is heavily obscured.

When a creature enters the spell's area for the first time on a turn or starts its turn there, that creature must make a Constitution saving throw. The creature takes 3d6 poison damage on a failed save, or half as much damage on a successful one. Constructs and undead are immune to this damage.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 2d6 and the area increases by 5 feet for each slot level above 2nd.
#### [Furnunculus](#spell-list)
<span id="spell-descr-Furnunculus"></span>
*The Pimple Jinx - Curse cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
___
Outbreaks of this jinx is a common occurrence when students get in fights, resulting in grotesque pimples covering the victims face. Make a ranged spell attack against a being within range. On a hit, it takes 1d4 psychic damage and has disadvantage on the next attack roll it makes before the end of its next turn. Additionally, it has disadvantage on the next Charisma ability check it makes.

This spell’s damage increases by 1d4 when you reach 5th level (2d4), 11th level (3d4), and 17th level (4d4).

\columnbreak
#### [Geminio](#spell-list)
<span id="spell-descr-Geminio"></span>
*The Doubling Charm - 2nd-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** 10 days
___
You tap an object that fits within a 1-foot cube with your wand and a perfect duplicate of it pops out from the object. The duplicate is indistinguishable from the object by normal means, but does not share any of its magical qualities or functions. The duplicate has one quarter of the original object's hit points and vanishes at the end of the spell's duration.

To detect the duplicate's inauthenticity, a creature within 5 feet of it can use an action to make an Intelligence (Investigation) check against your spell save DC. On a success, it perceives subtle flaws and understands it to be a fake. 5 days after casting this spell, the duplicate begins to show significant signs of degradation, granting advantage on the Investigation check. If *specialis revelio* is cast on the duplicate, the caster is made aware that the object is a duplicate created by this spell.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, the cube's size increases by 1 foot for each slot level above 2nd.
#### [Genu Recurvatum](#spell-list)
<span id="spell-descr-Genu-Recurvatum"></span>
*The Knee-Reversal Hex - Curse cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 minute
___
This hex flips around a beast or being's knees, forcing them to take awkward, uncoordinated steps. Make a ranged spell attack against a creature within range. On a hit, the target's speed is halved for the duration of the spell.
#### [Glacius](#spell-list)
<span id="spell-descr-Glacius"></span>
*The Water-Freezing Charm - 1st-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 hour
___
You freeze an area of water that you can see within range and that fits within a 5-foot cube. The area becomes difficult terrain for the duration. Each Medium or smaller creature that is covered, submerged or partially submerged in the affected water has its speed halved and must make a Constitution saving throw. On a failed save, a creature takes 3d8 cold damage, or half as much damage on a successful one.

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 1d8 and the cube's size increases by 5 feet for each slot level above 1st. If a creature of any size fits within the larger cube, it can be affected by this spell.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Glisseo](#spell-list)
<span id="spell-descr-Glisseo"></span>
*The Stairs-to-Slide Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Concentration, up to 1 minute
___
Famously used to protect the Hogwarts girls' dormitories from intruders, this spell changes the angle of all connected steps in a single flight of stairs within range. They angle downwards, turning into an abnormally slick ramp.
#### [Herbivicus](#spell-list)
<span id="spell-descr-Herbivicus"></span>
*The Gardening Charm - 3rd-level Charm*
___
- **Casting Time:** 1 action or 1 minute
- **Range:** 90 feet
- **Duration:** 1 hour or Instantaneous
___
This spell channels vitality into plants within a specific area. There are two possible uses for the spell, granting either immediate or long-term benefits.
- If you cast this spell using 1 action, choose a point within range. All non-magical plants in a 60-foot radius centered on that point become thick and overgrown for 1 hour, turning the area into difficult terrain. These plants can't be used in potions, due to being magically manipulated.
- If you cast this spell over 1 minute, you accelerate the growth of a single young plant you can see within range, magical or mundane. The plant instantly reaches maturity, but does not exceed a healthy "adult" size.
#### [Homenum Revelio](#spell-list)
<span id="spell-descr-Homenum-Revelio"></span>
*The Human-Presence-Revealing Spell - 4th-level Divination*
___
- **Casting Time:** 1 action
- **Range:** Self (60 foot sphere)
- **Duration:** Instantaneous
___
You sense the presence and general direction of each human or magical being within range. If any being is moving, you know its direction. If the being is transfigured into a beast or object, this spell won’t sense that being.

A being is alerted to being detected by this spell, as the spell produces an odd feeling of something standing right behind you or over you.
#### [Ignis Furore](#spell-list)
<span id="spell-descr-Ignis-Furore"></span>
*The Firestorm Spell - 6th-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** Dark
___
You create a ringed wall of fire within range up to 20 feet in diameter, 20 feet high, and 10 feet thick choosing whether it's touching the ground or in the air. The wall is opaque and lasts for the duration.

When the wall appears, each creature within its area must make a Dexterity saving throw. On a failed save, a creature takes 4d8 fire damage, or half as much damage on a successful save. A creature takes the same damage when it enters the wall for the first time on a turn or ends its turn there.

As an action, you can send a tendril of flames lashing out at any point within 60 feet of the center of the ring. Each creature within 5 feet of that point must make a Dexterity saving throw. A creature takes 4d8 fire damage on a failed save, or half as much damage on a successful one. A creature in the area of the wall and fiery burst is affected only once. 

The spell damages objects in the area and ignites flammable objects that aren’t being worn or carried.

***At Higher Levels.*** When you cast this spell using a spell slot of 7th level or higher, the damage increases by 1d8 and the ring's radius increases by 5 feet for each slot level above 6th.
#### [Ignis Laqueis](#spell-list)
<span id="spell-descr-Ignis-Laqueis"></span>
*The Fire Whip Spell - 3rd-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Dedication, up to 1 minute
- **Tags:** School of Magic - *Transfiguration*
___
You create a long, snaking whip of fire from the tip of your wand, lashing out and coiling around a creature in range. Make a melee spell attack against the target. On a hit, the creature takes 4d10 fire damage and is grappled for the duration. As an action, the target can make a Strength or Dexterity saving throw to end the spell's effects. 

On each of your following turns spent maintaining dedication, the whip tightens and you deal 4d10 fire damage to the target automatically. If the creature is Large or smaller, you can use a bonus action to pull the creature up to 10 feet closer to you.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the initial damage and subsequent turn damage increases by 1d10 for each slot level above 3rd.
#### [Illegibilus](#spell-list)
<span id="spell-descr-Illegibilus"></span>
*The Word-Scrambling Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 10 feet
- **Duration:** 1 hour
___
For the duration, no one can understand any written language that the spell is cast upon. The pieces of all the letters are separated and scrambled, rendering it impossible to try to decode.
#### [Immobulus](#spell-list)
<span id="spell-descr-Immobulus"></span>
*The Freezing Charm - 2nd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** Self (15 foot cube)
- **Duration:** 1 round
___
You send a pulse through the area in front of you, freezing everything in space and time. Roll 7d10; the total is how many hit points of creatures this spell can affect. All creatures and objects in a 15-foot cube originating from you are affected in the order of nearest to farthest. Each creature affected by this spell is paralyzed until the spell ends. While paralyzed, the creature is fixed in the space they occupied when the spell was cast, which may leave it suspended in air.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum

Subtract each creature's current hit points from the total before moving on to another creature. A creature's hit points must be equal to or less than the remaining total for that creature to be affected. Any object that is wholly within the area is automatically affect by this spell for the duration and does not count against the number of hit points you can affect. If casting the spell only affects objects and does not affect any creatures, the duration is up to 8 hours.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, roll an additional 2d10 for each slot level above 2nd. When you cast this spell using a spell slot of 4th level or higher, the duration increases by 1 round for each two slot levels above 2nd.
#### [Impedimenta](#spell-list)
<span id="spell-descr-Impedimenta"></span>
*The Impediment Jinx - 3rd-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 minute
___
A powerful dueling spell, this jinx alters time around one creature you can see within range, severely inhibiting its ability in combat. The target must succeed on a Wisdom saving throw or be affected by this spell for the duration.

An affected target's speed is halved, it takes a -2 penalty to AC and Dexterity saving throws, and it can't use reactions. On its turn, it can use either an action or a bonus action, not both. Regardless of the creature's abilities or magic items, it can't make more than one melee or ranged attack during its turn.

If the creature attempts to cast a spell with a casting time of 1 action, roll a d20. On an 11 or higher, the spell doesn't take effect until the creature's next turn, and the creature must use its action on that turn to complete the spell. If it can't, the spell is wasted.

A creature affected by this spell makes another Wisdom saving throw at the end of its turn. On a successful save, the effect ends for it.
#### [Imperio](#spell-list)
<span id="spell-descr-Imperio"></span>
*The Imperius Curse - 5th-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 10 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** Dark - *Unforgivable Curse*
___
When this Unforgivable Curse is cast, an incredibly wonderful, floating feeling comes over the victim, granting them a feeling of "untraceable happiness" and peace. In this state, the person's will is completely overridden by the caster and they will follow any command. A being of your choice within range must succeed on a Charisma saving throw at disadvantage or be charmed by you for the duration.

While the target is charmed, you have a telepathic link with it. You can use this telepathic link to issue commands to the creature while you are conscious (no action required), which it does its best to obey. You can specify a simple and general course of action, such as “Attack that creature,” “Run over there,” or “Fetch that object.” If the creature completes the order and doesn’t receive further direction from you, it defends and preserves itself to the best of its ability.

You can use your action to take total and precise control of the target. Until the end of your next turn, the creature takes only the actions you choose, and doesn’t do anything that you don’t allow it to do. During this time you can also cause the creature to use a reaction, but this requires you to use your own reaction as well.

Each time the target takes damage, it makes a new Charisma saving throw at disadvantage against the spell. If the saving throw succeeds, the spell ends.

***At Higher Levels.*** When you cast this spell using a higher level spell slot, the duration is concentration, up to 10 minutes (6th level), up to 1 hour (7th level), up to 8 hours (8th level), or until dispelled with no concentration (9th level).
#### [Impervius](#spell-list)
<span id="spell-descr-Impervius"></span>
*The Waterproofing Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** 1 hour
___
For the duration, a target object that you can see within range is waterproof and completely protected from any gas. It's as if any liquid or gas runs into a magnetic field around the object by which it is repelled, but the spell has no effect against solids impacting the target object.
#### [Inanimatus Conjurus](#spell-list)
<span id="spell-descr-Inanimatus-Conjurus"></span>
*Conjuration Incantation - 1st-level Transfiguration (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 10 feet
- **Duration:** 1 hour
___
You conjure up an inanimate object in your hand or in an unoccupied space within range that you can see. This object can be no larger than 2 feet on a side and weigh no more than 10 pounds, and its form must be that of a nonmagical object that you have seen.

The object disappears at the end of the spell's duration or if it takes any damage.

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, you may select or stack one of the following effects for each slot level above 1st.
* Increase the side length by 2 feet.
* Increase the weight limit by 10 pounds.
#### [Incarcerous](#spell-list)
<span id="spell-descr-Incarcerous"></span>
*The Binding Spell - 2nd-level Transfiguration (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** 24 hours
___
Black cords and ropes are conjured and wrap themselves forcefully around a target you can see within range. If the target is an unwilling creature, it must make a Strength saving throw. On a failed save, the creature is restrained for the duration. Upon casting, you can choose to anchor the ropes to the ground, preventing the target from being moved by external forces.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum

The restrained creature or someone else who can reach it can use an action to make a Strength check against your spell save DC. On a success, the restrained effect ends.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the creature is also incapacitated, rendering it unable make a Strength check to escape.
#### [Incendio](#spell-list)
<span id="spell-descr-Incendio"></span>
*The Fire-Making Spell - 1st-level Transfiguration (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** Dark
___
You create a bonfire on ground that you can see within range. Until the spell ends, the bonfire fills a 5-foot cube. Any creature in the bonfire’s space when you cast the spell must succeed on a Dexterity saving throw. It takes 3d6 fire damage on a failed save, or half as much damage on a successful one. A creature must also make the saving throw when it moves into the bonfire’s space for the first time on a turn or ends its turn there.

The bonfire ignites flammable objects in its area that aren’t being worn or carried. If there is adequate fuel for the bonfire to burn, it will continue burning after the spell ends.

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, the damage increases by 2d6 for each slot level above 2nd.
#### [Incendio Glacia](#spell-list)
<span id="spell-descr-Incendio-Glacia"></span>
*The Bluebell Flames Spell - Transfiguration cantrip*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** 1 hour
___
A flickering blue flame flows out from the tip of your wand, condensing on an object, in a container, or in your hand. The flame remains there for the duration and only emanates heat directly upwards. It doesn't harm anything beneath or around it, and seems to hover slightly above whatever it's resting upon. If placed beneath a flammable object, a natural fire may be started from the heat.

The flame sheds bright light in a 10-foot radius and dim light for an additional 10 feet. The spell ends if you dismiss it as a bonus action.
#### [Infirma Cerebra](#spell-list)
<span id="spell-descr-Infirma-Cerebra"></span>
*The Jelly-Brain Jinx - Curse cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 round
___
This jinxes a target's mind, giving them a brief moment of disorientation. Make a ranged spell attack against a creature within range. On a hit, the target takes 1d6 psychic damage, and the first time it makes a saving throw before the end of your next turn, it must roll a d4 and subtract the number rolled from the save.

This spell’s damage increases by 1d6 when you reach certain levels: 5th level (2d6), 11th level (3d6), and 17th level (4d6).

\columnbreak
#### [Intus Sunt](#spell-list)
<span id="spell-descr-Intus-Sunt"></span>
*The Entrail-Expelling Curse - 3rd-level Healing (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** School of Magic - *Healing*
___
Invented by Urquhart Rackharrow, this medieval remedy causes the recipient to purge and experience great abdominal pain. Choose one being that you can see within range to make a Constitution saving throw. If it fails, the target's exhaustion is set to 2 levels for the duration. At the end of each of its turns, the target can make a Constitution saving throw, without disadvantage from exhaustion. On a success, the spell ends. If the target has higher levels of exhaustion than the spell's effect, the spell does not change its levels of exhaustion. If the target gains any levels of exhaustion within the duration of this spell, it stacks with this spell's effect.

Additionally, if the target is suffering any condition or negative effects from something it ingested, such as drinking a poison, this spell ends those effects.

***At Higher Levels.*** If you cast this spell using a spell slot of 6th level or higher, the target's exhaustion is set to 3 levels (6th level), 4 levels (7th level), or 5 levels (8th level).
#### [Langlock](#spell-list)
<span id="spell-descr-Langlock"></span>
*The Gagging Jinx - 3rd-level Curse*
___
- **Casting Time:** 1 action or reaction, which you take when you see a creature within 60 feet of you casting a spell
- **Range:** 60 feet
- **Duration:** 1 round
- **Tags:** School of Magic - *Jinxes, Hexes, and Curses*
___
You attempt to interrupt a being you can see in the process of casting a spell. If the creature is verbally casting a spell of 3rd level or lower, its spell fails and has no effect. If it is verbally casting a spell of 4th level or higher, make an ability check using your spellcasting ability. The DC equals 10 + the spell’s level. On a success, the creature’s spell fails and has no effect. 

On a success or if the being was casting the spell non-verbally, the target must cast all other spells non-verbally until the end of its next turn. If it tries to cast a spell verbally, it must first succeed on an Intelligence saving throw, or the casting fails and the spell is wasted.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the interrupted spell has no effect if its level is less than or equal to the level of the spell slot you used.
#### [Lapifors](#spell-list)
<span id="spell-descr-Lapifors"></span>
*The Babbitty Rabbitty Spell - 4th-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Concentration, up to 1 hour
- **Tags:** School of Magic - *Transfiguration*
___
This spell transforms a creature with at least 1 hit point that you can see within range into the form of a rabbit. An unwilling creature must make a Wisdom saving throw to avoid the effect.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum

The transformation lasts for the duration, or until the target drops to 0 hit points or dies. The target's game statistics, including mental ability scores, are replaced by the statistics of a rabbit. It retains its alignment and personality. The HM has the creature's statistics.

The target assumes the hit points of its new form. When it reverts to its normal form, the creature returns to the number of hit points it had before it transformed. If it reverts as a result of dropping to 0 hit points, any excess damage carries over to its normal form. As long as the excess damage doesn't reduce the creature's normal form to 0 hit points, it isn't knocked unconscious.

The creature is limited in the actions it can perform by the nature of its new form, and it can't speak, cast spells, or take any other action that requires hands or speech.

The target's gear melds into the new form. The creature can't activate, use, wield, or otherwise benefit from any of its equipment.
<!--___
> ## Rabbit
>*Tiny beast*
> ___
> - **Armor Class** 11
> - **Hit Points** 1
> - **Speed** 35 ft., Burrow 5 ft
>___
>|STR|DEX|CON|INT|WIS|CHA|
>|:---:|:---:|:---:|:---:|:---:|:---:|
>|1 (-5)|13 (+1)|7 (-2)|2 (-4)|10 (+0)|3 (-4)|
>___
> - **Saving Throws** Dexterity
> - **Skills** Perception +2
> - **Senses** Passive perception 12
> ___
>
> ### Actions
> ***Bite.*** *Melee Weapon Attack:* +3 to hit, reach 5 ft., one target. *Hit:* 1 piercing damage.-->
#### [Legilimens](#spell-list)
<span id="spell-descr-Legilimens"></span>
*The Legilimency Spell - 3rd-level Divination*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** School of Magic - *Divination*
___
With legilimency, a being's eyes become windows to their mind, showing you a vision of their thoughts. For the duration, you can read the thoughts of a being you can see within range, as soon as eye contact can be made. After the spell effects begin, eye contact does not need to be maintained.

You initially learn the surface thoughts of the being - what is most on its mind in that moment. As an action, you can attempt to probe deeper into its mind. If you probe deeper, the target must make a Wisdom saving throw. If it fails, you gain insight into its reasoning (if any), its emotional state, and something that looms large in its mind (such as something it worries over, loves, or hates). If it succeeds, the spell ends. You can probe deeper a second time, forcefully pulling memories from the being's mind if it fails the second Wisdom saving throw.

Questions verbally directed at the target naturally shape the course of its thoughts, so this spell is particularly effective as part of an interrogation. If you cast the spell verbally and the target can hear you, it knows you are probing into its mind and the creature can use its action on its turn to make an Intelligence check contested by your Intelligence check. If it succeeds, the spell ends.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the DC of the Wisdom saving throws increases by 1 for each slot level above 3rd.
#### [Levicorpus/Liberacorpus](#spell-list)
<span id="spell-descr-Levicorpus-Liberacorpus"></span>
*The Dangling Jinx - 4th-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** 1 minute
___
One of the few spells that are a non-verbal spell by design, this jinx yanks a being's feet out from under it and dangles it in the air, hanging by its ankle. This spell always is cast with the effects of the Subtle Spell metamagic, at no sorcery point cost and whether you have Subtle Spell or not.

A creature you can see within range must make a Wisdom saving throw or take 3d10 psychic damage and be restrained. Additionally, if the target tries to cast a spell, it must first succeed on a Wisdom saving throw, or the casting fails and the spell is wasted.
#### [Locomotor](#spell-list)
<span id="spell-descr-Locomotor"></span>
*The Locomotion Charm - 1st-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** 1 hour
___
One object that isn't being worn or carried of your choice that you can see within range rises 3 feet off the ground, and remains suspended there for the duration. The spell can levitate a target that weighs up to 500 pounds. If more weight than the limit is placed on top of the object, the spell ends, and it falls to the ground.

The object is immobile while you are within 20 feet of it. If you move more than 20 feet away from it, the object follows you so that it remains within 20 feet of you. It can move across uneven terrain, up or down stairs, slopes and the like, but it can't cross an elevation change of 10 feet or more. For example, the object can't move across a 10-foot-deep pit, nor could it leave such a pit if it was created at the bottom.

If you move more than 100 feet from the object (typically because it can't move around an obstacle to follow you), the spell ends.
#### [Locomotor Mortis](#spell-list)
<span id="spell-descr-Locomotor-Mortis"></span>
*The Leg-Locker Curse - 1st-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** 1 minute
___
A common tool among bullies, this "curse" binds a creature's legs as if they were tied together with rope. A creature you can see within range must succeed on a Wisdom saving throw or have its speed halved and suffer disadvantage on Dexterity saving throws. Additionally, each time it moves within the duration, it must succeed on a Dexterity saving throw without disadvantage from this spell, or be knocked prone and take 2d4 bludgeoning damage.
#### [Locomotor Wibbly](#spell-list)
<span id="spell-descr-Locomotor-Wibbly"></span>
*The Jelly-Legs Jinx - Curse cantrip*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
___
This will make a person's legs so unsteady and weak that they aren't able to keep their balance. Make a ranged spell attack against a being within range. On a hit, the target is knocked prone.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Lumos/Nox](#spell-list)
<span id="spell-descr-Lumos-Nox"></span>
*The Wand-Lighting Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** Self
- **Duration:** Until dispelled
___
Upon muttering the incantation, the tip of your wand sheds bright light in a narrow 15-foot cone and dim light for an additional 15 feet, much like a flashlight. The light is a bright white with a slight bluish tint. Completely covering the tip of your wand with something opaque blocks the light. The spell ends if you dismiss it with the *nox* incantation, as a bonus action.
#### [Lumos Maxima](#spell-list)
<span id="spell-descr-Lumos-Maxima"></span>
*The Daylight Charm - 3rd-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** 1 hour
___
A 60-foot-radius sphere of light spreads out from a small floating ball of light that hovers in place. The sphere is bright light and sheds dim light for an additional 60 feet. As a bonus action, you can direct the ball of light to a new position within range.
#### [Melofors](#spell-list)
<span id="spell-descr-Melofors"></span>
*The Pumpkin-Conjuring Spell - 3rd-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 minute
___
You conjure a pumpkin around a target's head, blinding and deafening it. Choose one creature that you can see within range to make a Wisdom saving throw. If it fails, the target is blinded and deafened for the duration. At the end of each of its turns, the target can make a Wisdom saving throw. On a success, the spell's effect ends for that target.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, you can target one additional creature for each slot level above 3rd.
#### [Mimblewimble](#spell-list)
<span id="spell-descr-Mimblewimble"></span>
*The Tongue-Tying Curse - 1st-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** 1 round
___
If you're hit with this spell, this produces the strange sensation of your tongue being rolled up into the back of your mouth. Choose one being you can see within range. If it tries to cast a spell verbally before the end of its next turn, it must first succeed on a Dexterity saving throw, or the casting fails and the spell is wasted.

\columnbreak
#### [Mobilicorpus](#spell-list)
<span id="spell-descr-Mobilicorpus"></span>
*The Carrying Charm - 1st-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** 1 hour
___
One willing, paralyzed, petrified, restrained, stunned or unconscious being of your choice that you can see within range rises 3 feet off the ground, and remains suspended there for the duration as if it were hoisted by invisible ropes under its arms. The spell can levitate a target that weighs up to 500 pounds. If more weight than the limit is placed on top of the being, the spell ends, and it falls to the ground.

The being is immobile while you are within 20 feet of it. If you move more than 20 feet away from it, the being follows you so that it remains within 20 feet of you. It can move across uneven terrain, up or down stairs, slopes and the like, but it can't cross an elevation change of 10 feet or more. For example, the being can't move across a 10-foot-deep pit, nor could it leave such a pit if it was created at the bottom.

If you move more than 100 feet from the being (typically because it can't move around an obstacle to follow you), the spell ends.
#### [Molliare](#spell-list)
<span id="spell-descr-Molliare"></span>
*The Cushioning Charm - Charm Cantrip*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** 1 hour
___
This comfortable charm is most commonly found on a broomstick. One object you touch with your wand is wrapped in an invisible cushioning effect for the duration, almost like two magnets repelling one another.
#### [Muco Volatilis](#spell-list)
<span id="spell-descr-Muco-Volatilis"></span>
*The Bat-Bogey Hex - 4th-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Concentration, up to 1 minute
___
This terrifying spell transforms the victim's bogies (or boogers) into nasty green bats that crawl out of their nose and attack. Make a ranged spell attack against a being within range. On a hit, the target and any hostile creatures within 5 feet of the target take 6d4 slashing damage. At the start of the target's turn and when any hostile creature starts its turn within 5 feet of the target, it takes 3d4 slashing damage. If any creature has to make a saving throw to maintain concentration because of this spell's damage, the saving throw is made at disadvantage.

***At Higher Levels.*** When you cast this spell using a spell slot of 5th level or higher, the initial damage increases by 2d4 for each slot level above 4th.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Muffliato](#spell-list)
<span id="spell-descr-Muffliato"></span>
*The Anti-Eavesdropping Charm - 2nd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** Self
- **Duration:** Concentration, up to 1 hour
- **Tags:** School of Magic - *Charms*
___
For the duration, each creature you choose within 30 feet of you (including you) are able to converse with each other without anyone or anything else hearing. Instead of the voices, nearby creatures hear a faint buzzing, like white noise. If a creature is within 15 feet of you and sees your mouth move when you speak, it is aware that your voice is being magically masked.
#### [Ne Ustio](#spell-list)
<span id="spell-descr-Ne-Ustio"></span>
*The Flame-Freezing Charm - 5th-level Charm*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Concentration, up to 1 hour
- **Tags:** Defensive
___
For the duration, the creature you touch or yourself has immunity to fire damage, excluding dragon fire and the *azreth* spell (Fiendfyre).

***At Higher Levels.*** When you cast this spell using a spell slot of 6th level or higher, the duration is doubled for each slot level above 5th. When you use a spell slot of 8th level or higher, concentration is no longer required and its effect applies to dragon fire.
#### [Nebulus](#spell-list)
<span id="spell-descr-Nebulus"></span>
*The Fog Spell - 1st-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 120 feet
- **Duration:** Concentration, up to 1 hour
___
You create a 20-foot-radius sphere of fog centered on a point within range. The sphere spreads around corners, and its area is heavily obscured. It lasts for the duration or until a wind of moderate or greater speed (at least 10 miles per hour) disperses it.

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, the radius of the fog increases by 20 feet for each slot level above 1st.
#### [Novum Spirare](#spell-list)
<span id="spell-descr-Novum-Spirare"></span>
*The Bubble-Head Charm - 3rd-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** 24 hours
___
Accurately named, the bubble-head charm forms a large bubble-like mask over a creature's mouth, nose, and ears that is magically filled with never-ending fresh air. This spell grants one willing creature you can see within range the ability to breathe underwater or in a vacuum until the spell ends. Additionally, the creature is immune to poison damage due to inhalation for the duration. The creature can dispel this effect using an action.

\columnbreak
#### [Nullum Effugium](#spell-list)
<span id="spell-descr-Nullum-Effugium"></span>
*The Anti-Disapparition Jinx - 5th-level Curse*
___
- **Casting Time:** 10 minutes
- **Range:** Self (60-foot-radius sphere)
- **Duration:** 8 hours
- **Tags:** Defensive, School of Magic - *Jinxes, Hexes, and Curses*
___
Commonly used by the Department of Magical Law enforcement, this wards an area against apparition or disapparition. No one may arrive in the warded area via *apparition*, nor may any creatures within the warded area cast the spell. Any attempt to do so results in the typical *apparition* effect, except the creature stays exactly where they are.

***At Higher Levels.*** When you cast this spell using a spell slot of 6th level or higher, the radius of the sphere increases by 60 feet for each slot level above 5th.
#### [Obliviate](#spell-list)
<span id="spell-descr-Obliviate"></span>
*The Memory Charm - 5th-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** School of Magic - *Charms*
___
You attempt to reshape another being's memories. One being you can see within range must make a Wisdom saving throw. If you are fighting the creature, it has advantage on the saving throw. On a failed save, the target becomes charmed by you for the duration. The charmed target is incapacitated and unaware of its surroundings, though it can still hear you. If it takes any damage or is targeted by another spell, this spell ends, and none of the target's memories are modified.

You can eliminate the target's memory of an event or detail (or any individual aspect of that event or detail) that it experienced or perceived within the last 24 hours and that lasted no more than 10 minutes.

You must mentally describe or visualize how the memories are affected. The being's mind fills in any gaps in the details of your description. If the spell ends before you have finished describing or visualizing the modified memories, the target’s memory isn’t altered. Otherwise, the modified memories take hold when the spell ends.

A modified memory doesn't necessarily affect how a being behaves, particularly if the memory contradicts the creature's natural inclinations, alignment, or beliefs. An illogical modified memory, such as erasing all memory of how they were transported to and from a location, is dismissed by the target, perhaps as a bad dream. The HM might deem a modified memory too nonsensical to affect a being in a significant manner.

A *vulnera sanentur* or *obliviate* spell cast on the target restores the creature's true memory.

***At Higher Levels.*** If you cast this spell using a spell slot of 6th level or higher, you can eliminate the target's memories of an event that took place up to 7 days ago (6th level), 30 days ago (7th level), 1 year ago (8th level), or any time in the creature's past (9th level). Alternatively, you can eliminate a detail or topic in all memories across those same time frames.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Obscuro](#spell-list)
<span id="spell-descr-Obscuro"></span>
*The Blindfold Spell - 1st-level Transfiguration (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Until dispelled
___
You can conjure a black blindfold that magically wraps itself around a foe's head. Choose one creature that you can see within range to make a Dexterity saving throw. If it fails, the target is blinded for the duration. The creature can remove the blindfold as an action.
#### [Omnifracto](#spell-list)
<span id="spell-descr-Omnifracto"></span>
*The Shield Penetrating Spell - 5th-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Instantaneous
- **Tags:** School of Magic - *Jinxes, Hexes, and Curses*
___
A piercing beam of light shoots out from the tip of your wand, shattering any defensive magic it passes through. Choose a target within range. *Protego totalum*, *repello inimicum*, and all defensive spells that are improving that creature’s AC or granting it temporary hit points are dispelled.
#### [Oppugno](#spell-list)
<span id="spell-descr-Oppugno"></span>
*The Swarming Jinx - 2nd-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Concentration, up to 1 minute
___
You cast this jinx on a group of tiny objects or a group of birds within range. The targets start swarming in the air in a 5-foot-diameter sphere in an unoccupied space of your choice. Any creature that starts its turn within 5 feet of the swarm or enters the swarm’s area for the first time on a turn must make a Dexterity saving throw. The creature takes 4d4 slashing damage on a failed save, or half as much damage on a successful one. 

As a bonus action, you can move the sphere up to 30 feet. While the swarm shares the same space with a creature, that creature has disadvantage on attack rolls. The swarm's space counts as difficult terrain.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d4 for each slot level above 2nd.
#### [Orbis](#spell-list)
<span id="spell-descr-Orbis"></span>
*The Rooting Spell - 2nd-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** School of Magic - *Transfiguration*
___
You choose a space on the ground that is currently occupied by a Large or smaller creature you can see within range. The ground becomes a thick liquid and swirls out from under the creature in an orb-like shape. The material then slams back down and regains its solidity in an attempt to partially bury the creature. The target must make a Dexterity saving throw. On a failed save, the target takes 3d6 bludgeoning damage and is restrained for the spell’s duration.

As an action, you can cause the earth to crush the restrained target, who must make a Strength saving throw. It takes 3d6 bludgeoning damage on a failed save, or half as much damage on a successful one.

To break out, the restrained target can use its action to make a Strength check against your spell save DC. On a success, the target pulls its legs free and is no longer restrained.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d6 for each slot level above 2nd.
#### [Orchideous](#spell-list)
<span id="spell-descr-Orchideous"></span>
*The Flower-Conjuring Spell - Transfiguration Cantrip*
___
- **Casting Time:** 1 action
- **Range:** 10 feet
- **Duration:** Instantaneous
___
You conjure a blooming flower, bouquet, or wreath in the desired location within range.
#### [Partis Temporus](#spell-list)
<span id="spell-descr-Partis-Temporus"></span>
*The Barrier-Opening Charm - 2nd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Instantaneous
- **Tags:** Defensive
___
This unique charm redirects magical effects to create an opening. On any area spell of 3rd level or lower that forms a line, wall, or perimeter, an opening appears in the spell's effect at a point of your choice that you can see within range and lasts for the duration. You choose the opening’s dimensions: up to 5 feet wide and 8 feet tall. For a spell of 4th level or higher on the target, make an ability check using your spellcasting ability. The DC equals 10 + the spell’s level. On a successful check, the opening is created. The opening can be dispelled at will.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, you automatically create an opening in the spell if the spell's level is one level higher than, equal to or less than the level of the spell slot you used.
#### [Pellucidi Pellis](#spell-list)
<span id="spell-descr-Pellucidi-Pellis"></span>
*The Disillusionment Charm - 2nd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Concentration, up to 1 hour
___
With a tap of a wand on the top of the head and a sensation of raw egg being broken where the wand was tapped, a creature becomes invisible until the spell ends. Anything the target is wearing or carrying is invisible as long as it is on the target’s person. The spell ends for a target that attacks or casts a spell.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd. The targets must be within 5 feet of each other when you target them.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Pereo](#spell-list)
<span id="spell-descr-Pereo"></span>
*The Extinguishing Charm - Charm Cantrip*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Instantaneous
___
You choose a flame that you can see within range and that fits within a 5-foot cube. You instantaneously extinguish the flames within the cube.
#### [Perfusorius](#spell-list)
<span id="spell-descr-Perfusorius"></span>
*The Feather-Light Charm - 1st-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** 1 hour
___
This spell alters an object of up to 500 pounds, changing its weight to be just barely heavier than the atmosphere around it. The slightest force is needed to move, pick up, or carry this object for the duration. It can be easily thrown as well.
#### [Periculum/Verdimillious](#spell-list)
<span id="spell-descr-Periculum-Verdimillious"></span>
*The Flare Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** Self
- **Duration:** Instantaneous
___
This spell sends red (periculum) or green (verdimillious) sparks shooting from the casters wand for signaling purposes. It may also appear as a flare, traveling a desired distance before exploding in light and hovering in the air.
#### [Petrificus Totalus](#spell-list)
<span id="spell-descr-Petrificus-Totalus"></span>
*The Full Body-Bind Curse - 1st-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Dedication, up to 1 minute
___
This spell makes a being's arms and legs snap together, and it will fall down, stiff as a board. Make a ranged spell attack against a being within range. On a hit, the target is knocked prone and paralyzed for the duration.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, you can target a beast instead of a being.
#### [Piertotum Locomotor](#spell-list)
<span id="spell-descr-Piertotum-Locomotor"></span>
*The Animating Charm - 5th-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** School of Magic - *Charms*
___
Objects come to life at your command. Choose up to five nonmagical objects within range that are not being worn or carried. Medium targets count as one object, Large targets count as two objects, Huge targets count as four objects. You can't animate any object larger than Huge. Each target animates and becomes a creature under your control until the spell ends or until reduced to 0 hit points.

As a bonus action, you can mentally command any creature you made with this spell if the creature is within 500 feet of you (if you control multiple creatures, you can command any or all of them at the same time, issuing the same command to each one). You decide what action the creature will take and where it will move during its next turn, or you can issue a general command, such as to guard a particular chamber or corridor. If you issue no commands, the creature only defends itself against hostile creatures. Once given an order, the creature continues to follow it until its task is complete.
##### Animated Object Statistics
| Size   | HP | AC | Attack                     | Str | Dex |
|:-------|:--:|:--:|:---------------------------|:---:|:---:|
| Medium | 40 | 13 | +5 to hit, 2d6 + 1 damage  | 10  | 12  |
| Large  | 50 | 10 | +6 to hit, 2d10 + 2 damage | 14  | 10  |
| Huge   | 80 | 10 | +8 to hit, 2d12 + 4 damage | 18  | 6   |

An animated object is a construct with AC, hit points, attacks, Strength, and Dexterity determine by its size. Its Constitution is 10 and its Intelligence and Wisdom are 3, and its Charisma is 1. Its speed is 30 feet, if the Objects lack legs or other appendages it can use for locomotion, it instead has a flying speed of 30 feet and can hover. If the object is securely attached to a surface or larger object, such as a chain bolted to a wall, its speed is 0. It has blindsight with a radius of 30 feet and is blind beyond that distance. When the animated object drops to 0 hit points, it is destroyed.

If you command an object to attack, it can make a single melee attack against a creature within 5 feet of it. It makes a slam attack with an attack bonus and bludgeoning damage determine by its size. The HM might rule that a specific object inflicts slashing or piercing damage based on its form.

***At Higher Levels.*** If you cast this spell using a spell slot of 6th level or higher, you can animate one additional object for each slot level above 5th.
#### [Point Me](#spell-list)
<span id="spell-descr-Point-Me"></span>
*The Four-Point Spell - Divination cantrip*
___
- **Casting Time:** 1 action
- **Range:** Self
- **Duration:** Instantaneous
___
Placing your wand flat in your open palm, this spell picks up the wand and points north, much like a compass. The spell's usefulness is situational, but often grants advantage on Wisdom (Survival) checks to not get lost outdoors.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Prior Incantato](#spell-list)
<span id="spell-descr-Prior-Incantato"></span>
*The Reverse Spell - Divination cantrip*
___
- **Casting Time:** 1 action
- **Range:** Self
- **Duration:** Instantaneous
___
Often used as an investigative tool in wizarding crimes, this spell produces a ghostly recreation of the previous spell cast by the currently used wand. If the previously cast spell cannot be represented visually, you learn the incantation that was used, regardless of whether the incantation was spoken aloud at the time of casting. This spell can be cast a total of three consecutive times on a single wand, revealing the three most recently cast spells.
#### [Protego](#spell-list)
<span id="spell-descr-Protego"></span>
*The Shield Charm - 1st-level Charm*
___
- **Casting Time:** 1 action or reaction, which you take when you are hit by an attack
- **Range:** Self
- **Duration:** Dedication, up to 10 minutes
- **Tags:** Defensive
___
An invisible barrier of magical force appears in front of you and protects you. For the duration, you have a +5 bonus to AC, including against the triggering attack. If you are targeted by a spell that requires an attack roll and the spell's level is equal to or lower than half your proficiency bonus, the spell has no effect on you.

You can use a bonus action to change which direction the shield is facing. If you are attacked from either of your sides or from behind while casting this spell, you must use your reaction to redirect the shield to point towards the threat. Otherwise, this spell doesn't protect you.
#### [Protego Maxima](#spell-list)
<span id="spell-descr-Protego-Maxima"></span>
*The Orb Shield Charm - 2nd-level Charm*
___
- **Casting Time:** 1 action or reaction, which you take when you are hit by an attack
- **Range:** Self
- **Duration:** Dedication, up to 10 minutes
- **Tags:** Defensive
___
You cast a fully encompassing *protego* around yourself, sacrificing durability for coverage. For the duration, you have a +3 bonus to AC, including against the triggering attack. If you are subjected to an effect that allows you to make a Strength or Dexterity saving throw to take only half damage, you instead take no damage if you succeed on the saving throw and only half damage if you fail. 
#### [Protego Totalum](#spell-list)
<span id="spell-descr-Protego-Totalum"></span>
*The Area Shield Charm - 6th-level Charm*
___
- **Casting Time:** 1 action
- **Range:** Self (10-foot-radius sphere)
- **Duration:** Concentration, up to 1 minute
- **Tags:** Defensive, School of Magic - *Healing*
___
An immobile, faintly shimmering barrier springs into existence in a 10-foot radius around you and remains for the duration. 

Any attack or spell of 5th level or lower cast from outside the barrier can’t affect creatures or objects within it, even if the spell is cast using a higher level spell slot. Such a spell can target creatures and objects within the barrier, but the spell has no effect on them. Similarly, the area within the barrier is excluded from the areas affected by such spells.

***At Higher Levels.*** When you cast this spell using a spell slot of 7th level or higher, the barrier blocks spells of one level higher for each slot level above 6th.
#### [Reducio](#spell-list)
<span id="spell-descr-Reducio"></span>
*The Shrinking Charm - 1st-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** 1 hour
___
You cause an object that isn't being worn or carried and that you can see within range to shrink in size for the duration. The target’s size is halved in all dimensions, and its weight is reduced to one-eighth of normal. This reduction decreases its size by one category – from Medium to Small, for example.
#### [Reducto](#spell-list)
<span id="spell-descr-Reducto"></span>
*The Reductor Curse - 4th-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Instantaneous
___
This spell disintegrates a Large or smaller nonmagical object or transfigured/conjured construct you can see within range. If the target is a Huge or larger object or construct, this spell disintegrates a 10-foot-cube portion of it.
#### [Relashio](#spell-list)
<span id="spell-descr-Relashio"></span>
*The Revulsion Jinx - 2nd-Level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
___
This spell forces both living and inanimate targets to release their grip. Choose an object or creature that you can see within range. The object can be a set of manacles, a padlock, chains, or another object that is wrapped around or restraining something. If the target is a creature, it must make a Wisdom saving throw. On a failed save, it must let go of whatever it is restraining. This effect ends any grappled or restrained condition that is being imposed by the target.

An object that is secured by a mundane or magical lock or that is stuck becomes unlocked, unstuck, or unbarred. When you cast the spell on an object, a loud rattling or clanking, audible from as far away as 100 feet, emanates from the target object.

A creature is not forced to drop any object that it is holding. The creature must be restraining the object in some way, like holding onto an object that has had *accio* cast upon it.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Rennervate](#spell-list)
<span id="spell-descr-Rennervate"></span>
*The Reviving Spell - Healing cantrip*
___
- **Casting Time:** 1 action
- **Range:** 10 feet
- **Duration:** Instantaneous
___
The counterspell to *stupefy*, this incantation is invaluable in extended combat or team dueling. Magically induced unconsciousness is ended for a being of your choice you can see within range.
#### [Reparifarge](#spell-list)
<span id="spell-descr-Reparifarge"></span>
*The Untransfiguration Incantation - 2nd-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** Instantaneous
- **Tags:** Defensive, School of Magic - *Transfiguration*
___
Choose any creature, object, or magical effect within range. One Transfiguration spell of 2nd level or lower on the target ends. If you are aware of at least one spell affecting the target, you can specify that spell in your mind. If you are unaware of what spells are affecting the target, one randomly selected spell ends. For a spell of a higher level on the target, make an ability check using your spellcasting ability. The DC equals 10 + the spell's level. On a successful check, the spell ends.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, you automatically end the effects of a Transfiguration spell on the target if the spell's level is equal to or less than the level of the spell slot you used.
#### [Reparifors](#spell-list)
<span id="spell-descr-Reparifors"></span>
*The Curing Spell - 1st-level Healing*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Instantaneous
___
With a tap of your wand, a being that you can see within range regains 1d8 hit points. You can also end either one disease or one condition afflicting it. The condition can be blinded, deafened, paralyzed, or poisoned.

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, the healing increases by 1d8 for each slot level above 1st.
#### [Reparo](#spell-list)
<span id="spell-descr-Reparo"></span>
*The Mending Charm - 2nd-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Instantaneous
___
This spell magically reverses any damage done to any objects or structures within a 5-foot cube, collecting all the pieces or components and reassembling them. Anything previously contained by the broken target, like a spilled liquid, is not placed back inside it. Anything affected by the breaking of the target, like a person who fell through a broken platform, is not undone. There is no effect on anything within the area that's undamaged, nor on anything damaged by time or decay.

\columnbreak

This spell can physically repair a magic item, but the spell can’t restore magic to such an object.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, the cube's size increases by 10 feet for each slot level above 2nd.
#### [Repello Inimicum](#spell-list)
<span id="spell-descr-Repello-Inimicum"></span>
*The Evil Protection Charm - 3rd-level Charm*
___
- **Casting Time:** 1 minute
- **Range:** Self (20-foot-radius hemisphere)
- **Duration:** 1 hour
- **Tags:** Defensive
___
You create a 20-foot-radius hemisphere of magical energy to protect you from one or more of the following: Dark wizards, other Dark beings, or Dark beasts. The circle affects creatures of the chosen type(s) in the following ways.
* The affected creatures can't willingly enter the hemisphere by nonmagical means. If the creature tries to use *apparition* to do so, it must first succeed on a Charisma saving throw.
* The affected creatures have disadvantage on attack rolls against targets within the hemisphere.
* Targets within the hemisphere can't be charmed or frightened by affected creatures.

***At Higher Levels.*** When you cast this spell using a spell slot of 4th level or higher, the duration increases by 1 hour for each slot level above 3rd.
#### [Repello Muggletum](#spell-list)
<span id="spell-descr-Repello-Muggletum"></span>
*The Muggle-Repelling Charm - 4th-level Charm (ritual)*
___
- **Casting Time:** 10 minutes
- **Range:** Self (60-foot-radius hemisphere)
- **Duration:** 8 hours
- **Tags:** Defensive
___
Frequently used around wizarding areas, this charm keeps Muggles away from dangerous situations or overtly magical locations. You enchant an area to suggest a course of activity and magically influence a non-magical human. Upon entering the warded area, the subject must make a Wisdom saving throw at disadvantage. On a failed save, it pursues a course of action that takes it away from the area of the spell.

The subject's mind naturally thinks of the best reason to convince itself that it must depart, or barring an actual reason, invents an arbitrary emergency that demands its attention elsewhere. The spell's effect ends when the subject has either attended to the matter they thought of or when the subject has decided to take another course of action that does not involve entering the area of the spell.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Revelio](#spell-list)
<span id="spell-descr-Revelio"></span>
*The Revealing Charm - 3rd-level Divination*
___
- **Casting Time:** 1 action
- **Range:** 10 feet
- **Duration:** Instantaneous
___
With a twist of your wand, the true appearance of a creature or object is revealed. A disguised, hidden, invisible or otherwise magically concealed target is made visible, dispelling any spell producing such effects and magically removing physical alterations. Your wand must be pointing at the target for this spell to take effect.
#### [Rictusempra](#spell-list)
<span id="spell-descr-Rictusempra"></span>
*The Tickling Charm - 1st-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 round
___
This low-level dueling spell gives the recipient an intense tickling sensation. Make a ranged spell attack against a being within range. On a hit, the target will double over in laughter and become incapacitated with its speed halved until the start of your next turn.
#### [Riddikulus](#spell-list)
<span id="spell-descr-Riddikulus"></span>
*The Boggart-Banishing Spell - 1st-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Instantaneous
___
This spell has a very specific application: forcing a boggart to transform into a comedic version of its current form. Only a boggart may be targeted by this spell.
#### [Sagittario](#spell-list)
<span id="spell-descr-Sagittario"></span>
*The Arrow-Shooting Spell - 1st-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 150 feet
- **Duration:** Instantaneous
- **Tags:** Dark
___
A conjured arrow streaks toward a designated target. Make a ranged spell attack against a target within range. On a hit, the target takes piercing damage equal to 1d8 + your spellcasting ability modifier.

***At Higher Levels.*** When you cast this spell using a spell slot of 2nd level or higher, you conjure one additional arrow for each slot level above 1st. You can direct the arrows at the same target or at different ones. Make a separate attack roll for each arrow.
#### [Salvio Hexia](#spell-list)
<span id="spell-descr-Salvio-Hexia"></span>
*The Curse-Blocking Charm - 5th-level Charm*
___
- **Casting Time:** 1 action
- **Range:** Self (10-foot-radius sphere)
- **Duration:** Concentration, up to 1 minute
- **Tags:** Defensive
___
Each creature within the spell's area gains temporary hit points equal to your spellcasting modifier at the beginning of its turn and advantage on all saving throws against spells.
#### [Scourgify](#spell-list)
<span id="spell-descr-Scourgify"></span>
*The Scouring Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 10 feet
- **Duration:** Instantaneous
___
An object no larger than 5 cubic feet is flawlessly cleaned.
#### [Sectumsempra](#spell-list)
<span id="spell-descr-Sectumsempra"></span>
*The Lacerating Curse - 4th-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Instantaneous
- **Tags:** Dark, School of Magic - *Jinxes, Hexes, and Curses*
___
Make a ranged spell attack against a target within range. On a hit, the target must make a Constitution saving throw. On a failed save, a creature takes 10d6 slashing damage and another 5d6 slashing damage at the end of its next turn. On a successful save, a creature takes half the initial damage and half the damage at the end of its next turn.

***At Higher Levels.*** When you cast this spell using a spell slot of 5th level or higher, the initial damage increases by 2d6 for each slot level above 4th.
#### [Serpensortia](#spell-list)
<span id="spell-descr-Serpensortia"></span>
*The Snake Summons Spell - 2nd-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Instantaneous
- **Tags:** Dark
___
You conjure a venomous snake from thin air. A pit viper appears in an unoccupied space that you can see within range. Roll initiative for the summoned creature, which has its own turns. Although the pit viper won't willingly attack the caster, you cannot control the actions or targets of the pit viper. It is possible for the pit viper to be turned against you through magical means.

***At Higher Levels.*** When you cast this spell using a higher level spell slot, multiple pit vipers are conjured in unoccupied spaces that you can see within range. Choose from the following options: two pit vipers (4th level), three pit vipers (6th level), or four pit vipers (8th level). Initiative is rolled as a group.
#### [Silencio](#spell-list)
<span id="spell-descr-Silencio"></span>
*The Silencing Charm - 2nd-level Charm (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 90 feet
- **Duration:** 1 minute
___
This charm is extremely effective against wizards unpracticed in non-verbal magic. Choose one target that you can see within range. If it's a creature, it must make a Wisdom saving throw. If it fails or if it's an object, all sound created by the target is made completely silent. Casting a spell that includes a verbal component is impossible while under the effect of this spell.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
#### [Slugulus Eructo](#spell-list)
<span id="spell-descr-Slugulus-Eructo"></span>
*The Slug-Vomiting Hex - 2nd-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 1 round
___
This particularly nasty hex causes one to spit up slugs for the duration. Make a ranged spell attack against a creature within range. On a hit, it takes 3d8 psychic damage and gains one level of exhaustion. This spell cannot cause it to reach more than 5 levels of exhaustion. If it tries to cast a spell verbally before the end of its next turn, it must first succeed on a Constitution saving throw, or the casting fails and the spell is wasted.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, the damage increases by 1d8 for each slot level above 2nd.
#### [Sonorus/Quietus](#spell-list)
<span id="spell-descr-Sonorus-Quietus"></span>
*The Amplifying Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** Self
- **Duration:** Until dispelled
___
When you hold the tip of your wand to your neck and cast this spell, your voice booms up to three times as loud as normal. Your voice is loud enough to fill a large stadium, but won't cause any hearing damage. Casting *quietus* with your wand to your throat is the counter-charm and ends the effect.
#### [Specialis Revelio](#spell-list)
<span id="spell-descr-Specialis-Revelio"></span>
*The Spell Revealing Spell - 1st-level Divination*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Instantaneous
___
You tap your wand on an object or area, revealing magical influences. If it is a magic item or some other magic-imbued object, you learn its properties and how to use them, whether it requires attunement to use, and how many charges it has, if any. You learn whether any spells are affecting the item and what they are. If the item was created by a spell, you learn which spell created it. 

If cast on an area, you learn what spells, if any, are currently active within a 5-foot cube in front of you. The border of each spell's effect is illuminated within that cube, much like blowing dust through laser beams.
#### [Spongify](#spell-list)
<span id="spell-descr-Spongify"></span>
*The Softening Charm - Charm cantrip*
___
- **Casting Time:** 1 action or reaction, which you take when a collision occurs within 30 feet
- **Range:** 30 feet
- **Duration:** 1 minute
___
This spell makes an object you can see within range become soft and bouncy, like a sponge or mattress. Any damage from falling on or colliding with this object is nullified. This spell can be cast as a reaction to a collision affecting a creature or two objects you can see within range.

\columnbreak
#### [Stupefy](#spell-list)
<span id="spell-descr-Stupefy"></span>
*The Stunning Spell - 2nd-level Charm*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** 10 minutes
___
This charm is the most common dueling spell in the wizarding world, harmlessly ending a duel between two wizards. Make a ranged spell attack against a being within range. On a hit, the target falls unconscious for the duration, or until they are revived with *rennervate*.

***At Higher Levels.*** If you cast this spell using a spell slot of 3rd level or higher, the duration increases to 1 hour (3rd level) or 8 hours (4th level). Alternatively, when you cast this spell using a spell slot of 4th level or higher, you can target a beast instead of a being, for a duration of 10 minutes (4th level), 1 hour (5th level) or 8 hours (6th level).
#### [Tarantallegra](#spell-list)
<span id="spell-descr-Tarantallegra"></span>
*The Dancing Feet Jinx - 2nd-level Curse*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Concentration, up to 1 minute
___
This entertaining jinx forces its victim to do a comic dance in place: shuffling, tapping its feet, and capering. Make a ranged spell attack against a target within range. On a hit, a dancing creature must use all its movement to dance without leaving its space until the end of your next turn. While the creature is affected by this spell, it has disadvantage on Dexterity saving throws and attack rolls and other creatures have advantage on attack rolls against it. As an action, a dancing creature can make a Wisdom saving throw to regain control of itself. On a successful save, the spell ends.
#### [Tergeo](#spell-list)
<span id="spell-descr-Tergeo"></span>
*The Siphoning Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Concentration, up to 1 minute
___
You choose an specific liquid that you can see within range and that fits within a 5-foot cube. The liquid gathers up into a blob floating at the tip of your wand, and you can direct it to form into simple shapes, animate, or flow into a container.
#### [Transmogrify](#spell-list)
<span id="spell-descr-Transmogrify"></span>
*The Transmogrifian Torture - 5th-level Transfiguration*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Concentration, up to 1 minute
- **Tags:** Dark
___
A dark purpose for transfiguration, this tortuous spell slowly rearranges and dissolves a creature's internal organs. A creature you can see within range must make a Constitution saving throw. On a failed save, it takes 2d12 acid damage at the start of each of its turns and is subject to crippling pain. On a successful save, the spell has no effect.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum

While the target is affected by crippling pain, any speed it has can be no higher than 10 feet. The target also has disadvantage on attack rolls and ability checks. Finally, if the target tries to cast a spell, it must first succeed on a Constitution saving throw, or the casting fails and the spell is wasted.

A target suffering from this spell can make a Constitution saving throw at the end of each of its turns. On a successful save, the spell ends.

***At Higher Levels.*** When you cast this spell using a spell slot of 6th level or higher, the damage increases by 1d12 for each slot level above 5th.
#### [Ventus](#spell-list)
<span id="spell-descr-Ventus"></span>
*The Cyclone Jinx - 2nd-level Curse (ritual)*
___
- **Casting Time:** 1 action
- **Range:** 60 feet
- **Duration:** Concentration, up to 1 minute
___
A strong gust of air flows out from the tip of your wand, and creates one of the following effects at a point you can see within range:

* One Medium or smaller creature that you choose must succeed on a Strength saving throw or be instantaneously pushed up to 5 feet away from you and be rendered unable to move closer to you for the duration.
* You create a small blast of air capable of moving one object that is neither held nor carried and that weighs no more than 5 pounds. The object is pushed up to 10 feet away from you per round, for the duration of the spell. It isn’t pushed with enough force to cause damage.
* You create a harmless sensory effect using air, such as causing leaves to rustle, wind to slam shutters shut, or your clothing to ripple in a breeze. If desired, the air can be hot and function like a blow dryer.

***At Higher Levels.*** When you cast this spell using a spell slot of 3rd level or higher, you can target one additional creature for each slot level above 2nd. The creatures must be within 30 feet of each other when you target them.
#### [Vera Verto](#spell-list)
<span id="spell-descr-Vera-Verto"></span>
*The General Transfiguration Incantation - Transfiguration cantrip*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Until dispelled
___
This universal incantation is taught to Hogwarts students in their first Transfiguration class. You transfigure one nonmagical object that you can see within range and that fits within a 1-foot cube into another nonmagical object of similar size and mass and of equal or lesser value.

***At Higher Levels.*** When you cast this spell using a spell slot of 1st level or higher, you may select or stack one of the following effects for each slot level above 0.
* Increase the cube size by 2 feet.
* Target a living Beast (if unwilling, it must succeed on a Wisdom saving throw to avoid the effect).
* Transfigure into a construct (Duration: Concentration, up to 1 minute).

\columnbreak
#### [Vigilatus](#spell-list)
<span id="spell-descr-Vigilatus"></span>
*The Intruder Charm - 1st-level Charm (ritual)*
___
- **Casting Time:** 1 minute
- **Range:** 30 feet
- **Duration:** 8 hours
- **Tags:** Defensive
___
You set a mental alarm against unwanted intrusion. Choose a door, a window, or an area within range that is no larger than a 20-foot cube. Until the spell ends, a ping in your mind alerts you whenever a Tiny or larger creature touches or enters the warded area, if you are within 1 mile of the warded area. This ping awakens you if you are sleeping. 

When you cast the spell, you can designate creatures that won't set off the alarm.
#### [Vulnera Sanentur](#spell-list)
<span id="spell-descr-Vulnera-Sanentur"></span>
*The Regenerating Spell - 6th-level Healing*
___
- **Casting Time:** 1 action
- **Range:** Touch
- **Duration:** Concentration, up to 1 minute
- **Tags:** School of Magic - *Healing*
___
Tracing your wand over a being's wounds, you weave a complex counter-curse that undoes the damage dealt to a being. The target regains four times your spellcasting ability modifier + 4d8 hit points instantaneously, and then 4d4 hit points for every following turn for the duration of the spell.

If the target has lost body members (fingers, legs, and so on) and the severed part is held to its place throughout the entire duration of the spell, the spell causes the limb to heal back on after 1 minute of casting.

***At Higher Levels.*** When you cast this spell using a spell slot of 7th level or higher, the instantaneous healing increases by 1d8 and the subsequent healing increases by 3d4 for each slot level above 6th.

#### [Wingardium Leviosa](#spell-list)
<span id="spell-descr-Wingardium-Leviosa"></span>
*The Levitation Charm - Charm cantrip*
___
- **Casting Time:** 1 action
- **Range:** 30 feet
- **Duration:** Dedication, up to 1 minute
___
One creature other than yourself or object of your choice that you can see within range rises vertically, up to 20 feet, and remains suspended there for the duration. The spell can levitate a target that weighs up to 100 pounds. An unwilling creature that succeeds on a Constitution saving throw is unaffected.

The target can move only by pushing or pulling against a fixed object or surface within reach (such as a wall or a ceiling), which allows it to move as if it were climbing. You can change the target’s altitude by up to 20 feet in either direction on your turn. Otherwise, you can use your action to move the target, which must remain within the spell’s range.

If the spell is ended voluntarily, the target floats gently to the ground if it is still aloft. If ended involuntarily, the target immediately drops.

***At Higher Levels.*** When you cast this spell using a spell slot of 1st level or higher, the weight limit is increased by 150 pounds for each slot level above 0.
<div class='footnote'>Part 2 | Spells</div>

\pagebreakNum
# Appendix A: Potion Brewing
Potions are an essential part of wizarding life, especially in the halls of St. Mungo's Hospital for Magical Maladies and Injuries. Although Potions is a core class for young witches and wizards during their years at Hogwarts, it's not everyone's cup of tea. Brewing your own potions is not required. It's an optional pursuit                         for the wizards who are so inclined.
## Brewing Requirements
Potion brewing does not require any dice rolls and therefore does not require HM supervision. If the requirements are fulfilled, a PC can brew a potion in the background while other players are playing or while the player is away from the table. After a potion is brewed, the HM will confirm the proper recipe was used and assess the ingredient quality. Aside from the few potions with time restrictions, all you need to instantly brew a potion is:
* Access to a properly equipped potions laboratory
* A potioneer's kit in your possession
* Knowledge of the potion's recipe
* The ingredients specified in the recipe

A potions laboratory must be equipped with a cauldron, stirring rods, a source of heat, and a source of water. All Hogwarts students have access to the Potions classroom, but extracurricular use may require permission from the Potions Master. This is the only potions laboratory available to the average Hogwarts student, but adult wizards may be able to equip their own private laboratory or set up a more portable arrangement for their travels. 

A potioneer's kit is included in the Hogwarts shopping list, so every student should have one. It includes a set of brass scales, silver knife, cutting board, mortar and pestle, measuring cups, eye dropper and vials, jars and flasks, as well as some staple ingredients that aren't included in recipes. This will last a typical student's time at Hogwarts, but the avid amateur may require replacements or upgrades.

<div style="text-align:right; margin: 10px 0 -20px 0px; font-style: italic; color:#ECE6D0; text-shadow:1px 1px 2px #000, -1px 1px 2px #000, 1px -1px 2px #000, -1px -1px 2px #000, 1px 0px 2px #000, -1px 0px 2px #000, 0px -1px 2px #000, 0px 1px 2px #000 !important;">
© Pottermore Limited
</div>

<img src='https://www.gmbinder.com/images/4o1kmVz.png' style='margin: 90px 0px -300px 70px;'>

<img src='https://www.gmbinder.com/images/lNksJXW.png' style='width:180px; margin: 0px 20px -200px -300px; position:absolute; transform:rotate(-8deg);'>

<img src='https://www.gmbinder.com/images/yxRypcp.png' style='width:230px; margin: 40px 0px 0px -180px; position:absolute;'>

<img src='https://www.gmbinder.com/images/eOUC1Gd.png' style='width:130px; margin: 90px 20px -200px -320px; position:absolute;transform:scaleX(1);'>

<img src='https://www.gmbinder.com/images/25RdIK7.png' style='width:130px; margin: 110px 20px -200px -260px; position:absolute;'>

<img src='https://www.gmbinder.com/images/a68Pa4J.png' style='width:190px; margin: 165px 20px -200px -320px; position:absolute; transform:rotate(-35deg);'>


\columnbreak
## Learning Recipes
Approximately half of all recipes are learned in the standard Hogwarts curriculum. At the beginning of every school year, the new Potions textbook includes five potion recipes. If a student wants to learn additional recipes, they must search the Hogwarts library in their spare time, seek more advanced potioneers to tutor them and go on adventures to prove themselves worthy of ancient knowledge.

Alternatively, if a brewed potion is acquired, an aspiring potioneer can attempt to deconstruct that potion. This requires a potions laboratory, a potioneer's kit, casting *specialis revelio* and a Wisdom (Potion-Making) ability check. The potion is destroyed by this process, but if the check is successful, the potioneer learns the potion's recipe.

## Obtaining Ingredients
In a dim clearing of the Forbidden Forest, the private supplies of a trusted ally or the dusty shelves of an apothecary, you're going to find many magical and mundane essences that can be used as potion ingredients. Because of the magical applications of these potions and the danger in harvesting, potion ingredients are extremely valuable.

Different tools will be required to harvest different kinds of ingredients. As a general rule, plant-based ingredients will require the use of herbologist's tools, while harvesting ingredients from animals and magical beasts will use the potioneer's kit. Your own skill with these tools will determine the quality of the obtained ingredient. Doing a rough job at harvesting will produce Poor ingredients, while skilled work will produce Superior ingredients.

## Potion Effectiveness
A potion's effectiveness is dependent on the brewer's technical skill and the preparation of the ingredients. Proficiency in Wisdom (Potion-Making) and proficiency with the potioneer's kit are not necessary, but those proficiencies will improve the effectiveness of your potions. Skill can often help a brewer overcome the limitations of Poor ingredients, but truly Exceptional potions require Superior ingredients.

<div class='classTable' style='margin:35px 0px 60px;'>
<span style="text-align:center">

##### Potion-Making + Potioneer's Kit </br>Proficiencies and Potion Quality </span>
| Proficiency| Poor Ingredients | Normal Ingredients| Superior Ingredients |
|:----------:|:----------------:|:-----------------:|:--------------------:|
| None      | Flawed            | Flawed            | Normal            |
| One       | Flawed            | Normal            | Normal            |
| Both      | Normal            | Normal            | Exceptional       |
</div>

<div class='footnote'>Appendix A | Potion Brewing</div>

\pagebreakNum

<div class='wide' style='margin: -34px -10px 550px 0; text-align:right; font-style: italic; color:#ECE6D0; text-shadow:2px 2px 2px #000, -2px 2px 2px #000, 2px -2px 2px #000, -2px -2px 2px #000, 2px 0px 2px #000, -2px 0px 2px #000, 0px -2px 2px #000, 0px 2px 2px #000 !important;'>© Pottermore Limited</div><img src='https://www.gmbinder.com/images/dqekcCX.jpg' class='cover-image' style="width:150%; left:-250px; height:75%; top:-270px"><img src='https://www.gmbinder.com/images/dqekcCX.jpg' class='cover-image' style="width:150%; left:-250px"><img src='https://www.gmbinder.com/images/zdcYLtP.png' class='cover-image bgwatercolor' style="top:55px; height:80%; transform: scaleY(-1); filter:brightness(94%) sepia(15%)"><img src='https://www.gmbinder.com/images/WQXIOUB.png' class='cover-image bgwatercolor' style="transform: scaleX(-1); filter:brightness(94%) sepia(15%)">

## Recipe List 

<div class='spellList'>

These are the recipes included in each Hogwarts year's Potions class curriculum. Upon starting the school year or purchasing that year's Potions textbook, a character gains access to these recipes.
##### First Year Potions
- Antidote of Common Poisons
- Blemish Blitzer
- Confusing Concoction
- Forgetfulness Potion
- Herbicide Potion

\columnbreak
##### Second Year Potions
- Doxycide
- Dreamless Sleep Potion
- Elixir to Induce Euphoria
- Sleeping Draught
- Swelling Solution
##### Third Year Potions
- Antidote of Uncommon Poisons
- Baneberry Poison
- Girding Potion
- Shrinking Solution
- Wiggenweld Potion

\columnbreak
##### Fourth Year Potions
- Aging Potion
- Fire Protection Potion
- Garrotting Gas
- Pepperup Potion
- Wound-Cleaning Potion
##### Fifth Year Potions
- Befuddlement Draught
- Draught of Peace
- Murtlap Essence
- Noxious Potion
- Strengthening Solution

\columnbreak
##### Sixth Year Potions
- Draught of Living Death
- Erumpent Potion
- Memory Potion
- Polyjuice Potion
- Skele-Gro
##### Seventh Year Potions
- Essence of Insanity
- Invisibility Potion
- Mandrake Restorative Draught
- Weedosoros
- Wit-Sharpening Potion

</div>


<div class='footnote'>Appendix A | Potion Brewing</div>

\pagebreakNum

## Potion Recipes

### First Year Potions
#### Antidote of Common Poisons
* 1 bundle of galanthus nivalis
* 1 cluster of mistletoe berries
* 1 flask of honeywater
* 1 vial of billywig stings
#### Blemish Blitzer
* 1 bundle of nettles
* 1 flask of bubotuber pus
* 1 flask of flobberworm mucus
* 1 porcupine quill
#### Confusing Concoction
* 1 bundle of gurdyroots
* 2 bundles of lovage
* 1 flask of ethanol
#### Forgetfulness Potion
* 1 bundle of lovage
* 1 cluster of mistletoe berries
* 2 flasks of Lethe River water
#### Herbicide Potion
* 1 Flask of flobberworm mucus
* 1 powdered lionfish spine
* 1 powdered streeler shell
* 1 vial of doxy eggs

<!--doxy eggs https://drive.google.com/file/d/0B0TGf4bxO8wBWGhkNzF3RHVxNzQ/view?usp=sharing
flobberworm mucus https://drive.google.com/file/d/0B0TGf4bxO8wBckxIU2ozQWFxclk/view?usp=sharing
ethanol https://drive.google.com/file/d/0B0TGf4bxO8wBV2t4bWVGNkNKa00/view?usp=sharing
gurdyroot https://drive.google.com/file/d/0B0TGf4bxO8wBOXRmN1RaNDRVRDg/view?usp=sharing
honeywater https://drive.google.com/file/d/0B0TGf4bxO8wBT0ZwbGdIOEMzdWM/view?usp=sharing
lionfish spine https://drive.google.com/file/d/0B0TGf4bxO8wBcGYwLTBBeUxXWFU/view?usp=sharing
mistletoe berries https://drive.google.com/file/d/0B0TGf4bxO8wBa3o5VHRjS3FGSk0/view?usp=sharing
nettles https://drive.google.com/file/d/0B0TGf4bxO8wBdXNUZTA1NW1PMHM/view?usp=sharing
streeler shells https://drive.google.com/file/d/0B0TGf4bxO8wBU3hPRnpWSnp3R00/view?usp=sharing-->

### Second Year Potions
#### Doxycide
* 1 bundle of cowbane
* 1 bundle of hemlock
* 1 flask of bundimun secretion
* 1 powdered streeler shell
#### Dreamless Sleep Potion
* 1 bundle of poppy heads
* 1 cluster of baneberries
* 1 frog brain
* 1 powdered octopus
#### Elixir to Induce Euphoria
* 1 bundle of peppermint
* 1 bundle of shrivelfigs
* 1 flask of wormwood infusion
* 1 porcupine quill
#### Sleeping Draught
* 1 bundle of angel's trumpet
* 1 bundle of scurvy grass
* 1 flask of flobberworm mucus
#### Swelling Solution
* 1 bat spleen
* 1 bundle of nettles
* 1 flask of pufferfish eyes
* 1 vial of exploding ginger eyelashes

<!--bat spleen https://drive.google.com/file/d/0B0TGf4bxO8wBMXVWd3BGZ29QQk0/view?usp=sharing
cowbane https://drive.google.com/file/d/0B0TGf4bxO8wBZHV1RE81V2I4QzQ/view?usp=sharing
peppermint https://drive.google.com/file/d/0B0TGf4bxO8wBVDN5TjA4OENWSTA/view?usp=sharing
pufferfish eyes https://drive.google.com/file/d/0B0TGf4bxO8wBTmxTVVNfQTJxUDg/view?usp=sharing
shrivelfig https://drive.google.com/file/d/0B0TGf4bxO8wBRThwdDUycHVXZ3M/view?usp=sharing
wormwood infusion https://drive.google.com/file/d/0B0TGf4bxO8wBWVNLbmNsa01uekU/view?usp=sharing-->


\columnbreak

<div style='margin-top:40px;'></div>

### Third Year Potions
#### Antidote of Uncommon Poisons
* 1 flask of fire seeds
* 1 vial of billywig stings
* 1 vial of chizpurfle carapaces
#### Baneberry Poison
* 1 bundle of cowbane
* 1 bundle of shrivelfigs
* 2 clusters of baneberries
#### Girding Potion
* 1 set of fairy wings
* 1 powdered flying seahorse
* 1 vial of doxy eggs
#### Shrinking Solution
* 1 bundle of cowbane
* 1 bundle of shrivelfigs
* 1 flask of wormwood infusion
* 1 vial of woodlice extract
#### Wiggenweld Potion
* 1 bundle of wiggentree bark
* 1 flask of honeywater
* 1 powdered root of asphodel

<!--asphodel https://drive.google.com/file/d/0B0TGf4bxO8wBNEVpSGhtemhNbzg/view?usp=sharing
billywig stings https://drive.google.com/file/d/0B0TGf4bxO8wBTFlTZU53cFQ5Mk0/view?usp=sharing
woodlice https://drive.google.com/file/d/0B0TGf4bxO8wBVER2akJXSnRSQTQ/view?usp=sharing-->

<div style='margin-top:40px;'></div>

### Fourth Year Potions
#### Aging Potion
* 1 bursting mushroom
* 1 newt spleen
* 1 vial of chizpurfle carapaces
#### Fire Protection Potion
* 1 bursting mushroom
* 1 powdered wartcap
* 1 vial of salamander blood
#### Garrotting Gas
* 1 flask of bundimun secretion
* 1 flask of ethanol
* 1 powdered wartcap
* 1 vial of exploding ginger eyelashes
#### Pepperup Potion
* 1 cluster of boom berries
* 1 flask of ethanol
* 1 flask of vervain infusion
* 1 powdered octopus
#### Wound-Cleaning Potion
* 1 bundle of star grass
* 1 flask of vervain infusion
* 1 staghorn mushroom
* 1 vial of spirit of myrrh

<!--bundimun secretion https://drive.google.com/file/d/0B0TGf4bxO8wBNnR6ZzJ6QnFxeWc/view?usp=sharing
bursting mushroom https://drive.google.com/file/d/0B0TGf4bxO8wBRnNYTHdRMTR0UTg/view?usp=sharing
salamander blood https://drive.google.com/file/d/0B0TGf4bxO8wBV1BCdFFfelM3ZkE/view?usp=sharing
vervain https://drive.google.com/file/d/0B0TGf4bxO8wBazBPY2w4M1F1UzQ/view?usp=sharing-->

<div class='footnote'>Appendix A | Potion Brewing</div>

\pagebreakNum
### Fifth Year Potions
#### Befuddlement Draught
* 1 bundle of lovage
* 1 bundle of scurvy grass
* 1 bundle of sneezewort
#### Draught of Peace
* 1 porcupine quill
* 1 powdered moonstone
* 1 vial of syrup of hellebore
#### Murtlap Essence
* 2 murtlap tentacles
* 1 vial of spirit of myrrh
#### Noxious Potion
* 1 bundle of angel's trumpet
* 1 cluster of moonseed berries
* 1 vial of syrup of hellebore
#### Strengthening Solution
* 1 flask of re'em blood
* 1 vial of fanged geranium fangs
* 1 vial of salamander blood

<!--murtlap tentacle https://drive.google.com/file/d/0B0TGf4bxO8wBNWNDd3FhdjRoM3M/view?usp=sharing-->

<div style='margin-top:40px;'></div>

### Sixth Year Potions
#### Draught of Living Death
* 2 bundles of valerian roots
* 1 powdered root of asphodel
* 1 sloth brain
* 2 sopophorous beans
* 1 vial of African sea salt
#### Erumpent Potion
* 1 bundle of venomous tentacula leaves
* 1 flask of fire seeds
* 2 powdered erumpent horns
* 1 vial of exploding ginger eyelashes
#### Memory Potion
* 1 bundle of galanthus nivalis
* 1 bundle of sneezewort
* 1 jobberknoll feather
#### Polyjuice Potion
* 1 boomslang skin
* 1 bundle of full-moon fluxweed
* 2 bundles of knotgrass
* 1 flask of lacewing flies
* 1 powdered bicorn horn
* 1 sopophorous bean
#### Skele-Gro
* 1 chinese chomping cabbage
* 1 flask of pufferfish eyes
* 1 murtlap tentacle
* 1 powdered griffin claw
* 1 powdered scarab beetle

<!--beetle https://drive.google.com/file/d/0B0TGf4bxO8wBa1h1SlM4TXhEV0U/view?usp=sharing
bicorn horn https://drive.google.com/file/d/0B0TGf4bxO8wBcmJTaU1fQWZ0WWs/view?usp=sharing
fluxweed https://drive.google.com/file/d/0B0TGf4bxO8wBYnh6aVZEUFFyRDQ/view?usp=sharing
jobberknoll feather https://drive.google.com/file/d/0B0TGf4bxO8wBUmZrNC1ld2c2eDg/view?usp=sharing
knotgrass https://drive.google.com/file/d/0B0TGf4bxO8wBaEtIX2lmMlN5Uzg/view?usp=sharing-->

\columnbreak
### Seventh Year Potions
#### Essence of Insanity
* 1 bundle of weed-of-sorrows
* 1 clutch of runespoor eggs
* 1 giant purple toad wart
* 1 vial of belladonna essence
* 1 vial of syrup of arnica
#### Invisibility Potion
* 2 boomslang skins
* 1 unicorn hair
* 1 vial of African sea salt
* 1 vial of doxy eggs
#### Mandrake Restorative Draught
* 3 mandrake roots
* 1 vial of chizpurfle carapaces
* 1 vial of spirit of myrrh
#### Weedosoros
* 1 bundle of hemlock
* 1 bundle of valerian roots
* 1 bundle of weed-of-sorrows
* 1 vial of belladonna essence
* 1 vial of syrup of arnica
#### Wit-Sharpening Potion
* 1 clutch of runespoor eggs
* 1 newt spleen
* 1 powdered dragon claw
* 1 powdered scarab beetle
* 1 sloth brain

<!--unicorn hair https://drive.google.com/file/d/0B0TGf4bxO8wBLXI3S1F1UTYwaEE/view?usp=sharing-->

<div class='footnote'>Appendix A | Potion Brewing</div>

\pagebreakNum
# Appendix B: Patronus Rolling Tables
Your character's corporeal patronus can be determined several different ways. First, you can simply choose your patronus. Its form makes no significant mechanical impact on the *expecto patronum* spell. The second method is getting a random result by rolling on the d100 table below. 

The last method provides customized rolling tables with options based on your character's personality. Find your character's Background on the subsequent pages. Then, locate your House under that Background and use that rolling table to determine your corporeal patronus. If your character is not a Hogwarts student, choose a house based on your character's personality and values.

<div class='wide' style='column-count:3'>

|d100| Corporeal Patronus |
|:--:|:-------------------|
| 1  | Aardvark|
| 2  | Adder|
| 3  | Badger|
| 4  | Bat|
| 5  | Beagle|
| 6  | Black and White Cat|
| 7  | Black Bear|
| 8  | Black Mamba|
| 9  | Black Mare/Stallion|
| 10 | Bloodhound|
| 11 | Borzoi|
| 12 | Brown Bear|
| 13 | Brown Owl|
| 14 | Buffalo|
| 15 | Calico Cat|
| 16 | Capuchin Monkey|
| 17 | Cheetah|
| 18 | Chestnut Mare/Stallion|
| 19 | Chow Dog|
| 20 | Dapple Grey Mare/Stallion|
| 21 | Doe|
| 22 | Dolphin|
| 23 | Dragonfly|
| 24 | Eagle|
| 25 | Eagle Owl|
| 26 | Elephant|
| 27 | Falcon|
| 28 | Field Mouse|
| 29 | Fox|
| 30 | Ginger Cat|
| 31 | Goshawk|
| 32 | Grass Snake|
| 33 | Greyhound|

|   |  |
|:--:|:--------------|
| 34 | Hedgehog|
| 35 | Heron|
| 36 | Hummingbird|
| 37 | Husky|
| 38 | Hyena|
| 39 | Impala|
| 40 | Irish Wolfhound|
| 41 | King Cobra|
| 42 | Kingfisher|
| 43 | Leopard|
| 44 | Lion|
| 45 | Lynx|
| 46 | Magpie|
| 47 | Manx Cat|
| 48 | Marsh Harrier|
| 49 | Mastiff|
| 50 | Mole|
| 51 | Mountain Hare|
| 52 | Ocicat|
| 53 | Orangutan|
| 54 | Orca|
| 55 | Oryx|
| 56 | Osprey|
| 57 | Otter|
| 58 | Peacock|
| 59 | Pine Marten|
| 60 | Polar Bear|
| 61 | Polecat|
| 62 | Python|
| 63 | Ragdoll Cat|
| 64 | Rat|
| 65 | Rattlesnake|
| 66 | Raven|

|   |  |
|:--:|:--------------|
| 67 | Rhinoceros|
| 68 | Robin|
| 69 | Rottweiler|
| 70 | Salmon|
| 71 | Scops Owl|
| 72 | Seal|
| 73 | Shark|
| 74 | Siberian Cat|
| 75 | Snowy Owl|
| 76 | Sphynx Cat|
| 77 | Squirrel|
| 78 | St. Bernard|
| 79 | Stag|
| 80 | Swallow|
| 81 | Swan|
| 82 | Tiger|
| 83 | Tortoiseshell Cat|
| 84 | Vole|
| 85 | Vulture|
| 86 | West Highland Terrier|
| 87 | Wild Boar|
| 88 | Wild Rabbit|
| 89 | Wildcat|
| 90 | Wolf|
| 91 | Abraxan Winged Horse|
| 92 | Dragon|
| 93 | Erumpent|
| 94 | Fire-Dwelling Salamander|
| 95 | Granian Winged Horse|
| 96 | Hippogriff|
| 97 | Occamy|
| 98 | Runespoor|
| 99 | Thestral|
| 00 | Unicorn|
</div>

<div class='footnote'>Appendix B | Patronus Rolling Tables</div>

\pagebreakNum

## Artist
### Gryffindor
<div style='margin-top: 10px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Cheetah |
| 3-4 | Fox |
| 5-7 | Heron |
| 8-9 | Robin |
| 0 | Hippogriff |
<div style='margin-top: 20px;'></div>

### Hufflepuff
<div style='margin-top: 10px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Bay Mare/Stallion |
| 3-5 | Borzoi |
| 6-7 | Wood Mouse |
| 8-9 | Swallow |
| 0 | Granian Winged Horse |
<div style='margin-top: 20px;'></div>

### Ravenclaw
<div style='margin-top: 10px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Dolphin |
| 4-5 | Hummingbird |
| 6-7 | Little Owl |
| 8-9 | Siberian Cat |
| 0 | Fire-dwelling Salamander |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Adder |
| 3-5 | Blackbird |
| 6-7 | Greyhound |
| 8-9 | Oryx |
| 0 | Abraxan Winged Horse |
<div style='margin-top: 30px;'></div>

\columnbreak

## Bookworm
### Gryffindor
<div style='margin-top: 10px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Black and White Cat |
| 4-5 | Black Bear |
| 6-7 | Otter |
| 8-9 | Swift |
| 0 | Fire-dwelling Salamander |
<div style='margin-top: 20px;'></div>

### Hufflepuff
<div style='margin-top: 10px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Deerhound |
| 3-4 | Orangutan |
| 5-7 | Red Squirrel |
| 8-9 | Tonkinese Cat |
| 0 | Fire-dwelling Salamander |
<div style='margin-top: 20px;'></div>

### Ravenclaw
<div style='margin-top: 10px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Dolphin |
| 3-4 | Eagle |
| 5-7 | Field Mouse |
| 8-9 | Orangutan |
| 0 | Runespoor |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Calico Cat |
| 3-5 | Crow |
| 6-7 | Hyena |
| 8-9 | Python |
| 0 | Runespoor |
<div style='margin-top: 30px;'></div>

<div class='footnote'>Appendix B | Patronus Rolling Tables</div>

\pagebreakNum
## Dreamer
### Gryffindor
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Dapple Grey Mare/Stallion |
| 4-5 | Manx Cat |
| 6-7 | Otter |
| 8-9 | White Swan |
| 0 | Thestral |
<div style='margin-top: 30px;'></div>

### Hufflepuff
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Doe |
| 4-5 | Elephant |
| 6-7 | Vole |
| 8-9 | Wild Rabbit |
| 0 | Occamy |
<div style='margin-top: 30px;'></div>

### Ravenclaw
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Mountain Hare |
| 3-4 | Raven |
| 5-6 | Red Squirrel |
| 7-9 | White Swan |
| 0 | Unicorn |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Bat |
| 3-4 | Black Swan |
| 5-7 | Grass Snake |
| 8-9 | Python |
| 0 | Thestral |
<div style='margin-top: 30px;'></div>

\columnbreak
## Groundskeeper
### Gryffindor
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Brown Bear |
| 4-5 | Kingfisher |
| 6-7 | Lion |
| 8-9 | St. Bernard |
| 0 | Erumpent |
<div style='margin-top: 30px;'></div>

### Hufflepuff
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Bassett Hound |
| 3-5 | Hedgehog |
| 6-7 | Sparrow |
| 8-9 | Stag |
| 0 | Hippogriff |
<div style='margin-top: 30px;'></div>

### Ravenclaw
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Black Bear |
| 3-4 | Bloodhound |
| 5-7 | Marsh Harrier |
| 8-9 | Sparrow |
| 0 | Occamy |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Orca |
| 3-4 | Rattlesnake |
| 5-6 | Shrew |
| 7-9 | Wildcat |
| 0 | Thestral |
<div style='margin-top: 30px;'></div>

<div class='footnote'>Appendix B | Patronus Rolling Tables</div>

\pagebreakNum
## Klutz
### Gryffindor
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Irish Wolfhound |
| 4-5 | Pheasant |
| 6-7 | Salmon |
| 8-9 | Sparrowhawk |
| 0 | Erumpent |
<div style='margin-top: 30px;'></div>

### Hufflepuff
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Aardvark |
| 3-5 | Buffalo |
| 6-7 | Polar Bear |
| 8-9 | Weasel |
| 0 | Erumpent |
<div style='margin-top: 30px;'></div>

### Ravenclaw
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Capuchin Monkey |
| 3-4 | Mole |
| 5-6 | Polecat |
| 7-9 | Scops Owl |
| 0 | Thestral |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Leopard |
| 3-4 | Magpie |
| 5-6 | Mongrel Dog |
| 7-9 | Stoat |
| 0 | Fire-dwelling Salamander |
<div style='margin-top: 30px;'></div>

\columnbreak
## Potioneer
### Gryffindor
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Brown Owl |
| 4-5 | Grass Snake |
| 6-7 | Piebald Mare/Stallion |
| 8-9 | Tiger |
| 0 | Abraxan Winged Horse |
<div style='margin-top: 30px;'></div>

### Hufflepuff
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Chow Dog |
| 4-5 | Dragonfly |
| 6-7 | Ginger Cat |
| 8-9 | Snowy Owl |
| 0 | Occamy |
<div style='margin-top: 30px;'></div>

### Ravenclaw
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Crow |
| 3-5 | Eagle Owl |
| 6-7 | Husky |
| 8-9 | Russian Blue Cat |
| 0 | Hippogriff |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Adder |
| 4-5 | Black Mare/Stallion |
| 6-7 | King Cobra |
| 8-9 | Nightjar |
| 0 | Hippogriff |
<div style='margin-top: 30px;'></div>

<div class='footnote'>Appendix B | Patronus Rolling Tables</div>

\pagebreakNum
## Protector
### Gryffindor
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Great Grey Owl |
| 3-4 | Newfoundland |
| 5-7 | Stag |
| 8-9 | Swallow |
| 0 | Unicorn |
<div style='margin-top: 30px;'></div>

### Hufflepuff
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Badger |
| 4-5 | Dun Mare/Stallion |
| 6-7 | Mastiff |
| 8-9 | Sphynx Cat |
| 0 | Erumpent |
<div style='margin-top: 30px;'></div>

### Ravenclaw
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Brown Bear |
| 3-4 | King Cobra |
| 5-6 | Lynx |
| 7-9 | Husky |
| 0 | Unicorn |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Goshawk |
| 3-5 | Rhinoceros |
| 6-7 | Tiger |
| 8-9 | Tortoiseshell Cat |
| 0 | Dragon |
<div style='margin-top: 30px;'></div>



\columnbreak
## Quidditch Fan
### Gryffindor
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Fox Terrier |
| 3-5 | Lion |
| 6-7 | Rhinoceros |
| 8-9 | Rottweiler |
| 0 | Dragon |
<div style='margin-top: 30px;'></div>

### Hufflepuff
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Beagle |
| 3-4 | Ocicat |
| 5-6 | Osprey |
| 7-9 | Wild Boar |
| 0 | Dragon |
<div style='margin-top: 30px;'></div>

### Ravenclaw
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Black and White Cat |
| 3-5 | Falcon |
| 6-7 | Leopard |
| 8-9 | Robin |
| 0 | Granian Winged Horse |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Ocicat |
| 3-4 | Polar Bear |
| 5-7 | Rattlesnake |
| 8-9 | Shark |
| 0 | Runespoor |
<div style='margin-top: 30px;'></div>

<div class='footnote'>Appendix B | Patronus Rolling Tables</div>

\pagebreakNum
## Socialite
### Gryffindor
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Chestnut Mare/Stallion |
| 3-5 | Hummingbird |
| 6-7 | Pine Marten |
| 8-9 | Rat |
| 0 | Granian Winged Horse |
<div style='margin-top: 30px;'></div>

### Hufflepuff
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Grey Squirrel |
| 3-4 | Ibizan Hound |
| 5-7 | Ragdoll Cat |
| 8-9 | West Highland Terrier |
| 0 | Unicorn |
<div style='margin-top: 30px;'></div>

### Ravenclaw
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Brown Hare |
| 4-5 | Grey Squirrel |
| 6-7 | Nebelung Cat |
| 8-9 | Seal |
| 0 | Abraxan Winged Horse |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Cheetah |
| 3-4 | Dragonfly |
| 5-6 | Mink |
| 7-9 | Peacock |
| 0 | Granian Winged Horse |
<div style='margin-top: 30px;'></div>

\columnbreak
## Troublemaker
### Gryffindor
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Calico Cat |
| 3-4 | Magpie |
| 5-6 | Shark |
| 7-9 | Wolf |
| 0 | Dragon |
<div style='margin-top: 30px;'></div>

### Hufflepuff
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Black Mamba |
| 3-4 | Bat |
| 5-7 | Buzzard |
| 8-9 | White Mare/Stallion |
| 0 | Abraxan Winged Horse |
<div style='margin-top: 30px;'></div>

### Ravenclaw
<div style='margin-top: 15px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-2 | Falcon |
| 3-5 | Fox |
| 6-7 | Seal |
| 8-9 | Siberian Cat |
| 0 | Hippogriff |
<div style='margin-top: 30px;'></div>

### Slytherin
<div style='margin-top: 20px;'></div>

| d10 | Corporeal Patronus |
|:---:|:---|
| 1-3 | Black Mamba |
| 4-5 | Impala |
| 6-7 | Raven |
| 8-9 | Vulture |
| 0 | Runespoor |
<div style='margin-top: 30px;'></div>

<div class='footnote'>Appendix B | Patronus Rolling Tables</div>

\pagebreakNum
# Appendix C: Chocolate Frog Cards

<div class="wide" style="line-height:1.2; margin:-5px 0px 10px;">The following images originate from Harry Potter and the Chamber of Secrets (2002 video game) developed by </br>KnowWonder, Eurocom, EA UK, Argonaut, and Gryptonite Games and published by Electronic Arts.</div>

## Bronze Cards
<img src='https://vignette.wikia.nocookie.net/harrypotter/images/6/68/Merlin-01-chocFrogCard.png/revision/latest?cb=20160606202336' style='width:210px;'>

### #1 - Merlin
A legendary British wizard who lived during the Middle Ages

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/3/3a/Cornelius_Agrippa_Chocolate_Frog_Card.png/revision/latest?cb=20160606202201' style='width:210px;'>

### #2 - Cornelius Agrippa
A German wizard who authored many magical works

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/4/4d/Grogan_Stump-04-chocFrogCard.png/revision/latest?cb=20160606202258' style='width:210px;'>

### #4 - Grogan Stump
A British wizard who was Minister for Magic from 1811 to 1819 and was very popular in the job

\columnbreak

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/5/55/Gulliver_Pokeby-05-chocFrogCard.png/revision/latest?cb=20160606202300' style='width:210px;'>

### #5 - Gulliver Pokeby
A wizard, magizoologist, expert on magical birds and author of *Why I Didn't Die When the Augurey Cried*

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/d/d7/Glanmore_Peakes-06-chocFrogCard.png/revision/latest?cb=20160606202243' style='width:210px;'>

### #6 - Glanmore Peakes
A Scottish wizard who was famous for having slain the Sea Serpent of Cromer

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/6/6c/Hesper_Starkey-07-chocFrogCard.png/revision/latest?cb=20160606202319' style='width:210px;'>

### #7 - Hesper Starkey
A witch who studied how the moon's phases affected potion fabrication
<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/e/e3/Gunhilda_De_Gorsemoor-09-chocFrogCard.png/revision/latest?cb=20160606202302' style='width:210px;'>

### #9 - Gunhilda of Gorsemoor
A one-eyed, hump-backed British witch and healer who discovered a cure for dragon pox

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/1/15/Burdock_Muldoon-10-chocFrogCard.png/revision/latest?cb=20160606202148' style='width:210px;'>

### #10 - Burdock Muldoon
A British wizard and the Chief of the Wizards' Council either in the fourteenth or fifteenth century

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/2/2a/Merwyn_The_Malicious-12-chocFrogCard.png/revision/latest?cb=20160606202342' style='width:210px;'>

### #12 - Merwyn the Malicious
A medieval Dark Wizard credited with the invention of many unpleasant jinxes and hexes

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/a/a3/Uric_The_Oddball-18-chocFrogCard.png/revision/latest?cb=20160606202431' style='width:210px;'>

### #18 - Uric the Oddball
A medieval wizard who became famous for his eccentric behavior, such as wearing a jellyfish as a hat and sleeping in a room with fifty pet augureys

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/1/15/Newt_Scamander-19-chocFrogCard.png/revision/latest?cb=20160606202357' style='width:210px;'>

### #19 - Newt Scamander
An English wizard, famed magizoologist and the author of *Fantastic Beasts and Where to Find Them*

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/5/55/Lord_Stoddard_Withers-21-chocFrogCard.png/revision/latest?cb=20160606202333' style='width:210px;'>

### #21 - Lord Stoddard Withers
A wizard and magizoologist who bred winged horses

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/8/87/Adalbert_Waffling-24-chocFrogCard.png/revision/latest?cb=20160606202123' style='width:210px;'>

### #24 - Adalbert Waffling
A British wizard was a Magical Theoretician, credited to have written "All About Magic", and is considered the "Father of Magic Theory"

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/1/1b/Perpetua_Fancourt-25-chocFrogCard.png/revision/latest?cb=20160606202408' style='width:210px;'>

### #25 - Perpetua Fancourt
A witch who is credited with the invention of the lunascope, an astronomical device used to analyze the phases of the moon

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/1/19/Almeric_Sawbridge-26-chocFrogCard.png/revision/latest?cb=20160606202130' style='width:210px;'>

### #26 - Almeric Sawbridge
A British wizard and troll hunter who defeated the largest river troll to have ever existed in Britain

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/d/d6/Tilly_Toke-28-chocFrogCard.png/revision/latest?cb=20160606202429' style='width:210px;'>

### #28 - Tilly Toke
A British witch who saved the lives of several muggles during the Ilfracombe Incident in 1932

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/8/80/Archibald_Alderton-29-chocFrogCard.png/revision/latest?cb=20160606202134' style='width:210px;'>

### #29 - Archibald Alderton
A wizard who was known for blowing up the hamlet of Little Dropping while attempting to magically mix a birthday cake

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/79/Balfour_Blane-31-chocFrogCard.png/revision/latest?cb=20160606202137' style='width:210px;'>

### #31 - Balfour Blane
A British wizard who established the Committee on Experimental Charms

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/a/af/Bridget_Wenlock-32-chocFrogCard.png/revision/latest?cb=20160606202146' style='width:210px;'>

### #32 - Bridget Wenlock
A famous thirteenth-century English witch and arithmancer who was the first to establish the magical properties of the number seven

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/f/f8/Beaumont_Marjoribanks-33-chocFrogCard.png/revision/latest?cb=20160606202140' style='width:210px;'>

### #33 - Beaumont Marjoribanks
A wizard and pioneer in the field of Herbology, having collected and classified many rare magical plants and flowers

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/7e/Cassandra_Vablatsky-37-chocFrogCard.png/revision/latest?cb=20160606202151' style='width:210px;'>

### #37 - Cassandra Vablatsky
A witch, celebrated Seer and author of *Unfogging the Future*, a Divination textbook required at Hogwarts School of Witchcraft and Wizardry

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/0/05/Devlin_Whitehorn-44-chocFrogCard.png/revision/latest?cb=20160606202213' style='width:210px;'>

### #44 - Devlin Whitehorn
A British wizard who, in 1967, founded the Nimbus Racing Broom Company, considered to be "the top of the field"

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/f/f9/Miranda_Goshawk-46-chocFrogCard.png/revision/latest?cb=20160606202345' style='width:210px;'>

### #46 - Miranda Goshawk
A witch and celebrated author who specialized in writing Charms spellbooks, such as *The Standard Book of Spells*

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/4/4b/Edgar_Stroulger-47-chocFrogCard.png/revision/latest?cb=20160606202224' style='width:210px;'>

### #47 - Edgar Stroulger
A wizard who invented the Sneakoscope, a dark detector that lights up, spins and whistles if someone is doing something untrustworthy nearby

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/e/e5/Elladora_Ketteridge-49-chocFrogCard.png/revision/latest?cb=20160606202228' style='width:210px;'>

### #49 - Elladora Ketteridge
The first witch to discover the magical properties of gillyweed, having done so by accident

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/5/57/Musidora_Barkwith-50-chocFrogCard.png/revision/latest?cb=20160606202354' style='width:210px;'>

### #50 - Musidora Barkwith
A witch and composer. Her unfinished work, the *Wizarding Suite*, featured an exploding tuba and has been banned ever since a performance in 1902 blew the roof off of the town hall of Ackerley

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/d/d6/Ethelred_The_Ever-ready-51-chocFrogCard.png/revision/latest?cb=20160606202229' style='width:210px;'>

### #51 - Ethelred the Ever-Ready
A medieval Dark Wizard, infamous for being offended for no reason and cursing innocent bystanders

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/d/da/Greta_Catchlove-53-chocFrogCard.png/revision/latest?cb=20160606202256' style='width:210px;'>

### #53 - Greta Catchlove
A witch who wrote the original edition of *Charm Your Own Cheese*

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/74/Gifford_Ollerton-57-chocFrogCard.png/revision/latest?cb=20160606202241' style='width:210px;'>

### #57 - Gifford Ollerton
A British wizard famous for his reputation as a giant-slayer, having killed the giant Hengist of Upper Barnton who terrorized the small town of Upper Barnton in the fifteenth century

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/a/a0/Glover_Hipworth-58-chocFrogCard.png/revision/latest?cb=20160606202246' style='width:210px;'>

### #58 - Glover Hipworth
A wizard who specialized in Potion development and became famous for the invention of the pepperup potion, the cure for the common cold

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/3/37/Havelock_Sweeting-61-chocFrogCard.png/revision/latest?cb=20160606202308' style='width:210px;'>

### #61 - Havelock Sweeting
A British wizard and magizoologist well-known for being an expert on unicorns

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/2/2c/Herman_Wintringham-63-chocFrogCard.png/revision/latest?cb=20160606202314' style='width:210px;'>

### #63 - Herman Wintringham
A wizard and lutenist for the popular band The Weird Sisters

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/72/Jocunda_Sykes_Chocolate_Frog_Card.png/revision/latest?cb=20160606202324' style='width:210px;'>

### #64 - Jocunda Sykes
A witch who was famous for flying across the Atlantic Ocean

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/4/4f/Flavius_Belby-66-chocFrogCard.png/revision/latest?cb=20160606202232' style='width:210px;'>

### #66 - Flavius Belby
The only known wizard to survive a lethifold attack

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/a/ab/Justus_Pilliwickle-67-chocFrogCard.png/revision/latest?cb=20160606202327' style='width:210px;'>

### #67 - Justus Pilliwickle
A British wizard and celebrated Head of the Department of Magical Law Enforcement

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/4/4e/Mungo_Bonham-75-chocFrogCard.png/revision/latest?cb=20160606202352' style='width:210px;'>

### #75 - Mungo Bonham
A wizard and healer who founded St. Mungo's Hospital for Magical Maladies and Injuries in the 1600s

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/b/bc/Myron_Wagtail-76-chocFrogCard.png/revision/latest?cb=20160606202355' style='width:210px;'>

### #76 - Myron Wagtail
A wizard and lead singer of the wizarding world's popular band The Weird Sisters

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/f/fe/Norvel_Twonk-77-chocFrogCard.png/revision/latest?cb=20160606202359' style='width:210px;'>

### #77 - Norvel Twonk
A wizard who died saving a muggle child from a manticore

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/c/c8/Orsino_Thruston-78-chocFrogCard.png/revision/latest?cb=20160606202401' style='width:210px;'>

### #78 - Orsino Thruston
A wizard and the drummer for the popular band The Weird Sisters

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/1/15/Beatrix_Bloxam-80-chocFrogCard.png/revision/latest?cb=20160606202138' style='width:210px;'>

### #80 - Beatrix Bloxam
A witch who wrote the infamous *Toadstool Tales*,a series of children's books featuring bowdlerised adaptations of stories from earlier works, including *The Tales of Beedle the Bard*

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/2/25/Quong_Po-81-chocFrogCard.png/revision/latest?cb=20160606202415' style='width:210px;'>

### #81 - Quong Po
A Chinese wizard and dragonologist who studied the Chinese Fireball breed and discovered the magical uses of their powdered eggs

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/b/b3/Roderick_Plumpton%27s_Chocolate_Frog_Card.png/revision/latest?cb=20160606202419' style='width:210px;'>

### #83 - Roderick Plumpton
An English wizard who was the Seeker for the Tutshill Tornadoes quidditch team during the early 1900s

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/2/2d/Roland_Kegg-84-chocFrogCard.png/revision/latest?cb=20160606202420' style='width:210px;'>

### #84 - Roland Kegg
An English wizard who was President of the English Gobstones team

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/2/2d/Dorcas_Wellbeloved-86-chocFrogCard.png/revision/latest?cb=20160606202216' style='width:210px;'>

### #86 - Dorcas Wellbeloved
A witch famous for founding the Society of Distressed Witches

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/8/80/Celestina_Warbeck-88-chocFrogCard.png/revision/latest?cb=20160606202153' style='width:210px;'>

### #88 - Celestina Warbeck
A Welsh witch and popular singer known as "The Singing Sorceress"

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/9/9f/Wilfred_Elphick-91-chocFrogCard.png/revision/latest?cb=20160606202434' style='width:210px;'>

### #91 - Wilfred Elphick
The first wizard to be gored by an African erumpent, which is an extremely unlikely event, given the fact that the horn of an erumpent almost always explodes on contact, due to the fluid it contains

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/f/fc/Heathcote_Barbary-93-chocFrogCard.png/revision/latest?cb=20160606202310' style='width:210px;'>

### #93 - Heathcote Barbary
A wizard and the rhythm guitarist for the popular wizarding band The Weird Sisters

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/9/9b/Merton_Graves-94-chocFrogCard.png/revision/latest?cb=20160606202340' style='width:210px;'>

### #94 - Merton Graves
A wizard and the cellist for the popular wizarding band The Weird Sisters
<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/3/3e/Yardley_Platt-95-chocFrogCard.png/revision/latest?cb=20160606202437' style='width:210px;'>

### #95 - Yardley Platt
An infamous Dark wizard who was known for being a serial goblin killer

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/d/d2/Hengist_Of_Woodcroft-96-chocFrogCard.png/revision/latest?cb=20160606202313' style='width:210px;'>

### #96 - Hengist of Woodcroft
A medieval English wizard best known as the founder of the village of Hogsmeade

___
## Silver Cards

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/71/Elfrida_Clagg-03-chocFrogCard.png/revision/latest?cb=20160606202226' style='width:210px;'>

### #3 - Elfrida Clagg
A British witch and the Chieftainess of the Wizards' Council either in the fourteenth or seventeenth century

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/e/e1/Derwent_Shimpling-08-chocFrogCard.png/revision/latest?cb=20160606202212' style='width:210px;'>

### #8 - Derwent Shimpling
A wizarding comedian who once ate an entire Venomous Tentacula on a bet. Though he survived, his skin was left purple

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/3/32/Andros_The_Invincible-13-chocFrogCard.png/revision/latest?cb=20160606202132' style='width:210px;'>

### #13 - Andros the Invincible 
A celebrated Ancient Greek wizard who, reportedly, was able to conjure a Patronus of giant size

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/4/41/Fulbert_The_Fearful-14-chocFrogCard.png/revision/latest?cb=20160606202234' style='width:210px;'>

### #14 - Fulbert the Fearful
A wizard who was famous for being so cowardly that he never ventured out of his house

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/9/95/Cliodne-16-chocFrogCard.png/revision/latest?cb=20160606202159' style='width:210px;'>

### #16 - Cliodna (Cliodne)
A famous medieval Irish witch and druidess

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/1/18/Morgan_Le_Fay-17-chocFrogCard.png/revision/latest?cb=20160606202350' style='width:210px;'>

### #17 - Morgan le Fay (Morgana)
A medieval dark witch, famous for being the enemy of the legendary wizard Merlin and the half-sister of King Arthur

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/e/e6/Wendelin_The_Weird-20-chocFrogCard.png/revision/latest?cb=20160606202432' style='width:210px;'>

### #20 - Wendelin the Weird
An eccentric British medieval witch who was famous for being burnt at the stake no less than forty-seven times in various disguises

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/79/Circe-22-chocFrogCard.png/revision/latest?cb=20160606202157' style='width:210px;'>

### #22 - Circe
A witch who lived in ancient Greece on an island referred to as Circe's Island. She enjoyed transfiguring lost sailors into animals

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/c/cf/Glenda_Chittock-23-chocFrogCard.png/revision/latest?cb=20160606202244' style='width:210px;'>

### #23 - Glenda Chittock
A British witch who was host of the Wizarding Wireless Network programme, Witching Hour

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/3/38/Mirabella_Plunkett-27-chocFrogCard.png/revision/latest?cb=20160606202344' style='width:210px;'>

### #27 - Mirabella Plunkett
A British witch famous for falling in love with a merman in Loch Lomond while on holiday. After her parents forbade her to marry him, she transfigured herself into a haddock and was never seen again

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/f/f1/Artemisia_Lufkin-30-chocFrogCard.png/revision/latest?cb=20160606202135' style='width:210px;'>

### #30 - Artemisia Lufkin
The first witch to serve as Minister for Magic for Great Britain

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/e/ed/Donaghan_Tremlett-34-chocFrogCard.png/revision/latest?cb=20160606202215' style='width:210px;'>

### #34 - Donaghan Tremlett
A Muggle-born wizard who played bass for the popular wizarding band, The Weird Sisters

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/9/9a/Bowman_Wright-35-chocFrogCard.png/revision/latest?cb=20160606202145' style='width:210px;'>

### #35 - Bowman Wright
A half-blood wizard and a skilled metal charmer who lived in Godric's Hollow sometime during the Middle Ages

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/8/8b/Joscelind_Wadcock-36-chocFrogCard.png/revision/latest?cb=20160606202326' style='width:210px;'>

### #36 - Joscelind Wadcock
A British witch who played as a Chaser for the Puddlemere United Quidditch team. The record-holder for highest number of Quidditch goals in the British League during the 20th century

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/5/5e/Chauncey_Oldridge-38-chocFrogCard.png/revision/latest?cb=20160606202155' style='width:210px;'>

### #38 - Chauncey Oldridge
The first known victim of Dragon Pox

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/0/0a/Gwenog_Jones-39-chocFrogCard.png/revision/latest?cb=20160606202303' style='width:210px;'>

### #39 - Gwenog Jones
A professional Quidditch player who later achieved fame as the captain and beater of the Welsh all-female Quidditch team, the Holyhead Harpies

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/4/45/Crispin_Cronk-42-chocFrogCard.png/revision/latest?cb=20160606202204' style='width:210px;'>

### #42 - Crispin Cronk
An Egyptophile British wizard who insisted on keeping several sphinxes in his backyard

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/c/ce/Cyprian_Youdle-43-chocFrogCard.png/revision/latest?cb=20160606202207' style='width:210px;'>

### #43 - Cyprian Youdle
An English wizard and Quidditch referee from Norfolk, the only known referee to have been killed during a Quidditch match

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/f/fc/Dunbar_Oglethorpe-45-chocFrogCard.png/revision/latest?cb=20160606202218' style='width:210px;'>

### #45 - Dunbar Oglethorpe
A British wizard who served as the Chief of the Quidditch Union for the Administration and Betterment of the British League and its Endeavours

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/7c/Felix_Summerbee-52-chocFrogCard.png/revision/latest?cb=20160606202231' style='width:210px;'>

### #52 - Felix Summerbee
A wizard who invented the Cheering Charm

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/1/10/Gaspard_Shingleton-54-chocFrogCard.png/revision/latest?cb=20160606202236' style='width:210px;'>

### #54 - Gaspard Shingleton
A wizarding inventor who first devised the Self-Stirring Cauldron

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/6/62/Honoria_Nutcombe-55-chocFrogCard.png/revision/latest?cb=20160606202321' style='width:210px;'>

### #55 - Honoria Nutcombe
A witch who founded of the Society for the Reformation of Hags

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/4/44/Gideon_Crumb-56-chocFrogCard.png/revision/latest?cb=20160606202237' style='width:210px;'>

### #56 - Gideon Crumb 
A wizard who played bagpipes for the popular wizarding band, The Weird Sisters

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/a/a3/Gregory_The_Swarmy-59-chocFrogCard.png/revision/latest?cb=20160606202253' style='width:210px;'>

### #59 - Gregory the Smarmy
A medieval British wizard and Potioneer who invented Gregory's Unctuous Unction, a potion that makes the drinker believe whomever gave the potion is his or her best friend

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/c/ca/Laverne_De_Montmorency-60-chocFrogCard.png/revision/latest?cb=20160606202330' style='width:210px;'>

### #60 - Laverne de Montmorency
A nineteenth-century potioneer who invented a number of love potions

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/8/84/Ignatia_Wildsmith-62-chocFrogCard.png/revision/latest?cb=20160606202322' style='width:210px;'>

### #62 - Ignatia Wildsmith
A witch and wizarding inventor who was famously the creator of Floo Powder

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/0/02/Gondoline_Oliphant-65-chocFrogCard.png/revision/latest?cb=20160606202250' style='width:210px;'>

### #65 - Gondoline Oliphant
A British witch made famous for studying the life and habits of trolls

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/73/Kirley_Duke-68-chocFrogCard.png/revision/latest?cb=20160606202328' style='width:210px;'>

### #68 - Kirley Duke
A British wizard and the lead guitarist for the popular band, The Weird Sisters, and one of its first three members

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/6/64/Leopoldina_Smethwyck-70-chocFrogCard.png/revision/latest?cb=20160606202331' style='width:210px;'>

### #70 - Leopoldina Smethwyck
A British witch who was well known for her career as a Quidditch referee

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/f/f5/Queen_Maeve-71-chocFrogCard.png/revision/latest?cb=20160606202413' style='width:210px;'>

### #71 - Queen Maeve
A famous Irish witch who lived during the Middle Ages

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/d/df/Mopsus-73-chocFrogCard.png/revision/latest?cb=20160606202348' style='width:210px;'>

### #73 - Mopsus
A blind Seer whose power was great enough for him to accurately predict future events

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/1/19/Oswald_Beamish-79-chocFrogCard.png/revision/latest?cb=20160606202403' style='width:210px;'>

### #79 - Oswald Beamish
A wizarding activist and a pioneer of goblin rights

<!--<img src='https://vignette.wikia.nocookie.net/harrypotter/images/a/aa/Blenheim_Stalk_Chocolate_Frog_Card_COSG_PC.png/revision/latest/smart/width/250/height/230?cb=20210420005433' style='width:210px;'>-->

</br></br></br></br></br>

####                    [Card Not Found]

</br></br></br></br></br>

### #85 - Blenheim Stalk
A wizard and author who was a well-known expert on muggles

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/a/a9/Thaddeus_Thurkell-87-chocFrogCard.png/revision/latest?cb=20160606202428' style='width:210px;'>

### #87 - Thaddeus Thurkell
A wizard who fathered seven sons who were all squibs. He transfigured them into hedgehogs out of disgust

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/d/d8/Alberta_Toothill-89-chocFrogCard.png/revision/latest?cb=20160606202127' style='width:210px;'>

### #89 - Alberta Toothill
An English medieval witch and duellist who, defying all odds, won the All-England Wizarding Duelling Competition of 1430

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/b/b5/Sacharissa_Tugwood_FWC_COSG.png/revision/latest/scale-to-width-down/1000?cb=20210420010045' style='width:210px;'>

### #90 - Sacharissa Tugwood
A famous Potioneer and the first witch to use beauty potions, having developed quite a few of them herself

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/5/51/Xavier_Rastrick-92-chocFrogCard.png/revision/latest?cb=20160606202435' style='width:210px;'>

### #92 - Xavier Rastrick
A lively wizard entertainer who is famous for unexpectedly vanishing during a performance in Painswick before the very eyes of his audience, never to be seen again

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/3/30/Alberic_Grunnion-97-chocFrogCard.png/revision/latest?cb=20160606202125' style='width:210px;'>

### #97 - Alberic Grunnion
A nineteenth century wizard inventor who developed the dungbomb, a magical stink bomb that gives off a putrid odor

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/c/c8/Dymphna_Furmage-98-chocFrogCard.png/revision/latest?cb=20160606202222' style='width:210px;'>

### #98 - Dymphna Furmage
A British witch who famously campaigned for the destruction of pixies after being abducted by them while holidaying in Cornwall

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/e/e4/Daisy_Dodderidge-99-chocFrogCard.png/revision/latest?cb=20160606202209' style='width:210px;'>

### #99 - Daisy Dodderidge
The witch who built the Leaky Cauldron in a successful attempt to create a gateway between the muggle and wizarding worlds

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

## Gold Cards

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/78/Herpo_The_Foul-11-chocFrogCard.png/revision/latest?cb=20160606202317' style='width:210px;'>

### #11 - Herpo the Foul
An ancient Greek Dark wizard, infamous for being a pioneer the field of the Dark Arts, becoming the first known wizard to create the Basilisk, in addition to the first known Horcrux

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/9/9a/Paracelsus-15-chocFrogCard.png/revision/latest?cb=20160606202405' style='width:210px;'>

### #15 - Paracelsus
A wizard and alchemist about whom very little is known, but was credited with the discovery of Parseltongue

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/d/da/Carlotta_Pinkstone-40-chocFrogCard.png/revision/latest?cb=20160606202149' style='width:210px;'>

### #40 - Carlotta Pinkstone
A British witch who famously advocated for the repeal of the International Statute of Wizarding Secrecy

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/2/24/Godric_Gryffindor-41-chocFrogCard.png/revision/latest?cb=20160606202248' style='width:210px;'>

### #41 - Godric Gryffindor
An English wizard and one of the four founders of Hogwarts School of Witchcraft and Wizardry

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/8/84/Salazar_Slytherin-48-chocFrogCard.png/revision/latest?cb=20160606202426' style='width:210px;'>

### #48 - Salazar Slytherin
An English pure-blood wizard and one of the four founders of Hogwarts School of Witchcraft and Wizardry, skilled in Parseltongue

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/7/72/Bertie_Bott-69-chocFrogCard.png/revision/latest?cb=20160606202141' style='width:210px;'>

### #69 - Bertie Bott
A wizarding confectioner, who accidentally created Bertie Bott's Every Flavour Beans

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/0/0d/Helga_Hufflepuff-72-chocFrogCard.png/revision/latest?cb=20160606202311' style='width:210px;'>

### #72 - Helga Hufflepuff
A Welsh witch and was one of the four founders of Hogwarts School of Witchcraft and Wizardry

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/5/50/Montague_Knightley-74-chocFrogCard.png/revision/latest?cb=20160606202347' style='width:210px;'>

### #74 - Montague Knightley
A professional Wizard's Chess player. During his career, he eventually became the Wizard's Chess Champion

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/2/22/Rowena_Ravenclaw-82-chocFrogCard.png/revision/latest?cb=20160606202422' style='width:210px;'>

### #82 - Rowena Ravenclaw
A Scottish witch and one of the four founders of Hogwarts School of Witchcraft and Wizardry

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/b/b3/Harry_Potter-100-chocFrogCard.png/revision/latest?cb=20160606202307' style='width:210px;'>

### #100 - Harry Potter
An English half-blood wizard, one of the most famous wizards of modern times

<img src='https://vignette.wikia.nocookie.net/harrypotter/images/d/dd/Albus_Dumbledore-101-chocFrogCard.png/revision/latest?cb=20160606202128' style='width:210px;'>

### #101 - Albus Dumbledore
An English half-blood wizard, who was the Defence Against the Dark Arts professor, later the Transfiguration professor, and later Headmaster of Hogwarts School of Witchcraft and Wizardry

<div class='footnote'>Appendix C | Chocolate Frog Cards</div>

\pagebreakNum
# Glossary
## A
### Alchemy
A medieval forerunner of chemistry, alchemy was developed out of experiments to find a method of turning base metals into gold, and of making an elixir of life that would prolong life indefinitely. A very advanced and complex topic that requires in-depth knowledge about the nature of magic and the four basic elements: earth, air, fire, and water.
### Apparate
To apparate is to magically teleport a limited distance, creating a loud crack or pop whenever used. Apparition requires a licence from the Department of Magical Transportation, which can only be issued to those seventeen and over. Disapparition is the word to describe when a person disappears, leaving by apparating. 
### Arithmancy
Ancient study of the magical properties of numbers. Arithmancy is often needed in the modification or creation of spells, a very dangerous practice.
### Auror
Professional Dark wizard catcher and the equivalent to a Muggle detective or special agent. To become an Auror, a witch or wizard must gain at least five N.E.W.T.s with grades no lower than 'Exceeds Expectations' in subjects including: Defence Against the Dark Arts, Potions, Transfiguration, and Charms; pass stringent character and aptitude tests at the Ministry of Magic's Auror office, then do three years of Auror training.
### Azkaban
Island prison fortress where wizarding criminals are sent. Guarded day and night by the terrifying Dementors, who drain peace, hope and happiness out of any human in their vicinity.
## B
### Basilisk
A Dark creature much like a gargantuan, heavy-bodied snake, measuring up to 50 feet in length when fully grown. Unlike a snake, a basilisk has a full row of fangs, all of which contain the most deadly venom for which there is no antidote. Its yellow eyes will kill any creature that looks directly into them, and petrify (frozen in time, as if turned to stone) anyone who catches an indirect glimpse.

\columnbreak
### Beauxbatons Academy of Magic (Académie de Magie Beauxbâtons)
A co-ed wizarding school located somewhere in France, often seen as comparable to Hogwarts in quality of education.
### Broomstick
One of the most popular forms of wizarding transportation, broomsticks have been bewitched with countless enchantments to facilitate flight, such as a cushioning charm to sit upon, braking charms, and anti-jinx protections. A broomstick is controlled by the rider's grip on the handle, accelerating when squeezed.
### Butterbeer
A frothy butterscotch-flavored drink served hot or cold, depending on the weather. Has diminutive alcoholic content, but that has a severe effect on house-elves.
## C
### Construct
Not a magically animated robot, but rather simply a "living" creature that has been transfigured or conjured into existence. If a rock was transfigured into a dog to distract a dragon, that dog is a construct, meaning it's a materialization of the wizard's concept of a dog. It behaves how the wizard expects a dog to behave. It is an imitation of life and will eventually return to being a rock.
## D
### The Daily Prophet
The most popular wizarding newspaper in Great Britain.
## E
### Elves
See house-elf.
### Exploding Snap
The wizarding version of the muggle card game of snap, which uses a specifically-enchanted deck that may explode at any time.
<div class='footnote'>Glossary</div>

\pagebreakNum
## F
### Floo Powder
Glittering silver powder that allows witches and wizards to travel magically via the Floo Network by throwing the powder into a lit fireplace, stepping into the green flames, and naming their destination. A wizard may also kneel with their head in the green fire to merely communicate with whomever is near the destination fireplace. The Floo Network is managed by the Floo Network Authority under the Department of Magical Transportation, and connects wizarding fireplaces to each other.
## G
### Ghoul
A magical beast that resembles a slimy, buck-toothed ogre. They tend to live in the attics or barns of wizards and witches. They are relatively harmless creatures and are just seen as nuisances because of the noise they make. They are relatively dimwitted, and live off of bugs and other household pests. At most, they will groan and throw objects.
### Giant
Huge humanoid beings with extremely violent and tribalistic tendencies, growing up to 25 feet tall. Although they are intelligent and capable of interacting with other beings (sometimes resulting in part-giants), they almost invariable lose patience and resort to violence.
### Gnomes
Very small creatures with leathery skin and large, bald heads like knobbly potatoes. They have horny feet and razor-sharp teeth. They live in holes in gardens and aren't very bright. To de-gnome a garden, grab the gnome by the ankles, swing it in circles until it's dizzy, and throw it as far as you can.
### Goblins
Small clever beings with swarthy faces and very long hands and feet, showing some traits of the dwarves of Muggle fiction. Goblins own Gringotts Bank and are responsible for minting wizarding currencies, as well as various metalworks. They have a deep distrust of wizards due to centuries of goblin-wizard conflicts and uprisings. Wizards have historically oppressed goblins and denied them use of wands.
### Gobstones
The wizarding version of marbles. The pieces squirt a stinky substance into other players' faces when they lose a point.
## H
### Half-breed
A perjorative term used against humans with non-human ancestry or particular magical curses, like lycanthropy. Never used in civil conversation.

\columnbreak
### HM
HM stands for Headmaster or Headmistress, which typically refers to the witch or wizard in charge of Hogwarts. In the context of Wands & Wizards, the HM is the master of the table and runs the game.
### House-elf
A very small creature dedicated to manual labor and indentured to a specific wizarding family. House-elves are freed by
### Howler
Wizarding letter which, when opened, shrieks and howls at the reader in the deafening voice of the sender. Comes in a red envelope and is usually sent by someone who is very angry.
## M
### Mudblood
Highly offensive and derogatory term for a muggle-born wizard or witch. Only used by blood purists, who believe that those with ancestry of magical blood are superior.
### Muggle duelling
A non-magical physical fight.
## N
### N.E.W.T.s
Nastily Exhausting Wizarding Tests. Higher level examinations taken at the end of the seventh year at Hogwarts.
## O
### O.W.L.s
Ordinary Wizarding Levels. Hogwarts standard-level examinations which are taken at the end of the fifth year.
## P
### Pensieve
Stone basin which enables one to view thoughts and memories, pulled out from one's mind using a wand.
### Poltergeist
A humanoid spirit born entirely from mischevious energy. Unlike ghosts, a poltergeist never had a life, has color, and can turn itself invisible.
<div class='footnote'>Glossary</div>

\pagebreakNum
### Portkey
Any object can be bewitched for use as a portkey to teleport witches and wizards away to a prearranged destination the instant they touch it or at a scheduled time. Physical contact must be made to use a portkey. Use of a portkey should be authorised by the Ministry of Magic.
## R
### Remembrall
Magical glass ball, the size of a large marble, filled with white smoke. The smoke turns to a deep red if there is something you have forgotten to do.
## S
### Sorcerer
Non-gendered term for a witch or a wizard. 
### Squib
Someone who, despite being born into a wizarding family, has little or no magical ability. Anti-muggle magic typically doesn't affect them, and they are able to see Dementors. Squibs are often looked down upon and find themselves as rejects trapped in the wizarding world.
## U
### Unicorn
Mythical white horse-like creature with a golden mane and a golden horn sprouting from the head. Innocent and beautiful creatures. The tail hair and horn can be used in magic. It is considered a monstrous crime to slay a unicorn. Drinking its blood will keep you alive, even when close to death. However, you have killed something pure, and will therefore live a half, cursed life.
### Unspeakable
Employee of the Ministry of Magic's Department of Mysteries. Little is known about their workplace, and even less is known about their jobs. They are forbidden from discussing their jobs or disclosing any information about their department, hence the name "Unspeakable."
## W
### Warlock
A very old term that has two meanings: to describe a wizard of unusually fierce appearance or as a title denoting particular skill or achievement. It originally denoted one learned in duelling and all martial magic or was given as a title to a wizard who had performed feats of bravery (as Muggles are sometimes knighted). It is sometimes incorrectly used as interchangeable with the term "wizard."

\columnbreak
### Witch
Gender-specific term for a female human with natural magical ability, often referred to as 'magical blood.'
### Wizard
Gender-specific term for a male human with natural magical ability, often referred to as 'magical blood.'
### Wizarding
An adjective to describe anything that belongs to the magical world.
### Wizengamot
The Wizard High Court, consisting of about fifty witches and wizards who wear plum-coloured robes with a silver 'W' worked onto the left-hand breast.
### WWN
The Wizarding Wireless Network, a magical radio system that allows wizards to listen to wizarding music and news using a Muggle radio and a wand.
<div class='footnote'>Glossary</div>

<div class='pageNumber auto'></div>
<!--Black Dragon; Medium dragon, (alignment same as knight); Armour Class 14; Hit Points 8 (1d10 + 2); Speed 20 ft., fly 30 ft., swim 20 ft.; STR DEX CON INT WIS CHA; 14 (+2) 14 (+2) 14 (+2) 10 (+0) 12 (+1) 12 (+1); Saving Throws Same as knight; Skills Perception +5, Stealth +4; Damage Immunities acid; Senses darkvision 60 ft., passive Perception 15; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.
Blue Dragon; Medium dragon, (alignment same as knight); Armour Class 14 (natural armour); Hit Points 8 (1d10 + 2); Speed 20 ft., climb 20 ft., fly 30 ft.; STR DEX CON INT WIS CHA; 14 (+2) 10 (+0) 14 (+2) 12 (+1) 12 (+1) 14 (+2); Saving Throws Same as knight; Skills Perception +5, Stealth +2; Damage Immunities lightning; Senses darkvision 60 ft., passive Perception 15; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.
Brass Dragon; Medium dragon, (alignment same as knight); Armour Class 14 (natural armour); Hit Points 8 (1d10 + 2); Speed 20 ft., climb 20 ft., fly 30 ft.; STR DEX CON INT WIS CHA; 14 (+2) 10 (+0) 14 (+2) 12 (+1) 12 (+1) 14 (+2); Saving Throws Same as knight; Skills Perception +5, Stealth +2; Damage Immunities fire; Senses darkvision 60 ft., passive Perception 15; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.
Bronze Dragon; Medium dragon, (alignment same as knight); Armour Class 14 (natural armour); Hit Points 8 (1d10 + 2); Speed 20 ft., fly 30 ft., swim 20 ft.; STR DEX CON INT WIS CHA; 14 (+2) 12 (+1) 14 (+2) 12 (+1) 10 (+0) 14 (+2); Saving Throws Same as knight; Skills Perception +4, Stealth +3; Damage Immunities lightning; Senses darkvision 60 ft., passive Perception 14; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.
Copper Dragon; Medium dragon, (alignment same as knight); Armour Class 14 (natural armour); Hit Points 8 (1d10 + 2); Speed 20 ft., climb 20 ft., fly 30 ft.; STR DEX CON INT WIS CHA; 14 (+2) 12 (+1) 14 (+2) 14 (+2) 10 (+0) 12 (+1); Saving Throws Same as knight; Skills Perception +4, Stealth +3; Damage Immunities acid; Senses darkvision 60 ft., passive Perception 14; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.
Gold Dragon; Medium dragon, (alignment same as knight); Armour Class 14 (natural armour); Hit Points 8 (1d10 + 2); Speed 20 ft., fly 30 ft., swim 20 ft.; STR DEX CON INT WIS CHA; 14 (+2) 12 (+1) 14 (+2) 14 (+2) 10 (+0) 12 (+1); Saving Throws Same as knight; Skills Perception +4, Stealth +3; Damage Immunities fire; Senses darkvision 60 ft., passive Perception 14; Amphibious. The dragon can breathe air and water.; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.
Green Dragon; Medium dragon, (alignment same as knight); Armour Class 14 (natural armour); Hit Points 8 (1d10 + 2); Speed 20 ft., fly 30 ft., swim 20 ft.; STR DEX CON INT WIS CHA; 14 (+2) 12 (+1) 14 (+2) 14 (+2) 10 (+0) 12 (+1); Saving Throws Same as knight; Skills Perception +4, Stealth +3; Damage Immunities poison; Condition Immunities poisoned; Senses darkvision 60 ft., passive Perception 14; Amphibious. The dragon can breathe air and water.; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.
Red Dragon; Medium dragon, (alignment same as knight); Armour Class 14 (natural armour); Hit Points 8 (1d10 + 2); Speed 20 ft., climb 20 ft., fly 30 ft.; STR DEX CON INT WIS CHA; 14 (+2) 10 (+0) 14 (+2) 12 (+1) 12 (+1) 14 (+2); Saving Throws Same as knight; Skills Perception +5, Stealth +2; Damage Immunities fire; Senses darkvision 60 ft., passive Perception 15; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.
Silver Dragon; Medium dragon, (alignment same as knight); Armour Class 14 (natural armour); Hit Points 8 (1d10 + 2); Speed 20 ft., climb 20 ft., fly 30 ft.; STR DEX CON INT WIS CHA; 14 (+2) 10 (+0) 14 (+2) 14 (+2) 12 (+1) 12 (+1); Saving Throws Same as knight; Skills Perception +5, Stealth +2; Damage Immunities cold; Senses darkvision 60 ft., passive Perception 15; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.
White Dragon; Medium dragon, (alignment same as knight); Armour Class 14 (natural armour); Hit Points 8 (1d10 + 2); Speed 20 ft., climb 20 ft., fly 30 ft., swim 20 ft.; STR DEX CON INT WIS CHA; 14 (+2) 12 (+1) 14 (+2) 10 (+0) 12 (+1) 14 (+2); Saving Throws Same as knight; Skills Perception +5, Stealth +3; Damage Immunities cold; Senses darkvision 60 ft., passive Perception 15; Languages Draconic; Ice Walk. The dragon can move across across and climb icy surfaces without needing to make an ability check. Additionally, difficult terrain composed of ice or snow doesn’t cost it extra movement.; Actions; Claw. Melee Weapon Attack: +4 to hit, reach 5ft., one target. Hit: 4 (1d4 + 2) slashing damage.

Lucius Malfoy (Pierre Raveneau) - https://cdnb.artstation.com/p/assets/images/images/004/326/475/large/pierre-raveneau-lucius.jpg?1482456122

<img src='https://drive.google.com/uc?id=0B0TGf4bxO8wBazRQZmxyWU4tLTA' class='cover-image'> dragons

<img src='https://drive.google.com/uc?id=0B0TGf4bxO8wBcWpsYldEcVhINnM' class='cover-image'> bookstore

-->