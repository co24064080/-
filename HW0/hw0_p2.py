# coding: utf-8
#build dictionary by movie data

def build_dictionary(filename):
    md = {}
    with open(filename) as f:
        f.readline()   # skip the first line

        for line in f:
            line = line[:len(line)-1]   # remove '\n'
            data = line.split(",")

            movie_title = data[1]
            movie_genres = data[2].split("|")
            movie_director = data[3]

            movie_actors = data[4].split("|")
            for i in range(len(movie_actors)):
                movie_actors[i] = movie_actors[i].strip() # remove whitespace

            movie_year = data[5]
            movie_rating = data[7]
            movie_revenue = data[9]

            all_data = [movie_genres, movie_director, movie_actors, movie_year, movie_rating, movie_revenue]
            md[movie_title] = all_data
    return md

moviedict = build_dictionary("IMDB-Movie-Data.csv")
#Q1 Top-3 movies with the highest ratings in 2016?

#find topk rated movie in year
def topk_rated_movie_inyear(md, k, year):
    movie2rating = {}
    for m in md:
        if md[m][3] != year:
            continue
        movie2rating[m] = float(md[m][4])
        
    topkhighmovie = []
    topkhighscore = []
    for i in range(k):
        highest_score = 0
        highest_movie = ""
        for n in movie2rating:
            if n in topkhighmovie:
                continue
            score = movie2rating[n]
            if score > highest_score:
                highest_score = score
                highest_movie = n
                
        topkhighmovie.append(highest_movie)
        topkhighscore.append(highest_score)

    have_same_score = []
    highest_score = 0
    highest_movie = ""
    b = 0
    for m in movie2rating:
        if m in topkhighmovie:
            b += 1
            continue
        else:
            if int(movie2rating[m]) == topkhighmovie[-1]:
                have_same_score.append(m)
        b += 1
    
    topkhighmovie += have_same_score

    return topkhighmovie

topkmovies_2016 = topk_rated_movie_inyear(moviedict, 3, "2016")
print("Q1. Top-3 movies with the highest ratings in 2016 ? \nAns:\n ", topkmovies_2016)
#Q2 The actor generating the highest average revenue? 

#compute actor average revenue
def actor_avg_revenue(md, actor):
    actor_revenue = []
    for m in md:
        actors = md[m][2]
        if actor in actors and md[m][5] != "": # check missing revenue
            actor_revenue.append(float(md[m][5]))
    if len(actor_revenue) == 0:
        return 0    
    return round(sum(actor_revenue)/len(actor_revenue), 2)

#find topk actor average revenue v
def topk_actor_avg_revenue(md, k):
    actors = []
    for i in md:
        actor_in_movie = md[i][2]
        for j in actor_in_movie:
            if j in actors:
                continue
            actors.append(j)
                
    avg_revenue_actor = []
    avg_revenue = []
    for a in actors:
        avg_revenue_actor.append(a)
        avg_revenue.append(actor_avg_revenue(md, a))
        
    topk = []
    topk_revenue =[]
    for i in range(k):
        highest_avg_revenue = 0
        highest_actor = ""
        b = 0        
        for m in avg_revenue_actor:
            one_avg_revenue = float(avg_revenue[b])
            b += 1
            if m in topk:
                continue
            
            if one_avg_revenue > highest_avg_revenue:
                highest_avg_revenue = one_avg_revenue
                highest_actor = m
        topk.append(highest_actor)
        topk_revenue.append(highest_avg_revenue)

    have_same_revenue = []
    highest_revenue = 0
    highest_actor = ""
    b = 0
    for m in avg_revenue_actor:
        if m in topk:
            b += 1
            continue
        else:
            if float(avg_revenue[b]) == topk_revenue[-1]:
                have_same_revenue.append(m)
        b += 1
    
    topk += have_same_revenue        

    return (topk)




highest_avg_revenue_actor = topk_actor_avg_revenue(moviedict, 1)
print("Q2. The actor generating the highest average revenue?  \nAns:\n ", highest_avg_revenue_actor)
#Q3 The average rating of Emma Watson’s movies?

#compute actor average rating
def actor_avg_rating(md, actor):
    actor_rating = []
    for m in md:
        actors = md[m][2]
        if actor in actors and md[m][4] != "": # check missing rating
            actor_rating.append(float(md[m][4]))
    if len(actor_rating) == 0:
        return 0    
    return round(sum(actor_rating)/len(actor_rating), 2)


rating = actor_avg_rating(moviedict, "Emma Watson")
print("Q3. The average rating of Emma Watson’s movies?  \nAns:\n ", rating)
#Q4 Top-3 directors who collaborate with the most actors?

