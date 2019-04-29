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


