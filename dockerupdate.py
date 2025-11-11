from dotenv import dotenv_values
import os
import subprocess as sub

def LoadDotEnvs() -> dict:
	env_vars = dotenv_values(".env")
	return env_vars

def StopJellyDock(commands: dict):
	sub.run(commands["DOCKER_STOP"].split())

def DeleteJellyDock(commands: dict):
	sub.run(commands["DOCKER_REMOVE"].split())

def PullJellyDock(commands: dict):
	sub.run(commands["DOCKER_PULL"].split())

def RunJellyDock(commands: dict):
	sub.run(commands["DOCKER_RUN"].split())

def GetCurrJellyVersionDock(commands: dict) -> str:
	res = sub.run(commands["DOCKER_VERSION"], shell=True,  capture_output=True, text=True)
	return res.stdout.strip()

def GetLatestDockHubVersion(commands: dict) -> str:
	res = sub.run(commands["DOCKERHUB_VERSION"], shell=True, capture_output=True, text=True)
	return res.stdout.strip()

def main():
	print("main")
	commands = LoadDotEnvs()
	curr_ver = GetCurrJellyVersionDock(commands)
	hub_ver = GetLatestDockHubVersion(commands)
	if curr_ver != hub_ver:
		StopJellyDock(commands)
		DeleteJellyDock(commands)
		PullJellyDock(commands)
		RunJellyDock(commands)
	else:
		print(f"Version is up-to-date!\n(CurrentV: {curr_ver} || HubV: {hub_ver})")

if __name__ == "__main__":
	main()