#find topk director collaborate with actors
def topk_director_with_actors(md, k):
    directors = []
    number_of_director_collaborate = []
    for m in md:
        director = md[m][1] 
        if director in directors:
            continue
        directors.append(director)
        director_had_collaborate = []        
        for n in md:
            actors = md[n][2]
            if md[n][1] != director:
                continue
            for a in actors:
                if a in director_had_collaborate:
                    continue
                director_had_collaborate.append(a)
        number_of_director_collaborate.append(len(director_had_collaborate))
                    
    topk = []
    topk_collaborate =[]
    for i in range(k):
        highest_number = 0
        highest_director = ""
        b = 0        
        for m in directors:
            one_director_collaborate = int(number_of_director_collaborate[b])
            b += 1
            if m in topk:
                continue
            if one_director_collaborate > highest_number:
                highest_number = one_director_collaborate
                highest_director = m
        topk.append(highest_director)
        topk_collaborate.append(highest_number)

    have_same_collaborate = []
    highest_number = 0
    highest_director = ""
    b = 0
    for m in directors:
        if m in topk:
            b += 1
            continue
        else:
            if int(number_of_director_collaborate[b]) == topk_collaborate[-1]:
                have_same_collaborate.append(m)
        b += 1
    
    topk += have_same_collaborate
    
    return (topk)


director = topk_director_with_actors(moviedict,3)
print("Q4. Top-3 directors who collaborate with the most actors ? \nAns:\n ", director)
#Q5 Top-2 actors playing in the most genres of movies?

#find topk actor playing genres
def topk_actor_playing_genres(md, k):
    actors = []
    number_of_playing_genres = []
    for m in md:
        one_movie_actors = md[m][2]
        actor_had_playing_genres = []               
        for p in one_movie_actors:
            if p in actors:
                continue
            actors.append(p) 
            for n in md:
                genres = md[n][0]
                if p not in md[n][2]:
                    continue
                for a in genres:
                    if a in actor_had_playing_genres:
                        continue
                    actor_had_playing_genres.append(a)
            number_of_playing_genres.append(len(actor_had_playing_genres))
                    
    topk = []
    topk_playing = []
    for i in range(k):
        highest_number = 0
        highest_actor = ""
        b = 0        
        for m in actors:
            one_actor_playing = int(number_of_playing_genres[b])
            b += 1
            if m in topk:
                continue
            
            if one_actor_playing > highest_number:
                highest_number = one_actor_playing
                highest_actor = m
        topk.append(highest_actor)
        topk_playing.append(highest_number)
        
    have_same_number = []
    highest_number = 0
    highest_actor = ""
    b = 0
    for m in actors:
        if m in topk:
            b += 1
            continue
        else:
            if int(number_of_playing_genres[b]) == topk_playing[-1]:
                have_same_number.append(m)
        b += 1
    
    topk += have_same_number
        
        
    return (topk)    

actor = topk_actor_playing_genres(moviedict,2)
print("Q5. Top-2 actors playing in the most genres of movies ? \nAns:\n  ", actor)
#Q6 Top-3 actors whose movies lead to the largest maximum gap of years?

#compute topk gap of years
def topk_gap_of_years(md,k) :
    actors = []
    gap_of_years = []
    for m in md:
        one_movie_actors = md[m][2]
        year_of_movie = []               
        for p in one_movie_actors:
            if p in actors:
                continue
            actors.append(p) 
            for n in md:
                years = md[n][3]
                if p not in md[n][2]:
                    continue
                if years in year_of_movie:
                    continue
                year_of_movie.append(int(years))
            gap_of_years.append(max(year_of_movie)-min(year_of_movie))
            
    topk = []
    topk_gapYear = []
    for i in range(k):
        highest_number = 0
        highest_actor = ""
        b = 0        
        for m in actors:
            one_actor_playing = int(gap_of_years[b])
            b += 1
            if m in topk:
                continue
            
            if one_actor_playing > highest_number:
                highest_number = one_actor_playing
                highest_actor = m
                actor_gapYear = one_actor_playing
        topk.append(highest_actor)  
        topk_gapYear.append(actor_gapYear)

    have_same_gapYear = []
    highest_number = 0
    highest_actor = ""
    b = 0
    for m in actors:
        if m in topk:
            b += 1
            continue
        else:
            if int(gap_of_years[b]) == topk_gapYear[-1]:
                have_same_gapYear.append(m)
        b += 1
    
    topk += have_same_gapYear
    
    return (topk)

actors = topk_gap_of_years(moviedict,3)
print("Q6. Top-3 actors whose movies lead to the largest maximum gap of years ? \nAns:\n"  ,actors)
#Q7 Find all actors who collaborate with Johnny Depp in direct and indirect ways

#Find all actors who collaborate with Someone
def collaborate_with(md, someone):
    finish = False
    had_collaborate = [someone]    
    while finish == False:
        start_len = len(had_collaborate)        
        for m in md:
            actors = md[m][2]
            for k in had_collaborate:           
                if k in actors:
                    for a in actors:
                        if a in had_collaborate:
                            continue
                        had_collaborate.append(a)

        if len(had_collaborate) == start_len:
            finish = True

    return(had_collaborate[1:])  

Johnny_Depp_collaborate = collaborate_with(moviedict,"Johnny Depp")
print("Q7. All actors directly and indirectly collaborating with Johnny Depp include",len(Johnny_Depp_collaborate),"people:",Johnny_Depp_collaborate)
