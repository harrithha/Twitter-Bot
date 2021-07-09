import requests
from bs4 import BeautifulSoup
init = 0
    
def live_scores():
    final_print = []
    final_print += ['-----Live Scores-----\n']
    score_check = 0
    

    url = "https://www.espncricinfo.com/live-cricket-score"
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    live_check = soup.find_all("div", class_="match-info match-info-FIXTURES")


    for i in live_check:
        statusRed = 0
        for ik in i.children:
            if ik['class'] == ['status', 'red'] and ik.get_text() == 'live':
                statusRed += 1
        if statusRed == 1:
            teams_parent = i.find("div", class_="teams")
            score = []
            team_names = []
            i=0
            check_one = ''
            check_two = ''
            flag_one = 0
            flag_two = 0

            teams = teams_parent.find_all("div", class_="team")
            for team in teams:
                score_info = team.find("div", class_="score-detail")
                if score_info and i == 0:
                    score_value_A = team.find("span", class_="score").get_text().split("/")
                   # print(score_value_A[0])
                    score_check = score_value_A[0]
                    score.append(score_info.get_text())
                    check_one = 'Printed A Score'
                    flag_one = 1
                elif i == 0 and flag_one == 0 :
                    check_one = 'Did Not Print A Score'
                if score_info and i == 1:
                    score.append(score_info.get_text())
                    check_two = 'Printed B Score'
                    flag_two = 1
                elif i == 0 and flag_two == 0 :
                    check_two = 'Did Not Print B Score'
                team_Detail = team.find("div", class_="name-detail")
                if team_Detail:
                    team_names.append(team_Detail.get_text())
                    i+=1
            #print(check_one)
            #print(check_two)
            if len(team_names) == 2 and len(score) == 2:
               final_print += (team_names[0], score[0],  'Vs', team_names[1], score[1],"\n")
            elif len(team_names) == 2 and check_one == 'Printed A Score':
                final_print += (team_names[0], score[0],  'Vs', team_names[1],"\n")
            elif len(team_names) == 2 and check_two == 'Printed B Score':
                final_print += (team_names[0],  'Vs', team_names[1], score[0], "\n")
            else:
                print('Multiple teams Found For A Match')
    return(' '.join(final_print))

