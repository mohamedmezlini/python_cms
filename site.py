import pymongo
#chaque balise contient qu'une seull texte au maximum
#chaque balise ne contient que des autres balise de la fassson suivante json 
#les listes sont insupportes
site={"_id":"essai",
    "header":{"id":"head","rond":"1", },
    "nav":{ "id": "idnav","rond":"2",
            "menu1":{"id":"menu1","style":"background-color:\"red\"","text":"menu1"},
            "menu2":{"id":"menu2","text":"menu2"},
            "menu3":{"id":"menu3","text":"menu3"}
        },
    "div":{"id":"div","class":"main","rond":"3",
        "section1":{"id":"sec1","class":"sec1",
            "article1":{"id":"art1","text":"je suis article  1","rond":"1"},
            "article2":{"id":"art2","text":"je suis article  2","rond":"2"},
            "article3":{"id":"art3","text":"je suis article  3","rond":"3"},
            "article4":{"id":"art4","text":"je suis article  4","rond":"4"},
            "text":"je suis section5"

        },
        "section2":{"id":"sec2","class":"sec2","rond":"1","style":"background-color:\"red\"",
            "article1":{"id":"art1","text":"je suis article  6","rond":"1"},
            "article2":{"id":"art2","text":"je suis article  7","rond":"2"},
            "article3":{"id":"art3","text":"je suis article  8","rond":"3"},
            "article4":{"id":"art4","text":"je suis article  9","rond":"4"},
            "text":"je suis section 10"
        }
        },
    "footer":{ "rond":"4","id": "footg","class":"footg","text":"copyright Appsnsites"}
    }
pymongo.MongoClient().site.site.save(site);