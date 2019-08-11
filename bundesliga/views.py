from django.shortcuts import render

from .services import get_upcoming_matches


# Create your views here.

def bundeslig_detail(request, year):
    return_from_all_upcoming_maches = get_upcoming_matches(year)

    SELECTORS = {
        'all-matches-teams': return_from_all_upcoming_maches['all_matches'].values(),
        'all-upcoming-maches-teams': return_from_all_upcoming_maches['all_upcoming_maches'].values(),
        'all_teams_ratio': return_from_all_upcoming_maches['all_teams_ratio']
    }

    def get_dict_values_for_info_for_all_matches(arr):
        all_matches_home_teams = []
        all_matches_away_teams = []
        all_matches_date = []

        for m in list(arr):
            all_matches_home_teams.append(m[0])
            all_matches_away_teams.append(m[1])
            all_matches_date.append(m[2])

        return zip(all_matches_home_teams, all_matches_away_teams, all_matches_date)

    def get_dict_values_for_info_for_all_upcoming_matches(arr):
        all_matches_home_teams = []
        all_matches_away_teams = []
        all_matches_date = []
        for m in list(arr):
            all_matches_home_teams.append(m[0])
            all_matches_away_teams.append(m[1])
            all_matches_date.append(m[2])

        return zip(all_matches_home_teams, all_matches_away_teams, all_matches_date)

    def get_dict_info_for_win_loss(dictionary):
        all_teams = []
        all_wins = []
        all_losses = []
        all_drows = []

        for key in dictionary.keys():
            all_teams.append(key)
            all_wins.append(dictionary[key].win)
            all_losses.append(dictionary[key].loss)
            all_drows.append(dictionary[key].draw)
        return zip(all_teams, all_wins, all_losses, all_drows)

    return render(request, 'home_page.html', {
        'all_teams': list(get_dict_values_for_info_for_all_matches(SELECTORS['all-matches-teams'])),
        'all_upcoming_maches': list(get_dict_values_for_info_for_all_upcoming_matches(SELECTORS['all-upcoming-maches-teams'])),
        'all_teams_ratio': list(get_dict_info_for_win_loss(SELECTORS['all_teams_ratio']))
    })


def current_season(request):
    year = 2019

    return bundeslig_detail(request, year)


def season_2018(request):
    year = 2018

    return bundeslig_detail(request, year)


def season_2017(request):
    year = 2017

    return bundeslig_detail(request, year)


def season_2016(request):
    year = 2016

    return bundeslig_detail(request, year)


def season_2015(request):
    year = 2015

    return bundeslig_detail(request, year)
