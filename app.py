from flask import Flask, render_template
import os
import time
import sys
import fileinput
import json
app = Flask(__name__)

os.system ('mkdir /data/data/com.supercell.brawlstars/update/csv_logic')
os.system ('mkdir /data/data/com.supercell.brawlstars/update/csv_client')
os.system ('cp /data/data/com.termux/files/home/BS-Server/_data/locales.csv /data/data/com.supercell.brawlstars/update/csv_logic/locales.csv')


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/cheat/')
def cheat():
  return render_template('cheat.html')

@app.route('/mod/')
def mod():
  return render_template('mod.html')

@app.route('/values/')
def values():
  return render_template('values.html')

@app.route('/requests/')
def requests():
  return render_template('requests.html')

@app.route('/esport-ssl/')
def esportssl():
  return 'test'

@app.route('/gems/')
def gems():
  return 'test'

@app.route('/credits/')
def credits():
  os.system ('cp /data/data/com.termux/files/home/BS-Server/_data/assets/csv_client/credits.csv /data/data/com.termux/files/home/BS-Server/_temp/credits.csv')
  for i, line in enumerate(fileinput.input('/data/data/com.termux/files/home/BS-Server/_temp/credits.csv', inplace=1)):
    sys.stdout.write(line.replace('Santtu Ahola', '[CUSTOM DATA]'))
  os.system ('cp /data/data/com.termux/files/home/BS-Server/_temp/credits.csv /data/data/com.supercell.brawlstars/update/csv_client/credits.csv')
  os.system ('rm /data/data/com.termux/files/home/BS-Server/_temp/credits.csv')
  time.sleep(1.0)
  os.system ('killall -9 com.supercell.brawlstars')
  time.sleep(1.0)
  os.system ('am start --user 0 -n com.supercell.brawlstars/com.supercell.brawlstars.GameApp')
  return 'Injecting...'

if __name__ == '__main__':
  app.run(debug=True, port=8080, host='0.0.0.0')