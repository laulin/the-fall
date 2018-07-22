Architecture
~~~~~~~~~~~~

**This is a draft document. As a proposal, it can be changed and your contribution is welcome !**

game play 
=========

parameters
----------

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

technologies
------------

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
