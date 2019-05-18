from collections import defaultdict, namedtuple, Counter, deque
import csv
from urllib.request import urlretrieve

MOVIE_DATA = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

#make a defaultict of movies per director (keys = directors, values = list of movies)
movies_csv = 'days/04-06-collections/movies.csv'
urlretrieve(MOVIE_DATA, movies_csv)

#namedtuple to describe ech movie
Movie = namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movies_csv):
    """Extracts all movies from csv and stores them in a dictionary
       where keys are directors, and values is a list of movies (named tuples)"""
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            
            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)
    
    return directors

def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    pass


def _calc_mean(movies):
    '''Helper method to calculate mean of list of Movie namedtuples'''
    pass


def print_results(directors):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    fmt_director_entry = '{counter}. {director:<52} {avg}'
    fmt_movie_entry = '{year}] {title:<50} {score}'
    sep_line = '-' * 60


def main():
    directors = get_movies_by_director()
    
    cnt = Counter()
    for director, movies in directors.items():
        cnt[director] += len(movies)
    cnt.most_common(5)
    #directors = get_average_scores(directors)
    #print_results(directors)


if __name__ == '__main__':
    main()