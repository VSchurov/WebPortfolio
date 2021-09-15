# Temple of knowledge
### By Vyacheslav Shchurov
If you see 'bpv' in filename - it means blueprint view.
So bpv_* - blueprint instances


### Project Structure:
* application - all program modules of application 

* api - all application factories and high-level (same as create app_instance), connect to database, etc

* config - flask & jinja2 environment and application settings

* core - uhmm... Core of application?

* static - javascript & css app part

* templates - html templates and maybe several subhelping files

* models - database models

#### Actually I think application with this modules already perfect... BUT!
* deployment - contains docker images, kubernetes manifestos, terraform engine, circleCI deployment scenarios, and of course sh and py scripts (maybe Go... Later)
##### Core of this application is powered by Flask microframework (you can look at the documentation here: https://flask.palletsprojects.com/en/2.0.x/)
##### All of used frameworks will be described into requirements.txt, links on documentation will be duplicated in this list:
* Place for framework