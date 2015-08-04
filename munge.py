#!/usr/bin/env python3

import csv
import codecs
from data import *

def main():
    with open("Artworks.csv","r", encoding="utf-8-sig") as data:
        art_reader =csv.reader(data, delimiter=",", quotechar="\"", dialect=csv.excel)
        titles = next(art_reader)
        for line in art_reader:
            # unicode_row = [x.decode('utf8') for x in utf8_row]
            # print(line)
            tmp = {}
            for index,title in enumerate(titles):
                tmp[title]=line[index]
            artist = get_or_create(Artist,name=tmp.get("Artist"),bio=tmp.get("ArtistBio"))
            medium = get_or_create(Medium,description=tmp.get("Medium"))
            classification = get_or_create(Classification,description=tmp.get("Classification"))
            department = get_or_create(Department,description=tmp.get("Department"))
            new_art = Art()
            new_art.title = tmp.get("Title")
            new_art.artist = artist
            new_art.medium = medium
            new_art.classification = classification
            new_art.department = department
            new_art.curator_approved = True if tmp.get("CuratorApproved")=="Y" else False
            new_art.dimensions = tmp.get("Dimensions")
            new_art.museem_of_modern_art_number = tmp.get("MoMANumber")
            new_art.credit_line = tmp.get("CreditLine")
            new_art.date_acquired = tmp.get("DateAcquired")
            new_art.object_id = tmp.get("ObjectID")
            new_art.url = tmp.get("URL")
            db.session.add(new_art)
        db.session.commit()



if __name__ == '__main__':
    main()
