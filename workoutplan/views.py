from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# User Authenticated
def check_user_not_authenticated(user):
    return user.is_authenticated

@user_passes_test(check_user_not_authenticated, login_url='/login', redirect_field_name=None)
def plan(request):
    workout_plan = {
        "General": [
            "Nur Fleisch macht Fleisch",
            "Hart, schwer und richtig",
            "Wer regelkonform trainiert, sieht halt auch regelkonform aus",
            "8-12 Wochen 3-5 Übungen, 3-5 Sets, 3-5 Wiederholungen",
            "keine Supersets (BCAA)EAAs wenn möglich während des Trainings",
            "8-12 Wochen 6 Übungen, 3 Sets, 8-12 Wiederholungen",
            "Wenn du einem Pferd in den Arsch tritts und es kein rennpferd ist rennt es auch nicht schneller",
            "Pyramiden Prinzip: (Mit Gewicht) leicht anfangen, dann steigern",
            "Als Warm-Up: 10-20 Wiederholungen ohne Gewicht",
            "Mit höherer Satzzahl pro Übung beginn",
            "z.B. 10 Wdh, 8 Wdh. 4 Wdh.",
            "Immer wieder auch mal ne Wiederholung mehr rausholen",
            "Progression ist wichtig aber nicht in jedem Training",
            "1,5-2min Pause mit steigendem Gewicht länger",
            "Negativbewegungen mitnehmen",
            "Mal Mehr wiederholungen, Mal mehr negativbewegungen, mal mehr gewicht",
            "alle 2-3 wochen auf maximalkraft gehen",
            "sonst mit 80% des Maximalgewichts",
            "evtl. als letzten satz mit weniger gewicht auf Negativbewegung konzentrieren",
            "Dropset: hälfte des maximalgewichts, doppelte Wiederholungszahl"
        ],
        "Chest": [
            {"exercise": "Bankdrücken", "description": "- aussen greifen\n- Bank auf erste Stufe\n- Affengriff\n-3-4cm bis zum Brustmuskel ablassen\n- Multipresse schräg oder gerade beides ok"},
            {"exercise": "Incline Bankdrücken", "description": "- Schrägbank auf 60*"},
            {"exercise": "Dips", "description": "- bis maximal 90*\n- full range of motion\n- vorstellen mit Arm zu rudern"},
            {"exercise": "Cable Crossover", "description": "- Arme gestreckt\n- vor die untere Brust\n- Beine auf einer Höhe\n- Kabel von unten\n- leichteres Gewicht"}
        ],
        "Back": [
            {"exercise": "Klimmzüge", "description": "-zur Brust ziehen\n- Ellenbogen nach außen"},
            {"exercise": "Lat Pull Down", "description": "- breiter Griff\n- bis zur Brust ziehen\n- mit Bank auf ca. 135°/45°\n- Beine nach hinten Stellen\n- Spannung im Latissimus\n- vollkommen ausdehnen lassen"},
            {"exercise": "Rows", "description": "- einarmig"},
            {"exercise": "Überzüge", "description": "- halb Kreis\n- Arme zusammen\n- zum Bauch hin\n- Bizep rausnehemen\n- hoher Wiederholungsbereich\n- zwei Sätze"},
            {"exercise": "Bent over Row", "description": "- Langhantel"}
        ],
        "Arms": [
            {"exercise": "Over Head Press", "description": "-- 4-5 Sätze von leicht zu schwer\n- 5 Satz Reduktionssatz 3x 10 Wdh."},
            {"exercise": "Seitheben", "description": ""},
            {"exercise": "Rudern an der Schrägbank / Face Pulls", "description": "- weiter Hebel, gerade hoch gehen\n- leichter Winkel\n- beim hochziehen in einem Halbkreis, nicht gerade hoch\n- Arme zusammen bringen\n- Schulter fast parallel zum Boden"},
            {"exercise": "(isolierte) Bizep Curls", "description": "Mit links (schwachem Arm starten) & und am Peak anspannen (oben bewusst Bizeps anspannen)\n- letzte Wiederholung halten\n- langsam ablassen"},
            {"exercise": "Skullcrusher (Superset mit Bizeps)", "description": ""},
            {"exercise": "Bizep-Curls", "description": "- optional mit Bank am Kabelturm nach Rühl zur Stirn"},
            {"exercise": "Trizep Push down", "description": ""},
            {"exercise": "Hammercurls auf Schrägbank", "description": ""}
        ],
        "Legs": [
            {"exercise": "Squats", "description": "- Decke fixieren (Kopf nach oben)\n- leichtes Hohlkreuz\n- Schulterbreiter Stand\n- leichter V-Stand\n- Oberschenkel parallel zum Boden (oder 10 Grad tiefer)\n- Langhantel vorne möglich"},
            {"exercise": "Leg Press", "description": ""},
            {"exercise": "Leg Extensions", "description": "- oben kurz halten"},
            {"exercise": "Leg Curls", "description": ""}
        ],
        "Accessories": [
            {"exercise": "Unterarm Langhantelbank Curls", "description": "- Schulterbreit\n- hoch gehen so weit wies geht\n- kein Schwung holen\n- Unterarm auf Bank"},
            {"exercise": "Bauchmuskeltraining", "description": "https://www.youtube.com/watch?v=9oAbP7LHT9Q"},
            {"exercise": "Neck Curls", "description": ""},
            {"exercise": "Shrugs", "description": ""},
            {"exercise": "Calf Raises", "description": ""}
        ]
    }

    return render(request, "workoutplan.html", {'workout_plan': workout_plan})
