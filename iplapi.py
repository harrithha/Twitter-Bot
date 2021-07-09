import requests
from bs4 import BeautifulSoup

def work():
    url = "https://www.espncricinfo.com/live-cricket-score"
    r = requests.get(url)
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    live_check = soup.find_all("div", class_="match-info match-info-FIXTURES")

    print('----Live Scores----')

    for i in live_check:
        statusRed = 0
        for ik in i.children:
            if ik['class'] == ['status', 'red'] and ik.get_text() == 'live':
                statusRed += 1
        if statusRed == 1:
            teams_parent = i.find("div", class_="teams")
            score = ""
            team_names = []

            teams = teams_parent.find_all("div", class_="team")
            for team in teams:
                score_info = team.find("div", class_="score-detail")
                if score_info and score == "":
                    score = score_info.get_text()
                team_Detail = team.find("div", class_="name-detail")
                if team_Detail:
                    team_names.append(team_Detail.get_text())
            if len(team_names) == 2:
               print(team_names[0], 'Vs', team_names[1], score)
            else:
                print('Multiple teams Found For A Match')

print("Hi")
