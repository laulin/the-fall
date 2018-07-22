Architecture
~~~~~~~~~~~~

**This is a draft document. As a proposal, it can be changed and your contribution is welcome !**

ID everywhere
=============

In the following document, we use XXXX_id. In one hand, their are player_id, travel_id, make_id which are typically 
incremental unique integer without signification. In other hand, building, technlogy, vehicule (and so on) have 
an ID. To make it easy, let's use a convention :

- range 0-99 : building (warehouse, trade post, etc.)
- range 100-199 : technology 
- range 200-299 : infantery
- range 300-399 : vehicule 
- range 400-499 : defense 

We should call them *object_id*

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


building
--------

parameters:
- a session token
- a player_id
- object_id 
- source object_id (for infantery only)
- number (for unit only)

do:
- remove ressources 
- add object_id to the building list

conditions:
- player_id exists
- session_id of the player is valid
- object_id is valid 
- ressources are available
- technologies/buildings are compliance
- [technology/building only] the building is not in progress


get building list
-----------------

parameters:
- a session token
- a player_id

conditions:
- player_id exists
- session_id of the player is valid

return:
- list of make_id, building_type, object_id, start_timestamp, end_timestamp

cancel building 
---------------

parameters:
- a session token
- a player_id
- make_id 

do:
- add ressources 
- remove from the building list

conditions:
- player_id exists
- session_id of the player is valid

attack
------

parameters:
- a session token
- a player_id
- a target_id 
- a list of (object_id, number)

do:
- remove ressources
- add row in travel table 
- split entry in unit table and set travel_id

conditions:
- player_id exists
- session_id of the player is valid
- ressources are available
- target_id exists
- if vehicules are used, crew must be all present
- units must be available
- unit can be a defense

list travel
-----------

parameters:
- a session token
- a player_id

conditions:
- player_id exists
- session_id of the player is valid

return:
- list of:
    - travel_id
    - start/end timestamp
    - list of (object_id, number)
    - target_id
    - ressources

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
- object_id : integer


Building
--------

- make_id : unique integer key
- player_id : external key
- object_id : integer
- start_timestamp : integer (long ?), timstamp 
- end_timestamp : integer (long ?), timstamp 

Travel 
------

- travel_id : integer primary key 
- player_id : external key
- target_id : external key to another player id, zero if not a player targeted
- start_timestamp : integer (long ?), timstamp 
- end_timestamp : integer (long ?), timstamp 
- type : integer; 1 - attack, 2 - exploration, 3 - transport
- direction : bool
- ressource_supply : integer
- ressource_ammo : integer
- ressource_gasoline : integer


Unit 
----

- player_id : external key
- object_id : integer; reference to the blueprint owned by the player_id
- number : integer; how many unit is owned 
- travel_id: reference to the travel, zero if in a base 
- base_id: reference of the base when not traveling. travel_id xor base_id must be valid 
