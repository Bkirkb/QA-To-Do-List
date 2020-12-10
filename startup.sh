#!/bin/bash
export DATABASE_URI="mysql+pymysql://root:password@35.234.138.197/tdl"
export SECRET_KEY="ssssssshhhhhhhhhh"
cd /opt/QA-To-Do-List
sudo python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py