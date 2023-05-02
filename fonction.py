from datetime import date, timedelta, datetime
from urllib import request
# from dateutil.relativedelta import relativedelta


def up():
  remote_url = 'https://hp22.ynov.com/LYO/Telechargements/ical/Edt_CABECAS_SEGURA.ics?version=2022.0.4.3&idICal=F14B7AF80E432F9A1DE8572B2999B444&param=643d5b312e2e36325d2666683d3126663d31'

  local_file = 'hyper.txt'

  request.urlretrieve(remote_url, local_file)


def fichier(uwu):

  word = uwu
  oni = "Yboost"
  ino = "eYBoost"
  cours = ""
  salle = ""

  with open(r'./hyper.txt', 'r') as fp:
    lines = fp.readlines()
    for line in lines:

      if line.find(word) != -1:
        cours = lines[lines.index(line) + 2]
        salle = lines[lines.index(line) + 3]

        cours = cours.replace("SUMMARY;LANGUAGE=fr:", "")
        salle = salle.replace("LOCATION;LANGUAGE=fr:", "")

        if cours.find(oni) != -1:
          cours = "Rythme: Gaspard/Tommy/Hugo/Jules : Yboost " + '\n'
          salle = ""
          break

        if cours.find(ino) != -1:
          cours = "Rythme: Gaspard/Tommy/Hugo/Jules : eYBoost " + '\n'
          salle = ""
          break

        if cours.find("Ydays") != -1:
          cours = "Rythme: Gaspard/Tommy/Hugo/Jules : Ydays " + '\n'
          salle = ""
          break

  return cours, salle


def ajd():

  up()

  today = date.today()
  today = today.strftime("%Y%m%d")

  cours, salle = fichier("DTSTART:" + today)

  matin = 0

  if int(today[4:6]) % 2 == 0 and salle != "":
    matin = 1
  elif int(today[4:6]) % 2 == 1 and salle != "":
    matin = 2

  return cours, salle, matin


def prochain():
  up()
  today = date.today()

  tomorrow = today + timedelta(days=1)
  tomorrow = tomorrow.strftime("%Y%m%d")

  if today.strftime("%A") == "Friday":
    tomorrow = today + timedelta(days=3)
    tomorrow = tomorrow.strftime("%Y%m%d")

  if today.strftime("%A") == "Saturday":
    tomorrow = today + timedelta(days=2)
    tomorrow = tomorrow.strftime("%Y%m%d")

  if today.strftime("%A") == "Sunday":
    tomorrow = today + timedelta(days=1)
    tomorrow = tomorrow.strftime("%Y%m%d")

  cours, salle = fichier("DTSTART:" + tomorrow)

  matin = 0

  if int(tomorrow[4:6]) % 2 == 0 and salle != "":
    matin = 1
  elif int(tomorrow[4:6]) % 2 == 1 and salle != "":
    matin = 2

  return cours, salle, matin


def semaine():
  up()
  today = date.today()
  monday = today - timedelta(days=today.weekday())
  monday = monday.strftime("%Y%m%d")

  print(monday)

  uwu = []
  oni = []
  ino = []

  for i in range(5):
    cours, salle = fichier("DTSTART:" + monday)
    monday = datetime.strptime(monday, "%Y%m%d") + timedelta(days=1)
    monday = monday.strftime("%Y%m%d")
    uwu.append(cours)
    oni.append(salle)

    matin = 0

    if int(monday[4:6]) % 2 == 0 and salle != "":
      matin = 1
    elif int(monday[4:6]) % 2 == 1 and salle != "":
      matin = 2

    ino.append(matin)

  return uwu, oni, ino


# def mois():
#   today = date.today()
#   first_day = date(today.year, today.month, 1)
#   last_day = date(today.year, today.month + 1, 1) - timedelta(days=1)
#   monday = first_day - timedelta(days=first_day.weekday())
#   monday = monday.strftime("%Y%m%d")

#   with open("planning.txt", "w") as f:
#     while datetime.strptime(monday, "%Y%m%d").date() <= last_day:
#       cours, salle = fichier("DTSTART:" + monday)
#       monday = datetime.strptime(monday, "%Y%m%d") + timedelta(days=1)
#       monday = monday.strftime("%Y%m%d")

#       hh = datetime.strptime(monday, "%Y%m%d").strftime("%d %m %Y")

#       f.write(f"{hh}\n{cours}{salle}\n")
