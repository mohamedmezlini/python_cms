import pymongo
site={"_id":"essai",
    "pagefr":{"header":{"id":"headerg",
    "img":{"sr":"http://images.wizisites.com/img3a47b32acbdcbd3bed2360709517888e.png",
    "alt":"logo" }
    },

    "nav":{ "id": "idnav","rond":"2",
           "ul":{"id":"menu",
           "li1":{"id":"menu1","a":{"href":"#","p":{"text":"ACCUEIL "}}},
           "li2":{"id":"menu2","a":{"href":"#","p":{"text":"EQUIPPEMENTS ET CONSOMMABLES DE LOGO"}}},
           "li3":{"id":"menu3","a":{"href":"#","p":{"text":"SCIENCES DE LA VIE"}}},
           "li4":{"id":"menu4","a":{"href":"#","p":{"text":"QUI SOMMES NOUS ?"}}}
           } 
        },
    "div":{"id":"globaldiv","class":"main",
        "aside":{"id":""},
        "div":{"id":"maindiv",

        "section2":{"id":"sec2","class":"sec2",
            "article1":{"id":"art1sec2","p":{"text":"article 1"}},
            "article2":{"id":"art2sec2","p":{"text":"article 1"}},
        },
        "section3":{"id":"sec3","class":"sec2",
            "article1":{"id":"art1sec3","p":{"text":"article 1"}},
            "article2":{"id":"art2sec3","p":{"text":"article 1"}},
            }
        }

        },
       
    "footer":{ "rond":"4","id": "footg","class":"footg",
        "span":{"id":"spafoot", }

}
}
}
pymongo.MongoClient().site.site.update({"_id":"essai"},site, unset=True);