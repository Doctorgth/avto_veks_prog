import requests
from bs4 import BeautifulSoup

def find(info,mas):
    i=-1
    for j in range(len(mas)):
        if info==mas[j]:
            i=j
            return i
    return i

Sev_name=["ифнир","корвус","ксанатос","луций","рейвен","тарон","фанем","шаеда"]
Sev_id=["49","42","61","1","63","62","45","46"]

def get_slover_massiv(s_name="ифнир"):
    k=Sev_id[find(s_name,Sev_name)]
    response = requests.get("https://gisaa.ru/veksel/"+k)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    table = tables[2]
    # print(table)
    info = []
    res_type = ["Кожа", "Железо", "Ткань", "Дерево"]
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')

        # Вывести содержимое каждой ячейки
        for cell in cells:
            if cell.text != "" and cell.text != "\n":
                l = cell.text
                while l.find("  ") != -1:
                    l = l.replace("  ", " ")
                if l[0] == chr(10):
                    l = l[1:]
                if l[0] == " ":
                    l = l[1:]
                if l[-1] == " ":
                    l = l[:-1]
                if not (l in res_type):
                    info.append(l)
    name_locations = []
    count_res = []
    locations = []
    side = "wewewewewewewwweweweewewewewe"
    resurs = "LLLLLLLLFFFFFFIIIIIIIWWWWWWWW"
    resurs_f = []
    for i in resurs:
        if i == "L":
            resurs_f.append("Кожа")
        if i == "F":
            resurs_f.append("Ткань")
        if i == "I":
            resurs_f.append("Железо")
        if i == "W":
            resurs_f.append("Дерево")
    for i in info:
        if i.isdigit() or i=="?":
            count_res.append(i)
        else:
            name_locations.append(i)
    for i in range(len(count_res)):
        locations.append({"name": name_locations[i], "count": count_res[i], "side": side[i], "res": resurs_f[i]})
    return locations

def create_veksel(slov_all,s_name="ифнир"):
    side="we"
    type=["Железо","Дерево","Ткань","Кожа"]
    s_name=s_name.lower()
    i=find(s_name,Sev_name)
    if i!=-1:
        ret="Векселя для сервера: "+s_name+"\n"
    else:
        ret = "Имя сервера не найдено, Векселя для сервера: " + s_name + "\n"
    for s in side:
        if s=="w":
            ret+="ЗАПАД\n\n"
        else:
            ret+="ВОСТОК\n\n"
        for t in type:
            ret+=t+"\n\n"
            for i in slov_all:
                if i["res"]==t and i["side"]==s:
                    ret+=create_stroka(i)+"\n"
            ret+="\n"

    return ret


def create_selested_type(x):
  type,count=x["res"],x["count"]
  return {"res":type,"count":count}

def selest_location(west,east):
  selected=[]
  s_locations=[]
  for i in west:
    k=create_selested_type(i)
    if k not in selected:
      selected.append(k)
      s_locations.append(i)
  for i in east:
    k=create_selested_type(i)
    if k not in selected:
      selected.append(k)
      s_locations.append(i)
  return s_locations

def create_veks_table_mas(slov_all,s_name="ифнир"):
    side = "we"
    slov_all=get_slover_massiv(s_name)
    #msg = create_veksel(get_slover_massiv(s_name), s_name)
    type = ["Железо", "Дерево", "Ткань", "Кожа"]
    s_name = s_name.lower()
    i = find(s_name, Sev_name)
    ret=[]
    if i != -1:
        pass
    else:
        pass
    for s in side:

        for t in type:
            ret += t + "\n\n"
            for i in slov_all:
                if i["res"] == t and i["side"] == s:
                    ret.append(i)
    return ret


def delete_iron(a):
  ret=[]
  for i in a:
    if i["res"]!="Железо" or (i["count"]!="60" and i["count"]!="100"):
      ret.append(i)
  return ret

def create_stroka(x):
    return x["name"]+" "+x["count"]



