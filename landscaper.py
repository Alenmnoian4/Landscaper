game = {"tool": 0, "money": 0}

tools = [
    {"name": "Teeth", "profit": 1, "cost": 0},
    {"name": "Rusty Scissors", "profit": 5, "cost": 5},
    {"name": "Old-Timey Push Lawnmower", "profit": 50, "cost": 25},
    {"name": "Fancy Battery Powered Lawnmower", "profit": 100, "cost": 250},
    {"name": "Team of Starving Students", "profit": 250, "cost": 500}
]

def mow_lawn():
    tool = tools[game["tool"]]
    print(f"You clean a pool with your {tool['name']} and make ${tool['profit']}")
    game["money"] += tool["profit"]
    
    
def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have ${game['money']} and are using a {tool['name']}")
    
def upgrade():
    if (game["tool"]) >= len(tools) - 1:
        print("No more upgrades available")
        return 0
    
    next_tool = tools[game["tool"]+1]
    if (next_tool == None):
        print("There are no more tools")
        return 0
    if (game["money"] < next_tool["cost"]):
        print("Not enough to buy tool")
        return 0
    print("You are upgrading your tool")
    game["money"] -= next_tool["cost"]
    game["tool"] += 1

def win_check():
    
    if(game["money"] >= 1000):
        print("You Win")
        return True
    return False
    
    
while(True):
   
    user_choice = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [4] Quit")

    if(user_choice == "1"):
        mow_lawn()
    if(user_choice == "2"):
        check_stats()
    if(user_choice == "3"):
        upgrade()
    if(user_choice == "4"):
        print("You quit the game")
        break
    if(win_check()):
        break