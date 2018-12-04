#!/usr/bin/env python3
from requests import Session as reqSession
from datetime import datetime
from json import JSONDecodeError
from time import sleep
import argparse
from os import system

URL = "https://www.poste.it/online/dovequando/DQ-REST/ricercasemplice"
key_tracks = 'listaMovimenti'
last_saved_track =  []

class ServerFuckedUp(Exception):
    pass

def req(s, code, n=0):
    data = {
        "codiceSpedizione": code,
        "periodoRicerca": 1,
        "tipoRichiedente": "WEB"
    }
    result = s.post(URL, json=data)
    try:
        return result.json()
    except JSONDecodeError:
        if n > 3:
            raise ServerFuckedUp("Poste Italiane won't provide a good JSON response.")
        print("Error %d. Retrying..." % (result.status_code))
        sleep(5)
        return req(s, code, n+1)

def print_data(res):
    for key, data in res.items():
        if key == "dataOra":
            data = datetime.fromtimestamp(int(data)//1000.0)
        print(" %s: %s" % (key, data))

def get_mov_list(res):
    return res[key_tracks][::-1]

def parse_them_all():
    parser = argparse.ArgumentParser()
    parser.add_argument("CODE", help="Tacking code")
    parser.add_argument("-l", "--last", help="Print only last track info", action="store_true")
    parser.add_argument("-e", "--execute", help="Execute command when last track status changes.")
    return parser.parse_args()


def main():
    args = parse_them_all()

    #create session
    s = reqSession()
    # Send first request
    res = req(s, args.CODE)
    #get the move history
    track_list = get_mov_list(res)

    # print only the last move the package made.
    if args.last:
        print_data(track_list[0])
    # If we want to execute a command after we have an update
    elif args.execute:
        last_saved_track = track_list[0]
        
        while (True):
            sleep(60*5)
            current_track = get_mov_list(req(s, args.CODE))[0]
            if current_track != last_saved_track:
                last_saved_track = current_track
                system(args.execute)
    else:
        # Print the full history
        for update in track_list:
            print_data(update)
            print("--")

if __name__ == "__main__":
    main()