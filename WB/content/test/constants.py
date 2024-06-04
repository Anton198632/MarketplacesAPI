from environs import Env

env = Env()
env.read_env()

WB_API_KEY = env("WB_API_KEY")
