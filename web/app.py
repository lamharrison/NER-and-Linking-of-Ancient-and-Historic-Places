from flask import Flask, render_template, url_for, request
import spacy
import json

nlp = spacy.load('./ancient_place_model')

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():
    alert_result_word = "Number of Ancient Places:"

    if request.method == 'POST':
        rawtext = request.form['rawtext']
        doc = nlp(rawtext)
        results = []

        for ent in doc.ents:
            results.append({'text': ent.text, 'id': ent.ent_id_})

        non_repeat_temp = []

        for item in results:
            if not item in non_repeat_temp:
                non_repeat_temp.append(item)

        num_of_results = len(non_repeat_temp)

    return render_template("index.html", results=non_repeat_temp, num_of_results=num_of_results,
                           alert_result_word=alert_result_word)


def read_url_to_json(url):
    import urllib.request as request
    webpage = request.urlopen(url)
    get_data = webpage.read()
    data = json.loads(get_data)
    return data


def extract_receive_connections(url):
    from bs4 import BeautifulSoup
    import requests
    r = requests.get(url)
    demo = r.text

    soup = BeautifulSoup(demo, 'html.parser')

    receive_connection_ori = soup.find('div', id="connectionsField-reverse")

    receive_connection_ori_list = receive_connection_ori.find_all('a', class_="connection-subject state-published")

    receive_connection_list = []

    for each in receive_connection_ori_list:
        receive_connection_list.append({'link': each.get('href'), 'title': each.getText()})

    receive_connection_ori_relations_link = receive_connection_ori.find_all('a',
                                                                            class_="connection-verb state-published")

    receive_connection_ori_relations_link_list = []

    for each in receive_connection_ori_relations_link:
        receive_connection_ori_relations_link_list.append(each.get('href'))

    for each in receive_connection_list:
        index = receive_connection_list.index(each)
        each['connections'] = receive_connection_ori_relations_link_list[index]

    return receive_connection_list


@app.route('/place_info', methods=["POST"])
def place_info():
    if request.method == "POST":
        id = request.form["place_name"]

        url = 'http://pleiades.stoa.org/places/{}/json'.format(id)
        read_data = read_url_to_json(url)

        #  get place description
        description = read_data["description"]

        # get place name title
        name = read_data["title"]

        # get geo locations
        geoloc = read_data["reprPoint"]

        # get locations data
        locations = [item['properties'] for item in read_data["features"]]

        # get place names in history
        names = [item for item in read_data["names"]]

        # get all the connections
        connect_with = [item for item in read_data["connections"]]

        receieve_url = 'http://pleiades.stoa.org/places/{}'.format(id)
        receieve_connections = extract_receive_connections(receieve_url)

        # get place types
        place_type = read_data["placeTypes"]

        # get provenance
        provenance = read_data["provenance"]

        # reference
        reference_list = read_data["references"]
        seeFurther = []
        citesAsEvidence = []
        seeAlso = []
        citesAsRelated = []
        for each in reference_list:
            if each["type"] == 'seeFurther' and (each["citationDetail"] != "" or each["shortTitle"] != ""):
                seeFurther.append(each)
            elif each["type"] == 'citesAsEvidence' and (each["citationDetail"] != "" or each["shortTitle"] != ""):
                citesAsEvidence.append(each)
            elif each["type"] == 'seeAlso' and (each["citationDetail"] != "" or each["shortTitle"] != ""):
                seeAlso.append(each)
            elif each["type"] == 'citesAsRelated' and (each["citationDetail"] != "" or each["shortTitle"] != ""):
                citesAsRelated.append(each)

        # enter your mapbox api here to use map
        mapbox_tokens = {
            'access_token': 'pk.eyJ1IjoibGFtaGFycmlzb24iLCJhIjoiY2s4NTBqM2JzMDF0YjNubzd5cmw4c20ydiJ9.ws7Yzl9-ZTLSS0gwcJi6cA',
            'map_api': 'mapbox://styles/lamharrison/ckbxqzvkj299x1hquq5k53zyi'}

    return render_template("place_info.html", title=name, id=id, description=description, geoloc=geoloc,
                           locations=locations, names=names, connect_with=connect_with,
                           receieve_connections=receieve_connections, place_type=place_type,
                           provenance=provenance, seeFurther=seeFurther, citesAsEvidence=citesAsEvidence,
                           seeAlso=seeAlso, citesAsRelated=citesAsRelated, mapbox_tokens=mapbox_tokens)


if __name__ == '__main__':
    app.run(debug=False)
