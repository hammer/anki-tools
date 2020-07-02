import parse
import pandas as pd

# Grab decks.csv from Duolingo Drive-Thru https://drive-thru.duolingo.com
path_to_decks = ''
decks = pd.read_csv(path_to_decks)

# Collect decks from different sources
npcr_decks = decks.loc[decks['name'].str.startswith('NPCR')]
mc_decks = decks.loc[decks['name'].str.startswith('Mandarin Companion')]
duo_decks = decks.loc[decks['name'].str.startswith('Duolingo')]

# TODO(hammer): iterate through all of the decks
deck = npcr_decks.iloc[0]
outfile = deck.loc['name'] + '.csv'
cards_str = deck.loc['cards']

parse_pattern = '### Card {}\nFront\n* {characters}\n\nBack\n* {english}\n* {pinyin}\n\n'
cards_parsed = parse.findall(parse_pattern, cards_str)
cards_df = pd.DataFrame([note.named for note in list(cards_parsed)])
cards_df.to_csv(outfile, header=False, index=False, sep='|', encoding='utf-8')
