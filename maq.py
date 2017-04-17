#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os, sys
import pymongo


site={"_id":"panda",
"pagefr":{
"header":{"tag":"header","columns_total":"12","columns_current":"12"},    
"nav":{"tag":"nav","columns_total":"12","columns_current":"12","class":"navbar navbar-inverse",
      "art1_nav":{"tag":"article","columns_total":"12","columns_current":"12","class":"navbar-inner",
        "div1_nav":{"tag":"div","columns_total":"12","columns_current":"12","class":"container-fluid",
          "btn_btn":{"tag":"button","type":"button","class":"btn btn-navbar" ,"data-toggle":"collapse" ,"data-target":".nav-collapse",
            "span1_nav":{"tag":"span","class":"icon-bar"},
            "span2_nav":{"tag":"span","class":"icon-bar"},
            "span3_nav":{"tag":"span","class":"icon-bar"},
          },
          "a_nav":{"tag":"a","class":"brand" ,"href":"#","texte":"Site Panda"},
          "div2_nav":{"tag":"div","columns_total":"12","columns_current":"12","class":"nav-collapse collapse",
            "p_nav":{"tag":"p","class":"navbar-text pull-right","texte":"",
                "a_nav1":{"tag":"a","href":"#","class":"navbar-link","texte":""}},
            "ul_nav":{"tag":"ul","class":"nav",
              "li1_nav":{"tag":"li","class":"active","a_home":{"tag":"a","href":"#","texte":"Home"}},
              "li2_nav":{"tag":"li","a_about":{"tag":"a","href":"#about","texte":"About"}},
              "li3_nav":{"tag":"li","a_contact":{"tag":"a","href":"#contact","texte":"Contact"}}
            }
          }
        }
      }
 },


    
      "div":{"tag":"div","columns_total":"12","columns_current":"9 omega","class":"row-fluid",   
              
        "aside":{"tag":"aside","columns_total":"12","columns_current":"3","class":"span3",
          "art1_aside":{"tag":"article","columns_total":"3","columns_current":"3","class":"well sidebar-nav","class":"grand-art",
            "ul1_aside":{"columns_total":"3","columns_current":"3","tag":"ul","class":"nav nav-list",
              "li1_aside":{"tag":"li","class":"nav-header","texte":"LANGUAGES"},
              "li2_aside":{"tag":"li","a_fr":{"tag":"a","href":"#","texte":"Français"}},
              "li3_aside":{"tag":"li","a_eng":{"tag":"a","href":"#","texte":"English"}},
              "li4_aside":{"tag":"li","a_#":{"tag":"a","href":"#"}}},
            "ul2_aside":{"columns_total":"3","columns_current":"3","tag":"ul","class":"nav nav-list",
              "li5_aside":{"tag":"li","class":"nav-header","texte":"Sites utiles"},
              "li6_aside":{"tag":"li","a_fb":{"tag":"a","href":"#","texte":"Facebook"}},
              "li7_aside":{"tag":"li","a_gm":{"tag":"a","href":"#","texte":"Gmail"}},
              "li8_aside":{"tag":"li","a_google":{"tag":"a","href":"#","texte":"Google"}},
              "li9_aside":{"tag":"li","a_skype":{"tag":"a","href":"#","texte":"Skype"}}
            }
            
          }
        },


        "main" : {"tag":"div","columns_total":"9","columns_current":"12","class":"main",
                "sec1_div1":{"tag":"section","columns_total":"9","columns_current":"9","class":"sction-fluid",
                      "art1_sec1":{"tag":"article","columns_total":"9","columns_current":"9","class":"grand-art",
                          "h_111":{"tag":"h1","texte":"Hello world!"},
                          "p1_sec1":{"tag":"p","texte":"The giant panda lives in a few mountain ranges in central China, mainly in Sichuan province, but also in the Shaanxi and Gansu provinces.As a result of farming, deforestation and other development, the panda has been driven out of the lowland areas where it once lived."
                         },
        
                          "p2_sec1":{"tag":"p","img_1":{"tag":"img","src":"http://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Grosser_Panda.JPG/250px-Grosser_Panda.JPG"} 
                          },
                          "p3_sec1":{"tag":"p","a_p3":{"tag":"a","href":"#", "class":"btn btn-primary btn-large","texte":"Learn more »"}}
                          }
                        },
        
                  "sec2_div1":{"tag":"section","columns_total":"9","columns_current":"9","class":"row-fluid",
                        "art1_sec2":{"tag":"article","columns_total":"9","columns_current":"3","class":"art3",
                            "h_221":{"tag":"h2","texte":"Réunion de Panda"},
                            "p1_art1":{"tag":"p","iframe_1":{"tag":"iframe","class":"video", "src":"http://www.youtube.com/embed/DelNwx7EcBM?feature=player_embedded", "frameborder":"0" ,"allowfullscreen":""}},
                            "p2_art1":{"tag":"p","a_btn1":{"tag":"a","class":"btn" ,"href":"#","texte":"View details »"}}
                            },
                        "art2_sec2":{"tag":"article","columns_total":"9","columns_current":"3","class":"art3",
                            "h_222":{"tag":"h2","texte":"Emotion Panda" },
                            "p1_art2":{"tag":"p","iframe_2":{"tag":"iframe","class": "video", "src":"http://www.youtube.com/embed/rkxYw4-oIbM?feature=player_detailpage" ,"frameborder":"0" ,"allowfullscreen":""}},
                            "p2_art2":{"tag":"p","a_btn2":{"tag":"a","class":"btn" ,"href":"#","texte":"View details »"}}
                            },
                        "art3_sec2":{"tag":"article","columns_total":"9","columns_current":"3","class":"art-fin",
                            "h_223":{"tag":"h2","texte":"À l\'état sauvage"},
                            "p1_ar2se2":{"tag":"p","texte":"Entre 1947 et 1977, les pandas géants étaient alors 1100. Ensuite, entre 1985 et 1988, ils étaient 1000. Environ 1 600 pandas vivent encore en pleine nature. Leur habitat se réduit sans cesse, car les hommes abattent de plus en plus les forêts pour le bois et l\'agriculture, et il reste donc de moins en moins de bambous. De plus, les pandas géants sont parfois tués pour leur pelage ou meurent dans des pièges qui ont été placés pour attraper d\'autres animaux... "},
                            "p2_ar2se2":{"tag":"p","a_btn3":{"tag":"a","class":"btn" ,"href":"#","texte":"View details »"}}
                            }
                  },
                  "sec3_div1":{"tag":"section","columns_total":"9","columns_current":"9","class":"row-fluid",
        
                      "art1_sec3":{"tag":"article","columns_total":"9","columns_current":"3","class":"art3",
                          "h_224":{"tag":"h2","texte":"Panda is very tired"},
                          "p1_ar1se3":{"tag":"p","img_2":{"tag":"img","src":"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcR0PIqYNTMx9GNdKdYo3KVvWZqJDt74WdAlyJeIeYm1z5nY1g4Q"},
                          },
                          "p2_ar1se3":{"tag":"p","a_p2":{"tag":"a","class":"btn" ,"href":"#","texte":"View details »"}}
                      },
                     "art2_sec3":{"tag":"article","columns_total":"9","columns_current":"3","class":"art3",
                          "h_225":{"tag":"h2","texte":"répartition"},
                          "p1_ar2se3":{"tag":"p","texte":"Leur habitat est réduit à six régions dispersées en Chine, dans des forêts de montagnes situées de 1 800 à 3 500 m d’altitude. Il y a actuellement douze réserves qui hébergent environ 60 % des 1 000 pandas survivants. Au sein de ces parcs protégés comme en pleine nature, les animaux sont éparpillés en minuscules groupes ne circulant pas librement d’une montagne à l’autre en raison des vallées occupées par l’homme, ce qui ne favorise pas la reproduction..."},
                         "p2_ar2se3":{"tag":"p","a_p22":{"tag":"a","class":"btn" ,"href":"#","texte":"View details »"}}
                      },
                      
                      "art3_sec3":{"tag":"article","columns_total":"9","columns_current":"3","class":"art-fin",
                          "h_234":{"tag":"h2","texte":"Description"},
                          "p1_ar3se3":{"tag":"p","texte":"Le panda géant est volumineux et massif; il pèse de 80 à 125 kg avec une moyenne de 105,5 kg ; il mesure de 1,50 à 1,80 mètre de longueur, avec une moyenne de 1,65 mètre2. Les femelles sont généralement plus petites et moins massives Le panda est noir et blanc. Son pelage épais le protège fort bien contre le froid.Le panda possède six doigts dont un « faux pouce » opposable à ses cinq doigts. Il s\'agit d\'un os du poignet modifié (l\'os sésamoïde)..."},
                          "p2_ar3se3":{"tag":"p","a_btnhr":{"tag":"a","class":"btn" ,"href":"#","texte":"View details »"}},
                      }
                  }}
      },

      "footer":{"tag":"footer","columns_total":"12","columns_current":"12","class":"foot",
          "hr_foot":{"tag":"hr"},
          "p_foot":{"tag":"p","texte":"© Appsnsites 2013"},
      }

    
 }
}



pymongo.MongoClient().site.site.update({"_id":"panda"},site, unset=True);