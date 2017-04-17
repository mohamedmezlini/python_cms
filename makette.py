#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import pymongo


site={"_id":"panda",
"pagefr":{
"header":{"id":"_header",},    
"nav":{"id":"_nav","class":"navbar navbar-inverse navbar-fixed-top",
      "article":{"id":"art1_nav","class":"navbar-inner",
        "div":{"id":"div1_nav","class":"container-fluid",
          "button":{"id":"btn_btn","type":"button","class":"btn btn-navbar" ,"data-toggle":"collapse" ,"data-target":".nav-collapse",
            "span1":{"id":"span1_nav","class":"icon-bar"},
            "span2":{"id":"span2_nav","class":"icon-bar"},
            "span3":{"id":"span3_nav","class":"icon-bar"},
          },
          "a":{"id":"a_nav","class":"brand" ,"href":"#","text":"Site Panda"},
          "div":{"id":"div2_nav","class":"nav-collapse collapse",
            "p":{"id":"p_nav","class":"navbar-text pull-right","text":"Logged in as",
                "a":{"id":"a_nav1","href":"#","class":"navbar-link","text":"Username"}},
            "ul":{"id":"ul_nav","class":"nav",
              "li1":{"id":"li1_nav","class":"active","a":{"id":"a_home","href":"#","text":"Home"}},
              "li2":{"id":"li2_nav","a":{"id":"a_about","href":"#about","text":"About"}},
              "li3":{"id":"li3_nav","a":{"id":"a_contact","href":"#contact","text":"Contact"}}
            }
          }
        }
      }
 },
"main":{"id":"_main","class":"container-fluid",
    "div":{"id":"div0_divg","class":"row-fluid",
        "aside":{"id":"aside_div0","class":"span3",
          "article":{"id":"art1_aside","class":"well sidebar-nav",
            "ul":{"id":"ul1_aside","class":"nav nav-list",
              "li1":{"id":"li1_aside","class":"nav-header","text":"LANGUAGES"},
              "li2":{"id":"li2_aside","a":{"id":"a_fr","href":"#","text":"Français"}},
              "li3":{"id":"li3_aside","a":{"id":"a_eng","href":"#","text":"English"}},
              "li4":{"id":"li4_aside","a":{"id":"a_#","href":"#"}},
              "li5":{"id":"li5_aside","class":"nav-header","text":"Sites utiles"},
              "li6":{"id":"li6_aside","a":{"id":"a_fb","href":"#","text":"Facebook"}},
              "li7":{"id":"li7_aside","a":{"id":"a_gm","href":"#","text":"Gmail"}},
              "li8":{"id":"li8_aside","a":{"id":"a_google","href":"#","text":"Google"}},
              "li9":{"id":"li9_aside","a":{"id":"a_skype","href":"#","text":"Skype"}}
            }
          }
        },
    
        "div1":{"id":"div1_div0","class":"span9",
          "section1":{"id":"sec1_div1","class":"hero-unit",
              "article":{"id":"art1_sec1",
                  "h11":{"id":"h_111","text":"Hello world!"},
                  "p1":{"id":"p1_sec1","text":"The giant panda lives in a few mountain ranges in central China, mainly in Sichuan province, but also in the Shaanxi and Gansu provinces.As a result of farming, deforestation and other development, the panda has been driven out of the lowland areas where it once lived."
                 },

                  "p2":{"id":"p2_sec1","img":{"id":"img_1","src":"http://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Grosser_Panda.JPG/250px-Grosser_Panda.JPG"} 
                  },
                  "p3":{"id":"p3_sec1","a":{"id":"a_p3","href":"#", "class":"btn btn-primary btn-large","text":"Learn more &raquo;"}}
                  }
                },
          "section2":{"id":"sec2_div1","class":"row-fluid",
                "article":{"id":"art1_sec2","class":"span4",
                    "h22":{"id":"h_221","text":"Réunion de Panda"},
                    "p1":{"id":"p1_art1","iframe":{"id":"iframe_1","class":"video", "src":"http://www.youtube.com/embed/DelNwx7EcBM?feature=player_embedded", "frameborder":"0" ,"allowfullscreen":""}},
                    "p2":{"id":"p2_art1","a":{"id":"a_btn1","class":"btn" ,"href":"#","text":"View details &raquo;"}}
                    },
                "article2":{"id":"art2_sec2","class":"span4",
                    "h22":{"id":"h_222","text":"Emotion Panda" },
                    "p1":{"id":"p1_art2","iframe":{"id":"iframe_2","class": "video", "src":"http://www.youtube.com/embed/rkxYw4-oIbM?feature=player_detailpage" ,"frameborder":"0" ,"allowfullscreen":""}},
                    "p2":{"id":"p2_art2","a":{"id":"a_btn2","class":"btn" ,"href":"#","text":"View details &raquo;"}}
                    },
                "article3":{"id":"art3_sec2","class":"span4",
                    "h22":{"id":"h_223","text":"À l\'état sauvage"},
                    "p1":{"id":"p1_ar2se2","text":"Entre 1947 et 1977, les pandas géants étaient alors 1100. Ensuite, entre 1985 et 1988, ils étaient 1000. Environ 1 600 pandas vivent encore en pleine nature. Leur habitat se réduit sans cesse, car les hommes abattent de plus en plus les forêts pour le bois et l\'agriculture, et il reste donc de moins en moins de bambous. De plus, les pandas géants sont parfois tués pour leur pelage ou meurent dans des pièges qui ont été placés pour attraper d\'autres animaux... "},
                    "p2":{"id":"p2_ar2se2","a":{"id":"a_btn3","class":"btn" ,"href":"#","text":"View details &raquo;"}}
                    }
          },
          "section3":{"id":"sec3_div1","class":"row-fluid",

              "article1":{"id":"art1_sec3","class":"span4",
                  "h22":{"id":"h_224","text":"Panda is very tired"},
                  "p1":{"id":"p1_ar1se3","img":{"id":"img_2","src":"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcR0PIqYNTMx9GNdKdYo3KVvWZqJDt74WdAlyJeIeYm1z5nY1g4Q"},
                  },
                  "p2":{"id":"p2_ar1se3","a":{"id":"a_p2","class":"btn" ,"href":"#","text":"View details &raquo;"}}
              },
             "article2":{"id":"art2_sec3","class":"span4",
                  "h22":{"id":"h_225","text":"répartition"},
                  "p1":{"id":"p1_ar2se3","text":"Leur habitat est réduit à six régions dispersées en Chine, dans des forêts de montagnes situées de 1 800 à 3 500 m d’altitude. Il y a actuellement douze réserves qui hébergent environ 60 % des 1 000 pandas survivants. Au sein de ces parcs protégés comme en pleine nature, les animaux sont éparpillés en minuscules groupes ne circulant pas librement d’une montagne à l’autre en raison des vallées occupées par l’homme, ce qui ne favorise pas la reproduction..."},
                 "p2":{"id":"p2_ar2se3","a":{"id":"a_p22","class":"btn" ,"href":"#","text":"View details &raquo;"}}
              },
              
              "article3":{"id":"art3_sec3","class":"span4",
                  "h22":{"id":"h_234","text":"Description"},
                  "p1":{"id":"p1_ar3se3","text":"Le panda géant est volumineux et massif; il pèse de 80 à 125 kg avec une moyenne de 105,5 kg ; il mesure de 1,50 à 1,80 mètre de longueur, avec une moyenne de 1,65 mètre2. Les femelles sont généralement plus petites et moins massives Le panda est noir et blanc. Son pelage épais le protège fort bien contre le froid.Le panda possède six doigts dont un « faux pouce » opposable à ses cinq doigts. Il s\'agit d\'un os du poignet modifié (l\'os sésamoïde)..."},
                  "p2":{"id":"p1_ar3se3","a":{"id":"a_btnhr","class":"btn" ,"href":"#","text":"View details &raquo;"}},
              }
          }
      }
  }
},

      "footer":{"id":"","class":"foot",
          "p":{"id":"p_foot","text":"&copy; Appsnsites 2013"},
      }

    
 }
}



pymongo.MongoClient().site.site.update({"_id":"panda"},site, unset=True);