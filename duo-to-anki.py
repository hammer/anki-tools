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
parse_pattern = '### Card {}\nFront\n* {characters}\n\nBack\n* {english}\n* {pinyin:S}'
outfile = 'blah.csv'
cards_str = npcr_decks.iloc[0].loc['cards']
cards_parsed = parse.findall(parse_pattern, cards)
cards_df = pd.DataFrame([note.named for note in list(cards_parsed)])
cards_df.to_csv(outfile, sep='|', encoding='utf-8')
