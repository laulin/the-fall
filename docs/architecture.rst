Architecture
~~~~~~~~~~~~

**This is a draft document. As a proposal, it can be changed and your contribution is welcome !**

Top level action
================

This chapter describes each command that can be done by a player.

create a player
---------------

parameters :
- nickname
- email 
- password

do :
- add a row in Player table with parameters
- add a row in Base table with initial base values 
- add a row in Technologies with initial technologie values 
- add a row in Unit with initial unit 
- add many row in Blueprint with initial blueprints 

conditions:
- nickname doesn't exist
- email doesn't exist 
- password is secure



login
-----

parameters :
- email 
- password (hashed + salt)

conditions :
- email is valid
- password is valid

return:
- a session token, used by all commands
- a player_id, unique for the player

do:
- set the session_id in the player



logout
------

parameters:
- a session token
- a player_id

do:
- NULL the field session_id of the player 

conditions:
- player_id exists
- session_id of the player is valid



get ressources
--------------

parameters:
- a session token
- a player_id

return:
- supply quantity
- ammo quantity
- gasoline quantity

do:
- update travel mecanism

conditions:
- player_id exists
- session_id of the player is valid



get building level
------------------

parameters:
- a session token
- a player_id

return:
- trading_post level
- weapon_factory level
- vehicule_warehouse level
- barack level
- hq level

do:
- update building mecanism

conditions:
- player_id exists
- session_id of the player is valid


get units in the base
---------------------

parameters:
- a session token
- a player_id

return:
- a list of units (infantry, vehicule, defense) and the number of each available

do:
- update building and traveling mecanism

conditions:
- player_id exists
- session_id of the player is valid


upgrade building
----------------

parameters:
- a session token
- a player_id
- building 

do:
- remove ressources 
- add building to the building list

conditions:
- player_id exists
- session_id of the player is valid
- building is valid 
- ressources are available
- technologies/buildings are compliance
- the building is not still upgrading


upgrade technologie
-------------------

parameters:
- a session token
- a player_id
- technology 

do:
- remove ressources 
- add technologie to the building list

conditions:
- player_id exists
- session_id of the player is valid
- technlologie is valid 
- ressources are available
- technologies/buildings are compliance
- the technologies is not still upgrading


get blueprints
--------------

parameters:
- a session token
- a player_id

conditions:
- player_id exists
- session_id of the player is valid

returns:
- list of blueprint_id 


build vehicule/defense 
----------------------

parameters:
- a session token
- a player_id
- blueprint_id 
- number

do:
- add row per vehicule in the building list (FIFO)
- remove ressources

conditions:
- player_id exists
- session_id of the player is valid
- ressources are available
- technologies/buildings are compliance

equip infantry 
--------------

parameters:
- a session token
- a player_id
- blueprint_id 
- number
- source unit (blueprint_id)

do:
- add row per infantery in the building list (FIFO)
- remove ressources
- remove unit

conditions:
- player_id exists
- session_id of the player is valid
- ressources are available
- technologies/buildings are compliance
- source unit is infantery

Battle modeling
===============

Those parameters are interessing for the battle modeling only.

infantry:

- health : points
- armor : equilvalent in mm of steel
- damage : number of points removed to the health
- penetration : equivalent in mm of steel penetrated
- shot per round : number of shot done in a round of simulation
- ammo needed : per travel, number of munition needed
- backpack (cargo) : one point for one ressource 
- accuracy : chance to hit target par shot
- speed : unit speed
- target priority : give a priority list of unit targeted by the unit. For example, bazooka unit could have this list : [tank, light vehicule, infantry]
- class : infantry

vehicule:

A vehicule is a generic approach. The class define the type of vehicule.

- health : points
- armor : equilvalent in mm of steel
- damage : number of points removed to the health
- penetration : equivalent in mm of steel penetrated
- shot per round : number of shot done in a round of simulation
- ammo needed : per travel, number of munition needed
- cargo : one point for one ressource 
- accuracy : chance to hit target par shot
- speed : unit speed
- target priority : give a priority list of unit targeted by the unit. For example, bazooka unit could have this list : [tank, light vehicule, infantry]
- crew : number of infantry need to drive the vehicule 
- passager : number of infantry hosted
- class : can be : transport vehicule, light armored , medium armored, heavy armored

defense:

A defense is special unit which can move from the base.

- health : points
- armor : equilvalent in mm of steel
- damage : number of points removed to the health
- penetration : equivalent in mm of steel penetrated
- shot per round : number of shot done in a round of simulation
- ammo needed : per travel, number of munition needed
- accuracy : chance to hit target par shot
- target priority : give a priority list of unit targeted by the unit. For example, bazooka unit could have this list : [tank, light vehicule, infantry]
- class : infantry, light armored , medium armored, heavy armored

Technologies
============

barack:

- speed : improve the speed of each unit 
- armor : increase the armor of each unit
- damage : increase the damage of weapon 
- penetration : increase the paenetration of weapon
- cargo : increase the backpack's room 

vehicule warehouse:

- speed : improve the speed of each unit 
- armor : increase the armor of each unit
- damage : increase the damage of weapon 
- penetration : increase the paenetration of weapon
- cargo : increase the backpack's room 
- consumption : decrease the consumption
- ammo optimisation : decrease the need of ammunition

trading post:

- scaverage : increase the change to find blueprint

HQ:
**needed ?**

Data structure
==============

Player
------

- player_id : unique integer key 
- email : unique string
- password : string; should store the hash !
- nickname : unique string
- session_id : hash, used as a tocken


Base
----

- player_id : external key
- building_trading_post : integer
- building_weapon_factory : integer
- building_vehicule_warehouse : integer
- building_barack : integer
- building_hq : integer
- ressource_supply : integer
- ressource_ammo : integer
- ressource_gasoline : integer
- x : integer
- y : integer


Technologies
------------

- player_id : external key
- techno_infantry_speed : integer
- techno_infantry_armor : integer
- techno_infantry_damage : integer
- techno_infantry_penetration : integer
- techno_infantry_cargo : integer
- techno_vehicule_speed : integer
- techno_vehicule_armor : integer
- techno_vehicule_damage : integer
- techno_vehicule_penetration : integer
- techno_vehicule_cargo : integer
- techno_vehicule_consumption : integer
- techno_vehicule_ammo : integer
- techno_trade_blueprint : integer


Blueprint 
---------

- player_id : external key
- blueprint_id : integer


Building
--------

- player_id : external key
- building_type : integer; 1 for unit, 2 for building, 3 for technologie 
- blueprint_id : integer; reference to the blueprint owned by the player_id (to be assert), zero otherwise 
- building_id : integer, reference to the  building, zero otherwise 
- techno_id : integer, reference to the technologie, zero otherwise
- final_timestamp : integer (long ?), timstamp 

Travel 
------

- travel_id : integer primary key 
- player_id : external key
- target_id : external key to another player id, zero if not a player targeted
- final_timestamp : integer (long ?), timstamp 
- type : integer; 1 - attack, 2 - exploration, 3 - transport
- direction : bool
- ressource_supply : integer
- ressource_ammo : integer
- ressource_gasoline : integer


Unit 
----

- player_id : external key
- blueprint_id : integer; reference to the blueprint owned by the player_id
- number : integer; how many unit is owned 
- type : integer; 1 for infantry, 2 for vehicule, 3 for defense
- travel_id: reference to the travel, zero if in a base 
- base_id: reference of the base when not traveling. travel_id xor base_id must be valid 
