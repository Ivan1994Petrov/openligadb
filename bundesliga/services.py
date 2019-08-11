import requests


def get_upcoming_matches(year):
    # get_basics_match_info - get all home teams, away teams and dates and return list
    def get_basics_match_info(m):
        home_team = matches[m]['Team1']['TeamName']
        away_team = matches[m]['Team2']['TeamName']
        date = matches[m]['MatchDateTime']

        return [home_team, away_team, date]

    # class WinLossRatio store all wins, losses and draws for specific team
    class WinLossRatio:
        def __init__(self, win=0, loss=0, draw=0):
            self.win = win
            self.loss = loss
            self.draw = draw

        def __str__(self):
            return f'win - {self.win}, loss - {self.loss}, draw - {self.draw}'

    # get json from url
    url = f'https://www.openligadb.de/api/getmatchdata/bl1/{year}/'
    r = requests.get(url)
    matches = r.json()

    # objects for holding final result
    all_matches = {}
    all_upcoming_maches = {}
    all_teams_ratio = {}

    # loop for all matches to extract information
    for m in range(len(matches)):
        # get matche for the season
        all_matches[m] = get_basics_match_info(m)
        # if some match have PointsTeam1, this means the match is over
        try:
            # get goals for match
            home_goals = matches[m]['MatchResults'][0]['PointsTeam1']
            away_goals = matches[m]['MatchResults'][0]['PointsTeam2']

            # get the names of the teams
            basic_info_for_match = get_basics_match_info(m)
            home_team = basic_info_for_match[0]
            away_team = basic_info_for_match[1]

            # check if the team is in the dict - all_teams_ratio
            if home_team in all_teams_ratio or away_team in all_teams_ratio:
                if home_goals > away_goals:
                    all_teams_ratio[home_team].win += 1
                    all_teams_ratio[away_team].loss += 1
                elif away_goals > home_goals:
                    all_teams_ratio[home_team].loss += 1
                    all_teams_ratio[away_team].win += 1
                else:
                    all_teams_ratio[home_team].draw += 1
                    all_teams_ratio[away_team].draw += 1

            else:
                # team is not in the dict:
                # check if the result is H/A/D

                if home_goals > away_goals:

                    all_teams_ratio[home_team] = WinLossRatio(win=1)
                    all_teams_ratio[away_team] = WinLossRatio(loss=1)
                elif away_goals > home_goals:

                    all_teams_ratio[home_team] = WinLossRatio(loss=1)
                    all_teams_ratio[away_team] = WinLossRatio(win=1)

                else:
                    all_teams_ratio[home_team] = WinLossRatio(draw=1)
                    all_teams_ratio[away_team] = WinLossRatio(draw=1)


        except:
            all_upcoming_maches[m] = get_basics_match_info(m)

    return {
        'all_matches': all_matches,
        'all_upcoming_maches': all_upcoming_maches,
        'all_teams_ratio': all_teams_ratio,
    }
