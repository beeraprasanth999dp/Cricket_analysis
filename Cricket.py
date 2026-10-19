def TeamRegistration():
    while True:
        try:
    
            Number_teams=int(input("Enter  number of teams:"))  
            break
        except ValueError:
            print("Please Enter a valid integer") 
    teams=[]
    
    while Number_teams < 2:
        print("Enter at least 2 teams")
        try:
            Number_teams=int(input("Enter number of teams:"))
        except ValueError:
            print("please enter valid integer")
    while len(teams)<Number_teams:
        name=input("Enter Team Name:").strip()
        if name=="":
            print("Team cannot be empty")
            continue
        for team in teams:
            if name.lower() == team.lower():
                print("Team is already exist")
                break
        else:
            teams.append(name)
    return teams
def Match_deatils(teams):
    
    team1=input("Enter Team Name 1:")
    team2=input("Enter Team Name 2:")
    
   
    if team1 not in teams or team2 not in teams:
            print("Team not found")
            return None
    if team1==team2:
            print("Team Can't play with it's self")
            return None
    try:
        firstTeam_runs=int(input("Enter runs for team1:"))
        firstTeam_wickets=int(input("Enter wickets lost team1:"))
        firstTeam_overs=int(input("Enter first team overs faced team1:"))
        balls1=int(input("Enter remainig balls"))
        
        secondTeam_runs=int(input("Enter runs for team2:"))
        secondTeam_wickets=int(input("Enter wickets lost team2:"))
        secondTeam_overs=int(input("Enter second team overs faced team2:")) 
        balls2=int(input("Enter Reaminig balls"))
    except ValueError:
        print("please enter valid integers only") 
        return None
         
    if firstTeam_wickets<0 or secondTeam_wickets<0 or firstTeam_wickets>10 or secondTeam_wickets>10:
        print("Wickets must be 0 to 10:")
        return None
    if firstTeam_overs<0 or firstTeam_overs>20 or secondTeam_overs<0 or secondTeam_overs>20:
        print("Overs between 0,20")
        return None
    if firstTeam_runs<0 or secondTeam_runs<0:
        print("Invalid runs")
        return None
    elif balls1<0 or balls1>5 or balls2<0 or balls2>5:
        print("Balls range between 0,5")
        return None
    elif(firstTeam_overs==0 and balls1 ==0 or secondTeam_overs==0 and balls2==0):
        print("Enter Atleast one legal ball for each innings")
        return None
    else:
         balls1=firstTeam_overs*6+balls1
         balls2=secondTeam_overs*6+balls2
    return team1,team2,firstTeam_runs,firstTeam_wickets,balls1,secondTeam_runs,secondTeam_wickets,balls2
def Team_stats(teams):
    stats={}
    for team in teams:
        stats[team]={
            "played":0,
            "won":0,
           "lost":0,
            "tied":0,
            "points":0,
            "runs_scored":0,
            "runs_given":0,
            "overs_faces":0,
            "overs_bowled":0
             }
    return stats
def update_stats(board,stats):
    team1,team2,firstTeam_runs,firstTeam_wickets,balls1,secondTeam_runs,secondTeam_wickets,balls2=board
    balls1=adjusted_balls(firstTeam_wickets,balls1)
    balls2=adjusted_balls(secondTeam_wickets,balls2)

    stats[team1]["played"]+=1
    stats[team2]["played"]+=1

    stats[team1]["runs_scored"]+=firstTeam_runs
    stats[team1]["runs_given"]+=secondTeam_runs
    stats[team2]["runs_scored"]+=secondTeam_runs
    stats[team2]["runs_given"]+=firstTeam_runs

    stats[team1]["overs_faces"]+=balls1
    stats[team1]["overs_bowled"]+=balls2
    stats[team2]["overs_faces"]+=balls2
    stats[team2]["overs_bowled"]+=balls1

    if firstTeam_runs>secondTeam_runs:
        stats[team1]["won"]+=1
        stats[team1]["points"]+=2
        stats[team2]["lost"]+=1
    elif secondTeam_runs>firstTeam_runs:
        stats[team2]["won"]+=1
        stats[team2]["points"]+=2
        stats[team1]["lost"]+=1
    else:
        stats[team1]["tied"]+=1
        stats[team2]["tied"]+=1
        stats[team1]["points"]+=1
        stats[team2]["points"]+=1
def adjusted_balls(wickets,balls):
    if wickets==10 and balls<120:
        balls=120
    return balls
def caluculate_NRR(stats):
    for team in stats:
        balls_faced=stats[team]["overs_faces"]
        balls_bowled=stats[team]["overs_bowled"]
        if balls_faced>0 and balls_bowled>0:
            runs_rate_scored=stats[team]["runs_scored"]*6/balls_faced
            runs_rate_given=stats[team]["runs_given"]*6/balls_bowled
            stats[team]["NRR"]=runs_rate_scored-runs_rate_given
        else:
            stats[team]["NRR"]=0

def Display_points_table(stats):
    teams=list(stats)
    for i in range(len(teams)):
        for j in range(i+1,len(teams)):
            if stats[teams[j]]["points"]>stats[teams[i]]["points"] or stats[teams[j]]["points"]==stats[teams[i]]["points"] and stats[teams[j]]["NRR"]>stats[teams[i]]["NRR"]:
                teams[i],teams[j]=teams[j],teams[i]
    print("\nCRICKET TOURNAMENT POINTS TABLE")
    print("-"*80)
    print(f"{'Team':<15}{'MP':<5}{'Won':<5}{'Lost':<5}{'Tied':<5}{'Points':<8}{'NRR':<8}")
    print("-"*80)
    for team in teams:
        print(f"{team:<15}{stats[team]['played']:<5}{stats[team]['won']:<5}{stats[team]['lost']:<5}{stats[team]['tied']:<5}{stats[team]['points']:<8}{stats[team]['NRR']:<8.3f}")
    print("-"*80)
    
          
teams=TeamRegistration()
stats=Team_stats(teams)
match_number=1
total_matches=len(teams)*(len(teams)-1)
while match_number<=total_matches:
    print("\nMatch Number:",match_number)
    board=Match_deatils(teams)
    if board is not None:
        update_stats(board,stats)
        match_number+=1
    else:
        print("Enter the match details again")
        
caluculate_NRR(stats)
print(Display_points_table(stats))


       