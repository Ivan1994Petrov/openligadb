from django.shortcuts import render
from django.http import HttpResponse
import time

from .services import get_upcoming_matches


# Create your views here.


def bundeslig_detail(request):
    return_from_all_upcoming_maches = get_upcoming_matches()
    SELECTORS = {
        'all-matches-teams': return_from_all_upcoming_maches['all_matches'].values(),
        'all-upcoming-maches-teams': return_from_all_upcoming_maches['all_upcoming_maches'].values()

    }

    def get_zipped_info_for_all_matches(arr):
        all_matches_home_teams = []
        all_matches_away_teams = []
        all_matches_date = []
        for m in list(arr):
            all_matches_home_teams.append(m[0])
            all_matches_away_teams.append(m[1])
            all_matches_date.append(m[2])

        return zip(all_matches_home_teams, all_matches_away_teams, all_matches_date)

    def get_zipped_info_for_all_upcoming_matches(arr):
        all_matches_home_teams = []
        all_matches_away_teams = []
        all_matches_date = []
        for m in list(arr):
            all_matches_home_teams.append(m[0])
            all_matches_away_teams.append(m[1])
            all_matches_date.append(m[2])

        return zip(all_matches_home_teams, all_matches_away_teams, all_matches_date)

    print(list(get_zipped_info_for_all_upcoming_matches(SELECTORS['all-upcoming-maches-teams'])))
    return render(request, 'home_page.html', {
        'all_teams': get_zipped_info_for_all_matches(SELECTORS['all-matches-teams']),
        'all_upcoming_maches': get_zipped_info_for_all_upcoming_matches(SELECTORS['all-upcoming-maches-teams'])
    })
