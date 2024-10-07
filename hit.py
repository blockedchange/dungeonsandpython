from roll_dice import *

def hit_chance():
	dice = roll_dice()
	if dice == 1:
		attackresult = "Missed"
	elif dice == 2:
		attackresult = "Blocked"
	else:
		attackresult = "Hit"
	return attackresult


def critical_hit():
	dice1 = roll_dice()
	dice2 = roll_dice()
	if dice1 == dice2:
		iscrit = "true"
	else:
		iscrit = "false"
	return iscrit


def hit_damage(level,iscrit):
	if iscrit == "true":
		damage = (level + 1) * roll_dice()
		return damage
	else:
		damage = level * roll_dice()
		return damage


def attack(level):
	didhit = hit_chance()
	if didhit == "Hit":
		iscriticalhit = critical_hit()
		attackdamage = hit_damage(level,iscriticalhit)
		if iscriticalhit == "true":
			attackresults = ["Critical Hit", attackdamage]
			return attackresults
		else:
			attackresults = ["Hit", attackdamage]
			return attackresults
	else:
		attackresults = [didhit, 0]
		return attackresults