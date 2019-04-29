# Data_Fusion_Social

## rest_group2_plot.pickle:
'ls_exit_id_set': a set of exit IDs from iExit. These exits are geographically close.

'ls_id_set': a set of restaurant IDs from iExit. These restaurants are geographically close.

For each reading in rest_group2_plot.pickle, a 'ls_exit_id_set' and a 'ls_id_set' are geographically close.

## A preview of merged price tiers and ratings are in the bottom of 'Seminar_Fusion_Project.ipynb'

## Merged data is saved in 'trust_scores_df.pickle'

## 'out/aggregated_reviews.pkl' the aggregated reviews

## query.py: query restaurants by exit:

python query.py -e [EXIT_ID] -l [NUMBER_OF_VENUE_RETURN] -s [SORT_BY]

example:  python3 query.py -e 58544 -l 5 -s quality_from_review
and it gives:

-------------------- Venue 1 : Subway -------------------------
Address: 3461 Horizon Blvd, Trevose, PA 19053
Phone Number: 1-215-355-0600
------------------
Ratings: 4.85
Price Tier: 1.0
------------------
The venue has in total 3 reviews.
2 of them are from the Yelp, and 1 of them are from the FourSquare.
------------------
From the reviews, generally people think the place is fair
------------------------------------------------------




-------------------- Venue 2 : Chick-Fil-A -------------------------
Address: 307 Neshaminy Mall, Bensalem, PA 19020
Phone Number: 1-215-364-9155
------------------
Ratings: 7.425449515905948
Price Tier: 1.0
------------------
The venue has in total 11 reviews.
3 of them are from the Yelp, and 8 of them are from the FourSquare.
------------------
From the reviews, generally people think the place is fair
The food of this place is excellent
The deal of this place is excellent
------------------------------------------------------




-------------------- Venue 3 : Burger King -------------------------
Address: 1035 Bustleton Pike, Feasterville Trevose, PA 19053-7608
Phone Number: 1-215-357-5670
------------------
Ratings: 5.311134163208851
Price Tier: 1.0
------------------
The venue has in total 12 reviews.
3 of them are from the Yelp, and 9 of them are from the FourSquare.
------------------
From the reviews, generally people think the place is fair
The service of this place is not good
The ambience of this place is good
------------------------------------------------------




-------------------- Venue 4 : Chick-Fil-A -------------------------
Address: 3621 Horizon Blvd, Trevose, PA 19053
Phone Number: 1-215-355-3500
------------------
Ratings: 8.701273667000684
Price Tier: 2.0
------------------
The venue has in total 23 reviews.
3 of them are from the Yelp, and 20 of them are from the FourSquare.
------------------
From the reviews, generally people think the place is fair
The service of this place is good
The ambience of this place is good
The food of this place is good
------------------------------------------------------
