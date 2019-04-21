import glob
import json
import pickle
import csv
import numpy as np
import pandas as pd
import argparse


def numReview(inst):
    return inst['reviews']['num_reviews']
def numYelp(inst):
    return inst['reviews']['num_Yelp']
def numFS(inst):
    return inst['reviews']['num_FS']
def quality_review(inst):
    return inst['reviews']['overall']
def price(inst):
    return inst['price']
def rating(inst):
    return inst['rating']

sortRev = {
    'num_review': numReview,
    'num_yelp_review': numYelp,
    'num_fs_revies': numFS,
    'quality_from_review': quality_review
}

sortScore = {
    'price_tier': price,
    'ratings': rating
}

choices = list(sortRev.keys()) + list(sortScore.keys())

parser = argparse.ArgumentParser(description='Input Param')
parser.add_argument('-e', '--exitID', required=True)
parser.add_argument('-l', '--limit', required=True)
parser.add_argument('-s', '--sortBy', required=True, choices=choices)
# parser.add_argument('-d', '--descending', required=True)

args = parser.parse_args()

queryID = int(args.exitID)
lmt = int(args.limit)
sortField = args.sortBy
# desc = args.descending


# queryID = 35189
# sortField = 'num_review'
desc = True

#-------------------------

def score2quality(score):
    if score < 2:
        _quality = 'poor'
    elif score < 2.5:
        _quality = 'not good'
    elif score < 3.5:
        _quality = 'fair'
    elif score < 4:
        _quality = 'good'
    else:
        _quality = 'excellent'
    return _quality

          
def verbose(rev_out, score_out, rank):
    _rating = score_out['rating']
    _price = score_out['price']
    _address = rev_out['address']
    _phone = rev_out['phone']
    _ova_reviews = rev_out['reviews']['overall']
    _aspects = rev_out['reviews']['aspects']
    _num_rev = rev_out['reviews']['num_reviews']
    _num_yelp = rev_out['reviews']['num_Yelp']
    _num_fs = rev_out['reviews']['num_FS']
    
    
    print('\n')
    print('-------------------- Venue', rank, '-------------------------')
    print('Address:', _address)
    print('Phone Number:', _phone)
    print('------------------')
    print('Ratings:', _rating)
    print('Price Tier:', _price)
    print('------------------')
    print('The venue has in total', _num_rev, 'reviews.')
    print(_num_yelp, 'of them are from the Yelp, and', _num_fs, 'of them are from the FourSquare.')
    print('------------------')
    print('From the reviews, generally people think the place is', score2quality(_ova_reviews))
    for _aspect in _aspects:
        if score2quality(_aspects[_aspect]) != 'fair':
            print('The', _aspect, 'of this place is', score2quality(_aspects[_aspect]))
    print('------------------------------------------------------')
    print('\n')
    
    return 




trust_df = pd.read_pickle('trust_scores_df')
iE_group = pd.read_pickle('rest_group2_plot')
aggReviews = pickle.load(open('out/aggregated_reviews.pkl', 'rb'))
iExit_out = pickle.load(open('out/iExit_agg.pkl', 'rb'))


exitKeys = iE_group['ls_exit_id_set']
venues = iE_group['ls_id_set']
exitID2Venue = {}
for i in range(len(exitKeys)):
    ExitIDs = exitKeys[i]
    VenueIDs = venues[i]
    for eid in ExitIDs:
        exitID2Venue[eid] = VenueIDs
        
        
queryScores = {}
for i in range(len(trust_df)):
    queryScores[int(trust_df['iExit_IDs'][i])] = {
        'price': trust_df['prices_merge'][i],
        'rating': trust_df['ratings_merge'][i]
    }

venuesReview = [iExit_out[vid] for vid in exitID2Venue[queryID]]
venuesScore = [queryScores[vid] for vid in exitID2Venue[queryID]]


if sortField in sortRev:
    venuesReview.sort(key=sortRev[sortField], reverse=True)
    i = 1
    for venue in venuesReview:
        _id = int(venue['id'])
        verbose(venue, queryScores[_id], i)
        i += 1
        if i >= lmt:
            break
elif sortField in sortScore:
    venuesScore.sort(key=sortScore[sortField], reverse=True)
    i = 1
    for venue in venuesScore:
        _id = int(venue['id'])
        verbose(iExit_out[_id], venue, i)
        i += 1
        if i >= lmt:
            break