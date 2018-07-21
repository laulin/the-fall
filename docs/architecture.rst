Architecture
~~~~~~~~~~~~

**This is a draft document. As a proposal, it can be changed and your contribution is welcome !**

game play 
=========

parameters
----------

Those parameters are interessing for the fight modeling.

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
- class : can be : transport vehicule, light armored vehicule, medium armored vehicule, heavy armored vehicule

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
- password : string
- nickname : unique string 


Base
----

- base_id : unique integer key 
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